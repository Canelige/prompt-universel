# Qui le lit, et quand : `diapo-fabricant` le copie tel quel en <sous-dossier>/travail/controles.py (P6.20) et y ajoute, si besoin, les contrôles de charte de la phase 7 ; la discussion de projet le lance, ne lit que sa sortie courte (porte de la phase 6).
"""controles.py : la porte de la phase 6. Usage : python controles.py [rendus/<nom>.pdf]  (par défaut le dernier PDF complet de rendus/).

  P6.21  au moins 3 vraies images ; aucune page avec une bande vide de plus de 35 % de la hauteur
  P6.22  aucun nombre imprimé qui ne soit dans 02_contenu.yaml, donnees.csv ou les sorties de calculs.py ; aucun nombre imprimé écrit dans build.py ou blocs.py
  P6.23  nombre de feuilles du PDF au plus égal au maximum de PAGES PROMISES (ETAT.md)
  P7.16  (partiel) débordements, éléments hors marges, polices en erreur, tirets longs
Sortie : une ligne par contrôle, puis « A OUVRIR EN GRAND » : les seules pages qu'un script désigne (en Express, on lit les planches, pas les pages).
Code de sortie 1 au moindre défaut.
"""
import ast, glob, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymupdf
from commun import T, BUILD, RENDUS, ETAT, LANG, reglages, roles, hex2rgb, rgb2oklch, compteur, rendus_complets, plafond_feuilles, detail_chargees, m, MSG

MSG.update({
    "images": ("moins de {min} vraies images ({n}) : télécharge des images libres de droits et sourcées (P6.21)", "fewer than {min} real images ({n}): download royalty-free, sourced images (P6.21)"),
    "blanc": ("feuille {f} : bande vide de {pct} % de la hauteur : ajoute une image ou un visuel, jamais du texte étiré (P6.21)", "sheet {f}: empty band of {pct} % of the height: add an image or a visual, never stretched text (P6.21)"),
    "nombre": ("nombre imprimé absent de 02_contenu.yaml et des sorties de calculs.py : {x} (feuille(s) {p}). Un nombre écrit à la main dans le gabarit ? Mets-le dans le YAML ou dans calculs.py (P6.22).", "printed number missing from 02_contenu.yaml and from the calculs.py outputs: {x} (sheet(s) {p}). A number written by hand in the template? Put it in the YAML or in calculs.py (P6.22)."),
    "code": ("nombre imprimé écrit dans {f} ligne {l} : {x} (P6.22)", "printed number written in {f} line {l}: {x} (P6.22)"),
    "tiret": ("tiret long ou demi-tiret, feuille {f}", "long dash or en dash, sheet {f}"),
    "mesure": ("mesure.json absente : lance d'abord un rendu complet", "mesure.json missing: run a full render first"),
    "origine": ("couleurs.origine absente ou invalide dans reglages.yaml : écris en une ligne d'où vient l'accent, sous la forme « marque : … », « destinataire : … », « secteur : … », « pays : … », « lieu : … », « produit : … » ou « photo : … » (DA.5, DA.9). Jamais une couleur décorative.", "couleurs.origine missing or invalid in reglages.yaml: write in one line where the accent comes from, as \"brand: ...\", \"recipient: ...\", \"sector: ...\", \"country: ...\", \"place: ...\", \"product: ...\" or \"photo: ...\" (DA.5, DA.9). Never a decorative color."),
    "energie": ("energie absente de reglages.yaml (sobre, vivant, affiche ou sombre) : la surface colorée ne peut pas être bornée (P7.10)", "energie missing from reglages.yaml (sobre, vivant, affiche or sombre; sober, vivid, poster, dark are accepted): the colored area cannot be bounded (P7.10)"),
    "surface_ens": ("surface colorée d'ensemble {x} % hors de la plage de l'énergie {e} ({a} à {b} %) (P7.10)", "overall colored area {x} % outside the range of the {e} energy ({a} to {b} %) (P7.10)"),
    "surface_page": ("feuille {f} : {x} % de surface colorée, au-delà des {max} % permis en {e} : trop de couleur, retire un aplat (P7.10)", "sheet {f}: {x} % colored area, above the {max} % allowed in {e}: too much color, remove a flat (P7.10)"),
    "vif": ("feuille {f} : aplat vif (chroma OKLCH au-delà de 0,14) sur {x} % de la page, au-delà de {max} % en {e} : aplat criard, adoucis-le ou réduis-le", "sheet {f}: vivid flat (OKLCH chroma above 0.14) on {x} % of the page, above {max} % in {e}: loud flat, soften or shrink it"),
    "plancher": ("feuille {f} : {x} % de surface colorée, sous le plancher de 3 % (P7.11) ; `sobre_typographique: true` dans reglages.yaml si la charte l'a choisi", "sheet {f}: {x} % colored area, under the 3 % floor (P7.11); `sobre_typographique: true` in reglages.yaml if the style chose it"),
    "hors_roles": ("feuille {f} : aplat {c} sur {x} % de la page, hors du tableau des rôles : une couleur sortie de nulle part (DA.51) ; remets un rôle de reglages.yaml", "sheet {f}: flat {c} on {x} % of the page, outside the roles table: a color from nowhere (DA.51); use a role of reglages.yaml"),
    "ecart": ("compteur RENDUS COMPLETS : {c} pour {n} PDF complet(s) dans rendus/ : un rendu perdu ou un PDF effacé ; refais le rendu manquant ou corrige le compteur (PI.31)", "RENDUS COMPLETS counter: {c} for {n} full PDF(s) in rendus/: a lost render or a deleted PDF; redo the missing render or fix the counter (PI.31)"),
    "l_surface": ("P7.10  {s}  surface colorée d'ensemble {x} % (énergie {e}, plage {a} à {b} %)", "P7.10  {s}  overall colored area {x} % (energy {e}, range {a} to {b} %)"),
    "l_origine": ("DA.5   {s}  origine de l'accent : {o}", "DA.5   {s}  accent origin: {o}"),
    "l_compteur": ("PI.31  {s}  compteur {c} / 3, {n} PDF complet(s) dans rendus/", "PI.31  {s}  counter {c} / 3, {n} full PDF(s) in rendus/"),
    "pdf": ("aucun PDF complet dans rendus/ : lance d'abord un rendu complet", "no full PDF in rendus/: run a full render first"),
})

