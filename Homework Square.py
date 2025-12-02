import turtle

screen = turtle.Screen()
screen.bgcolor("brown")  
my_turtle = turtle.Turtle()
my_turtle.shape("square")  
my_turtle.speed(2)  

for _ in range(4): 
    my_turtle.forward(100)  
    my_turtle.left(90)  

turtle.done()
