import numpy as np

class machine_learning :    

    def __init__(self, taxi, matrice) :
        self.taxi = taxi
        self.matrice = matrice
        self.indice = [0,0]

    def deplacement(self, matrice) :
        self.matrice 

    def affiche(self) :
        print(self.matrice)

    def taxi_init(self) :
        self.matrice[0,0] = self.taxi

    def trouve_indice(self):
        self.indice = list(zip(np.where(self.matrice == 1)))
        print(self.indice)

    #def droite(self):
        

#--------------------------------#

M = np.zeros((3,3))

test=machine_learning(1, M)
test.taxi_init()
test.affiche()
test.trouve_indice()

