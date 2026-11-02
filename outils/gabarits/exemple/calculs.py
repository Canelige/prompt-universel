# calculs.py de l'exemple : le total du budget, calculé et non écrit à la main
import sys
ETAPES = {"Cadrer": 400, "Mesurer": 500, "Décider": 300}
if __name__ == "__main__":
    print("total", sum(ETAPES.values()))
