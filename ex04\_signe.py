texte = input("Entrez un nombre : ")          # Demande une saisie (texte)

try:                                          # Bloc protege : conversion peut echouer
    nombre = float(texte)                     # Conversion texte -> float
    if nombre > 0:                            # Test : strictement positif ?
        resultat = "positif"                  # Oui : stocke "positif"
    elif nombre < 0:                          # Test : strictement negatif ?
        resultat = "negatif"                  # Oui : stocke "negatif"
    else:                                     # Sinon, c'est 0
        resultat = "nul"                      # Stocke "nul"
    print("Le nombre saisi est", resultat)    # Affiche le resultat
except ValueError:                            # Si float(...) echoue
    print("Erreur : la saisie n'est pas un nombre decimal valide.")  # Message d'erreur
