# Who reads it, and when: the author of the prompt, after any change to this folder; never an agent during a work.
"""autotest.py: runs the three templates and the gate checks on exemple/, in a temporary folder.
Cases that must pass: the three renders. Cases that must fail: sheet ceiling (P6.23), stale or hard-coded number (P6.22),
render counter (PI.31: reserve of the 3rd, --pages on all sheets, gap with rendus/), color (origin, flat outside the roles, vivid flat, energy).
Usage: python autotest.py   (the work's Python launcher: pyyaml, pymupdf, pillow, playwright, python-pptx)"""
import os, re, shutil, subprocess, sys, tempfile
ICI = os.path.dirname(os.path.abspath(__file__))
SOMBRE = "energie: sombre\n"   # the example is too empty for a bounded energy: only its templates count here
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
    open(os.path.join(t, "ETAT.md"), "w").write("FULL RENDERS : 1 / 3\nPAGES PROMISED : 1 to 2\n")
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "3 sheets for 2 promised" in r.stdout, "P6.23: sheet ceiling refused", r))
    t = monter(racine, "diapo", "diaporama.py", "3", SOMBRE); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0 and os.path.exists(os.path.join(racine, "diapo", "livraison", "Plan_Deliverable_Demo-Workshop.pptx")), "slide deck: PDF and PPTX", r))
    t = monter(racine, "synthese", "synthese_a4.py", "1", SOMBRE); r = lancer(t, "build.py"); res.append(verifie(r.returncode == 0, "A4 summary: one sheet", r))
    # PI.31: --pages on all sheets refused; the 3rd full render is reserved for phase 8; the 4th refused; counter and PDFs of rendus/ agree
    t = monter(racine, "compteur", "document_a4.py", "2 to 3"); etat = lambda: open(os.path.join(t, "ETAT.md")).read()
    r = lancer(t, "build.py", "--pages", "1,2,3"); res.append(verifie(r.returncode != 0 and "covers all 3 sheets" in r.stderr + r.stdout, "PI.31: --pages on all sheets refused", r))
    r = lancer(t, "build.py"); r2 = lancer(t, "build.py"); r3 = lancer(t, "build.py")
    res.append(verifie(r.returncode == 0 and r2.returncode == 0 and r3.returncode != 0 and "reserved for phase 8" in r3.stderr + r3.stdout and "2 / 3" in etat(), "PI.31: the 3rd full render is reserved for phase 8", r3))
    r = lancer(t, "build.py", "--audit"); res.append(verifie(r.returncode == 0 and "3 / 3" in etat() and len(os.listdir(os.path.join(t, "rendus"))) >= 3, "PI.31: --audit lifts the reserve, three distinct PDFs", r))
    r = lancer(t, "build.py", "--audit"); res.append(verifie(r.returncode != 0 and "ceiling of full renders reached" in r.stderr + r.stdout, "PI.31: the 4th full render is refused", r))
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 0 and "counter 3 / 3, 3 full PDF" in r.stdout, "PI.31: counter and PDFs of rendus/ agree", r))
    open(os.path.join(t, "ETAT.md"), "w").write("FULL RENDERS : 1 / 3\nPAGES PROMISED : 2 to 3\n")
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "RENDUS COMPLETS counter: 1 for 3 full PDF" in r.stdout, "PI.31: gap between counter and PDFs refused", r))
    open(os.path.join(t, "ETAT.md"), "w").write("FULL RENDERS : 0 / 3\n")
    r = lancer(t, "-c", "import commun; commun.compteur(True); commun.compteur_annuler(); print(commun.compteur())"); res.append(verifie(r.stdout.strip() == "0", "PI.31: a render that crashes is not counted", r))
    # color: missing origin, flat outside the roles table, vivid flat, missing energy
    ry = os.path.join(t, "reglages.yaml"); base = open(ry, encoding="utf-8").read()
    open(ry, "w", encoding="utf-8").write(re.sub(r'origine: "[^"]*"', 'origine: ""', base)); open(os.path.join(t, "ETAT.md"), "w").write("FULL RENDERS : 3 / 3\nPAGES PROMISED : 2 to 3\n")
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "couleurs.origine" in r.stdout, "DA.5: accent without origin refused", r))
    open(ry, "w", encoding="utf-8").write(base.replace("energie: vivid\n", ""))
    r = lancer(t, "controles.py"); res.append(verifie(r.returncode == 1 and "energie missing" in r.stdout, "P7.10: missing energy refused", r))
    open(ry, "w", encoding="utf-8").write(base)
    page = lambda couleur, h: lancer(t, "-c", "import pymupdf, controles, commun\nd = pymupdf.open(); p = d.new_page(width=595, height=842); p.draw_rect((0, 0, 595, %d), color=None, fill=%s); d.save('x.pdf')\nS = commun.reglages(); print('\\n'.join(controles.controle_couleur('x.pdf', S, commun.roles(S))[0]))" % (h, couleur))
    r = page("(0.95, 0.64, 0.70)", 250); res.append(verifie("roles table" in r.stdout, "DA.51: pink flat outside the roles table refused", r))
    r = page("(0.91, 0.64, 0.09)", 400); res.append(verifie("vivid flat" in r.stdout and "too much color" in r.stdout, "P7.10: vivid flat and too much color on a sheet refused", r))
    open(ry, "w", encoding="utf-8").write(base.replace("sobre_typographique: true", "sobre_typographique: false"))
    r = page("(1, 1, 1)", 10); res.append(verifie("3 % floor" in r.stdout, "P7.11: sheet without color refused outside typographic Sober", r))
    open(ry, "w", encoding="utf-8").write(base)
    # template pieces (defect 7 of trial no. 7): multi-value totals, strip of the parts, second font family
    r = lancer(t, "-c", "import commun\nS = commun.reglages(); S['frise'] = ['A', 'B']; S['polices']['titres'] = {'famille': 'Titres', 'fichiers': {700: 'polices/T.ttf'}}\nh = commun.tableau(['L', 'x', 'y'], [['a', '1', '2']], S, [['Total', '3', '4']])\nprint(h.count('class=\"num\">') >= 4, 'class=\"on\">B' in commun.frise(S, 1), 'font-family:\"Titres\"' in commun.css_plus(S['polices']))")
    res.append(verifie(r.stdout.strip() == "True True True", "template: multi-value totals, strip, titles font", r))
    shutil.rmtree(racine); print("AUTOTEST: %s" % ("OK" if all(res) else "ECHEC")); return 0 if all(res) else 1
if __name__ == "__main__": sys.exit(main())
