from Silksong_Waiter import Silksong_Waiter
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
        ("Announce the release date of Silksong", 10, -5),  # 10% probability
        ("Shadowdrop Silksong", 5, 0),                    # 5% probability
        ("Generate bait", 70, -30),                         # 70% probability
        ("Announce we are hard at work", 10, -15),          # 10% probability
        ("Silksong is cancelled", 5, -100)                   # 5% probability
    ]
    
    # Generate a random number between 0 and 100 (for percentages)
    random_value = random.randint(0, 100)
    
    # Track the cumulative probability
    cumulative_probability = 0
    
    # Check which event the random value falls into based on probabilities
    for event, probability, penalty in events:
        cumulative_probability += probability
        if random_value < cumulative_probability:
            return event, penalty

def journee(user, compagnie):
    event, penalty = evenement()
    user._sanity += penalty
    print(f"Aujourd'hui {compagnie.nom} decide: {event}")
    if user._sanity < 10:
        user.kms(user._sanity)
    else:
        user.pass_day(user._sanity)
    print(f"{user.nom} a une sanité de {user._sanity}.")

    # if event == "Announce the release date of Silksong":
    #     print(f"The release date is {compagnie.annoncer()}")
    # match event:
    #     case "Announce the release date of Silksong":
    #
    #     case "Shadowdrop Silksong":
    #
    #     case "Generate bait":
    #
    #     case "Announce we are hard at work":
    #
    #     case "Silksong is cancelled":




def create_waiter():
    nom = input("Entrez votre nom: ")
    sanity = int(input("Entrez votre niveau de sanité de 0 à 100 : "))
    return Silksong_Waiter(nom, sanity)

def create_compagnie():
    return Compagnie()

def main():
    user_1 = create_waiter()
    silksongsters = create_compagnie()

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        match choix:
            case "1":
                journee(user_1, silksongsters)
            case "2":
                user_1.kms()
            case "0":
                print("Au revoir !")
                break
            case _:
                print("Choix invalide !")

if __name__ == '__main__':
    import sys
    main()
    sys.exit(0)
