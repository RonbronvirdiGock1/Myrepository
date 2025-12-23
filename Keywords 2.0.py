for x in range(10):
    if x % 20 == 0:
        print("Twist")
    
    elif x % 15 ==0:
        pass          #pass statement

    elif x % 5 == 0:
        print("fizz")

    elif x % 3 == 0:
        print("buzz")

    else:
        print(x)