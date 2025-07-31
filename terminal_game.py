
# Introduction to Labyrinth 317
# This code snippet is part of a text-based adventure game where the player navigates through a labyrinth.

print('''
==================================
     WELCOME TO LABYRINTH 317
==================================
\n''')
print("Hello, traveller! You have found a special place. This is Labyrinth 317.")
print("I am LYRA, your guide through this labyrinth. You only have one task: to find the exit and escape this place.\n")

player_name = input("Before we begin, do you mind telling me your name? ")

print("\n")
print(f"Hello, {player_name}. Due to technological restrictions in Labyrinth 317, your visual perceptions would be limited.")
print("You will only be able to see the text I provide, so please pay attention to the details and follow my instructions carefully.\n")

ready_or_not = input("Let me know when you're ready to start your journey. Type 'ready' to proceed.\n").lower()
while ready_or_not != "ready":
    ready_or_not = input(f'''Listen to my instructions, {player_name}. That's the only way you'll be able to escape.
    Type 'ready' when you are prepared to start your journey: \n''').lower()

print("\n")
print("Great! I will now open the door to the labyrinth. Please proceed with caution.\n")

# Corridor 1
print("You find yourself in a dimly lit corridor. The walls are damp, and the air is musty.")
print("There are two paths ahead: one to the left and one to the right.")

path_choice = input("Which path do you choose? Type 'left' or 'right': \n").lower()
while path_choice not in ["left", "right"]:
    path_choice = input(f'''Now don't be stubborn, {player_name}. Choose only from the options I gave you.
    Please type 'left' or 'right' to choose your path: \n''').lower()

print("\n")

# Left Path: Orb Room
if path_choice == "left":
    print("You take the left path and find yourself in a small room with a flickering light.")
    print("In the center of the room, there is a pedestal with a glowing orb on it.")
    print("Behind the orb, there are two doors: one red and one white.\n")
    orb_room = input("Which door do you choose? ").lower()

    print("\n")

    # TRAPPED
    while orb_room in ["red", "white"]:
        print("\n")
        print("You step towards the door you chose, and slowly open it.")
        print("You found yourself in a sealed room with no exit.")
        print("You realize you need to go back to the corridor.\n")
        print("HOWEVER!")
        print("There is one rule I forgot to mention: once you enter a room, you can never go back.\n")
        print(f"Aren't I silly? I should have told you that earlier, {player_name}, but I guess it's too late now.\n")
        print("You are now trapped in this room forever.")
        print(f"Sorry, {player_name}, but you have failed to escape Labyrinth 317.")
        print("\n")
        print("[DEAD END]")
        exit()

    # Hidden Passage
    print("You have found a hidden passage that leads to the outside of the labyrinth!")
    print(f"Congratulations, {player_name}, you have escaped Labyrinth 317!")
    print('''
==================================
     ✦✦✦ CONGRATULATIONS ✦✦✦
==================================
    \n''')
    exit()

# Right Path: Symbol Hallway
else:
    print("You take the right path and enter a long hallway filled with strange symbols on the walls.")
    print("At the end of the hallway, you see a door that seems to be slightly ajar.\n")
    print("You enter the room and find it filled with ancient artifacts and scrolls.")
    print("In the center of the room, there is a large book on a pedestal.")
    print("You walked towards the book to inspect it.\n")
    book_choice = input("Do you want to read the book? Type 'yes' or 'no': ").lower()

    print("\n")

    # Yes Book Reading
    if book_choice == "yes":
        print("You open the book and find it filled with cryptic symbols and strange illustrations.")
        print("You flip through the pages and find a note that reads:\n")
        print("The labyrinth is only as strong as the mind that holds it.")
        print("\n")
        print("You turn away from the book, and found two passages: one leading to a dark room and another leading to a bright room.")

        # TRAPPED
        passage_choice = input("Which passage would you like to take? You can type in 'dark' or 'bright'\n").lower()
        if passage_choice in ["dark", "bright"]:
            print("\n")
            print("You step towards the passage you chose, and slowly open it.\n")
            print("You found yourself in a sealed room with no exit.\n")
            print("The door where you entered has vanished, and you are now trapped here, possibly, for all eternity.\n")
            print(f"Sorry, {player_name}, but you have failed to escape Labyrinth 317.")
            print("Better luck next time, if there ever is one.\n")
            print("\n")
            print("[DEAD END]")
            exit()

        # Hidden Passage
        else:
            print("You have found a hidden passage that leads to the outside of the labyrinth!")
            print(f"Congratulations, {player_name}, you have escaped Labyrinth 317!")
            print('''
==================================
     ✦✦✦ CONGRATULATIONS ✦✦✦
==================================
            \n''')
            exit()

    # No Book Reading
    else:
        print("You decide not to read the book and explore the room instead.\n")
        print("You found two passages: one leading to a dark room and another leading to a bright room.")

        # TRAPPED
        passage_choice = input("Which passage would you like to take? You can type in 'dark' or 'bright'\n").lower()
        if passage_choice in ["dark", "bright"]:
            print("\n")
            print("You step towards the passage you chose, and slowly open it.\n")
            print("You found yourself in a sealed room with no exit.\n")
            print("The door where you entered has vanished, and you are now trapped here, possibly, for all eternity.\n")
            print(f"Sorry, {player_name}, but you have failed to escape Labyrinth 317.")
            print("Better luck next time, if there ever is one.\n")
            print("\n")
            print("[DEAD END]")
            exit()

        # Hidden Passage
        else:
            print("You have found a hidden passage that leads to the outside of the labyrinth!")
            print(f"Congratulations, {player_name}, you have escaped Labyrinth 317!")
            print('''
==================================
     ✦✦✦ CONGRATULATIONS ✦✦✦
==================================
            \n''')
            exit()