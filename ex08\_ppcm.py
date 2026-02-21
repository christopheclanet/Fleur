print("------- PPCM de deux entiers -------")                  # Titre

def pgcd(a, b):                                               # Fonction PGCD (utile pour PPCM)
    a = abs(a)                                                # Valeur absolue de a
    b = abs(b)                                                # Valeur absolue de b
    while b != 0:                                             # Boucle Euclide
        a, b = b, a % b                                       # Mise a jour du couple
    return a                                                  # Renvoie le PGCD

def ppcm(a, b):                                               # Fonction : calcule le PPCM
    if a == 0 or b == 0:                                      # Cas special : si un nombre est 0
        return 0                                              # Convention : PPCM(0,b)=0
    return abs(a * b) // pgcd(a, b)                           # Formule : |a*b| / PGCD

try:                                                         # Bloc protege
    A = int(input("Veuillez saisir un entier A : "))          # Saisie + conversion de A
    B = int(input("Veuillez saisir un entier B : "))          # Saisie + conversion de B
    print(f"PPCM({A}, {B}) = {ppcm(A, B)}")                   # Calcule et affiche PPCM
except ValueError:                                            # Si conversion impossible
    print("Erreur : veuillez saisir des entiers.")            # Message d'erreur
