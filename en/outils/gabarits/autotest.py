# Who reads it, and when: the author of the prompt, after any change to this folder; never an agent during a work.
"""autotest.py: runs the three templates and the P6.22 and P6.23 checks on exemple/, in a temporary folder.
Cases that must pass: the three renders. Cases that must fail: sheet ceiling (P6.23), stale or hard-coded number (P6.22).
Usage: python autotest.py   (the work's Python launcher: pyyaml, pymupdf, pillow, playwright, python-pptx)"""
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
    open(os.path.join(t, "ETAT.md"), "w").write("FULL RENDERS : 0 / 3\nPAGES PROMISED : %s\n" % promis)
    return t
def verifie(ok, nom, r=None):
    print(("ok     " if ok else "FAIL   ") + nom + ("" if ok or r is None else "\n" + r.stdout[-600:] + r.stderr[-600:])); return ok
def main():
    racine = tempfile.mkdtemp(); res = []
    t = monter(racine, "a4", "document_a4.py", "2 to 3"); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0, "A4 document: render, ceiling respected", r))
    r = lancer(t, "build.py", "--pages", "2"); res.append(verifie(r.returncode == 0, "A4 document: --pages 2 and replacement", r))
    # P6.22 stale: the YAML corrected after the render, the PDF still prints the old number
    y = os.path.join(t, "02_contenu.yaml"); s = open(y, encoding="utf-8").read(); open(y, "w", encoding="utf-8").write(re.sub(r"\b6\b", "8", s))
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "6 weeks" in r.stdout, "P6.22: stale number refused", r))
    open(y, "w", encoding="utf-8").write(s)
    # P6.22 hard-coded: a work-specific block writes an amount by hand
    open(os.path.join(t, "blocs.py"), "w").write('PIECES = {}\nPIED = "Fixed fees: 777 EUR"\n')
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "blocs.py" in r.stdout, "P6.22: number written in blocs.py refused", r)); os.remove(os.path.join(t, "blocs.py"))
    # P6.23: three sheets for a ceiling of two
    open(os.path.join(t, "ETAT.md"), "w").write("FULL RENDERS : 0 / 3\nPAGES PROMISED : 1 to 2\n")
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "3 sheets for 2 promised" in r.stdout, "P6.23: sheet ceiling refused", r))
    t = monter(racine, "diapo", "diaporama.py", "3"); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0 and os.path.exists(os.path.join(racine, "diapo", "livraison", "Plan_Deliverable_Demo-Workshop.pptx")), "slide deck: PDF and PPTX", r))
    t = monter(racine, "synthese", "synthese_a4.py", "1"); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0, "A4 summary: one sheet", r))
    shutil.rmtree(racine); print("AUTOTEST: %s" % ("OK" if all(res) else "ECHEC")); return 0 if all(res) else 1
if __name__ == "__main__": sys.exit(main())
