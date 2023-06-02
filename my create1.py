import turtle
import math

screen = turtle.Screen()
screen.title('5 Degree Square Spiral in a Square - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

def draw_square(x,y,direction,length):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(direction)
    turtle.back(length/2)
    turtle.left(90)
    turtle.back(length/2)
    turtle.seth(direction)
    turtle.down()
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)

def square_spiral(x,y,direction,length):
    if length < 5: return
    
    draw_square(x,y,direction,length)
    square_spiral(x,y,direction+alpha,length/(math.sin(math.radians(alpha)) + math.cos(math.radians(alpha))))


alpha=5
square_spiral(0,0,0,1600)