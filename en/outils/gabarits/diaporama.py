# Who reads it, and when: `diapo-fabricant`, never in full: he copies this file as <subfolder>/travail/build.py (with commun.py, controles.py, reglages.yaml) and edits only reglages.yaml, plus blocs.py for a work-specific block.
"""diaporama.py: 02_contenu.yaml to 16:9 HTML (1920 x 1080) to PDF, plus a faithful PPTX (P6.3: one 3840 x 2160 image per slide).

  python build.py                 full render (counter FULL RENDERS in ETAT.md, refused beyond 3);
                                  fails if the slides exceed PAGES PROMISED (P6.23) or if one overflows
  python build.py --pages 4,7     renders only slides 4 and 7 (outside the counter), replaces them in livraison/ (PDF and PPTX)
  Writes rendus/<name>_<timestamp>.pdf, rendus/planche.png (read it instead of the pages), livraison/<name>.pdf and .pptx, livrable.txt.

A slide carries few words: `points` (list of short sentences) or, failing that, a `corps` of at most `densite.diaporama.mots_max`
words (reglages.yaml), otherwise the render fails and says which page to cut. The slide plan is `feuilles:` of reglages.yaml
(one page of the YAML can have several slides: `suite: true`).
Templates: couverture, synthese (text and pieces), image (photo or diptych), tableau, decision; `rupture: true`: color slab.
Page fields read in addition to those of P2.1: `points`, `etape`, `tuiles`, `images` ({fichier, alt, credit}); `notes` goes into the PPTX notes.
"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import *
try: import blocs
except ImportError: blocs = None

def css_diapo(S, R):
    return css_base(S, R, None, "diaporama") + """
