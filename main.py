import math
import time

from turtl3 import *

model = None


def start(t: Turtl3):
    global model
    model = load_model("sphere.obj")
    model.move(Vec3(0, 5, 10))
    t.rotate(0, 5, 0)
    t.move(0, 0, 0)
    t.fps = 60
    t.ups = 30
    t.speed = 0.05
    t.rot_speed = 0.01
    t.light_dir = Vec3(0.9, 0.9, 0.9)
    t.light_intensity = 5
    t.back_face_inv = False
    t.enable_lighting = True
    t.enable_depth_test = True
    t.negative_z_check = True
    t.back_face_check = True
    t.set_wireframe_overlay(False)
    listen_for_keys(["w", "a", "s", "d", "space", "Shift_L", "Up", "Down", "Left", "Right"])


def draw(t: Turtl3):
    t.cube(-5, 0, 5, 10, 1, 10,
           colors=[Vec3(0.5, 0, 0.5), Vec3(0.5, 0, 0), Vec3(0, 0.5, 0), Vec3(0, 0, 0.5), Vec3(0.5, 0.5, 0),
                   Vec3(0, 0.5, 0.5)])
    t.model(model)


def update(t: Turtl3):
    if is_pressed("space"):
        t.move(0, -1, 0)
    if is_pressed("Shift_L"):
        t.move(0, 1, 0)
    if is_pressed("w"):
        t.move(-1, 0, 0)
    if is_pressed("a"):
        t.move(0, 0, 1)
    if is_pressed("s"):
        t.move(1, 0, 0)
    if is_pressed("d"):
        t.move(0, 0, -1)
    if is_pressed("Up"):
        t.rotate(-1, 0, 0)
    if is_pressed("Down"):
        t.rotate(1, 0, 0)
    if is_pressed("Left"):
        t.rotate(0, -1, 0)
    if is_pressed("Right"):
        t.rotate(0, 1, 0)

    t.light_dir = Vec3(math.sin(t.frame / 50), 0, math.cos(t.frame / 50))


def main():
    t = Turtl3(1000, 800)
    t.loop(start, draw, update)


if __name__ == '__main__':
    main()
