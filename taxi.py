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
        self.fenetre.after(100, self.dessiner_obstacles)
        self.fenetre.after(100, self.mise_a_jour_taxi)


    def dessiner_grille(self):
        print("Dessiner la grille")
        for i in range(5):
            for j in range(5):
                x1, y1 = j * 80, i * 80
                x2, y2 = (j + 1) * 80, (i + 1) * 80
                rect_tag = f"rect_{i}_{j}" # Créer une balise unique pour chaque rectangle
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='grey', fill='white', tags=[rect_tag])
                print(f"Rectangle créé à: ({x1}, {y1}, {x2}, {y2})")

    def dessiner_points(self):
        print("Dessiner les points")
        for i in range(5):
            for j in range(5):
                print(f"Valeur à {i}, {j}: {self.matrice.grille[i][j]}")
                if self.matrice.grille[i][j] != '0':
                    x1, y1 = j * 80 + 10, i * 80 + 10
                    x2, y2 = j * 80 + 70, i * 80 + 70
                    self.canvas.create_image(x1, y1, image=self.image, anchor='nw')
                    print(f"Image créée à: ({x1}, {y1})")
    def dessiner_obstacles(self):
        for (x, y), directions in self.matrice.mouvements_interdits.items():
            for direction in directions:
                if direction == 'gauche':
                    self.canvas.create_line(y * 80, x * 80, y * 80, (x + 1) * 80, width=2, fill='black')
                elif direction == 'droite':
                    self.canvas.create_line((y + 1) * 80, x * 80, (y + 1) * 80, (x + 1) * 80, width=5, fill='black')
        for i in range(5):
            for j in range(5):
               if self.matrice.grille[i][j] == 'R':
                   self.canvas.create_rectangle(j * 80 + 10, i * 80 + 10, j * 80 + 70, i * 80 + 70, fill='red')
               elif self.matrice.grille[i][j] == 'Y':
                   self.canvas.create_rectangle(j * 80 + 10, i * 80 + 10, j * 80 + 70, i * 80 + 70, fill='yellow')
               elif self.matrice.grille[i][j] == 'G':
                   self.canvas.create_rectangle(j * 80 + 10, i * 80 + 10, j * 80 + 70, i * 80 + 70, fill='green')
               elif self.matrice.grille[i][j] == 'B':
                   self.canvas.create_rectangle(j * 80 + 10, i * 80 + 10, j * 80 + 70, i * 80 + 70, fill='blue')
    def mise_a_jour_taxi(self):
        print("Mise à jour du taxi")
        taxi_pos = self.matrice.indice()
        print(f"Position du taxi: {taxi_pos}")
        if taxi_pos:
            x, y = taxi_pos
            self.canvas.delete("taxi")
            x1, y1 = y * 80 + 10, x * 80 + 10
            x2, y2 = y * 80 + 70, x * 80 + 70
            self.canvas.create_image(x1, y1, image=self.image, anchor='nw', tags="taxi")
            print(f"Taxi créé à: ({x1}, {y1})")
            self.canvas.itemconfig('case', fill='#000000')

# Exemple d'utilisation
root = tk.Tk()
matrice = Matrice()
matrice.placer_point(0, 0, 'R')
matrice.placer_point(4, 0, 'Y')
matrice.placer_point(2, 2, 'P')
app = Taxi(root, matrice )
app.image = tk.PhotoImage(file=r"taxi.png") # Charger l'image
root.mainloop()
