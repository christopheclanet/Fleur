print("------- Somme des diviseurs premiers (sans fonctions) -------")  # Titre

try:                                                                   # Bloc protege
    n = int(input("Veuillez saisir un entier n > 0 : "))                # Saisie + conversion
    if n <= 0:                                                          # Controle
        print("Erreur : n doit etre strictement positif.")               # Message
    else:
        somme = 0                                                       # Somme des diviseurs premiers
        for d in range(2, n + 1):                                       # d = 2..n
            if n % d == 0:                                              # Si d divise n
                est_premier = True                                      # Hypothese : d est premier
                for k in range(2, d):                                   # Cherche un diviseur de d
                    if d % k == 0:                                      # Si k divise d
                        est_premier = False                             # d n'est pas premier
                        break                                           # Arret du test
                if est_premier:                                         # Si d est reste premier
                    somme += d                                          # Ajoute d
        print(f"Somme des diviseurs premiers de {n} = {somme}")          # Affiche resultat
except ValueError:                                                      # Si conversion impossible
    print("Erreur : veuillez saisir un entier.")                        # Message d'erreur
