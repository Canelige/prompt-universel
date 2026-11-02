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
from commun import T, BUILD, RENDUS, reglages, plafond_feuilles, detail_chargees, m, MSG

MSG.update({
    "images": ("moins de {min} vraies images ({n}) : télécharge des images libres de droits et sourcées (P6.21)", "fewer than {min} real images ({n}): download royalty-free, sourced images (P6.21)"),
    "blanc": ("feuille {f} : bande vide de {pct} % de la hauteur : ajoute une image ou un visuel, jamais du texte étiré (P6.21)", "sheet {f}: empty band of {pct} % of the height: add an image or a visual, never stretched text (P6.21)"),
    "nombre": ("nombre imprimé absent de 02_contenu.yaml et des sorties de calculs.py : {x} (feuille(s) {p}). Un nombre écrit à la main dans le gabarit ? Mets-le dans le YAML ou dans calculs.py (P6.22).", "printed number missing from 02_contenu.yaml and from the calculs.py outputs: {x} (sheet(s) {p}). A number written by hand in the template? Put it in the YAML or in calculs.py (P6.22)."),
    "code": ("nombre imprimé écrit dans {f} ligne {l} : {x} (P6.22)", "printed number written in {f} line {l}: {x} (P6.22)"),
    "tiret": ("tiret long ou demi-tiret, feuille {f}", "long dash or en dash, sheet {f}"),
    "mesure": ("mesure.json absente : lance d'abord un rendu complet", "mesure.json missing: run a full render first"),
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
    try:   # contrôles de charte propres au travail (P6.20) : controles_charte.verifier(S, pdf, rep) -> liste de défauts
        import controles_charte
        fc = controles_charte.verifier(S, pdf, rep); fautes += fc; lignes.append("charte %s  %d défaut(s)" % ("ECHEC " if fc else "ok    ", len(fc)))
    except ImportError: pass
    # tirets (livrable et scripts)
    tir = re.compile("[" + "".join(chr(c) for c in (0x2012, 0x2013, 0x2014, 0x2015, 0x2212)) + "]")
    for i, p in enumerate(d, 1):
        if tir.search(p.get_text()): fautes.append(m("tiret", f=i)); grand.add(i)
    print("\n".join(lignes)); print("CONTROLES : %s" % ("OK" if not fautes else "%d défaut(s)" % len(fautes)))
    for x in fautes: print("  - " + x)
    if grand: print("A OUVRIR EN GRAND : feuilles %s" % ", ".join(map(str, sorted(grand))))
    return 1 if fautes else 0

if __name__ == "__main__":
    sys.exit(main())
