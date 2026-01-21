import random

while True:
    user_action = input("Enter your choice(rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_actions = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_actions}. \n")


    if user_action == computer_actions:
        print(f"Both players chose {user_action}. Its a tie !!!")
    elif user_action == "rock":
        if computer_actions == "scissors":
            print("Rock smashes scissors. You win !!!")
        else :
            print("Paper covers rock. You lose !!!")
    elif user_action == "scissors":
        if computer_actions == "paper":
            print("Scissors cut paper. You win !!!")
        else :
            print("Rock smashes scissors. You lose !!!")
    
    play_again = input("Play again??? (y/n):")
    if play_again != "y":
        break