# Who reads it, and when: `diapo-fabricant`, never in full: he copies this file as <subfolder>/travail/build.py (with commun.py, controles.py, reglages.yaml) and edits only reglages.yaml, plus blocs.py for a work-specific block.
"""document_a4.py: 02_contenu.yaml to A4 portrait HTML to PDF (Chromium via Playwright).

  python build.py                 full render (counter FULL RENDERS in ETAT.md, refused beyond 3);
                                  fails if the sheets exceed PAGES PROMISED (P6.23) or if a sheet overflows
  python build.py --pages 4,7     renders only sheets 4 and 7 (outside the counter), replaces them in livraison/
  Writes rendus/<name>_<timestamp>.pdf, rendus/planche.png (read it instead of the pages), livraison/<name>.pdf, livrable.txt.

The YAML carries all the text and all the numbers; reglages.yaml carries colors, fonts, density and the sheet plan
(`feuilles:`); a piece of a work-specific type is declared in blocs.py (PIECES = {field: function}).
Page fields read in addition to those of P2.1: `etape` (banner label), `tuiles`, `images` ({fichier, alt, credit}).
Templates: couverture, synthese (text and pieces), image (photo or diptych), tableau, decision. `points: true` in a sheet: the `points` list of the YAML replaces the body.
"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import *
try: import blocs
except ImportError: blocs = None

def css_a4(S, R):
    d = S["densite"]["a4"]
    return css_base(S, R, d, "a4") + """
