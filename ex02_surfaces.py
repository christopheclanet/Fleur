import math                                  # Importe math (besoin de pi)

def demander_float_positif(message):         # Fonction de saisie robuste
    """Demande un float > 0 et redemande tant que c'est invalide."""  # Docstring
    while True:                              # Boucle infinie (on sortira avec return)
        texte = input(message)               # Affiche message et recupere la saisie utilisateur
        try:                                 # Debut du bloc "on essaye"
            valeur = float(texte)            # Convertit le texte en nombre decimal (float)
            if valeur > 0:                   # Test : strictement positif ?
                return valeur                # Oui : renvoie la valeur
            else:                            # Sinon : 0 ou negatif
                print("Erreur : le nombre doit etre strictement positif.")  # Message
        except ValueError:                   # Si conversion float impossible
            print("Erreur : ecris un nombre (ex: 3 ou 3.5).")              # Message

def surface_carre(c):                        # Surface d'un carre (cote c)
    return c * c                             # Renvoie c^2

def surface_rectangle(h, l):                 # Surface rectangle (hauteur h, largeur l)
    return h * l                             # Renvoie h*l

def surface_triangle(h, b):                  # Surface triangle (hauteur h, base b)
    return (h * b) / 2                       # Renvoie (h*b)/2

def surface_cercle(r):                       # Surface cercle (rayon r)
    return math.pi * r * r                   # Renvoie pi*r^2

def surface_forme_geometrique(forme):        # Choisit la bonne formule
    """Calcule la surface selon la forme demandee."""  # Explication
    match forme:                             # Match/case (Python 3.10+)
        case "carre":                        # Cas carre
            cote = demander_float_positif("Mesure du cote du carre : ")  # Saisie cote
            return surface_carre(cote)       # Renvoie surface carre
        case "rectangle":                    # Cas rectangle
            largeur  = demander_float_positif("Largeur du rectangle : ") # Saisie largeur
            longueur = demander_float_positif("Longueur du rectangle : ")# Saisie longueur
            return surface_rectangle(longueur, largeur)                  # Renvoie surface
        case "cercle":                       # Cas cercle
            rayon = demander_float_positif("Rayon du cercle : ")         # Saisie rayon
            return surface_cercle(rayon)     # Renvoie surface
        case "triangle":                     # Cas triangle
            base = demander_float_positif("Base du triangle : ")         # Saisie base
            hauteur = demander_float_positif("Hauteur du triangle : ")   # Saisie hauteur
            return surface_triangle(hauteur, base)                       # Renvoie surface
        case _:                              # Cas par defaut
            return None                      # Renvoie None si forme inconnue

forme = input("Choisis une forme (Cercle, Triangle, Rectangle ou Carre) : ")  # Demande forme
forme = forme.strip().lower()               # Normalise : enleve espaces + minuscules

while forme not in ["carre", "cercle", "triangle", "rectangle"]:  # Tant que invalide...
    forme = input("Erreur. Choisis : Cercle, Triangle, Rectangle ou Carre : ")  # Redemande
    forme = forme.strip().lower()          # Renormalise

resultat = surface_forme_geometrique(forme) # Calcule la surface
print("Surface =", resultat)                # Affiche le resultat
