# Exercice 2 - Lab 3 : moyenne des diviseurs premiers
# Objectif : demander un entier n et afficher la moyenne de ses diviseurs premiers.


def Primalite(n):
    """Retourne True si n est premier, False sinon."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    d = 3
    # On teste les diviseurs impairs jusqu'a sqrt(n)
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2

    return True


def MoyenneDiviseursPremiers(n):
    """Calcule la moyenne des diviseurs premiers de n."""
    S = 0  # Somme des diviseurs premiers
    C = 0  # Nombre de diviseurs premiers

    d = 2
    while d <= n:
        if n % d == 0 and Primalite(d):
            S = S + d
            C = C + 1
        d = d + 1

    # Cas theoretique : si n < 2, il n'y a pas de diviseur premier
    if C == 0:
        return 0

    return S / C


# Corps du programme
n = int(input("Veuillez saisir un entier positif n : "))

moyDivPrem = MoyenneDiviseursPremiers(n)
print(f"La moyenne des diviseurs premiers de {n} est : {moyDivPrem}")