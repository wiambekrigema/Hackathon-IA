import tkinter as tk
from matrice import Matrice
class TaxiApp:
    def __init__(self, fenetre, matrice):
        self.fenetre = fenetre
        self.matrice = matrice
        fenetre.title("Taxi Application")

        self.buttons = [[None for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.buttons[i][j] = tk.Button(fenetre, text=self.matrice.grille[i][j], command=lambda i=i, j=j: self.move_taxi(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def move_taxi(self, x, y):
        if self.matrice.est_mouvement_autorise((x, y), 'droite'):
            print(f"Mouvement de {x}, {y} à droite autorisé.")
            self.matrice.deplacer((x, y), 'droite')
            for i in range(5):
                for j in range(5):
                    self.buttons[i][j]['text'] = self.matrice.grille[i][j]

root = tk.Tk()
matrice = Matrice()
app = TaxiApp(root, matrice)
root.mainloop()
