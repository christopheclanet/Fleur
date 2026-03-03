def factorielle(n):
    # Initialisation de la variable fact
    fact = 1

    # Calcul du n! (pour n=0, la boucle ne tourne pas et fact reste a 1)
    for k in range(2, n + 1):
        fact *= k

    return fact


def EntierFac(P):
    # Initialisation de n
    n = 0

    # Incremente n tant que n! <= P
    while factorielle(n) <= P:
        n += 1

    return n


# Corps du programme
try:
    P = int(input("Veuillez saisir un entier positif P \t"))
    if P < 0:
        raise ValueError("P negatif")

    n = EntierFac(P)
    print(f"Le plus petit entier n tel que n! > {P} est: {n}")
except:
    print("La valeur de P saisie n'est pas un entier positif")
