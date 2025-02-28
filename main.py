from Silksong_waiter import Silksong_waiter
from Compagnie import Compagnie
from textwrap import dedent

def afficher_menu():
    print(dedent("""
    Menu:
    1- Commencer journée
    2- Se suicider
    0- Quitter
    """))

def main():

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        match choix:
            case "1":

            case "2":

            case "0":
                print("Au revoir !")
                break
            case _:
                print("Choix invalide !")

if __name__ == '__main__':
    import sys
    main()
    sys.exit(0)