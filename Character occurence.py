string = input("Please enter your own word : ")
char = input("Please enter your own character : ")
i = 0
count = 0

while(i < len(string)):   #string operation

    if(string[i].lower() == char):   #conditoin 1
        count = count + 1
    i = i + 1

#Display the result
print("The total Numbers of Times ", char, " has Occurred = " , count)