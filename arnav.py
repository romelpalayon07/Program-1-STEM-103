import time

class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        print(f"\n{name}:\n{description}")

def prompt_name():
    name = input("Welcome! Please enter your name: ")
    return name

def select_character():
    print("\nChoose your character:")
    print("1. Warrior - Strong and skilled in combat.")
    print("2. Wizard - Master of magic and spells.")
    print("3. Rogue - Agile and stealthy.")
    choice = input("Enter the number corresponding to your chosen character: ")

    characters = {
        "1": Character("Warrior", "Strong and skilled in combat."),
        "2": Character("Wizard", "Master of magic and spells."),
        "3": Character("Rogue", "Agile and stealthy.")
    }

    return characters.get(choice)

def main():
    print("Welcome to the Adventure Game!")
    name = prompt_name()
    character = select_character()

    if character:
        print(f"\nWelcome, {name}! You have chosen the {character.name}.")
        print("Let the adventure begin!\n")
        # Start the game logic here
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
