# Exercice 1 - Lab 3 : Fibonacci
# Objectif : demander un entier P, puis trouver le plus petit n tel que S_n > P

def Fibonacci(n):                 # Definir une fonction qui calcule S_n
    S0 = 0                        # Initialiser S0 (premier terme)
    S1 = 1                        # Initialiser S1 (deuxieme terme)

    if n == 0:                    # Si on demande le terme 0...
        return S0                 # ... on renvoie 0

    if n == 1:                    # Si on demande le terme 1...
        return S1                 # ... on renvoie 1

    i = 2                         # Compteur : on commence a 2 (car S0 et S1 existent deja)
    while i <= n:                 # Tant qu'on n'a pas atteint n...
        S2 = S0 + S1              # Calculer le terme suivant : S2 = S0 + S1
        S0 = S1                   # Decaler : l'ancien S1 devient le nouveau S0
        S1 = S2                   # Decaler : l'ancien S2 devient le nouveau S1
        i = i + 1                 # Passer au prochain i

    return S2                     # A la fin, S2 est S_n, donc on le renvoie


P = int(input("Veuillez saisir un nombre entier P : "))  # Demander P et convertir en entier
n = 2                                                    # Commencer a n = 2 (comme suggere dans l'enonce)

while Fibonacci(n) <= P:                                 # Tant que S_n n'est pas strictement plus grand que P...
    n = n + 1                                            # ... augmenter n de 1 et tester le terme suivant

print("Le plus petit n tel que S_n > P est :", n)         # Afficher le resultat