# ---------------------------------------------------------------- nombres (P6.22)
NUM = r"\d{1,3}(?:[ ,.]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?"
def motifs(S):
    mots = [u for u in S["unites"] if u[-1].isalpha()]; sym = [u for u in S["unites"] if not u[-1].isalpha()]
    unit = "|".join(["%", "[€$£¥]", "EUR", "USD", "JPY", "CAD", "GBP"] + [re.escape(u) for u in sym if u not in ("%", "€")] + [re.escape(u) + r"\b" for u in mots])
    return [r"[€$£¥]\s?(?:%s)" % NUM, r"(?:%s)\s?(?:%s)" % (NUM, unit), r"\b(?:19|20)\d\d\b"]
def netteté(t): return re.sub(r"[   ]", " ", t)
def valeur(n):
    if re.fullmatch(r"\d{1,3}(?: \d{3})+(?:[.,]\d+)?", n): n = n.replace(" ", "")
    elif re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", n): n = n.replace(",", "")
    elif re.fullmatch(r"\d{1,3}(?:\.\d{3})+(?:,\d+)?", n): n = n.replace(".", "").replace(",", ".")
    return float(n.replace(",", "."))
def decimales(n): mt = re.search(r"[.,](\d+)$", n); return len(mt.group(1)) if mt else 0
def autorises(S):
    """Valeurs de 02_contenu.yaml (exactes) ; valeurs de donnees.csv et des sorties de calculs.py (calculées, donc aussi arrondies à 0..4 décimales)."""
    lire = lambda f: open(os.path.join(T, f), encoding="utf-8").read() if os.path.exists(os.path.join(T, f)) else ""
    calcules = [lire("donnees.csv")]
    if os.path.exists(os.path.join(T, "calculs.py")):
        for cmd in S["calculs_commandes"]:
            calcules.append(subprocess.run([sys.executable, "calculs.py"] + ([cmd] if cmd else []), cwd=T, capture_output=True, text=True).stdout)
    ok = {d: set() for d in range(5)}
    for texte, arrondi in [(lire("02_contenu.yaml"), False)] + [(t, True) for t in calcules]:
        for n in re.findall(NUM, netteté(texte)):
            try: v = valeur(n)
            except ValueError: continue
            for d in range(5): ok[d].add(round(v, d) if arrondi else v)
    return ok
