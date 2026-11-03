# Who reads it, and when: `diapo-fabricant`, never in full. He copies this file as is into <subfolder>/travail/ with the template of his type (phase-6-fabrication.md, "Production templates") and does not modify it: the settings are in reglages.yaml, the work-specific blocks in blocs.py.
"""commun.py: library of the production templates (phase 6: A4 document, slide deck, A4 summary).

Contract (P6.2, P6.19, P6.22, P6.23, PI.31):
- all the content and every printed number come from 02_contenu.yaml, donnees.csv or calculs.py;
- the art direction (colors, fonts, density, sheet layout) comes from reglages.yaml;
- sheets are counted and the render fails beyond PAGES PROMISED (ETAT.md);
- --pages renders only precise sheets; the delivered PDF is written to <subfolder>/livraison/ with livrable.txt.
"""
import csv, datetime, glob, html, json, math, os, re, subprocess, sys
import yaml
import pymupdf
from PIL import Image

LANG = "en"
T = os.path.dirname(os.path.abspath(__file__))              # <subfolder>/travail
BUILD, RENDUS = os.path.join(T, ".build"), os.path.join(T, "rendus")
LIVRAISON = os.path.join(os.path.dirname(T), "livraison")
ETAT = os.path.join(T, "ETAT.md")

# ---------------------------------------------------------------- messages (fr, en)
MSG = {
    "plafond_feuilles": ("{n} feuilles pour {max} promises (PAGES PROMISES : {promis}). Coupe {exces} feuille(s) : {detail}. Le rédacteur condense (pages fusionnées ou texte coupé) ; seul un accord écrit de la personne relève le plafond (P6.23).",
                         "{n} sheets for {max} promised (PAGES PROMISED: {promis}). Cut {exces} sheet(s): {detail}. The writer condenses (merged pages or cut text); only the person's written agreement raises the ceiling (P6.23)."),
    "plafond_vide": ("PAGES PROMISES absent de ETAT.md : P6.23 ne peut pas être vérifiée.", "PAGES PROMISED missing from ETAT.md: P6.23 cannot be checked."),
    "deborde": ("feuille {f} (page {p}) déborde de {px} px : coupe environ {lignes} lignes de texte, ou déplace une pièce sur une feuille de suite (une feuille de plus, comptée dans le plafond).",
                "sheet {f} (page {p}) overflows by {px} px: cut about {lignes} lines of text, or move a piece onto a continuation sheet (one more sheet, counted in the ceiling)."),
    "large": ("feuille {f} : élément qui sort des marges ({e}).", "sheet {f}: element outside the margins ({e})."),
    "police": ("police en erreur : {x}", "font in error: {x}"),
    "rendus": ("plafond de rendus complets atteint (3 / 3) : rends seulement les pages fautives avec --pages (PI.31)", "ceiling of full renders reached (3 / 3): render only the faulty pages with --pages (PI.31)"),
    "gabarit_yaml": ("page {p} : gabarit du YAML ({y}) différent de reglages.yaml ({r})", "page {p}: template in the YAML ({y}) differs from reglages.yaml ({r})"),
    "mots": ("page {p} : le corps fait {n} mots, ce gabarit en accepte {max} : écris un champ `points` ou coupe.", "page {p}: the body has {n} words, this template accepts {max}: write a `points` field or cut."),
    "remplacement": ("le nombre de feuilles a changé ({a} puis {b}) : une correction qui change le nombre de pages demande un rendu complet (P6.2)", "the number of sheets changed ({a} then {b}): a correction that changes the page count needs a full render (P6.2)"),
    "detail": ("feuilles de suite à fusionner ou supprimer : {suites} ; feuilles les plus chargées : {mots}", "continuation sheets to merge or remove: {suites}; heaviest sheets: {mots}"),
    "reserve": ("le 3e rendu complet est réservé à la phase 8 : rends seulement les pages fautives avec --pages ; en phase 8, `build.py --audit` lève la réserve (PI.31)", "the 3rd full render is reserved for phase 8: render only the faulty pages with --pages; in phase 8, `build.py --audit` lifts the reserve (PI.31)"),
    "toutes": ("--pages couvre les {n} feuilles : c'est un rendu complet, lance build.py sans --pages (il sera compté, PI.31)", "--pages covers all {n} sheets: that is a full render, run build.py without --pages (it will be counted, PI.31)"),
    "hors": ("--pages : la feuille {x} n'existe pas (il y en a {n})", "--pages: sheet {x} does not exist (there are {n})"),
    "pdf_absent": ("aucun PDF de rendu dans {d}", "no rendered PDF in {d}"),
}
def m(cle, **kw): return MSG[cle][0 if LANG == "fr" else 1].format(**kw)

# ---------------------------------------------------------------- settings
DEFAUTS = {
    "document": {"titre": "", "auteur": "[to be completed]", "sujet": "", "nom_fichier": "Sujet_Livrable_Auteur", "langue": "fr"},
    "couleurs": {"teinte": "#3A4A5C", "accent": "#E07A1F", "accent_2": "#3A4A5C", "series": {}, "roles": {}, "origine": ""},
    "energie": "", "sobre_typographique": False, "frise": [],
    "polices": {"famille": "sans-serif", "fichiers": {}, "titres": {"famille": "", "fichiers": {}}},
    "densite": {
        "a4": {"corps": 14, "cellule": 11.1, "source": 10.4, "legende": 10, "titre": 27, "marge_mm": 14, "interligne": 1.33},
        "diaporama": {"corps": 30, "cellule": 24, "source": 17, "legende": 17, "titre": 56, "marge_px": 96, "interligne": 1.3, "mots_max": 70},
    },
    "images": {"logo": "", "logo_alt": "", "couverture": "", "couverture_alt": "", "couverture_credit": "", "largeur_max_px": 1600},
    "libelles": {"sources": "Sources", "suite": "(continued)", "total": "Total", "hypotheses": "Hypotheses"},
    "etiquettes": [], "exposant": "", "unites": [], "intertitres": False, "formule": "",
    "calculs_commandes": [""],
    "feuilles": [],
}
def fusion(a, b):
    for k, v in b.items(): a[k] = fusion(a[k], v) if isinstance(v, dict) and isinstance(a.get(k), dict) else v
    return a
