print("------- Nombre avec le plus de diviseurs (saisies jusqu'a -1) -------")  # Titre

def nombre_diviseurs(n):                                                         # Compte les diviseurs de n
    compteur = 0                                                                 # Initialise compteur
    for d in range(1, n + 1):                                                    # d = 1..n
        if n % d == 0:                                                           # Si d divise n
            compteur += 1                                                        # Incremente compteur
    return compteur                                                              # Renvoie compteur

meilleur_n = None                                                                # Meilleur nombre (aucun au debut)
meilleur_nb = -1                                                                 # Meilleur score (nb diviseurs)

while True:                                                                      # Boucle de saisie
    texte = input("Saisis un entier > 0 (ou -1 pour arreter) : ")                # Demande une valeur
    if texte.strip() == "-1":                                                    # Si l'utilisateur arrete
        break                                                                    # Sort de la boucle

    try:                                                                         # Bloc protege
        n = int(texte)                                                           # Convertit en entier
        if n <= 0:                                                               # Controle : n > 0
            print("Erreur : il faut un entier strictement positif.")              # Message
            continue                                                             # Passe a la saisie suivante

        nb = nombre_diviseurs(n)                                                 # Calcule nb de diviseurs
        if nb > meilleur_nb:                                                     # Si record battu
            meilleur_nb = nb                                                     # Met a jour meilleur score
            meilleur_n = n                                                       # Met a jour meilleur n

    except ValueError:                                                           # Si conversion impossible
        print("Erreur : veuillez saisir un entier.")                             # Message

if meilleur_n is None:                                                           # Si aucun n valide
    print("Aucun entier valide n'a ete saisi.")                                  # Message final
else:
    print(f"Le nombre avec le plus de diviseurs est {meilleur_n} (il a {meilleur_nb} diviseurs).")
                                                                                # Affiche le gagnant
