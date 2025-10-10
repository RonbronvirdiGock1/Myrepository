markOne = int(input("Enter a number"))
markTwo = int(input("Enter a number"))
markThree = int(input("Enter a number"))
markFour = int(input("Enter a number"))
markFive = int(input("Enter a number"))

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your grade is A1")
elif avg>=81 and avg<=90:
    print("Your grade is A2")
elif avg>=71 and avg<=80:
    print("Your grade is B1")
elif avg>=61 and avg<=70:
    print("Your grade is B2")
elif avg>=51 and avg<=60:
    print("Your grade is B3")
elif avg>=41 and avg<=50:
    print("Your grade is C")
else:
    print("Not successful")