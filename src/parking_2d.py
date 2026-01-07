import random
import matplotlib.pyplot as plt

def capacite_a_accueillir_un_nouveau_camion2(L):
    # Vérification horizontale (ligne haut et bas)
    for j in range(len(L[0]) - 2): # -2 car on ignore le '99' de fin
        if L[0][j] + L[0][j+1] == 0:
            return 0
        if L[1][j] + L[1][j+1] == 0:
            return 0
            
    # Vérification verticale
    for j in range(len(L[0]) - 1): # -1 pour ignorer le '99'
        if L[1][j] + L[0][j] == 0:
            return 0
            
    return 1 # Parking plein

def nb_place_occupe2(n):
    # Création du parking 2xN
    # Ajout d'un nombre (99) en dernière position pour gérer les débordements d'indice
    L = [[0] * n + [99], [0] * n + [99]]
    
    x = 0
    while x == 0:
        emplacement = random.randint(0, n - 1)
        # 0 = Horiz. Bas, 1 = Vertical, 2 = Horiz. Haut
        position = random.randint(0, 2) 
        
        if position == 0: # Horizontal Bas
            if emplacement < n: # Check bornes
                if L[1][emplacement] + L[1][emplacement+1] == 0:
                    L[1][emplacement] = 1
                    L[1][emplacement+1] = 1
                    
        elif position == 1: # Vertical
             if L[1][emplacement] + L[0][emplacement] == 0:
                L[1][emplacement] = 1
                L[0][emplacement] = 1
                
        elif position == 2: # Horizontal Haut
            if emplacement < n:
                if L[0][emplacement] + L[0][emplacement+1] == 0:
                    L[0][emplacement] = 1
                    L[0][emplacement+1] = 1
                    
        x = capacite_a_accueillir_un_nouveau_camion2(L)
        
    # Compter les places occupées (en excluant les marqueurs 99)
    Mn = 0
    for i in range(2):
        for j in range(n):
            if L[i][j] == 1:
                Mn += 1
    return Mn

if __name__ == "__main__":
    tailles = [5, 50, 100, 500, 1000]
    resultats = []
    
    print("Simulation 2D en cours...")
    for n in tailles:
        somme_ratios = 0
        for _ in range(100):
            # Le nombre total de places est 2*n
            mn = nb_place_occupe2(n)
            somme_ratios += mn / (2*n)
        resultats.append(somme_ratios / 100)

    plt.figure()
    plt.plot(tailles, resultats, label='Simulation 2D')
    plt.axhline(y=0.9155, color='orange', label='Limite approx (~0.9155)')
    plt.xlabel('Taille du parking n')
    plt.ylabel('Densité (Mn / 2n)')
    plt.title('Convergence du parking 2D')
    plt.legend()
    plt.show()