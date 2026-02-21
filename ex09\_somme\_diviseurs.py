print("------- Somme des diviseurs d'un entier n -------")     # Titre

try:                                                          # Bloc protege
    n = int(input("Veuillez saisir un entier n > 0 : "))       # Saisie + conversion
    if n <= 0:                                                 # Controle : n strictement positif
        print("Erreur : n doit etre strictement positif.")      # Message si invalide
    else:
        somme = 0                                              # Initialise la somme
        for i in range(1, n + 1):                              # i = 1..n
            if n % i == 0:                                     # Si i divise n
                somme += i                                     # Ajoute i
        print(f"Somme des diviseurs de {n} = {somme}")          # Affiche resultat
except ValueError:                                             # Si conversion echoue
    print("Erreur : veuillez saisir un entier.")               # Message d'erreur
