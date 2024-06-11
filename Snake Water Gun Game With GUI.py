import tkinter as tk
from random import choice
from tkinter import font

# Define the game logic
def game(player_selection):
    items = ["Snake", "Water", "Gun"]
    computer_selection = choice(items)
    result = ""

    if computer_selection == "Snake" and player_selection == "Snake":
        result = "Draw 😐"
    elif computer_selection == "Snake" and player_selection == "Water":
        result = "Loser 😞"
    elif computer_selection == "Snake" and player_selection == "Gun":
        result = "Winner 😃"
    elif computer_selection == "Water" and player_selection == "Snake":
        result = "Winner 😃"
    elif computer_selection == "Water" and player_selection == "Water":
        result = "Draw 😐"
    elif computer_selection == "Water" and player_selection == "Gun":
        result = "Loser 😞"
    elif computer_selection == "Gun" and player_selection == "Snake":
        result = "Loser 😞"
    elif computer_selection == "Gun" and player_selection == "Water":
        result = "Winner 😃"
    elif computer_selection == "Gun" and player_selection == "Gun":
        result = "Draw 😐"

    result_label.config(text=f"Computer: {computer_selection}\n\nPlayer: {player_selection}\n\n{result}")

# Create the GUI
root = tk.Tk()
root.title("Snake Water Gun Game")

# Define the font
game_font = font.Font(family='Helvetica', size=14, weight='bold')

instructions = tk.Label(root, text="Press 1 for Snake.\nPress 2 for Water.\nPress 3 for Gun.", font=game_font)
instructions.pack(pady=10)

result_label = tk.Label(root, text="", font=game_font)
result_label.pack(pady=10)

snake_button = tk.Button(root, text="Snake", command=lambda: game("Snake"), font=game_font)
snake_button.pack(pady=10)

water_button = tk.Button(root, text="Water", command=lambda: game("Water"), font=game_font)
water_button.pack(pady=10)

gun_button = tk.Button(root, text="Gun", command=lambda: game("Gun"), font=game_font)
gun_button.pack(pady=10)

root.mainloop()
