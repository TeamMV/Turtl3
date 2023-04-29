# Turtl3
I think all python devs know the turtle library, but this python file brings turtle to another DIMENSION!!! Welcome to turtl3.py, a 3D turtle library.
To start, create a `Turtl3` object and call its `loop()` method with two methods for the start, update and draw event.
```python
def start(t):
    pass

def update(t):
    pass

def draw(t):
    pass

t3 = Turtl3(800, 600)
t3.loop(start, draw, update)
```
Additionally, other fields of the `Turtl3` instance can be set.

In start, you can define which keys to observe by calling either the `listen_for_key()` or the `listen_for_keys()` function.
```python
turtl3.listen_for_keys(["w", "a", "s", "d"])
```

It is also possible to load an .obj wavefront model file. Simply do:
```python
model = load_model("monkey.obj")
model.move(Vec3(0, 0, 10))
```

Since there is no lighting, I recommend to enable the wireframe by calling
```python
t3.set_wireframe_overlay(True)
```

In the draw loop, a model or a cube can be rendered like that:
```python
t3.cube(0, 0, -2, 5, 5, 5, colors=[Vec3(0, 0, 0), Vec3(1, 0, 0), Vec3(0, 1, 0), Vec3(0, 0, 1), Vec3(1, 1, 0), Vec3(0, 1, 1)])
t3.model(model)
```
The `colors` parameter sets the colors for the individual faces of the cube, but the parameter `color` can also be used, to set all the faces at once.

In update or draw, the keys can be checked to update the scene:
```python
def update(t3: Turtl3):
    if is_pressed("space"):
        t3.move(0, 1, 0)
    if is_pressed("Shift_L"):
        t3.move(0, -1, 0)
    if is_pressed("w"):
        t3.move(-1, 0, 0)
    if is_pressed("a"):
        t3.move(0, 0, -1)
    if is_pressed("s"):
        t3.move(1, 0, 0)
    if is_pressed("d"):
        t3.move(0, 0, 1)
    if is_pressed("Up"):
        t3.rotate(1, 0, 0)
    if is_pressed("Down"):
        t3.rotate(-1, 0, 0)
    if is_pressed("Left"):
        t3.rotate(0, 1, 0)
    if is_pressed("Right"):
        t3.rotate(0, -1, 0)
```

__IMPORTANT__ Only keys that where specified via either the `listen_for_key()` or the `listen_for_keys()` function can be checked!

Anyways, have fun with this stupid little thing!
:D