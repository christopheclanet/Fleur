import matplotlib.pyplot as plt              # Importe pyplot pour dessiner

plt.figure(figsize=(3, 3))                   # Cree une figure (3x3 pouces)

plt.fill([0, 2, 2, 0], [0, 0, 2, 2], "r")     # Remplit un polygone rouge (carre) via ses sommets

points_x = [0.5, 0.5, 0.5, 1.5, 1.5, 1.5]     # Liste des x des points
points_y = [0.5, 1.0, 1.5, 0.5, 1.0, 1.5]     # Liste des y correspondants
plt.plot(points_x, points_y, "ow")            # Trace les points : o=rond, w=blanc

plt.axis("equal")                             # Meme echelle x/y (carre reste carre)
plt.axis("off")                               # Cache les axes
plt.show()                                    # Affiche la figure
