print("------- PGCD de deux entiers -------")                   # Titre

def pgcd(a, b):                                                # Fonction : calcule le PGCD
    a = abs(a)                                                 # Ignore le signe de a
    b = abs(b)                                                 # Ignore le signe de b
    while b != 0:                                              # Tant que b n'est pas nul
        a, b = b, a % b                                        # Euclide : (a,b) <- (b, a mod b)
    return a                                                   # Quand b=0, a est le PGCD

try:                                                          # Bloc protege
    A = int(input("Veuillez saisir un entier A : "))           # Saisie + conversion de A
    B = int(input("Veuillez saisir un entier B : "))           # Saisie + conversion de B
    resultat = pgcd(A, B)                                      # Calcule le PGCD
    print(f"PGCD({A}, {B}) = {resultat}")                      # Affiche le resultat
except ValueError:                                             # Si saisie non entiere
    print("Erreur : veuillez saisir des entiers.")             # Message d'erreur
