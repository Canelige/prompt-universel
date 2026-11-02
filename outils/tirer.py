# Qui le lit, et quand : la discussion de projet le copie dans <sous-dossier>/travail/tirer.py à l'étape E (demarrage.md) ; tous les tirages de style passent ensuite par lui.
# [RÈGLE OU.1] Script de tirage reproductible : la graine est écrite une seule fois par travail, chaque tirage est noté dans tirages.log.
import hashlib, sys, time, pathlib
sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(__file__).resolve().parent
G = D / "graine.txt"
def h(s): return hashlib.sha256(s.encode()).hexdigest()
def graine(base=""):
    if not G.exists():
        G.parent.mkdir(exist_ok=True); G.write_text(h(f"{base}|{time.time_ns()}"), encoding="utf-8")
    return G.read_text(encoding="utf-8").strip()
def tirer(etiquette, options, k=1):
    s = graine(); options = list(dict.fromkeys(options))
    return sorted(options, key=lambda o: h(f"{s}|{etiquette}|{o}"))[:k]
if __name__ == "__main__":
    if sys.argv[1] == "init":
        graine(sys.argv[2]); print("graine ecrite")
    else:
        r = tirer(sys.argv[1], sys.argv[3:], int(sys.argv[2]))
        print("\n".join(r))
        with open(D / "tirages.log", "a", encoding="utf-8") as f:
            f.write(f"{sys.argv[1]} | k={sys.argv[2]} | {' ; '.join(sys.argv[3:])} => {' ; '.join(r)}\n")
