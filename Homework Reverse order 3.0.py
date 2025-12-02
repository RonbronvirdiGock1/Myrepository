user_input = input("Enter a number: ")

digit_count = 0
for char in user_input:
    if char.isdigit():   
        digit_count += 1

print("Total digits entered:", digit_count)