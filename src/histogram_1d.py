import matplotlib.pyplot as plt
# On importe la fonction de simulation du fichier précédent
from parking_1d import nb_place_occupe 

X = []
# 500 simulations de M10
print("Génération de l'histogramme pour n=10...")
for i in range(500):
    Mn = nb_place_occupe(10)
    X.append(Mn)

# Affichage de l'histogramme
plt.figure()
plt.hist(X, bins=range(12), align='left', rwidth=0.8, edgecolor='black', density=True)
plt.xlabel('Valeurs de Mn')
plt.ylabel('Proportion sur 500 simulations')
plt.title('Distribution de M10')
plt.show()