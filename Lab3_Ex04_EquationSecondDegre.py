import math

def ResoudreEquation(a, b, c):
    # On suppose a != 0 (equation du second degre)
    delta = b*b - 4*a*c

    if delta < 0:
        print("Pas de solution")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Une solution double: x = {x:.3f}")
    else:
        rac = math.sqrt(delta)
        x1 = (-b - rac) / (2*a)
        x2 = (-b + rac) / (2*a)
        print(f"Deux solutions distinctes: x1 = {x1:.3f} et x2 = {x2:.3f}")


# Corps du programme
try:
    a = float(input("Veuillez saisir la valeur de a \t"))
    b = float(input("Veuillez saisir la valeur de b \t"))
    c = float(input("Veuillez saisir la valeur de c \t"))

    ResoudreEquation(a, b, c)
except:
    print("L'une des valeurs saisies n'est pas un nombre")
