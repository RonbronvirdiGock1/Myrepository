import random
playing = True
number = str(random.randint(10,20))


print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
print("The game ends when you get one hero!")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your wasnt quite write, please try again. \n")
