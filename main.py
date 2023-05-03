import math
import time

from turtl3 import *

model = None

sphere = False

def start(t: Turtl3):
    global model
    model = load_model("sphere.obj")
    model.move(Vec3(0, 5, 10))
    t.rotate(0, 5, 0)
    t.move(0, 0, 0)
    t.fps = 60
    t.ups = 30
    t.speed = 0.005
    t.rot_speed = 0.001
    t.light_dir = Vec3(0.9, 0.9, 0.9)
    t.light_itensity = 5
    t.back_face_inv = False
    t.enable_lighting = False #l
    t.enable_depth_test = False #b
    t.negative_z_check = False #z
    t.back_face_check = False #c
    t.set_wireframe_overlay(False) #x
    listen_for_keys(["w", "a", "s", "d", "space", "Shift_L", "Up", "Down", "Left", "Right", "l", "b", "z", "x", "o", "c", "i"])


def draw(t: Turtl3):
    t.cube(-5, 0, 5, 10, 1, 10, colors=[Vec3(0.5, 0, 0.5), Vec3(0.5, 0, 0), Vec3(0, 0.5, 0), Vec3(0, 0, 0.5), Vec3(0.5, 0.5, 0), Vec3(0, 0.5, 0.5)])
    if sphere:
        t.model(model)


def update(t: Turtl3):
    global sphere
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

    if is_pressed("l"):
        t.enable_lighting = not t.enable_lighting
    if is_pressed("b"):
        t.enable_depth_test = not t.enable_depth_test
    if is_pressed("z"):
        t.negative_z_check = not t.negative_z_check
    if is_pressed("x"):
        t.set_wireframe_overlay(not t.wireframe_overlay)
    if is_pressed("o"):
        sphere = not sphere
        if sphere:
            t.speed = 0.05
            t.rot_speed = 0.01
        else:
            t.speed = 0.005
            t.rot_speed = 0.001
    if is_pressed("c"):
        t.back_face_check = not t.back_face_check
    if is_pressed("i"):
        t.back_face_inv = not t.back_face_inv

    t.light_dir = Vec3(math.sin(t.frame / 50), 0, math.cos(t.frame / 50))


def main():
    t = Turtl3(1000, 800)
    t.loop(start, draw, update)


if __name__ == '__main__':
    main()
