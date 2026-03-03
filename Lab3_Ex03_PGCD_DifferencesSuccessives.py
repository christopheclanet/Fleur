def PGCD(A, B):
    # Methode des differences successives (Euclide)
    # On suppose A et B positifs.
    while A != B:
        if A > B:
            A = A - B
        else:
            B = B - A
    return A


# Corps du programme
nb_1 = int(input("veuillez saisir le premier entier positif: "))
nb_2 = int(input("veuillez saisir le second entier positif: "))

print(f"Le PGCD de {nb_1} et {nb_2} est egal a: {PGCD(nb_1, nb_2)}")
