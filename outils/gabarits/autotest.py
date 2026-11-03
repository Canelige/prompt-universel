# Qui le lit, et quand : l'auteur du prompt, après toute modification de ce dossier ; jamais un agent pendant un travail.
"""autotest.py : fait tourner les trois gabarits et les contrôles de la porte sur exemple/, dans un dossier temporaire.
Cas qui doivent passer : les trois rendus. Cas qui doivent échouer : plafond de feuilles (P6.23), nombre périmé ou écrit en dur (P6.22),
compteur de rendus (PI.31 : réserve du 3e, --pages sur toutes les feuilles, écart avec rendus/), couleur (origine, aplat hors rôles, aplat vif, énergie).
Usage : python autotest.py   (le lanceur Python du travail : pyyaml, pymupdf, pillow, playwright, python-pptx)"""
import os, re, shutil, subprocess, sys, tempfile
ICI = os.path.dirname(os.path.abspath(__file__))
SOMBRE = "energie: sombre\n"   # l'exemple est trop vide pour une énergie bornée : seuls ses gabarits comptent ici
def lancer(t, script, *args):
    return subprocess.run([sys.executable, script, *args], cwd=t, capture_output=True, text=True)
def monter(racine, nom, script, promis, reglages_en_plus=""):
    t = os.path.join(racine, nom, "travail"); os.makedirs(t)
    for f in ("commun.py", "controles.py", "document_a4.py", "diaporama.py", "synthese_a4.py"): shutil.copy(os.path.join(ICI, f), t)
    for f in os.listdir(os.path.join(ICI, "exemple")): shutil.copy(os.path.join(ICI, "exemple", f), t)
    shutil.copy(os.path.join(t, script), os.path.join(t, "build.py"))
    open(os.path.join(t, "reglages.yaml"), "a", encoding="utf-8").write(reglages_en_plus)
    open(os.path.join(t, "ETAT.md"), "w").write("RENDUS COMPLETS : 0 / 3\nPAGES PROMISES : %s\n" % promis)
    return t
def verifie(ok, nom, r=None):
    print(("ok     " if ok else "ECHEC  ") + nom + ("" if ok or r is None else "\n" + r.stdout[-600:] + r.stderr[-600:])); return ok
