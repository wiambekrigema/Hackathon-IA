from matrice import  Matrice


matrice = Matrice()
matrice.placer_point(0, 4, 'G')  
matrice.placer_point(0, 0, "R")
matrice.placer_point(4, 0, 'Y')  
matrice.placer_point(4, 3, "B")


matrice.placer_point(0, 4, 'taxi')  
matrice.afficher()
print("Tentative de déplacement à droite:")
matrice.deplacer((0, 1), 'droite')




class Apprentisage:
    print('')