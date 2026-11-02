# Qui le lit, et quand : `diapo-fabricant`, jamais en entier : il copie ce fichier en <sous-dossier>/travail/build.py, avec document_a4.py, commun.py, controles.py et reglages.yaml, et n'édite que reglages.yaml.
"""synthese_a4.py : une page de synthèse A4 (une seule feuille) tirée d'une page de 02_contenu.yaml.

  python build.py                 rendu complet ; échoue si la page déborde ou si PAGES PROMISES (ETAT.md) est inférieur à 1 feuille
  python build.py --pages 1       rend la feuille seule
Le réglage `synthese:` de reglages.yaml désigne la page et sa mise en page (mêmes clés qu'une feuille de document_a4.py) :
  synthese: {page: 2, rupture: true, tuiles: true, colonnes: 2, pieces: [0]}
Il n'y a qu'une feuille : ce qui ne tient pas se coupe dans le YAML (P6.23), jamais en feuille de suite.
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
