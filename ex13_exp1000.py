import math                                     # Importe math pour exp(x)
import matplotlib.pyplot as plt                 # Importe pyplot pour tracer

x = 0.0                                         # Initialise x a 0
pas = 0.1                                       # Pas d'augmentation de x

x_vals = []                                     # Liste des x
y_vals = []                                     # Liste des y

while True:                                     # Boucle infinie
    y = math.exp(x)                             # Calcule y = exp(x)
    x_vals.append(x)                            # Ajoute x dans la liste
    y_vals.append(y)                            # Ajoute y dans la liste
    if y >= 1000:                               # Condition d'arret
        break                                   # Sort de la boucle
    x += pas                                    # Sinon incremente x

plt.figure(figsize=(5, 4))                      # Cree une figure
plt.title("Courbe de y = exp(x)")               # Titre
plt.xlabel("x")                                 # Axe x
plt.ylabel("exp(x)")                            # Axe y
plt.grid(True)                                  # Grille

plt.plot(x_vals, y_vals, marker=".", linestyle="-", label="exp(x)")  # Trace la courbe
plt.legend()                                  # Affiche la legende
plt.show()                                    # Affiche le graphique