def main():
    racine = tempfile.mkdtemp(); res = []
    t = monter(racine, "a4", "document_a4.py", "2 à 3"); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0, "document A4 : rendu, plafond respecté", r))
    r = lancer(t, "build.py", "--pages", "2"); res.append(verifie(r.returncode == 0, "document A4 : --pages 2 et remplacement", r))
    # P6.22 périmé : le YAML corrigé après le rendu, le PDF imprime encore l'ancien nombre
    y = os.path.join(t, "02_contenu.yaml"); s = open(y, encoding="utf-8").read(); open(y, "w", encoding="utf-8").write(re.sub(r"\b6\b", "8", s))
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "6 semaines" in r.stdout, "P6.22 : nombre périmé refusé", r))
    open(y, "w", encoding="utf-8").write(s)
    # P6.22 en dur : un bloc propre au travail écrit un montant à la main
    open(os.path.join(t, "blocs.py"), "w").write('PIECES = {}\nPIED = "Frais fixes : 777 EUR"\n')
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "blocs.py" in r.stdout, "P6.22 : nombre écrit dans blocs.py refusé", r)); os.remove(os.path.join(t, "blocs.py"))
    # P6.23 : trois feuilles pour un plafond de deux
    open(os.path.join(t, "ETAT.md"), "w").write("RENDUS COMPLETS : 1 / 3\nPAGES PROMISES : 1 à 2\n")
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "3 feuilles pour 2 promises" in r.stdout, "P6.23 : plafond de feuilles refusé", r))
    t = monter(racine, "diapo", "diaporama.py", "3", SOMBRE); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0 and os.path.exists(os.path.join(racine, "diapo", "livraison", "Plan_Livrable_Atelier-Demo.pptx")), "diaporama : PDF et PPTX", r))
    t = monter(racine, "synthese", "synthese_a4.py", "1", SOMBRE); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0, "synthèse A4 : une feuille", r))
    # PI.31 : --pages sur toutes les feuilles refusé ; le 3e rendu complet est réservé à la phase 8 ; le 4e refusé ; compteur et PDF de rendus/ d'accord
    t = monter(racine, "compteur", "document_a4.py", "2 à 3"); etat = lambda: open(os.path.join(t, "ETAT.md")).read()
    r = lancer(t, "build.py", "--pages", "1,2,3"); res.append(verifie(r.returncode != 0 and "couvre les 3 feuilles" in r.stderr + r.stdout, "PI.31 : --pages sur toutes les feuilles refusé", r))
    r = lancer(t, "build.py"); r2 = lancer(t, "build.py"); r3 = lancer(t, "build.py")
    res.append(verifie(r.returncode == 0 and r2.returncode == 0 and r3.returncode != 0 and "réservé à la phase 8" in r3.stderr + r3.stdout and "2 / 3" in etat(), "PI.31 : le 3e rendu complet est réservé à la phase 8", r3))
    r = lancer(t, "build.py", "--audit"); res.append(verifie(r.returncode == 0 and "3 / 3" in etat() and len(os.listdir(os.path.join(t, "rendus"))) >= 3, "PI.31 : --audit lève la réserve, trois PDF distincts", r))
    r = lancer(t, "build.py", "--audit"); res.append(verifie(r.returncode != 0 and "plafond de rendus complets atteint" in r.stderr + r.stdout, "PI.31 : le 4e rendu complet est refusé", r))
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 0 and "compteur 3 / 3, 3 PDF complet" in r.stdout, "PI.31 : compteur et PDF de rendus/ d'accord", r))
    open(os.path.join(t, "ETAT.md"), "w").write("RENDUS COMPLETS : 1 / 3\nPAGES PROMISES : 2 à 3\n")
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "compteur RENDUS COMPLETS : 1 pour 3 PDF" in r.stdout, "PI.31 : écart compteur et PDF refusé", r))
    open(os.path.join(t, "ETAT.md"), "w").write("RENDUS COMPLETS : 0 / 3\n")
    r = lancer(t, "-c", "import commun; commun.compteur(True); commun.compteur_annuler(); print(commun.compteur())"); res.append(verifie(r.stdout.strip() == "0", "PI.31 : un rendu qui plante n'est pas compté", r))
    # couleur : origine absente, aplat hors du tableau des rôles, aplat vif, énergie absente
    ry = os.path.join(t, "reglages.yaml"); base = open(ry, encoding="utf-8").read()
    open(ry, "w", encoding="utf-8").write(re.sub(r'origine: "[^"]*"', 'origine: ""', base)); open(os.path.join(t, "ETAT.md"), "w").write("RENDUS COMPLETS : 3 / 3\nPAGES PROMISES : 2 à 3\n")
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "couleurs.origine" in r.stdout, "DA.5 : accent sans origine refusé", r))
    open(ry, "w", encoding="utf-8").write(base.replace("energie: vivant\n", ""))
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "energie absente" in r.stdout, "P7.10 : énergie absente refusée", r))
    open(ry, "w", encoding="utf-8").write(base)
    page = lambda couleur, h: lancer(t, "-c", "import pymupdf, controles, commun\nd = pymupdf.open(); p = d.new_page(width=595, height=842); p.draw_rect((0, 0, 595, %d), color=None, fill=%s); d.save('x.pdf')\nS = commun.reglages(); print('\\n'.join(controles.controle_couleur('x.pdf', S, commun.roles(S))[0]))" % (h, couleur))
    r = page("(0.95, 0.64, 0.70)", 250); res.append(verifie("tableau des rôles" in r.stdout, "DA.51 : aplat rose hors du tableau des rôles refusé", r))
    r = page("(0.91, 0.64, 0.09)", 400); res.append(verifie("aplat vif" in r.stdout and "trop de couleur" in r.stdout, "P7.10 : aplat vif et trop de couleur sur une feuille refusés", r))
    open(ry, "w", encoding="utf-8").write(base.replace("sobre_typographique: true", "sobre_typographique: false"))
    r = page("(1, 1, 1)", 10); res.append(verifie("plancher de 3 %" in r.stdout, "P7.11 : feuille sans couleur refusée hors Sobre typographique", r))
    open(ry, "w", encoding="utf-8").write(base)
    # pièces du gabarit (défaut 7 de l'essai n°7) : totaux à plusieurs valeurs, frise des parties, seconde famille de polices
    r = lancer(t, "-c", "import commun\nS = commun.reglages(); S['frise'] = ['A', 'B']; S['polices']['titres'] = {'famille': 'Titres', 'fichiers': {700: 'polices/T.ttf'}}\nh = commun.tableau(['L', 'x', 'y'], [['a', '1', '2']], S, [['Total', '3', '4']])\nprint(h.count('class=\"num\">') >= 4, 'class=\"on\">B' in commun.frise(S, 1), 'font-family:\"Titres\"' in commun.css_plus(S['polices']))")
    res.append(verifie(r.stdout.strip() == "True True True", "gabarit : totaux à plusieurs valeurs, frise, polices des titres", r))
    shutil.rmtree(racine); print("AUTOTEST : %s" % ("OK" if all(res) else "ECHEC")); return 0 if all(res) else 1
if __name__ == "__main__": sys.exit(main())
