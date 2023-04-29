from turtl3 import *

model = None


def start(t: Turtl3):
    global model
    model = load_model("monkey.obj")
    model.move(Vec3(0, 0, 10))
    t.fps = 60
    t.ups = 30
    t.set_wireframe_overlay(True)
    listen_for_keys(["w", "a", "s", "d", "space", "Shift_L", "Up", "Down", "Left", "Right"])


def draw(t: Turtl3):
    t.cube(0, 0, -2, 5, 5, 5, colors=[Vec3(0, 0, 0), Vec3(1, 0, 0), Vec3(0, 1, 0), Vec3(0, 0, 1), Vec3(1, 1, 0), Vec3(0, 1, 1)])
    t.model(model)


def update(t: Turtl3):
    if is_pressed("space"):
        t.move(0, 1, 0)
    if is_pressed("Shift_L"):
        t.move(0, -1, 0)
    if is_pressed("w"):
        t.move(-1, 0, 0)
    if is_pressed("a"):
        t.move(0, 0, -1)
    if is_pressed("s"):
        t.move(1, 0, 0)
    if is_pressed("d"):
        t.move(0, 0, 1)
    if is_pressed("Up"):
        t.rotate(1, 0, 0)
    if is_pressed("Down"):
        t.rotate(-1, 0, 0)
    if is_pressed("Left"):
        t.rotate(0, 1, 0)
    if is_pressed("Right"):
        t.rotate(0, -1, 0)


def main():
    t = Turtl3(800, 600)
    t.loop(start, draw, update)


if __name__ == '__main__':
    main()
