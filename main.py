from taxi import Taxi
def main():
    # Créer une instance de Taxi
    taxi = Taxi([0, 0], [5, 5])

    # Afficher l'état initial du taxi
    print(f"Position initial: {taxi.position}")

    # Déplacer le taxi
    for _ in range(5):
        taxi.move("gauche")
        taxi.move("bas")

    # Afficher l'état après le déplacement
    print(f"Aprés avoir bouger il arrive : {taxi.position}")

    # Vérifier si le taxi a atteint sa destination
    if taxi.arrived():
        print("Le taxi est arrivé ")
    else:
        print("Le taxi n'est pas encore arrivé.")

if __name__ == "__main__":
    main()


