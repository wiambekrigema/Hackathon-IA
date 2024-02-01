import numpy as np

class Matrice:
    def __init__(self):
        self.grille = [['0' for _ in range(5)] for _ in range(5)]
        # Définir les mouvements interdits sous forme de {(x, y): ['direction1', 'direction2', ...]}
        self.mouvements_interdits = {
            (0, 1): ['droite'],
            (0, 2): ['gauche'],
            (1, 1): ['droite'],
            (1, 2): ['gauche'],
            (3, 0): ['droite'],
            (3, 1): ['gauche'],
            (3, 2): ['droite'],
            (3, 3): ['gauche'],
            (4, 0): ['droite'],  
            (4, 1): ['gauche'],  
            (4, 2): ['droite'],
            (4, 3): ['gauche']
        }

    def placer_point(self, x, y, symbole):
        self.grille[x][y] = symbole

    def afficher(self):
        for ligne in self.grille:
            print(' '.join(ligne))

    def est_mouvement_autorise(self, position_actuelle, direction):
        # Vérifier si le mouvement est autorisé
        directions_interdites = self.mouvements_interdits.get(position_actuelle, [])
        return direction not in directions_interdites

    def deplacer(self, position_actuelle, direction):
        # Calculer la nouvelle position en fonction de la direction
        x, y = position_actuelle
        if direction == 'haut':
            nouvelle_position = (x - 1, y)
        elif direction == 'bas':
            nouvelle_position = (x + 1, y)
        elif direction == 'gauche':
            nouvelle_position = (x, y - 1)
        elif direction == 'droite':
            nouvelle_position = (x, y + 1)
        else:
            return False  # Direction non reconnue

        # Vérifier si le déplacement est autorisé
        if self.est_mouvement_autorise(position_actuelle, direction):
            print(f"Mouvement de {position_actuelle} à {nouvelle_position} autorisé.")
            symbole = self.grille[x][y]
            self.placer_point(x, y, '0')  # Remplace l'ancienne position par '0'
            self.placer_point(*nouvelle_position, symbole)  # Place le symbole à la nouvelle position
            return True
        else:
            print(f"Mouvement de {position_actuelle} à {nouvelle_position} interdit.")
            return False
<<<<<<< HEAD
         
    def trouver_coordonnee(self, symbole):
        grille_np = np.array(self.grille)
        resultats = np.where(grille_np == symbole)
        if resultats[0].size > 0:
            return (resultats[0][0], resultats[1][0])
        else:
            return None
=======
        # Chercher l'indice de la valeur 1 dans la matrice
    def indice(self):
            for i in range(len(self.grille)):
                for j in range(len(self.grille[i])):
                    if self.grille[i][j] == 'P':
                        print("Indice de la valeur 'P' :", (i, j))
                        return (i,j)
>>>>>>> 4c1f68c600bcd8c00e8e0c4ad9341c5f2ccef080

         
matrice = Matrice()
matrice.placer_point(0, 4, 'G')  
matrice.placer_point(0, 0, "R")
matrice.placer_point(4, 0, 'Y')  
matrice.placer_point(4, 3, "B")


<<<<<<< HEAD
matrice.placer_point(2, 3, 'X')  # Placez 'P' à la position (2, 3)
print("Coordonnées de 'X':", matrice.trouver_coordonnee('X'))
matrice.afficher()
=======
matrice.placer_point(2, 2, 'P')  
matrice.afficher()
print("Tentative de déplacement à droite:")
matrice.deplacer(matrice.indice(), 'droite')
matrice.afficher()
>>>>>>> 4c1f68c600bcd8c00e8e0c4ad9341c5f2ccef080