def imprimes(texte, S):
    """{jeton: valeur numérique} des nombres que P3.25 gèle : unité, symbole ou année."""
    out = {}
    for rx in motifs(S):
        for mt in re.finditer(rx, netteté(texte)):
            n = re.search(NUM, mt.group(0))
            if n: out[mt.group(0).strip()] = (valeur(n.group(0)), decimales(n.group(0)))
    return out
def controle_nombres(pdf, S):
    ok, fautes, vus = autorises(S), [], {}
    for i, p in enumerate(pymupdf.open(pdf), 1):
        for jeton, (v, d) in imprimes(p.get_text(), S).items():
            if v not in ok[min(d, 4)]: vus.setdefault(jeton, []).append(i)
    for jeton, pages in vus.items(): fautes.append(m("nombre", x=jeton, p=", ".join(map(str, pages))))
    return fautes
def controle_code(S):
    """P6.22, côté code : aucun littéral de build.py ou blocs.py ne contient un nombre imprimé (les chaînes de CSS et de HTML sont exclues)."""
    fautes = []
    for f in ("build.py", "blocs.py"):
        p = os.path.join(T, f)
        if not os.path.exists(p): continue
        arbre = ast.parse(open(p, encoding="utf-8").read())
        docs = {id(n.body[0].value) for n in ast.walk(arbre) if isinstance(n, (ast.Module, ast.FunctionDef, ast.ClassDef)) and n.body and isinstance(n.body[0], ast.Expr) and isinstance(n.body[0].value, ast.Constant)}
        for n in ast.walk(arbre):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs and not re.search(r"[{};<]", n.value):
                for rx in motifs(S):
                    mt = re.search(rx, netteté(n.value))
                    if mt: fautes.append(m("code", f=f, l=n.lineno, x=mt.group(0).strip())); break
    return fautes

# ---------------------------------------------------------------- couleur (DA.5, DA.9, DA.51, DA.54, P7.10, P7.11) et compteur (PI.31)
ORIGINES = ("marque", "destinataire", "secteur", "pays", "lieu", "produit", "photo", "brand", "recipient", "sector", "country", "place", "product")
ENERGIES = {"sobre": "sobre", "sober": "sobre", "vivant": "vivant", "vivid": "vivant", "affiche": "affiche", "poster": "affiche", "sombre": "sombre", "dark": "sombre"}
BORNES = {"sobre": ((0.08, 0.25), 0.30, 0.15), "vivant": ((0.10, 0.30), 0.45, 0.20), "affiche": ((0.30, 0.60), 0.75, 1.0), "sombre": ((0.0, 1.0), 1.0, 1.0)}   # DA.54 : (plage d'ensemble, maximum par feuille, aplat vif maximum par feuille)
def pct(x): return ("%.1f" % (100 * x)).replace(".", ",") if LANG == "fr" else "%.1f" % (100 * x)
def controle_origine(S):
    """DA.5 : la couleur d'accent vient du sujet ou du destinataire, et reglages.yaml le dit en une ligne (« marque : … », « pays : … »)."""
    o = (S["couleurs"].get("origine") or "").strip()
    return [] if o and "\n" not in o and len(o.split()) >= 4 and re.split(r"[:\s]", o, 1)[0].lower() in ORIGINES else [m("origine")]
def surfaces(pdf, R):
    """Par feuille, à 100 dpi, photos exclues (DA.54) : part de surface colorée (chroma OKLCH > 0,04), part d'aplat vif (> 0,14), et aplats de plus de 1,5 % de la feuille hors du tableau des rôles."""
    from PIL import Image, ImageDraw
    roles_rgb = [tuple(round(v * 255) for v in hex2rgb(h)) for h in R.values() if re.fullmatch(r"#[0-9A-Fa-f]{6}", h)]
    out = []
    for p in pymupdf.open(pdf):
        s = 100 / 72; pix = p.get_pixmap(matrix=pymupdf.Matrix(s, s)); im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples); marque = (1, 2, 3)
        dr = ImageDraw.Draw(im)
        for inf in p.get_image_info(): dr.rectangle([round(v * s) for v in inf["bbox"]], fill=marque)
        cols = [(n, c) for n, c in im.getcolors(maxcolors=pix.width * pix.height) if c != marque]; tot = sum(n for n, c in cols) or 1; col = vif = 0; plats = []
        for n, c in cols:
            ch = rgb2oklch(*(v / 255 for v in c))[1]
            if ch > 0.04: col += n
            if ch > 0.14: vif += n
            if ch > 0.03 and n / tot >= 0.015 and min(sum((a - b) ** 2 for a, b in zip(c, r)) for r in roles_rgb) > 100: plats.append(("#%02X%02X%02X" % c, n / tot))
        out.append({"col": col / tot, "vif": vif / tot, "plats": plats, "n": tot})
    return out
