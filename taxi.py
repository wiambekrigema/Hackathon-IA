import tkinter as tk
from tkinter import messagebox

class Taxi:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        fenetre.title("Taxi Autonome")

        self.label = tk.Label(fenetre, text="Binevenue dans notre appli!")
        self.label.pack()
    def move_taxi(self, x, y):
        print(f" taxi bouge ({x}, {y})")

root = tk.Tk()
app = Taxi(root)
root.mainloop()

