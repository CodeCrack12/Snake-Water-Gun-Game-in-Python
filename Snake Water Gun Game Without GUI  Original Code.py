from random import choice

print("\nSnake Water Gun Game:\n\nSnake, Water and Gun is a variation "
      "of the children's game \"rock-paper-"
      "scissors\" where\n"
      "players use hand "
      "gestures to represent a snake, water, or a gun. \n"
      "\nThe gun beats the snake, the water beats the gun, "
      "and the snake beats the water.\nGame Instructions:\n\nPress 1 for "
      "Snake.\nPress 2 for Water."
      "\nPress 3 for Gun")

items = ["Snake", "Water", "Gun"]

computer_selection = choice(items)

print("\nEnter Your Value According To The Above Given Instructions:")
player_selection = int(input("Value: "))

print("Computer: ", computer_selection) 
if player_selection == 1:
    print("Player: Snake")
elif player_selection == 2:
    print("Player: Water")
elif player_selection == 3:
    print("Player: Gun")

if player_selection == 1 or player_selection == 2 or player_selection == 3:
    if computer_selection == "Snake" and player_selection == 1:
        print("Draw")
    elif computer_selection == "Snake" and player_selection == 2:
        print("Looser.")
    elif computer_selection == "Snake" and player_selection == 3:
        print("Winner.")
    elif computer_selection == "Water" and player_selection == 1:
        print("Winner.")
    elif computer_selection == "Water" and player_selection == 2:
        print("Draw.")
    elif computer_selection == "Water" and player_selection == 3:
        print("Looser.")
    elif computer_selection == "Gun" and player_selection == 1:
        print("Looser.")
    elif computer_selection == "Gun" and player_selection == 2:
        print("Winner.")
    elif computer_selection == "Gun" and player_selection == 3:
        print("Draw.")
else:
    print("Just Enter 1, 2 and 3.")