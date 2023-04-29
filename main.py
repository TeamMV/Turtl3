from turtl3 import *


def start(t: Turtl3):
    t.fps = 60
    t.ups = 30
    listen_for_keys(["w", "a", "s", "d", "space", "Shift_L", "uparrow", "downarrow", "leftarrow", "rightarrow"])


def draw(t: Turtl3):
    t.cube(10, 10, -40, 10, 10, 10, Vec3(0, 0, 0))


def update(t: Turtl3):
    if is_pressed("space"):
        t.move(0, 1, 0)
    if is_pressed("Shift_L"):
        t.move(0, -1, 0)
    if is_pressed("w"):
        t.move(-1, 0, 0)
    if is_pressed("a"):
        t.move(0, 0, 1)
    if is_pressed("s"):
        t.move(1, 0, 0)
    if is_pressed("d"):
        t.move(0, 0, -1)
    if is_pressed("uparrow"):
        t.rotate(1, 0, 0)
    if is_pressed("downarrow"):
        t.rotate(-1, 0, 0)
    if is_pressed("leftarrow"):
        t.rotate(0, 1, 0)
    if is_pressed("rightarrow"):
        t.rotate(0, -1, 0)


def main():
    t = Turtl3(800, 600)
    t.loop(start, draw, update)


if __name__ == '__main__':
    main()
