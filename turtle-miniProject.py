import turtle

window = turtle.Screen()
window.bgcolor("white")


def draw_square():
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    for i in range(4):
        brad.forward(100)
        brad.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.color("green")
    count = 0
    angie.speed(20)
    while(count < 360):
        angie.circle(60)
        count += 15
        angie.right(15)
    count = 0
    angie.right(7.5)
    angie.speed(20)
    angie.color("blue")
    while(count < 360):
        angie.circle(70)
        count += 15
        angie.right(15)
    count = 0
    angie.right(7.5)
    angie.speed(20)
    angie.color("red")
    while(count < 360):
        angie.circle(65)
        count += 15
        angie.right(15)
    angie.right(7.5)
    angie.speed(20)
    count = 0
    angie.color("purple")
    while(count < 360):
        angie.circle(90)
        count += 15
        angie.right(30)

def draw_triangle():
    teddy = turtle.Turtle()
    teddy.shape("turtle")
    teddy.color("green")
    for i in range(3):
        teddy.forward(100)
        teddy.right(120)

def draw_pattern():
    art = turtle.Turtle()
    art.shape("turtle")
    art.speed(25)
    art.right(90)
    length = 40
    for i in range(36):
        art.forward(length)
        art.right(45)
        art.forward(length)
        art.right(135)
        art.forward(length)
        art.right(45)
        art.forward(length)
        art.right(125)
    art.forward(150)

    
draw_pattern()
window.exitonclick() 
