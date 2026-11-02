# calculs.py of the example: the budget total, computed and not written by hand
import sys
ETAPES = {"Frame": 400, "Measure": 500, "Decide": 300}
if __name__ == "__main__":
    print("total", sum(ETAPES.values()))
