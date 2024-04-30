# Arnav Code Space Project 1
name = input("Enter your name: ")
print("Hello " + name )

userInput = input("Press Enter to continue")

print("\n**********************************************************************")

# Promt for users interests
print("Enter your character ")
print("Wizard ( Has magical powers )")
print("Vampire ( Can transfer into bats, lives forever ) ")
print("Werewolf ( Wolf like senses, speed, strenght, agility ) ")

character = input("")
print("\n")

while True:
    if character == "Wizard":
        print("You selected " + character)
        break
    elif character == "Vampire":
        print("You selected " + character)
        break
    elif character == "Werewolf":
        print("You selected " + character)
        break
    else:
        print("Invalid character. Please select again.")
        character = input("")

print("\n")
userInput = input("Press Enter to continue")
print("\n**********************************************************************")

print("You start on your adventure, and you stumble across a four-forked road.")
print("Each road has a sign that is associated with a program.\nPlease enter your area of interest (Input 1, 2, 3, or 4)\n")


interest = input("1 - Computing and IT\n2 - Science\n3 - Engineering\n4 - Health Sciences\n")

# Ryan Bell Code Space Project 1
print("\n")
userInput = input("Press Enter to continue")
print("\n**********************************************************************")

while True:
    if interest == "1":
        print("Congrats! You have choosen the Computing and IT pathway!")
        print("You should take the classes STEM 101, STEM 103, and English 101!")
        break
    elif interest == "2":
        print("Congrats! You have choosen the Science pathway!")
        print("You should take the classes STEM 101, STEM 102, and Pre Calculus!")
        break
    elif interest == "3":
        print("Congrats! You have choosen the Engineering pathway!")
        print("You should take the classes STEM 101, ENGR 111, and Pre Calculus!")
        break
    elif interest == "4":
        print("Congrats! You have choosen the Health Sciences pathway!")
        print("You should take the classes STEM 101, STEM 102, and English 101!")
        break
    else:
        print("Incorrect direction, please try again.")
        interest = input("")

print("\n")
userInput = input("Press Enter to continue")
print("\n**********************************************************************")
print("Good luck on your journey, " + name + "!")
