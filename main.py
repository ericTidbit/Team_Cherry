from Silksong_waiter import Silksong_waiter
from Compagnie import Compagnie
from textwrap import dedent
import random

def afficher_menu():
    print(dedent("""
    Menu:
    1- Commencer journée
    2- Se suicider
    0- Quitter
    """))

def evenement():
    # Define the events and their probabilities (as percentages)
    events = [
        ("Announce the release date of Silksong", 10),  # 10% probability
        ("Shadowdrop Silksong", 5),                    # 5% probability
        ("Generate bait", 70),                         # 70% probability
        ("Announce we are hard at work", 10),          # 10% probability
        ("Silksong is cancelled", 5)                   # 5% probability
    ]
    
    # Generate a random number between 0 and 100 (for percentages)
    random_value = random.randint(0, 100)
    
    # Track the cumulative probability
    cumulative_probability = 0
    
    # Check which event the random value falls into based on probabilities
    for event, probability in events:
        cumulative_probability += probability
        if random_value < cumulative_probability:
            return event
    

def main():

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        match choix:
            case "1":
                Silksong_waiter("Juanito", 11)
                event = evenement()
            case "2":
                Silksong_waiter.kms(0)
            case "0":
                print("Au revoir !")
                break
            case _:
                print("Choix invalide !")

if __name__ == '__main__':
    import sys
    main()
    sys.exit(0)
