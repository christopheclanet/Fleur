print("------- Factorielle d'un nombre (boucle for) -------")  # Titre

texte = input("Veuillez saisir un entier n >= 0 : ")           # Demande n (texte)

try:                                                           # Bloc protege
    n = int(texte)                                             # Conversion texte -> int
    if n < 0:                                                  # Controle : n doit etre >= 0
        print("Erreur : n doit etre >= 0.")                     # Message si negatif
    else:                                                      # Cas valide
        fact = 1                                               # Initialise fact a 1
        for i in range(2, n + 1):                              # i prend 2..n (borne sup exclue)
            fact *= i                                          # Multiplie fact par i
        print(f"{n}! = {fact}")                                # Affiche n! calcule
except ValueError:                                             # Si int(...) echoue
    print("Erreur : veuillez saisir un entier (ex: 0, 5, 12).") # Message d'erreur