def reglages():
    S = json.loads(json.dumps(DEFAUTS))
    p = os.path.join(T, "reglages.yaml")
    if os.path.exists(p): fusion(S, yaml.safe_load(open(p, encoding="utf-8")) or {})
    return S

def charger():
    Y = yaml.safe_load(open(os.path.join(T, "02_contenu.yaml"), encoding="utf-8"))
    p = os.path.join(T, "donnees.csv")
    D = list(csv.DictReader(open(p, encoding="utf-8"))) if os.path.exists(p) else []
    return Y, D

def valeur_csv(D, ref):
    """ref = 'serie|annee' (annee optional)."""
    serie, _, an = ref.partition("|")
    for r in D:
        if r["serie"] == serie and (not an or r["annee"] == an): return float(r["valeur"])
    raise KeyError(ref)

# ---------------------------------------------------------------- color (OKLCH, DA.43 to DA.47)
def _lin(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def _gam(c): return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
def hex2rgb(h): h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
def rgb2hex(r, g, b): return "#%02X%02X%02X" % tuple(round(max(0, min(1, x)) * 255) for x in (r, g, b))
def rgb2oklch(r, g, b):
    r, g, b = _lin(r), _lin(g), _lin(b)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    mm = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * mm - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * mm + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * mm - 0.8086757660 * s
    return L, math.hypot(a, bb), math.degrees(math.atan2(bb, a)) % 360
def oklch2rgb(L, C, h):
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l, mm, s = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3, (L - 0.1055613458 * a - 0.0638541728 * b) ** 3, (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l - 3.3077115913 * mm + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * mm - 0.3413193965 * s
    bl = -0.0041960863 * l - 0.7034186147 * mm + 1.7076147010 * s
    return (_gam(max(r, 0)), _gam(max(g, 0)), _gam(max(bl, 0)), min(r, g, bl) >= -1e-4 and max(r, g, bl) <= 1 + 1e-4)
def ok2hex(L, C, h):
    lo, hi = 0.0, C
    if not oklch2rgb(L, C, h)[3]:
        for _ in range(30):
            mid = (lo + hi) / 2
            if oklch2rgb(L, mid, h)[3]: lo = mid
            else: hi = mid
        C = lo
    return rgb2hex(*oklch2rgb(L, C, h)[:3])
def lum(x): r, g, b = (_lin(v) for v in hex2rgb(x)); return 0.2126 * r + 0.7152 * g + 0.0722 * b
def contraste(a, b): la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)
def foncer(x, fond, cible=4.5):
    L, C, h = rgb2oklch(*hex2rgb(x))
    while contraste(ok2hex(L, C, h), fond) < cible and L > 0.2: L -= 0.02
    return ok2hex(L, C, h)

def roles(S):
    c = S["couleurs"]; hp = rgb2oklch(*hex2rgb(c["teinte"]))[2]
    fond, encre = ok2hex(0.975, 0.011, hp), ok2hex(0.24, 0.035, hp)
    Lf, Le = rgb2oklch(*hex2rgb(fond))[0], rgb2oklch(*hex2rgb(encre))[0]
    La, Ca, ha = rgb2oklch(*hex2rgb(c["accent"]))
    r = {"fond": fond, "encre": encre, "accent": c["accent"], "accent-2": c["accent_2"], "fond-rupture": c["accent"],
         "accent-fonce": foncer(c["accent"], fond), "accent-clair": (ok2hex(min(Lf - 0.03, 0.95), min(Ca * 0.3, 0.04), ha) if Lf > 0.5 else ok2hex((Lf + La) / 2 + 0.03, Ca / 2, ha)),
         "encre-secondaire": ok2hex(Le + (Lf - Le) * 0.25, 0.03, hp), "filet": ok2hex(Lf - 0.10, 0.012, hp),
         "blanc-chaud": ok2hex(0.99, 0.004, hp)}
    for i, (nom, x) in enumerate(c["series"].items()):
        Ls, Cs, hs = rgb2oklch(*hex2rgb(x))
        r.update({"s%d" % i: x, "s%d-fonce" % i: foncer(x, fond), "s%d-clair" % i: ok2hex(0.91, Cs * 0.4, hs)})
    r.update(c["roles"]); return r

# ---------------------------------------------------------------- text
def nombres_prot(S):
    mots = "|".join(re.escape(u) for u in S["unites"] if u[-1].isalpha())
    mots = (r"|-?\d[\d,.]*\s(?:" + mots + r")\b") if mots else ""
    return r"[€$£¥]\s?\d[\d,.]*k?|±\s?\d[\d.,]*(?:\s?%|\s?points?)?|-?\d[\d,.]*\s?(?:%|€|\$|£|¥)" + mots

def fmt(texte, S):
    """Escapes, then protects numbers and uncertainty tags (non-breaking)."""
    parts = []
    if S["etiquettes"]: parts.append(r"(?P<tag>\b(?:%s)\b)" % "|".join(re.escape(t) for t in S["etiquettes"]))
    if S["exposant"]: parts.append(r"(?P<hyp>,\s%s|\s?\(%s\)|%s)" % ((S["exposant"],) * 3))
    parts.append(r"(?P<nb>%s)" % nombres_prot(S))
    out, i = [], 0
    for mt in re.finditer("|".join(parts), texte):
        out.append(html.escape(texte[i:mt.start()])); s = html.escape(mt.group(0)); k = mt.lastgroup
        if k == "hyp": out.append('<sup class="hyp">%s</sup>' % s.strip(" ,()").replace(" ", "&nbsp;"))
        else: out.append('<span class="%s">%s</span>' % ("tag" if k == "tag" else "nb", s.replace(" ", "&nbsp;")))
        i = mt.end()
    out.append(html.escape(texte[i:])); return "".join(out)

def paragraphes(corps, S):
    out = []
    for bloc in [b for b in corps.strip().split("\n\n") if b.strip()]:
        for l in [x.strip() for x in bloc.split("\n") if x.strip()]:
            if re.match(r"^\d\. ", l): n, reste = l.split(" ", 1); out.append('<p class="item"><b>%s</b> %s</p>' % (n, fmt(reste, S)))
            elif S["formule"] and re.match(S["formule"], l): out.append('<p class="formule">%s</p>' % fmt(l, S))
            elif len(l.split()) <= 4 and l.endswith("."): out.append('<p class="lead"><b>%s</b></p>' % fmt(l, S))
            else:
                mt = re.match(r"^([A-Z][\w\-’']+(?: [\w\-’']+){0,3})(?=[.:]\s)", l) if S["intertitres"] else None
                if mt and len(l) > len(mt.group(0)) + 20: out.append("<p><b>%s</b>%s</p>" % (fmt(mt.group(0), S), fmt(l[mt.end():], S)))
                else: out.append("<p>%s</p>" % fmt(l, S))
    return "\n".join(out)

def liste_points(pg, S):
    return '<ul class="points">%s</ul>' % "".join("<li>%s</li>" % fmt(x, S) for x in pg["points"])

def nb_mots(t): return len(re.findall(r"\w+", t))

# ---------------------------------------------------------------- images (one preparation: max size, JPEG 85)
def image(chemin, S):
    """Resizes into .build/img/ and returns the path relative to .build/."""
    os.makedirs(os.path.join(BUILD, "img"), exist_ok=True)
    src = os.path.join(T, chemin)
    if chemin.lower().endswith(".svg"): return "../" + chemin
    im = Image.open(src); w = S["images"]["largeur_max_px"]
    if im.width > w: im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    alpha = im.mode in ("RGBA", "LA", "P")
    nom = re.sub(r"\W", "_", chemin) + (".png" if alpha else ".jpg")
    im.convert("RGBA" if alpha else "RGB").save(os.path.join(BUILD, "img", nom), **({} if alpha else {"quality": 85}))
    return "img/" + nom

def figure(img, S, cls=""):
    src = image(img["fichier"], S)
    return '<figure class="fig %s"><img class="photo" src="%s" alt="%s"><figcaption>%s</figcaption></figure>' % (cls, src, html.escape(img.get("alt", "")), html.escape(img.get("credit", "")))

# ---------------------------------------------------------------- HTML blocks (pieces of the YAML)
_NUM = re.compile(r"^[\d.,\s±%€$£¥]+$")
def serie_de(texte, S, contient=False):
    """Index of the series (role color) whose name is the text (or, if `contient`, the only name quoted in the text), or -1."""
    t = texte.strip().lower(); noms = [n.lower() for n in S["couleurs"]["series"]]
    if not contient: return noms.index(t) if t in noms else -1
    cites = [i for i, n in enumerate(noms) if re.search(r"\b%s\b" % re.escape(n), t)]
    return cites[0] if len(cites) == 1 else -1

def tableau(colonnes, lignes, S, totaux=None, total_poids=None, cls=""):
    n = len(colonnes)
    num = [i for i in range(1, n) if all((not str(r[i]).strip()) or _NUM.match(str(r[i]).strip()) for r in lignes) and any(str(r[i]).strip() for r in lignes)]
    def th(i, c):
        k = (["num"] if i in num else []) + (["ser%d" % serie_de(c, S, True)] if serie_de(c, S, True) >= 0 else [])
        return '<th class="%s">%s</th>' % (" ".join(k), fmt(c, S))
    out = ['<table class="%s"><thead><tr>%s</tr></thead><tbody>' % (cls, "".join(th(i, c) for i, c in enumerate(colonnes)))]
    for r in lignes:
        tds = []
        for i, c in enumerate(r):
            c = str(c); k = ["num"] if i in num else []
            if i == 0 and serie_de(c, S) >= 0: k.append("tser%d" % serie_de(c, S))
            tds.append('<td class="%s">%s</td>' % (" ".join(k), fmt(c, S)))
        out.append("<tr>%s</tr>" % "".join(tds))
    if total_poids is not None: out.append('<tr class="tot"><td>%s</td><td class="num">%s</td>%s</tr>' % (html.escape(S["libelles"]["total"]), fmt(str(total_poids), S), "<td></td>" * (n - 2)))
    vc = max(num) if num else n - 1   # totals fall under the last numeric column
    for t in (totaux or []):
        lbl, vals = t[0], list(t[1:])
        if len(vals) > 1:   # plusieurs valeurs : sous les dernières colonnes
            out.append('<tr class="tot"><td colspan="%d" class="tl">%s</td>%s</tr>' % (max(n - len(vals), 1), fmt(lbl, S), "".join('<td class="num">%s</td>' % fmt(str(v), S) for v in vals))); continue
        v = vals[0]
        if len(str(v)) > 14: out.append('<tr class="tot"><td colspan="%d">%s: %s</td></tr>' % (n, fmt(lbl, S), fmt(str(v), S)))
        else: out.append('<tr class="tot"><td colspan="%d" class="tl">%s</td><td class="num">%s</td>%s</tr>' % (vc, fmt(lbl, S), fmt(str(v), S), "<td></td>" * (n - 1 - vc)))
    return "".join(out) + "</tbody></table>"

def frise(S, i):
    """Footer strip of the parts (axis 7): `frise:` of reglages.yaml, the current part `i` (index) in the accent."""
    if not S["frise"] or i is None: return ""
    return '<span class="frise">%s</span>' % "".join('<i%s>%s</i>' % (' class="on"' if k == i else "", html.escape(x)) for k, x in enumerate(S["frise"]))

def chaine(etapes, S, vertical=False):
    if vertical:
        return '<div class="vchain">%s</div>' % "".join('<div class="vrow"><div class="chev">%s</div><p>%s</p><p>%s</p></div>' % (fmt(a, S), fmt(b, S), fmt(c, S)) for a, b, c in etapes)
    return '<div class="chain" style="grid-template-columns:repeat(%d,1fr)">%s</div>' % (len(etapes), "".join(
        '<div class="cstep"><div class="chev">%s</div><p>%s</p><p class="ref">%s</p></div>' % (fmt(a, S), fmt(b, S), fmt(c, S)) for a, b, c in etapes))

def tuiles(liste, S, cls=""):
    return '<div class="tuiles %s" style="grid-template-columns:repeat(%d,1fr)">%s</div>' % (cls, len(liste), "".join(
        '<div class="tile t-%s"><b>%s</b><span>%s</span></div>' % (t.get("role", "clair"), html.escape(str(t["valeur"])), fmt(t["legende"], S)) for t in liste))

def graphique(g, D, S, larg=680):
    """Horizontal bars from zero, one panel per group; values read from the YAML or donnees.csv (`csv: serie|annee`)."""
    pans = g["panneaux"]; cote = g.get("disposition", "cote") == "cote"
    nbar = max(len(p["barres"]) for p in pans); rowh = 22
    def val(b): return valeur_csv(D, b["csv"]) if "csv" in b else float(b["valeur"])
    vmax = max(val(b) for p in pans for b in p["barres"]) or 1
    pw = (larg - 28) / 2 if cote and len(pans) > 1 else larg; lab = g.get("etiquette_px", 172); sc = (pw - lab - 70) / vmax
    h = (28 + rowh * nbar) if cote else sum(28 + rowh * len(p["barres"]) for p in pans)
    s = ['<svg viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-label="%s">' % (larg, h, larg, h, html.escape(g.get("titre", "")))]
    y0 = 0
    for k, p in enumerate(pans):
        x0 = k * (pw + 28) if cote else 0; y = 0 if cote else y0
        i = serie_de(p.get("serie", ""), S); col = "s%d" % i if i >= 0 else "accent"
        s.append('<text x="%.1f" y="%d" class="gl" fill="var(--%s-fonce)">%s</text>' % (x0, y + 12, col if i >= 0 else "accent", html.escape(p["titre"])))
        s.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="var(--encre)"/>' % (x0 + lab, y + 18, x0 + lab, y + 24 + rowh * len(p["barres"])))
        for j, b in enumerate(p["barres"]):
            v = val(b); yy = y + 24 + j * rowh; ww = v * sc
            txt = (b.get("format") or "{:g}").format(v) + b.get("unite", "")
            s.append('<text x="%.1f" y="%d" text-anchor="end" class="gl2">%s</text>' % (x0 + lab - 6, yy + 13, html.escape(b["label"])))
            if ww > 0: s.append('<rect x="%.1f" y="%d" width="%.1f" height="16" fill="var(--%s)"/>' % (x0 + lab, yy + 2, ww, col))
            s.append('<text x="%.1f" y="%d" class="gv">%s</text>' % (x0 + lab + ww + 5, yy + 14, html.escape(txt)))
        y0 += 28 + rowh * len(p["barres"])
    return "".join(s) + "</svg>"

def fiches(liste, p, S):
    """One card per entry of a YAML list: head (3 fields) | body (fields, then one-line groups)."""
    f, lib = p["fiches"], p.get("libelles", {})
    v = lambda r, c: ", ".join(map(str, r[c])) if isinstance(r[c], list) else str(r[c])
    out = ['<div class="registre">']
    for r in liste:
        a, b, c = f["tete"]
        corps = "".join("<p>%s</p>" % fmt(v(r, k), S) for k in f.get("corps", []))
        corps += "".join('<p class="m">%s</p>' % '<i class="sep"></i>'.join("<b>%s.</b> %s" % (html.escape(lib.get(k, k)), fmt(v(r, k), S)) for k in grp) for grp in f.get("notes", []))
        out.append('<div class="hyp"><div class="hid"><b>%s</b><span class="hval">%s</span><span class="hobj">%s</span></div><div class="hbody">%s</div></div>' % (html.escape(v(r, a)), fmt(v(r, b), S), fmt(v(r, c), S), corps))
    return "".join(out) + "</div>"

def piece(p, Y, D, S, blocs=None):
    """Renders a piece of the YAML. A work-specific type is added in blocs.PIECES (field name -> function)."""
    for champ, fn in (getattr(blocs, "PIECES", {}) if blocs else {}).items():
        if champ in p: return fn(p, Y, D, S)
    corps = '<h2 class="ph">%s</h2>' % fmt(p["nom"], S)
    if "renvoi" in p:
        if "fiches" in p: return corps + fiches(Y[p["renvoi"]], p, S)
        lib = p.get("libelles", {}); cols = list(lib) or list(Y[p["renvoi"]][0])
        return corps + tableau([lib.get(c, c) for c in cols], [[", ".join(map(str, r[c])) if isinstance(r[c], list) else r[c] for c in cols] for r in Y[p["renvoi"]]], S)
    if "etapes" in p: return corps + chaine(p["etapes"], S, p.get("disposition") == "verticale")
    if "colonnes" in p:
        corps += tableau(p["colonnes"], p["lignes"], S, p.get("totaux"), p.get("total_poids"))
        if p.get("note_table"): corps += '<p class="note">%s</p>' % fmt(p["note_table"], S)
    if "arrows" in p: corps += '<div class="arrows">%s</div>' % "".join('<span class="chev light">%s</span>' % fmt(a, S) for a in p["arrows"])
    if "graphique" in p: corps += '<div class="graph">%s<p class="gsrc">%s</p></div>' % (graphique(p["graphique"], D, S), fmt(p["graphique"].get("note", ""), S))
    return corps

def sources_html(pg, S):
    li = "".join("<li>%s</li>" % fmt(s, S) for s in pg.get("sources", []))
    hyp = '<p class="hyps">%s: %s</p>' % (html.escape(S["libelles"]["hypotheses"]), ", ".join(html.escape(h) for h in pg["hypotheses"])) if pg.get("hypotheses") else ""
    return '<div class="srcl">%s</div><ul>%s</ul>%s' % (html.escape(S["libelles"]["sources"]), li, hyp)

# ---------------------------------------------------------------- shared CSS (tokens and blocks)
def css_plus(p):
    """Titles font family (setting `polices.titres`) and the strip of the parts: added to the base CSS."""
    t = p["titres"]
    faces = "".join('@font-face{font-family:"%s";font-weight:%s;src:url(../%s)}' % (t["famille"], w, f) for w, f in t["fichiers"].items()) if t["famille"] else ""
    reg = 'h1,.ph,.tile b,.chev{font-family:"%s",sans-serif}' % t["famille"] if t["famille"] else ""
    return faces + reg + ".frise{display:flex;gap:14px;font-size:var(--tl);letter-spacing:.04em;color:var(--encre-secondaire)}.frise i{font-style:normal;padding-bottom:1px}.frise i.on{color:var(--accent-fonce);font-weight:700;border-bottom:2px solid var(--accent)}"

def css_base(S, R, echelle, type_):
    d = S["densite"][type_]; p = S["polices"]
    faces = "".join('@font-face{font-family:"%s";font-weight:%s;src:url(../%s)}' % (p["famille"], w, f) for w, f in p["fichiers"].items())
    root = ";".join("--%s:%s" % (k, v) for k, v in R.items())
    ser = "".join(".ser%d{border-top:3px solid var(--s%d);color:var(--s%d-fonce);padding-top:4px}.tser%d{color:var(--s%d-fonce)}" % (i, i, i, i, i) for i in range(len(S["couleurs"]["series"])))
    return faces + """
:root{%s;--r:6px;--t:%spx;--tc:%spx;--ts:%spx;--tl:%spx;--t1:%spx;--il:%s}
*{box-sizing:border-box;margin:0;padding:0;print-color-adjust:exact;-webkit-print-color-adjust:exact}
html{font-synthesis:none;background:var(--fond)}
body{font:400 var(--t)/var(--il) "%s",sans-serif;color:var(--encre);background:var(--fond)}
.sheet>*{flex-shrink:0}
h1{font-weight:700;font-size:var(--t1);line-height:1.12;text-wrap:balance;letter-spacing:-.005em}
.texte p{line-height:var(--il);margin:0 0 .36em;text-wrap:pretty}
.texte .item{padding-left:1.15em;text-indent:-1.15em}
.texte .formule{background:var(--accent-clair);padding:.4em .7em;font-weight:700;border-radius:var(--r);margin:.3em 0 .6em}
.texte.c2{column-count:2;column-gap:1.6em}.texte.c2 p{orphans:2;widows:2}
.nb{white-space:nowrap}
.points{list-style:none;margin:0 0 .6em}.points li{margin:0 0 .45em;padding-left:1.1em;text-indent:-1.1em;line-height:var(--il)}
.points li::before{content:"";display:inline-block;width:.45em;height:.45em;margin-right:.65em;background:var(--accent);vertical-align:.08em}
sup.hyp{font-size:.62em;font-weight:700;color:var(--encre-secondaire);vertical-align:super;line-height:0;white-space:nowrap}
.tag{font-weight:700;font-size:.88em;letter-spacing:.03em;color:var(--accent-2)}
.fig img{display:block;width:100%%;height:auto}
.fig figcaption{font-size:var(--tl);line-height:1.3;color:var(--encre-secondaire);margin-top:4px}
.ph{font-size:calc(var(--tc)*1.12);font-weight:700;color:var(--accent-2);margin:.45em 0 .2em}
table{width:100%%;border-collapse:collapse;font-size:var(--tc);line-height:1.3;font-variant-numeric:tabular-nums;break-inside:avoid}
th{font-weight:700;text-align:left;vertical-align:bottom;padding:.35em .8em .35em 0;border-bottom:1.5px solid var(--encre);line-height:1.25}
td{padding:.14em .8em .14em 0;vertical-align:top;border-bottom:.75px solid var(--filet)}
td:first-child{font-weight:700}th:last-child,td:last-child{padding-right:0}
.num{text-align:right;white-space:nowrap}
%s
tr.tot td{font-weight:700;border-top:1.5px solid var(--encre);border-bottom:0}tr.tot td.tl{text-align:right}
.note{font-size:calc(var(--tc)*.96);line-height:1.35;color:var(--encre-secondaire);margin-top:.4em}
.chain{display:grid;gap:3px}
.chev{background:var(--accent-2);color:var(--blanc-chaud);font-weight:700;font-size:calc(var(--tc)*.98);letter-spacing:.05em;text-align:center;padding:.55em .9em .55em 1.3em;
  clip-path:polygon(0 0,calc(100%% - .9em) 0,100%% 50%%,calc(100%% - .9em) 100%%,0 100%%,.9em 50%%);white-space:nowrap}
.chev.light{background:var(--accent-clair);color:var(--encre);display:inline-block;margin-right:3px}
.cstep p{font-size:calc(var(--tc)*.95);line-height:1.25;margin-top:3px;padding-right:4px}.cstep p.ref{font-weight:700;color:var(--accent-fonce)}
.vchain .vrow{display:grid;grid-template-columns:12em 1fr 1.2fr;gap:12px;align-items:center;padding:.15em 0;border-bottom:.75px solid var(--filet);font-size:var(--tc);line-height:1.3}
.vchain .chev{padding:.35em .9em .35em 1.3em}
.arrows{margin-top:6px;display:flex;gap:2px}.arrows .chev{font-size:calc(var(--tc)*.88);margin:0}
.tuiles{display:grid;gap:7px}
.tile{padding:.6em .8em .5em;border-radius:var(--r);display:flex;flex-direction:column;gap:2px;justify-content:flex-end}
.tile b{font-size:2.1em;line-height:1.05;font-weight:700;white-space:nowrap}.tile span{font-size:var(--tc);line-height:1.25}
.t-principal{background:var(--accent-2);color:var(--blanc-chaud)}.t-secondaire{background:var(--accent);color:var(--encre)}.t-clair{background:var(--accent-clair);color:var(--encre)}
.graph svg{display:block;width:100%%;height:auto}.graph text{font-family:"%s",sans-serif}
.gl{font-size:12.5px;font-weight:700}.gl2{font-size:10.7px;fill:var(--encre)}.gv{font-size:11px;font-weight:700;fill:var(--encre);font-variant-numeric:tabular-nums}
.gsrc{font-size:var(--tl);color:var(--encre-secondaire);margin-top:4px}
.bas{background:var(--accent-clair);border-top:2px solid var(--accent);border-radius:var(--r);padding:.35em .85em;font-weight:700;line-height:1.3;margin:3px 0 2px}
.sources{font-size:var(--ts);line-height:1.25;color:var(--encre-secondaire)}
.sources ul{list-style:none;column-count:2;column-gap:22px}.sources li{break-inside:avoid;margin-bottom:1px}
.srcl{font-weight:700;letter-spacing:.1em;color:var(--accent-fonce);margin-bottom:1px;text-transform:uppercase}
.hyps{margin-top:2px}
.registre .hyp{display:grid;grid-template-columns:128px 1fr;gap:14px;padding:6px 0;border-bottom:.75px solid var(--filet);font-size:var(--tc);line-height:1.3}
.registre .hid{display:flex;flex-direction:column;gap:1px}.registre .hid b{font-size:1.12em}
.registre .hval{font-weight:700;color:var(--accent-fonce)}.registre .hobj{font-size:.96em;color:var(--encre-secondaire)}
.registre p{margin:0 0 1px}.sep{display:inline-block;width:1px;height:10px;background:var(--filet);margin:0 9px;vertical-align:-1px}
.regle{flex:1;height:2px;background:var(--filet)}
""" % (root, d["corps"], d["cellule"], d["source"], d["legende"], d["titre"], d["interligne"], p["famille"], ser, p["famille"]) + css_plus(p)

# ---------------------------------------------------------------- planned sheets (reglages.yaml, otherwise one per page)
def plan_feuilles(S, Y):
    f = S["feuilles"] or [{"page": i + 1} for i in range(len(Y["pages"]))]
    for x in f:
        pg = Y["pages"][x["page"] - 1]
        if not x.get("suite"): x.setdefault("gabarit", pg.get("gabarit", "synthese"))
        elif "gabarit" not in x: x["gabarit"] = "tableau"
        if not x.get("suite") and pg.get("gabarit") and pg["gabarit"] != x["gabarit"]:
            raise SystemExit(m("gabarit_yaml", p=x["page"], y=pg["gabarit"], r=x["gabarit"]))
    return f

# ---------------------------------------------------------------- measure and render (Playwright)
MESURE_JS = r"""() => {
 const R = {fonts: [...document.fonts].map(f => f.family + ':' + f.weight + ':' + f.status), sheets: []};
 document.querySelectorAll('.sheet').forEach(s => {
  const sr = s.getBoundingClientRect(), main = s.querySelector('.main'), bot = s.querySelector('.bottom');
  const mb = main ? main.getBoundingClientRect().bottom - sr.top : 0, bt = bot ? bot.getBoundingClientRect().top - sr.top : sr.height;
  const h1 = s.querySelector('h1'); let lines = 0;
  if (h1) lines = Math.round(h1.getBoundingClientRect().height / parseFloat(getComputedStyle(h1).lineHeight));
  const photos = [...s.querySelectorAll('img.photo')].map(i => {const r = i.getBoundingClientRect(); return [r.left - sr.left, r.top - sr.top, r.width, r.height]});
  const wide = []; s.querySelectorAll('.main *, .bottom *').forEach(e => {const r = e.getBoundingClientRect();
    if (r.width > 0 && (r.right > sr.right - 4 || r.left < sr.left + 4) && !e.closest('.plein')) wide.push(e.tagName + '.' + e.className)});
  const mins = {}, cats = {'.texte p': 'corps', 'td': 'cellule', '.sources li': 'source', '.fig figcaption': 'legende'};
  for (const sel in cats) {let v = 99; s.querySelectorAll(sel).forEach(e => {v = Math.min(v, parseFloat(getComputedStyle(e).fontSize))}); mins[cats[sel]] = v;}
  R.sheets.push({f: s.dataset.f, p: s.dataset.p, over: s.scrollHeight - s.clientHeight, gap: Math.round(bt - mb), h: sr.height, h1lines: lines, photos: photos, wide: wide.slice(0, 4), mins: mins});
 });
 return R;
}"""

def chromium_args():
    """Playwright's Chromium, otherwise a Chromium from the cache (P6.16)."""
    mots = ("chrome-headless-shell", "chrome", "Chromium")
    for base in ("~/Library/Caches/ms-playwright", "~/.cache/ms-playwright", "~/AppData/Local/ms-playwright"):
        for f in sorted(glob.glob(os.path.expanduser(base) + "/**/*", recursive=True), reverse=True):
            if os.path.isfile(f) and os.access(f, os.X_OK) and os.path.basename(f) in mots and "headless_shell" in f: return {"executable_path": f}
    return {}

def rendre(html_path, sortie, largeur, hauteur, pages=None):
    """Measures the layout, then prints the PDF (page_ranges = requested sheets). Returns the measure report."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        try: nav = pw.chromium.launch()
        except Exception: nav = pw.chromium.launch(**chromium_args())
        pg = nav.new_page(viewport={"width": largeur, "height": hauteur})
        pg.goto("file://" + html_path); pg.wait_for_load_state("load")
        pg.evaluate("document.fonts.ready.then(() => 1)")
        rep = pg.evaluate(MESURE_JS)
        pg.pdf(path=sortie, prefer_css_page_size=True, print_background=True, outline=True, tagged=True, page_ranges=",".join(map(str, pages)) if pages else "")
        nav.close()
    return rep

def fautes_mesure(rep, lh, feuilles=None):
    fautes = []
    for f in rep["fonts"]:
        if f.endswith(":error"): fautes.append(m("police", x=f))
    for s in rep["sheets"]:
        if feuilles and int(s["f"]) not in feuilles: continue
        if s["over"] > 1: fautes.append(m("deborde", f=s["f"], p=s["p"], px=s["over"], lignes=max(1, round(s["over"] / lh))))
        if s["wide"]: fautes.append(m("large", f=s["f"], e=s["wide"]))
    return fautes

# ---------------------------------------------------------------- ETAT.md: sheet ceiling, render counter (PI.31)
def plafond_feuilles():
    """(min, max) of `PAGES PROMISED: 8 to 10`, or None if \"no ceiling\", or False if the heading is missing."""
    if not os.path.exists(ETAT): return False
    t = re.search(r"PAGES PROMIS\w+\s*:\s*(.+)", open(ETAT, encoding="utf-8").read())
    if not t: return False
    n = [int(x) for x in re.findall(r"\d+", t.group(1))]
    return (min(n), max(n)) if n else None

def compteur(incrementer=False, audit=False):
    """RENDUS COMPLETS counter of ETAT.md. The first two renders serve the first cycle; the 3rd is reserved for phase 8 (`audit=True`)."""
    if not os.path.exists(ETAT): return 0
    t = open(ETAT, encoding="utf-8").read(); mt = re.search(r"(RENDUS COMPLETS|FULL RENDERS) : (\d+) / 3", t)
    if not mt: return 0
    n = int(mt.group(2))
    if incrementer:
        if n >= 3: raise SystemExit(m("rendus"))
        if n >= 2 and not audit: raise SystemExit(m("reserve"))
        open(ETAT, "w", encoding="utf-8").write(t.replace(mt.group(0), "%s : %d / 3" % (mt.group(1), n + 1)))
    return n

def compteur_annuler():
    """A render that crashes before writing its PDF is not counted (PI.31): otherwise the counter exceeds the PDFs of rendus/."""
    t = open(ETAT, encoding="utf-8").read(); mt = re.search(r"(RENDUS COMPLETS|FULL RENDERS) : (\d+) / 3", t)
    if mt and int(mt.group(2)) > 0: open(ETAT, "w", encoding="utf-8").write(t.replace(mt.group(0), "%s : %d / 3" % (mt.group(1), int(mt.group(2)) - 1)))

def rendus_complets():
    """Full PDFs of rendus/ (neither single pages nor the contact sheet): the gate compares them to the counter (PI.31)."""
    return sorted(x for x in glob.glob(os.path.join(RENDUS, "*.pdf")) if not os.path.basename(x).startswith("pages-"))

# ---------------------------------------------------------------- outputs: livrable.txt, contact sheet, page replacement
def detail_chargees(d, feuilles=None):
    """What to cut to get under the ceiling: continuation sheets first, then the heaviest sheets."""
    suites = ", ".join("%d (page %d)" % (k, f["page"]) for k, f in enumerate(feuilles or [], 1) if f.get("suite")) or "aucune"
    mots = ", ".join("%d (%d mots)" % (i, w) for w, i in sorted(((len(p.get_text().split()), i + 1) for i, p in enumerate(d)), reverse=True)[:3])
    return m("detail", suites=suites, mots=mots)

def livrable_txt(pdf):
    d = pymupdf.open(pdf)
    open(os.path.join(T, "livrable.txt"), "w", encoding="utf-8").write("\n".join("=== page %d ===\n%s" % (i + 1, p.get_text()) for i, p in enumerate(d))); d.close()

def pngs(pdf, dossier, dpi=110, numeros=None):
    d = pymupdf.open(pdf); os.makedirs(dossier, exist_ok=True); out = []
    for i, p in enumerate(d):
        f = os.path.join(dossier, "p%02d.png" % (numeros[i] if numeros else i + 1)); p.get_pixmap(dpi=dpi).save(f); out.append(f)
    d.close(); return out

def planche(pdf, sortie, cols=6, larg=300):
    """Contact sheet of thumbnails: what the lead and the agents read in Express (P6.2, PI.31)."""
    d = pymupdf.open(pdf); r = d[0].rect.height / d[0].rect.width; hh = int(larg * r); pad = 12
    im = Image.new("RGB", (cols * (larg + pad) + pad, math.ceil(len(d) / cols) * (hh + pad) + pad), (120, 110, 122))
    for i, p in enumerate(d):
        pix = p.get_pixmap(dpi=int(2 * larg * 72 / p.rect.width))
        t = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).resize((larg, hh), Image.LANCZOS)
        im.paste(t, (pad + (i % cols) * (larg + pad), pad + (i // cols) * (hh + pad)))
    im.save(sortie); d.close(); return sortie

def remplacer(livre, partiel, pages):
    """Recipe of P6.2: PyMuPDF replaces each page in the delivered PDF, outline and metadata kept."""
    doc, part = pymupdf.open(livre), pymupdf.open(partiel)
    toc, meta = doc.get_toc(), doc.metadata
    for i, n in enumerate(pages):
        doc.delete_page(n - 1); doc.insert_pdf(part, from_page=i, to_page=i, start_at=n - 1)
    doc.set_toc(toc); doc.set_metadata(meta)
    doc.save(livre + ".tmp", garbage=4, deflate=True); doc.close(); part.close(); os.replace(livre + ".tmp", livre)

def metadonnees(pdf, S, titre):
    d = pymupdf.open(pdf); doc = S["document"]
    d.set_metadata({"title": titre, "author": doc["auteur"], "subject": doc["sujet"], "creator": "gabarits/commun.py"})
    d.save(pdf + ".tmp", garbage=4, deflate=True); d.close(); os.replace(pdf + ".tmp", pdf)

# ---------------------------------------------------------------- orchestration shared by the three templates
def main(construire, largeur, hauteur, type_, planche_cols, argv=None, apres=None):
    """construire() -> (html_path, sheets [dicts of reglages.yaml], title). Handles --pages, the render counter, the gate (controles.py), delivery.
    apres(delivered_pdf, report, sheets), optional, produces the other formats (PPTX)."""
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", help="sheet numbers to render alone, e.g. 4,7 (outside the full-render counter)")
    ap.add_argument("--audit", action="store_true", help="phase 8: lifts the reserve of the 3rd full render (PI.31)")
    a = ap.parse_args(argv)
    S = reglages(); d = S["densite"][type_]; lh = d["corps"] * d["interligne"]; os.makedirs(RENDUS, exist_ok=True); os.makedirs(LIVRAISON, exist_ok=True); os.makedirs(BUILD, exist_ok=True)
    path, feuilles, titre = construire()
    nom = S["document"]["nom_fichier"]; livre = os.path.join(LIVRAISON, nom + ".pdf")
    sel = [int(x) for x in a.pages.split(",")] if a.pages else None
    if sel:
        sel = sorted(set(sel)); hors = [x for x in sel if not 1 <= x <= len(feuilles)]
        if hors: raise SystemExit(m("hors", x=hors[0], n=len(feuilles)))
        if len(sel) == len(feuilles): raise SystemExit(m("toutes", n=len(feuilles)))   # all sheets = a full render: it goes through the counter
    if sel:   # partial render: not in the counter nor among the full renders of rendus/
        sortie = os.path.join(RENDUS, "pages-" + "-".join(map(str, sel)) + ".pdf")
        rep = rendre(path, sortie, largeur, hauteur, sel)
        png = pngs(sortie, sortie[:-4], numeros=sel); fautes = fautes_mesure(rep, lh, sel)
        if os.path.exists(livre) and not fautes:
            n = len(pymupdf.open(livre))
            if n != len(feuilles): fautes.append(m("remplacement", a=n, b=len(feuilles)))
            else:
                remplacer(livre, sortie, sel); livrable_txt(livre)
                if apres: apres(livre, rep, feuilles)
        print("pages %s rendered: %s" % (sel, " ".join(png)))
    else:
        n = compteur(incrementer=True, audit=a.audit)
        sortie = os.path.join(RENDUS, "%s_r%d_%s.pdf" % (nom, n + 1, datetime.datetime.now().strftime("%Y%m%d-%H%M%S")))
        try: rep = rendre(path, sortie, largeur, hauteur); metadonnees(sortie, S, titre)
        except BaseException: compteur_annuler(); raise
        json.dump(rep, open(os.path.join(BUILD, "mesure.json"), "w"))
        livrable_txt(sortie); pl = planche(sortie, os.path.join(RENDUS, "planche.png"), cols=planche_cols)
        print("full render %d / 3: %s, %d sheet(s), %.2f MB\ncontact sheet: %s" % (n + 1, sortie, len(pymupdf.open(sortie)), os.path.getsize(sortie) / 1e6, pl))
        import controles   # the phase 6 gate: sheet ceiling, numbers, images, overflows
        fautes = ["controles.py"] if controles.main(["controles.py", sortie]) else []
        if not fautes: import shutil; shutil.copy(sortie, livre)
        if apres and not fautes: apres(sortie, rep, feuilles)
        sys.exit(1 if fautes else 0)
    if fautes:
        print("FAILED: %d fault(s)" % len(fautes)); [print("  - " + x) for x in fautes]; sys.exit(1)
    print("OK")