@page{size:1920px 1080px;margin:0}
:root{--m:%spx}
.sheet{width:1920px;height:1080px;position:relative;overflow:hidden;break-after:page;display:flex;flex-direction:column;padding:0 var(--m);background:var(--fond)}
.sig{position:absolute;left:0;right:0;top:0;height:16px;background:var(--accent-2);border-bottom:5px solid var(--accent)}
.top{display:flex;flex-direction:row-reverse;justify-content:space-between;align-items:center;margin-top:40px;height:46px}
.logo{height:46px;width:auto;display:block}
.etape{font-size:var(--tl);font-weight:700;letter-spacing:.14em;color:var(--encre-secondaire)}
h1{margin:0;max-width:1500px}
.bandeau{background:var(--accent-clair);margin:22px calc(-1 * var(--m)) 30px;padding:24px var(--m) 22px}
.g-decision .bandeau,.rupture .bandeau{background:var(--accent-2);color:var(--blanc-chaud)}.g-decision .bandeau h1,.rupture .bandeau h1{color:var(--blanc-chaud)}
.main{flex:0 0 auto}
.cols{display:grid;grid-template-columns:5fr 7fr;gap:56px;align-items:start}
.cols.demi{grid-template-columns:1fr 1fr}.cols.un{grid-template-columns:1fr}
.col{min-width:0}
.piece{margin-top:14px}
.tuiles{margin:0 0 24px}.tuiles.grand .tile b{font-size:3.2em}.tuiles.grand .tile{min-height:190px}
.tile b{font-size:2.3em}
.fig img{height:520px;object-fit:cover}.fig.demi img{height:520px}
.dipt{display:grid;grid-template-columns:1fr 1fr;gap:28px}.dipt .fig img{height:380px;object-fit:cover}
.bottom{margin-top:auto;padding-bottom:50px}
.bas{font-size:calc(var(--t)*.92);margin:0 0 12px}
.g-decision .bas{font-size:calc(var(--t)*1.08)}
.sources ul{column-count:3}
.pied{position:absolute;left:var(--m);right:var(--m);bottom:16px;display:flex;align-items:center;gap:20px}.pied .num{font-size:var(--tl);font-weight:700}
.rupture{background:var(--accent-2);color:var(--blanc-chaud)}
.rupture .top .etape{color:var(--accent)}.rupture .sig{background:var(--accent)}
.rupture .texte p,.rupture .points li{color:var(--blanc-chaud)}.rupture .bas{background:transparent;color:var(--blanc-chaud);border-top:3px solid var(--accent)}
.rupture .sources,.rupture .pied .num{color:var(--blanc-chaud)}.rupture .srcl{color:var(--accent)}.rupture .regle{background:var(--accent)}
.rupture .t-clair{background:var(--blanc-chaud)}.rupture .t-principal{background:var(--accent);color:var(--encre)}
.g-couverture .colonne{position:absolute;right:0;top:0;bottom:0;width:760px;background:var(--accent-2)}
.g-couverture .pack{position:absolute;right:60px;bottom:120px;width:640px;height:auto}
.g-couverture .credit{position:absolute;right:60px;bottom:50px;width:640px;text-align:right;font-size:var(--tl);color:var(--blanc-chaud)}
.g-couverture .main,.g-couverture .top,.g-couverture .bottom{position:relative;z-index:2;width:1000px}
.g-couverture h1{font-size:92px;line-height:1.06;margin:70px 0 36px;max-width:1000px}
.g-couverture .top{flex-direction:row;height:86px;margin-top:60px}.g-couverture .logo{height:86px}
.g-couverture .sources ul{column-count:1}.g-couverture .bas{margin-top:20px}
""" % S["densite"]["diaporama"]["marge_px"]

def texte(pg, S, p):
    if pg.get("points"): return liste_points(pg, S)
    n, mx = nb_mots(pg.get("corps", "")), S["densite"]["diaporama"]["mots_max"]
    if n > mx: raise SystemExit(m("mots", p=p, n=n, max=mx))
    return '<div class="texte">%s</div>' % paragraphes(pg["corps"], S) if pg.get("corps") else ""

def couverture(pg, k, S):
    im = S["images"]
    logo = '<img class="logo" src="%s" alt="%s">' % (image(im["logo"], S), html.escape(im["logo_alt"])) if im["logo"] else ""
    pack = ('<img class="pack photo" src="%s" alt="%s"><p class="credit">%s</p>' % (image(im["couverture"], S), html.escape(im["couverture_alt"]), html.escape(im["couverture_credit"]))) if im["couverture"] else ""
    return ('<section class="sheet g-couverture" data-f="%d" data-p="1"><div class="sig"></div><div class="colonne plein">%s</div><header class="top">%s</header>'
            '<main class="main"><h1>%s</h1>%s<div class="bas">%s</div></main><div class="bottom"><div class="sources">%s</div></div></section>') % (
            k, pack, logo, fmt(pg["titre"], S), texte(pg, S, 1), fmt(pg["bas"], S), sources_html(pg, S))

def feuille(f, k, Y, D, S):
    pg = Y["pages"][f["page"] - 1]; g = f["gabarit"]
    if g == "couverture": return couverture(pg, k, S)
    im = S["images"]; classes = "sheet g-%s%s%s" % (g, " rupture" if f.get("rupture") else "", " suite" if f.get("suite") else "")
    logo = '<img class="logo" src="%s" alt="%s">' % (image(im["logo"], S), html.escape(im["logo_alt"])) if im["logo"] else ""
    top = '<div class="sig"></div><header class="top">%s<span class="etape">%s</span></header>' % (logo, html.escape(pg.get("etape", "")))
    titre = fmt(pg["titre"], S) if not f.get("suite") else "%s %s" % (fmt(pg["titre"], S), html.escape(S["libelles"]["suite"]))
    P = lambda i: '<section class="piece">%s</section>' % piece(pg["pieces"][i], Y, D, S, blocs)
    gauche, droite = "", ""
    if f.get("tuiles") and pg.get("tuiles"): gauche += tuiles(pg["tuiles"], S, "grand" if f.get("rupture") else "")
    if not f.get("suite") and not f.get("sans_texte"): gauche += texte(pg, S, f["page"])
    if f.get("diptyque"): droite += '<div class="dipt">%s%s</div>' % (figure(pg["images"][0], S), figure(pg["images"][1], S))
    elif f.get("image") is not None: droite += figure(pg["images"][f["image"]], S, "demi")
    pieces = f.get("pieces", [])
    cote = f.get("pieces_a", "droite")
    pg_html = "".join(P(i) for i in pieces)
    if cote == "droite": droite += pg_html
    else: gauche += pg_html
    disp = f.get("colonnes", "")  # "un": all on one column; "demi": two equal columns; otherwise 5/7
    if not droite: corps = '<div class="cols un"><div class="col">%s</div></div>' % gauche
    elif not gauche: corps = '<div class="cols un"><div class="col">%s</div></div>' % droite
    else: corps = '<div class="cols %s"><div class="col">%s</div><div class="col">%s</div></div>' % (disp, gauche, droite)
    bot = ""
    if f.get("fin", True) and not f.get("suite"): bot += '<div class="bas">%s</div><div class="sources">%s</div>' % (fmt(pg["bas"], S), sources_html(pg, S))
    bot += '<div class="pied"><span class="num">%d</span><span class="regle"></span></div>' % k
    return '<section class="%s" data-f="%d" data-p="%d">%s<div class="bandeau"><h1>%s</h1></div><main class="main">%s</main><div class="bottom">%s</div></section>' % (classes, k, f["page"], top, titre, corps, bot)

def construire():
    S = reglages(); Y, D = charger(); R = roles(S); fe = plan_feuilles(S, Y)
    titre = S["document"]["titre"] or Y["pages"][0]["titre"]
    corps = "\n".join(feuille(f, k + 1, Y, D, S) for k, f in enumerate(fe))
    page = '<!doctype html><html lang="%s"><head><meta charset="utf-8"><title>%s</title><style>%s%s</style></head><body>%s</body></html>' % (
        S["document"]["langue"], html.escape(titre), css_diapo(S, R), getattr(blocs, "CSS", ""), corps)
    path = os.path.join(BUILD, "livrable.html"); os.makedirs(BUILD, exist_ok=True); open(path, "w", encoding="utf-8").write(page)
    return path, fe, titre

def pptx_fidele(pdf, rep, feuilles):
    """Faithful PPTX (P6.3): one 3840 x 2160 image per slide (PNG; JPEG 85 if a photo covers more than half), notes from the YAML, alt text = title."""
    from pptx import Presentation
    from pptx.util import Emu
    from PIL import Image
    S = reglages(); Y, _ = charger(); d = pymupdf.open(pdf); prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
    os.makedirs(os.path.join(BUILD, "pptx"), exist_ok=True)
    for i, (p, f) in enumerate(zip(d, feuilles)):
        pg = Y["pages"][f["page"] - 1]; photos = rep["sheets"][i]["photos"]
        plein = sum(w * h for _, _, w, h in photos) / (1920 * 1080) > 0.5
        pix = p.get_pixmap(dpi=192); fichier = os.path.join(BUILD, "pptx", "d%02d.%s" % (i + 1, "jpg" if plein else "png"))
        if plein: Image.frombytes("RGB", (pix.width, pix.height), pix.samples).save(fichier, quality=85)
        else: pix.save(fichier)
        sl = prs.slides.add_slide(prs.slide_layouts[6])
        pic = sl.shapes.add_picture(fichier, 0, 0, prs.slide_width, prs.slide_height)
        pic._element.nvPicPr.cNvPr.set("descr", pg["titre"])
        if pg.get("notes"): sl.notes_slide.notes_text_frame.text = pg["notes"].strip()
    sortie = os.path.join(LIVRAISON, S["document"]["nom_fichier"] + ".pptx"); prs.save(sortie); print("pptx: " + sortie)

if __name__ == "__main__":
    main(construire, 1920, 1080, "diaporama", 3, apres=pptx_fidele)