@page{size:210mm 297mm;margin:0}
:root{--m:%smm}
.sheet{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;display:flex;flex-direction:column;padding:0 var(--m);background:var(--fond)}
.sig{position:absolute;left:0;right:0;top:0;height:8px;background:var(--accent-2);border-bottom:3px solid var(--accent)}
.top{display:flex;flex-direction:row-reverse;justify-content:space-between;align-items:center;margin-top:13px;height:26px}
.logo{height:26px;width:auto;display:block}
.etape{font-size:11.5px;font-weight:700;letter-spacing:.14em;color:var(--encre-secondaire)}
h1{margin:8px 0 8px;max-width:640px}
.suite h1{font-size:21px}
.main{flex:0 0 auto}
.texte p{font-size:var(--t)}
.grid{display:grid;grid-template-columns:1fr 2fr;gap:22px;align-items:start}.grid.dual{margin:6px 0 4px}
.rail,.droite{min-width:0}
.dipt{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:0 0 6px}.dipt .fig img{height:110px;object-fit:cover}
.piece{margin-top:4px}
.tuiles{margin:2px 0 12px}
.bandeau{background:var(--accent-2);color:var(--blanc-chaud);margin:8px calc(-1 * var(--m)) 12px;padding:13px var(--m) 11px}.bandeau h1{margin:0;color:var(--blanc-chaud)}
.bandeau.clair{background:var(--accent-clair);margin:6px calc(-1 * var(--m)) 10px;padding:9px var(--m) 8px}.bandeau.clair h1{color:var(--encre)}
.bandeau.slab{margin-bottom:0;padding-bottom:12px}
.slabtiles{background:var(--accent-2);margin:0 calc(-1 * var(--m)) 10px;padding:0 var(--m) 12px}.slabtiles .tuiles{margin:0}
.slabtiles .t-principal{background:var(--accent);color:var(--encre)}.slabtiles .t-clair{background:var(--blanc-chaud)}
.cont{background:var(--accent-clair);margin:8px calc(-1 * var(--m)) 8px;padding:10px var(--m)}.cont h1{font-size:13px;line-height:1.2;margin:0;color:var(--encre-secondaire);letter-spacing:.06em}
.g-decision .texte p{margin-bottom:3px}.g-decision .piece{margin-top:2px}
.dense table{font-size:calc(var(--tc)*1.0)}.dense td{padding:.1em .7em .1em 0}
.roomy table{font-size:calc(var(--tc)*1.13)}.roomy td{padding:.55em .8em .55em 0}.roomy th{font-size:calc(var(--tc)*1.06)}
.bottom{margin-top:auto;padding-bottom:26px}
.bas{font-size:var(--t);margin:3px 0 2px}
.pied{position:absolute;left:var(--m);right:var(--m);bottom:11px;display:flex;align-items:center;gap:10px}.pied .num{font-size:11.5px;font-weight:700}
.g-couverture .colonne{position:absolute;left:0;right:0;bottom:0;height:372px;background:var(--accent-2)}
.g-couverture .pack{position:absolute;right:26px;bottom:34px;width:440px;height:auto;display:block}
.g-couverture .credit{font-size:9.5px;color:var(--blanc-chaud);position:absolute;bottom:12px;right:26px;width:440px;text-align:right}
.g-couverture .main,.g-couverture .top,.g-couverture .bottom{position:relative;z-index:2}
.g-couverture h1{font-size:54px;line-height:1.06;margin:30px 0 24px;max-width:690px;letter-spacing:-.01em}
.g-couverture .top{margin-top:30px;flex-direction:row;height:64px}.g-couverture .logo{height:64px}
.g-couverture .gauche{width:440px}.g-couverture .gauche p{font-size:var(--t);margin-bottom:8px;line-height:1.33}
.g-couverture .bas{margin:14px 0 0}
.g-couverture .bottom{padding-bottom:22px;width:250px;color:var(--blanc-chaud)}
.g-couverture .sources{color:var(--blanc-chaud)}.g-couverture .srcl,.g-couverture .sources .tag{color:var(--accent)}.g-couverture .sources ul{column-count:1}
""" % d["marge_mm"]

def couverture(pg, num, S):
    im = S["images"]; fmt_ = lambda t: fmt(t, S)
    paras = [p for p in pg["corps"].strip().split("\n\n") if p.strip()]
    logo = '<img class="logo" src="%s" alt="%s">' % (image(im["logo"], S), html.escape(im["logo_alt"])) if im["logo"] else ""
    pack = ('<img class="pack photo" src="%s" alt="%s"><p class="credit">%s</p>' % (image(im["couverture"], S), html.escape(im["couverture_alt"]), html.escape(im["couverture_credit"]))) if im["couverture"] else ""
    return ('<section class="sheet g-couverture" data-f="%s" data-p="1"><div class="sig"></div><div class="colonne plein">%s</div>'
            '<header class="top">%s</header><main class="main cov"><h1>%s</h1><div class="gauche texte">%s<div class="bas">%s</div></div></main>'
            '<div class="bottom"><div class="sources">%s</div></div></section>') % (
            num, pack, logo, fmt_(pg["titre"]), "".join("<p>%s</p>" % fmt_(p) for p in paras), fmt_(pg["bas"]), sources_html(pg, S))

def feuille(f, k, Y, D, S):
    pg = Y["pages"][f["page"] - 1]; g = f["gabarit"]; num = "%d%s" % (f["page"], f.get("lettre", ""))
    if g == "couverture": return couverture(pg, k, S)
    im = S["images"]
    classes = "sheet g-%s%s%s%s" % (g, " suite" if f.get("suite") else "", " roomy" if f.get("roomy") else "", " dense" if f.get("dense") else "")
    logo = '<img class="logo" src="%s" alt="%s">' % (image(im["logo"], S), html.escape(im["logo_alt"])) if im["logo"] else ""
    top = '<div class="sig"></div><header class="top">%s<div class="meta"><span class="etape">%s</span></div></header>' % (logo, html.escape(pg.get("etape", "")))
    if f.get("suite"): h1 = '<div class="cont"><h1>%s</h1></div>' % html.escape(S["libelles"]["suite"])
    else: h1 = '<div class="bandeau%s"><h1>%s</h1></div>' % (" slab" if f.get("rupture") else ("" if g == "decision" else " clair"), fmt(pg["titre"], S))
    body = ""
    P = lambda i: '<section class="piece">%s</section>' % piece(pg["pieces"][i], Y, D, S, blocs)
    rail = lambda r: figure(pg["images"][r["image"]], S) if "image" in r else '<div class="graph">%s</div>' % piece(pg["pieces"][r["piece"]], Y, D, S, blocs)
    if not f.get("suite"):
        if f.get("tuiles") and pg.get("tuiles"): body += '<div class="slabtiles plein">%s</div>' % tuiles(pg["tuiles"], S) if f.get("rupture") else tuiles(pg["tuiles"], S)
        if f.get("diptyque"): body += '<div class="dipt">%s%s</div>' % (figure(pg["images"][0], S), figure(pg["images"][1], S))
        txt = liste_points(pg, S) if f.get("points") and pg.get("points") else paragraphes(pg["corps"], S); c2 = " c2" if f.get("colonnes", 1) == 2 else ""
        if f.get("rail") and f.get("rail_pos", "texte") == "texte":
            body += '<div class="grid"><aside class="rail">%s</aside><div class="texte%s">%s</div></div>' % (rail(f["rail"]), c2, txt)
        else: body += '<div class="texte%s">%s</div>' % (c2, txt)
        if f.get("rail") and f.get("rail_pos") == "pieces":
            body += '<div class="grid dual"><aside class="rail">%s</aside><div class="droite">%s</div></div>' % (rail(f["rail"]), "".join(P(i) for i in f.get("droite", [])))
    for i in f.get("pieces", []): body += P(i)
    bot = ""
    if f.get("fin"): bot += '<div class="bas">%s</div><div class="sources">%s</div>' % (fmt(pg["bas"], S), sources_html(pg, S))
    bot += '<div class="pied"><span class="num">%s</span><span class="regle"></span></div>' % num
    return '<section class="%s" data-f="%d" data-p="%d">%s%s<main class="main">%s</main><div class="bottom">%s</div></section>' % (classes, k, f["page"], top, h1, body, bot)

def plan(S, Y):
    fe = plan_feuilles(S, Y)
    for i, f in enumerate(fe):
        if "pieces" not in f and not f.get("suite"):
            f["pieces"] = [j for j in range(len(Y["pages"][f["page"] - 1].get("pieces", []))) if j not in ({f["rail"].get("piece")} if f.get("rail") else set()) | set(f.get("droite", []))]
        f["fin"] = f.get("fin", not (i + 1 < len(fe) and fe[i + 1].get("suite") and fe[i + 1]["page"] == f["page"]))
        if f.get("suite"): f["lettre"] = chr(ord("a") + sum(1 for x in fe[:i] if x["page"] == f["page"]))
    return fe

def construire():
    S = reglages(); Y, D = charger(); R = roles(S); fe = plan(S, Y)
    titre = S["document"]["titre"] or Y["pages"][0]["titre"]
    corps = "\n".join(feuille(f, k + 1, Y, D, S) for k, f in enumerate(fe))
    page = '<!doctype html><html lang="%s"><head><meta charset="utf-8"><title>%s</title><style>%s%s</style></head><body>%s</body></html>' % (
        S["document"]["langue"], html.escape(titre), css_a4(S, R), getattr(blocs, "CSS", ""), corps)
    path = os.path.join(BUILD, "livrable.html"); os.makedirs(BUILD, exist_ok=True); open(path, "w", encoding="utf-8").write(page)
    return path, fe, titre

if __name__ == "__main__":
    main(construire, 794, 1123, "a4", 6)
