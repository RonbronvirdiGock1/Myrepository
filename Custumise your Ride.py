print("Select your ride")
print("1. Bike")
print("2. Car")

choice = int( input("Enter your choice: ") )

if ( choice ==1 ): #condition 1 outer if statement
    print( "What type of bike? " )
    print("1.Scooty\n")
    print("2.Scooter\n")

    choice2 = int(  input("Enter you choice2: "))
    if choice2==1: #inner if statement
        print("you hav selected scooty")
    else:
        print("you have selected scooter")

elif( choice ==2 ): #outer elif statment
    print("what type of car?")
    print("1. Sedan")
    print("2. XUV")

    choice3= int( input("enter your choice 3"))

    if choice3==1: #inner if statements
        print("you have selected sedan")
    else:
        print("you have selected XUV")

else: #outer else statements
    print("Wrong Choice!")