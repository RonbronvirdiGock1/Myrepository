count = 0  
print("You can enter numbers. Type 'done' when you're finished.")

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input == "done":  
        break
    
    if user_input.isdigit():  
        count += 1  
    else:
        print("That's not a valid number. Please try again.")

print(f"You have entered {count} valid numbers.")
