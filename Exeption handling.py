#using try and exept
try:

    number = int(input("Enter a number:  "))
    print("The number entered is", number)

#using valueError
except ValueError as ex:
    print("Exception: please enter a valid number here")