def controle_couleur(pdf, S, R):
    """Origine de l'accent, surface colorée bornée par l'énergie (feuille et ensemble), aplat vif, aplat hors du tableau des rôles. Rend (fautes, lignes, tableau par feuille, surface d'ensemble)."""
    fautes = controle_origine(S); lignes = [m("l_origine", s="ECHEC " if fautes else "ok    ", o=S["couleurs"].get("origine", ""))]; e = ENERGIES.get(str(S.get("energie", "")).lower()); tab = []
    if not e: return fautes + [m("energie")], lignes + ["P7.10  ECHEC  energie ?"], tab, None
    (a, b), pmax, vmax = BORNES[e]; sf = surfaces(pdf, R); ens = sum(x["col"] * x["n"] for x in sf) / (sum(x["n"] for x in sf) or 1)
    for i, x in enumerate(sf, 1):
        tab.append((i, x["col"], x["vif"]))
        if x["col"] > pmax: fautes.append(m("surface_page", f=i, x=pct(x["col"]), max=pct(pmax), e=e))
        if x["vif"] > vmax: fautes.append(m("vif", f=i, x=pct(x["vif"]), max=pct(vmax), e=e))
        if x["col"] < 0.03 and not S.get("sobre_typographique"): fautes.append(m("plancher", f=i, x=pct(x["col"])))
        for c, part in x["plats"]: fautes.append(m("hors_roles", f=i, c=c, x=pct(part)))
    if not a <= ens <= b: fautes.append(m("surface_ens", x=pct(ens), e=e, a=round(a * 100), b=round(b * 100)))
    lignes.append(m("l_surface", s="ECHEC " if not a <= ens <= b else "ok    ", x=pct(ens), e=e, a=round(a * 100), b=round(b * 100)))
    return fautes, lignes, tab, ens
def controle_compteur():
    """PI.31 : le compteur RENDUS COMPLETS de ETAT.md égale le nombre de PDF complets de rendus/."""
    if not os.path.exists(ETAT) or not re.search(r"RENDUS COMPLETS|FULL RENDERS", open(ETAT, encoding="utf-8").read()): return [], None
    c, n = compteur(), len(rendus_complets())
    return ([m("ecart", c=c, n=n)] if c != n else []), m("l_compteur", s="ECHEC " if c != n else "ok    ", c=c, n=n)
def ecrire_controles(lignes, tab, ens, fautes):
    """Écrit 07_controles.md (P7.3) : les lignes de contrôle, SURFACE COLORÉE d'ensemble (lue par portes.py 7, P7.10b) et le tableau par feuille."""
    with open(os.path.join(T, "07_controles.md"), "w", encoding="utf-8") as f:
        f.write("# 07_controles.md\n\n" + "\n".join("- " + l for l in lignes) + "\n\n")
        if ens is not None: f.write(("SURFACE COLORÉE : %s %%\n\n" if LANG == "fr" else "COLORED AREA: %s %%\n\n") % pct(ens))
        f.write("| %s | %s | %s |\n|---|---|---|\n" % (("Feuille", "Surface colorée", "Aplat vif") if LANG == "fr" else ("Sheet", "Colored area", "Vivid flat")))
        f.write("".join("| %d | %s %% | %s %% |\n" % (i, pct(c), pct(v)) for i, c, v in tab))
        f.write("\n" + ("CONTROLES :" if LANG == "fr" else "CHECKS:") + (" OK" if not fautes else " %d" % len(fautes)) + "\n")

# ---------------------------------------------------------------- feuilles, images, blancs
def blancs(pdf):
    """Part de la hauteur de la plus longue bande de lignes uniformes, par feuille (P6.21)."""
    from PIL import Image
    out = []
    for p in pymupdf.open(pdf):
        s = 800 / p.rect.width; pix = p.get_pixmap(matrix=pymupdf.Matrix(s, s)); im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples); px = im.load()
        run = best = 0
        for y in range(im.height):
            ref = px[8, y]; vide = all(sum(abs(a - b) for a, b in zip(px[x, y], ref)) < 14 for x in range(8, im.width - 8, 4))
            run = run + 1 if vide else 0; best = max(best, run)
        out.append(best / im.height)
    return out

