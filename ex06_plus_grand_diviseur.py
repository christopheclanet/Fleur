print("------- Plus grand diviseur d'un entier -------")        # Titre

texte = input("Veuillez saisir un entier n >= 2 : ")            # Demande n (texte)

try:                                                           # Bloc protege
    n = int(texte)                                             # Conversion en int
    if n < 2:                                                  # Controle
        print("Erreur : n doit etre >= 2.")                     # Message si invalide
    else:
        plus_grand_diviseur = 1                                # Par defaut : 1 divise toujours n
        for i in range(n - 1, 1, -1):                          # i = n-1, ..., 2
            if n % i == 0:                                     # Si i divise n
                plus_grand_diviseur = i                        # On memorise i
                break                                          # On arrete : c'est le plus grand

        if plus_grand_diviseur == 1:                           # Si aucun diviseur > 1
            print(f"{n} est un nombre premier.")                # Alors n est premier
        else:
            print(f"Le plus grand diviseur de {n} (different de {n}) est {plus_grand_diviseur}.")
except ValueError:                                             # Si int(...) echoue
    print("Erreur : veuillez saisir un entier.")                # Message d'erreur
