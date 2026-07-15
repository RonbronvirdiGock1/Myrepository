import tkinter as tk
import random

user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

def play_game(user_choice):
    """
    This function runs one round of Rock-Paper-Scissors.
    It gets the user's choice, makes a computer choice,
    determines the winner, and updates the score and display.
    """
    global user_score, computer_score 
    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"You chose: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text="You Win!")
        user_score += 1 
    else:
        result_label.config(text="Computer Wins!")
        computer_score += 1 

    score_label.config(text=f"Score: You {user_score} - Computer {computer_score}")

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")
root.config(bg="#E0FFFF") 

title_label = tk.Label(root, text="Rock, Paper, Scissors!",
                       font=("Arial", 18, "bold"), bg="#E0FFFF", fg="darkblue")
title_label.pack(pady=15)

user_choice_label = tk.Label(root, text="You chose: ---",
                            font=("Arial", 12), bg="#E0FFFF")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer chose: ---",
                                font=("Arial", 12), bg="#E0FFFF")
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Make your move!",
                       font=("Arial", 14, "italic"), bg="#E0FFFF", fg="purple")
result_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#E0FFFF")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock",
                        command=lambda: play_game("rock"),
                        font=("Arial", 12), width=8, bg="lightgray", fg="black")
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper",
                         command=lambda: play_game("paper"),
                         font=("Arial", 12), width=8, bg="lightgray", fg="black")
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors",
                            command=lambda: play_game("scissors"), 
                            font=("Arial", 12), width=8, bg="lightgray", fg="black")
scissors_button.grid(row=0, column=2, padx=5)

# Score Label
score_label = tk.Label(root, text=f"Score: You {user_score} - Computer {computer_score}",
                       font=("Arial", 14, "bold"), bg="#E0FFFF", fg="darkgreen")
score_label.pack(pady=15)

root.mainloop()