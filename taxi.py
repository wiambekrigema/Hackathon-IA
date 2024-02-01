import tkinter as tk
from matrice import Matrice

class Taxi:
    def __init__(self, fenetre, matrice):
        self.fenetre = fenetre
        self.matrice = matrice
        fenetre.title("Taxi Autonome")
        self.canvas = tk.Canvas(fenetre, width=400, height=400)
        self.canvas.pack()

        self.initialiser_affichage()

    def initialiser_affichage(self):
        # Initialiser la grille et les points après un court délai pour s'assurer que la fenêtre est affichée
        self.fenetre.after(100, self.dessiner_grille)
        self.fenetre.after(100, self.dessiner_points)
        self.fenetre.after(100, self.mise_a_jour_taxi)

    def dessiner_grille(self):
        print("Dessiner la grille")
        for i in range(5):
            for j in range(5):
                x1, y1 = j * 80, i * 80
                x2, y2 = (j + 1) * 80, (i + 1) * 80
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')
                print(f"Rectangle créé à: ({x1}, {y1}, {x2}, {y2})")

    def dessiner_points(self):
        print("Dessiner les points")
        for i in range(5):
            for j in range(5):
                print(f"Valeur à {i}, {j}: {self.matrice.grille[i][j]}")
                if self.matrice.grille[i][j] != '0':
                    x1, y1 = j * 80 + 10, i * 80 + 10
                    x2, y2 = j * 80 + 70, i * 80 + 70
                    self.canvas.create_oval(x1, y1, x2, y2, fill='yellow')
                    print(f"Ovale créé à: ({x1}, {y1}, {x2}, {y2})")

    def mise_a_jour_taxi(self):
        print("Mise à jour du taxi")
        taxi_pos = self.matrice.indice()
        print(f"Position du taxi: {taxi_pos}")
        if taxi_pos:
            x, y = taxi_pos
            self.canvas.delete("taxi")
            x1, y1 = y * 80 + 10, x * 80 + 10
            x2, y2 = y * 80 + 70, x * 80 + 70
            self.canvas.create_oval(x1, y1, x2, y2, fill='yellow', tags="taxi")
            print(f"Taxi créé à: ({x1}, {y1}, {x2}, {y2})")

# Exemple d'utilisation
root = tk.Tk()
matrice = Matrice()
matrice.placer_point(2, 2, 'P')  # Placer le taxi à la position initiale
app = Taxi(root, matrice )
root.mainloop()
