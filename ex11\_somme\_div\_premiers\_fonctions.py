print("------- Somme des diviseurs premiers (avec fonctions) -------")  # Titre

def est_premier(n):                                                    # Fonction primalite
    if n < 2:                                                          # 0 et 1 ne sont pas premiers
        return False                                                   # Donc False
    for k in range(2, n):                                              # k = 2..n-1
        if n % k == 0:                                                 # Si k divise n
            return False                                               # n non premier
    return True                                                        # Sinon n est premier

def somme_diviseurs_premiers(n):                                       # Fonction somme
    somme = 0                                                          # Initialise
    for d in range(2, n + 1):                                          # d = 2..n
        if n % d == 0 and est_premier(d):                              # Diviseur ET premier ?
            somme += d                                                 # Ajoute d
    return somme                                                       # Renvoie la somme

try:                                                                   # Bloc protege
    n = int(input("Veuillez saisir un entier n > 0 : "))                # Saisie + conversion
    if n <= 0:                                                          # Controle
        print("Erreur : n doit etre strictement positif.")               # Message
    else:
        resultat = somme_diviseurs_premiers(n)                          # Calcule
        print(f"Somme des diviseurs premiers de {n} = {resultat}")       # Affiche
except ValueError:                                                      # Si conversion echoue
    print("Erreur : veuillez saisir un entier.")                        # Message
