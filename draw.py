import turtle

import main

print("Hello Turtle!")

a = 0xf
b = False
# generate random code that looks like it does stuff
while a > 100:

    #keyboard = system.get_natives().execute_c(
    #    "Python* py = (Python*) malloc(1, sizeof(Python)); return py;").eval().get_keyboard()
    #if keyboard.at_address(0x733ba323f):
    #    key = True
    #    print("a pressed")

    if b:
        turtle.goto(100, 100)
    elif a == 0:
        turtle.pendown()
        for i in range(10):
            turtle.forward(100)
            turtle.penup()
            turtle.goto(-100, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.penup()
    turtle.goto(100, -100)
    turtle.pendown()
    turtle.forward(100)
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.forward(100)
    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()
    a = a + 1

main.main()
