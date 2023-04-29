import time
import turtle

from turtl3 import *

draw = Turtl3(800, 600)
speed = 3


def w():
    draw.move(0, 0, speed)


def a():
    draw.move(-speed, 0, 0)


def s():
    draw.move(0, 0, -speed)


def d():
    draw.move(speed, 0, 0)


def space():
    draw.move(0, speed, 0)


def shift():
    draw.move(0, -speed, 0)


def l():
    draw.rotate(0, 0.05, 0)

def r():
    draw.rotate(0, -0.05, 0)

def u():
    draw.rotate(0.05, 0, 0)

def do():
    draw.rotate(-0.05, 0, 0)

def main():
    turtle.onkeypress(w, "w")
    turtle.onkeypress(a, "a")
    turtle.onkeypress(s, "s")
    turtle.onkeypress(d, "d")
    turtle.onkeypress(space, "space")
    turtle.onkeypress(shift, "x")
    turtle.onkeypress(l, "Left")
    turtle.onkeypress(r, "Right")
    turtle.onkeypress(u, "Up")
    turtle.onkeypress(do, "Down")
    while True:
        turtle.listen()
        draw.cube(10, 10, -40, 10, 10, 10, Vec3(0, 0, 0))
        draw.render(T3_TRIANGLES)


if __name__ == '__main__':
    main()
