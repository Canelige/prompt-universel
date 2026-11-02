# Who reads it, and when: `diapo-fabricant`, never in full: he copies this file as <subfolder>/travail/build.py, with document_a4.py, commun.py, controles.py and reglages.yaml, and edits only reglages.yaml.
"""synthese_a4.py: an A4 summary page (a single sheet) taken from one page of 02_contenu.yaml.

  python build.py                 full render; fails if the page overflows or if PAGES PROMISED (ETAT.md) is below 1 sheet
  python build.py --pages 1       renders the sheet alone
The `synthese:` setting of reglages.yaml designates the page and its layout (same keys as a sheet of document_a4.py):
  synthese: {page: 2, rupture: true, tuiles: true, colonnes: 2, pieces: [0]}
There is a single sheet: what does not fit is cut in the YAML (P6.23), never moved to a continuation sheet.
"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import *
import document_a4 as a4

def construire():
    S = reglages(); Y, D = charger(); R = roles(S)
    f = {"gabarit": "synthese", "fin": True, "page": 1}; f.update(S.get("synthese", {})); S["feuilles"] = [f]
    fe = a4.plan(S, Y); pg = Y["pages"][fe[0]["page"] - 1]
    titre = S["document"]["titre"] or pg["titre"]
    page = '<!doctype html><html lang="%s"><head><meta charset="utf-8"><title>%s</title><style>%s%s</style></head><body>%s</body></html>' % (
        S["document"]["langue"], html.escape(titre), a4.css_a4(S, R), getattr(a4.blocs, "CSS", ""), a4.feuille(fe[0], 1, Y, D, S))
    path = os.path.join(BUILD, "livrable.html"); os.makedirs(BUILD, exist_ok=True); open(path, "w", encoding="utf-8").write(page)
    return path, fe, titre

if __name__ == "__main__":
    main(construire, 794, 1123, "a4", 1)
