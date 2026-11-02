# Qui le lit, et quand : l'auteur du prompt, après toute modification de ce dossier ; jamais un agent pendant un travail.
"""autotest.py : fait tourner les trois gabarits et les contrôles P6.22 et P6.23 sur exemple/, dans un dossier temporaire.
Cas qui doivent passer : les trois rendus. Cas qui doivent échouer : plafond de feuilles (P6.23), nombre périmé ou écrit en dur (P6.22).
Usage : python autotest.py   (le lanceur Python du travail : pyyaml, pymupdf, pillow, playwright, python-pptx)"""
import os, re, shutil, subprocess, sys, tempfile
ICI = os.path.dirname(os.path.abspath(__file__))
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
    open(os.path.join(t, "ETAT.md"), "w").write("RENDUS COMPLETS : 0 / 3\nPAGES PROMISES : 1 à 2\n")
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "3 feuilles pour 2 promises" in r.stdout, "P6.23 : plafond de feuilles refusé", r))
    t = monter(racine, "diapo", "diaporama.py", "3"); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0 and os.path.exists(os.path.join(racine, "diapo", "livraison", "Plan_Livrable_Atelier-Demo.pptx")), "diaporama : PDF et PPTX", r))
    t = monter(racine, "synthese", "synthese_a4.py", "1"); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0, "synthèse A4 : une feuille", r))
    shutil.rmtree(racine); print("AUTOTEST : %s" % ("OK" if all(res) else "ECHEC")); return 0 if all(res) else 1
if __name__ == "__main__": sys.exit(main())