def pdf_courant(argv):
    if len(argv) > 1: return argv[1]
    f = sorted(x for x in glob.glob(os.path.join(RENDUS, "*.pdf")) if not os.path.basename(x).startswith("pages-"))
    return f[-1] if f else None

def main(argv=None):
    argv = argv or sys.argv; S = reglages(); pdf = pdf_courant(argv)
    if not pdf: print(m("pdf")); return 1
    d = pymupdf.open(pdf); n = len(d); fautes, grand = [], set(); lignes = []
    # P6.23
    plaf = plafond_feuilles()
    if plaf is False: fautes.append(m("plafond_vide")); lignes.append("P6.23  ECHEC  PAGES PROMISES absent")
    elif plaf and n > plaf[1]:
        fautes.append(m("plafond_feuilles", n=n, max=plaf[1], promis="%d à %d" % plaf if plaf[0] != plaf[1] else plaf[1], exces=n - plaf[1], detail=detail_chargees(d, S["feuilles"]))); lignes.append("P6.23  ECHEC  %d feuilles pour %d promises" % (n, plaf[1]))
    else: lignes.append("P6.23  ok     %d feuille(s), plafond %s" % (n, plaf[1] if plaf else "aucun"))
    # P6.22
    f22 = controle_nombres(pdf, S) + controle_code(S); fautes += f22
    lignes.append("P6.22  %s  %d nombre(s) hors YAML et calculs" % ("ECHEC " if f22 else "ok    ", len(f22)))
    # mesure : P6.21 images, débordements
    mp = os.path.join(BUILD, "mesure.json")
    if not os.path.exists(mp): fautes.append(m("mesure")); rep = {"sheets": [], "fonts": []}
    else: rep = json.load(open(mp))
    nimg = sum(len(s["photos"]) for s in rep["sheets"]); mini = S.get("images_min", 3)
    if nimg < mini: fautes.append(m("images", min=mini, n=nimg))
    lignes.append("P6.21  %s  %d image(s) ; blancs ci-dessous" % ("ECHEC " if nimg < mini else "ok    ", nimg))
    for i, v in enumerate(blancs(pdf), 1):
        if v > S.get("blanc_max", 0.35): fautes.append(m("blanc", f=i, pct=round(v * 100))); grand.add(i)
    for s in rep["sheets"]:
        if s["over"] > 1: fautes.append("feuille %s : débordement de %d px" % (s["f"], s["over"])); grand.add(int(s["f"]))
        if s["wide"]: fautes.append(m("large", f=s["f"], e=s["wide"])); grand.add(int(s["f"]))
    for f in rep["fonts"]:
        if f.endswith(":error"): fautes.append(m("police", x=f))
    lignes.append("P7.16  %s  débordements, marges, polices" % ("ECHEC " if any(s["over"] > 1 or s["wide"] for s in rep["sheets"]) else "ok    "))
    fcl, lcl, tab, ens = controle_couleur(pdf, S, roles(S)); fautes += fcl; lignes += lcl   # DA.5, P7.10, P7.11
    fcp, lcp = controle_compteur(); fautes += fcp; lignes += [lcp] if lcp else []   # PI.31
    try:   # contrôles de charte propres au travail (P6.20) : controles_charte.verifier(S, pdf, rep) -> liste de défauts
        import controles_charte
        fc = controles_charte.verifier(S, pdf, rep); fautes += fc; lignes.append("charte %s  %d défaut(s)" % ("ECHEC " if fc else "ok    ", len(fc)))
    except ImportError: pass
    # tirets (livrable et scripts)
    tir = re.compile("[" + "".join(chr(c) for c in (0x2012, 0x2013, 0x2014, 0x2015, 0x2212)) + "]")
    for i, p in enumerate(d, 1):
        if tir.search(p.get_text()): fautes.append(m("tiret", f=i)); grand.add(i)
    ecrire_controles(lignes, tab, ens, fautes)
    print("\n".join(lignes)); print("CONTROLES : %s" % ("OK" if not fautes else "%d défaut(s)" % len(fautes)))
    for x in fautes: print("  - " + x)
    if grand: print("A OUVRIR EN GRAND : feuilles %s" % ", ".join(map(str, sorted(grand))))
    return 1 if fautes else 0

if __name__ == "__main__":
    sys.exit(main())
