import turtle
import math
import time

T3_LINES = 2
T3_TRIANGLES = 3
T3_QUADS = 4

PI_4 = math.radians(90)

keys = []


def listen_for_key(k):
    turtle.onkeypress(lambda: keys.append(k) if not keys.__contains__(k) else 0, k)
    turtle.onkeyrelease(lambda: keys.remove(k) if keys.__contains__(k) else 0, k)


def listen_for_keys(ks):
    for k in ks:
        listen_for_key(k)


def is_pressed(k):
    return keys.__contains__(k)


class Turtl3:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ren = Renderer3D(self)
        self.vertices = []
        self.indices = []
        self.colors = []
        self.obj_ptr = 0
        self.fps = 60
        self.ups = 30
        self.speed = 0.2
        self.rot_speed = 0.1
        self.mode = T3_TRIANGLES
        self.wireframe = False
        self.wireframe_overlay = False
        self.pos = Vec3(0, 0, -25)
        self.rot = Vec3(0, -0.5, 0)
        self.light_dir = Vec3(0, 0, 0)
        self.light_itensity = 10
        self.frame = 0
        self.back_face_inv = False
        self.enable_depth_test = True
        self.enable_lighting = True
        self.view = Mat4()
        self.projection = Mat4()
        self.projection.perspective(80, self.width / self.height, 0, 2000)
        turtle.setup(width, height, 0, 0)
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)
        turtle.Screen().bgcolor("white")

    def set_draw_mode(self, mode):
        self.mode = mode

    def set_wireframe(self, wireframe):
        self.wireframe = wireframe

    def set_wireframe_overlay(self, wireframe_overlay):
        if wireframe_overlay:
            self.wireframe = False
        self.wireframe_overlay = wireframe_overlay

    def loop(self, start, draw, update):
        """The main loop of the program, call it once and receive the update and draw event wit the given function"""
        r = time.time() * 1000
        u = time.time() * 1000
        fps = 60
        ups = 20
        fb = 1000 / fps
        ub = 1000 / ups
        start(self)
        turtle.listen()
        while True:
            if (time.time() * 1000) - r >= fb:
                draw(self)
                self.render(self.mode)
                self.frame += 1
            if (time.time() * 1000) - u >= ub:
                update(self)

    def move(self, x, y, z):
        x *= self.speed
        y *= self.speed
        z *= self.speed
        if z != 0:
            self.pos.set_x(self.pos.x() + math.cos(self.rot.y()) * z)
            self.pos.set_z(self.pos.z() + math.sin(self.rot.y()) * z)

        if x != 0:
            self.pos.set_x(self.pos.x() + math.cos(self.rot.y() - PI_4) * x)
            self.pos.set_z(self.pos.z() + math.sin(self.rot.y() - PI_4) * x)

        self.pos.set_y(self.pos.y() + y)

        self.view.move(self.pos, self.rot)

    def rotate(self, x, y, z):
        self.rot += Vec3(x, y, z) * self.rot_speed
        self.view.move(self.pos, self.rot)

    def render(self, mode):
        turtle.clear()
        self.ren.render(self.vertices, self.indices, self.colors, self.projection, self.view, mode, self.width,
                        self.height, self.wireframe, self.wireframe_overlay)
        turtle.update()
        self.vertices.clear()
        self.indices.clear()
        self.colors.clear()
        self.obj_ptr = 0

    def model(self, model):
        for vertex in model.vertices:
            self.vertices.append(vertex)
        for index in model.indices:
            self.indices.append(self.obj_ptr + index)
        self.obj_ptr += len(model.vertices)
        for i in range(len(model.indices) // 3):
            self.colors.append(Vec3(0.5, 0.5, 0.5))

    def cube(self, x, y, z, w, h, d, **kwargs):
        self.vertices.append(Vec3(x, y, z), )
        self.vertices.append(Vec3(x + w, y, z))
        self.vertices.append(Vec3(x + w, y, z + d))
        self.vertices.append(Vec3(x, y, z + d))
        self.vertices.append(Vec3(x, y + h, z))
        self.vertices.append(Vec3(x + w, y + h, z))
        self.vertices.append(Vec3(x + w, y + h, z + d))
        self.vertices.append(Vec3(x, y + h, z + d))

        if self.back_face_inv:
            self.indices.append(self.obj_ptr + 5)
            self.indices.append(self.obj_ptr + 1)
            self.indices.append(self.obj_ptr + 0)
            self.indices.append(self.obj_ptr + 0)
            self.indices.append(self.obj_ptr + 4)
            self.indices.append(self.obj_ptr + 5)

            self.indices.append(self.obj_ptr + 6)
            self.indices.append(self.obj_ptr + 2)
            self.indices.append(self.obj_ptr + 1)
            self.indices.append(self.obj_ptr + 1)
            self.indices.append(self.obj_ptr + 5)
            self.indices.append(self.obj_ptr + 6)

            self.indices.append(self.obj_ptr + 7)
            self.indices.append(self.obj_ptr + 3)
            self.indices.append(self.obj_ptr + 2)
            self.indices.append(self.obj_ptr + 2)
            self.indices.append(self.obj_ptr + 6)
            self.indices.append(self.obj_ptr + 7)

            self.indices.append(self.obj_ptr + 4)
            self.indices.append(self.obj_ptr + 0)
            self.indices.append(self.obj_ptr + 3)
            self.indices.append(self.obj_ptr + 3)
            self.indices.append(self.obj_ptr + 7)
            self.indices.append(self.obj_ptr + 4)

            self.indices.append(self.obj_ptr + 6)
            self.indices.append(self.obj_ptr + 5)
            self.indices.append(self.obj_ptr + 4)
            self.indices.append(self.obj_ptr + 4)
            self.indices.append(self.obj_ptr + 7)
            self.indices.append(self.obj_ptr + 6)

            self.indices.append(self.obj_ptr + 0)
            self.indices.append(self.obj_ptr + 1)
            self.indices.append(self.obj_ptr + 2)
            self.indices.append(self.obj_ptr + 2)
            self.indices.append(self.obj_ptr + 3)
            self.indices.append(self.obj_ptr + 0)
        else:
            self.indices.append(self.obj_ptr + 0)
            self.indices.append(self.obj_ptr + 1)
            self.indices.append(self.obj_ptr + 5)
            self.indices.append(self.obj_ptr + 5)
            self.indices.append(self.obj_ptr + 4)
            self.indices.append(self.obj_ptr + 0)

            self.indices.append(self.obj_ptr + 1)
            self.indices.append(self.obj_ptr + 2)
            self.indices.append(self.obj_ptr + 6)
            self.indices.append(self.obj_ptr + 6)
            self.indices.append(self.obj_ptr + 5)
            self.indices.append(self.obj_ptr + 1)

            self.indices.append(self.obj_ptr + 2)
            self.indices.append(self.obj_ptr + 3)
            self.indices.append(self.obj_ptr + 7)
            self.indices.append(self.obj_ptr + 7)
            self.indices.append(self.obj_ptr + 6)
            self.indices.append(self.obj_ptr + 2)

            self.indices.append(self.obj_ptr + 3)
            self.indices.append(self.obj_ptr + 0)
            self.indices.append(self.obj_ptr + 4)
            self.indices.append(self.obj_ptr + 4)
            self.indices.append(self.obj_ptr + 7)
            self.indices.append(self.obj_ptr + 3)

            self.indices.append(self.obj_ptr + 4)
            self.indices.append(self.obj_ptr + 5)
            self.indices.append(self.obj_ptr + 6)
            self.indices.append(self.obj_ptr + 6)
            self.indices.append(self.obj_ptr + 7)
            self.indices.append(self.obj_ptr + 4)

            self.indices.append(self.obj_ptr + 2)
            self.indices.append(self.obj_ptr + 1)
            self.indices.append(self.obj_ptr + 0)
            self.indices.append(self.obj_ptr + 0)
            self.indices.append(self.obj_ptr + 3)
            self.indices.append(self.obj_ptr + 2)

        self.obj_ptr += 8

        if kwargs.get('color', None) is not None:
            for i in range(0, 12):
                self.colors.append(kwargs['color'])
        elif kwargs.get('colors', None) is not None:
            for i in range(0, 6):
                self.colors.append(kwargs['colors'][i])
                self.colors.append(kwargs['colors'][i])
        else:
            color = Vec3()
            for i in range(0, 12):
                self.colors.append(color)


def average(*values):
    s = 0
    for value in values:
        s += value
    return s / len(values)

class Renderer3D:
    def __init__(self, turtl3):
        self.turtl3 = turtl3

    def render(self, vertices, indices, colors, projection, view, mode: int, width, height, wireframe, overlay):
        """Vec3(x, y, z)"""
        mapped = []
        points = []
        vp = projection * view
        w = width / 2
        h = height / 2

        for vertex in vertices:
            point = vp.vec_mul(Vec4(float(vertex.x()), float(vertex.y()), float(vertex.z()), 1.0))
            points.append(Vec3(point.x(), point.y(), point.z()))
            if point.w() == 0:
                mapped.append(Vec2(0.0, 0.0))
            else:
                mapped.append(Vec2((point.x() / point.w()), (point.y() / point.w())))

        if self.turtl3.enable_depth_test:
            idx = 0
            distances = []
            max_distance = 0
            while idx < len(indices):
                v1 = vertices[indices[idx]]
                v2 = vertices[indices[idx + 1]]
                v3 = vertices[indices[idx + 2]]
                color = colors[idx // 3]
                dist = average(v1.distance(self.turtl3.pos), v2.distance(self.turtl3.pos), v3.distance(self.turtl3.pos))
                max_distance = max(dist, 0.0)
                distances.append((dist, (indices[idx], indices[idx + 1], indices[idx + 2], color)))
                idx += 3

            distances.sort(key=lambda d: d[0])
            sorted_indices = [d[1] for d in distances]
            appended_indices = []
            appended_colors = []
            for s1, s2, s3, c in sorted_indices: #[(s1, s2, s3, c),...]
                appended_indices.append(s1)
                appended_indices.append(s2)
                appended_indices.append(s3)
                appended_colors.append(c)
            indices = appended_indices
            colors = appended_colors


        i = 0
        while i < len(indices):
            # check null indices
            if indices[i] == -1:
                i += mode
                continue

            current = [mapped[j] for j in indices[i:i + mode]]

            #check for indices outside the camera
            for vertex in current:
                if abs(vertex.x()) < 1.0 or abs(vertex.y()) < 1.0:
                    break
            else:
                pass
                i += mode
                continue

            # check for back-facing polygons
            s = 0
            for j in range(mode):
                k = j + 1
                if j == mode - 1:
                    k = 0
                a = current[j]
                b = current[k]
                s += a.x() * b.y()
                s -= a.y() * b.x()
            if self.turtl3.back_face_inv:
                if s < 0:
                    i += mode
                    continue
            else:
                if s >= 0:
                    i += mode
                    continue

            color = colors[i // mode]

            # calculate light
            if self.turtl3.enable_lighting:
                norm = self.surface_normal(vertices[indices[i]], vertices[indices[i + 1]], vertices[indices[i + 2]]).normalize()
                dotp = norm.dot(self.turtl3.light_dir)
                diff = min(max(dotp, 0.3), 1.0)
                color = color * diff

            # if isinstance(color, str):
            #     turtle.pencolor(color)
            #     turtle.fillcolor(color)
            # else:
            turtle.pencolor(color.x(), color.y(), color.z())
            turtle.fillcolor(color.x(), color.y(), color.z())
            if overlay:
                turtle.pencolor("black")
            turtle.penup()
            turtle.goto(current[mode - 1].x() * w, current[mode - 1].y() * h)
            turtle.pendown()
            if not wireframe:
                turtle.begin_fill()
            for vertex in current:
                turtle.goto(vertex.x() * w, vertex.y() * h)
            if not wireframe:
                turtle.end_fill()
            turtle.penup()
            i += mode

    def surface_normal(self, p1, p2, p3):
        u = p2 - p1
        v = p3 - p1
        return Vec3(
            u.y() * v.z() - u.z() * v.y(),
            u.z() * v.x() - u.x() * v.z(),
            u.x() * v.y() - u.y() * v.x()
        )


def fma(a, b, c):
    return a * b + c


class Mat4:
    def __init__(self):
        self.mat4 = [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]

    def __getitem__(self, item):
        return self.mat4[item]

    def __mul__(self, other):
        product = Mat4()
        for i in range(4):
            for j in range(4):
                product[i][j] = self[i][0] * other[0][j] + self[i][1] * other[1][j] + \
                                self[i][2] * other[2][j] + self[i][3] * other[3][j]
        return product

    def mul(self, other):
        return self.__mul__(other)

    def vec_mul(self, other):
        product = Vec4()
        for i in range(4):
            product.vec4[i] = self[i][0] * other[0] + self[i][1] * other[1] + self[i][2] * \
                              other[2] + self[i][3] * other[3]
        return product

    def ident(self):
        self.mat4 = [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]

    def zero(self):
        self.mat4 = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]

    def ortho(self, left, right, bottom, top, near, far):
        self.ident()
        self[0][0] = 2.0 / (right - left)
        self[1][1] = 2.0 / (top - bottom)
        self[2][2] = 2.0 / (near - far)
        self[0][3] = (right + left) / (left - right)
        self[1][3] = (top + bottom) / (bottom - top)
        self[2][3] = (far + near) / (near - far)

    def perspective(self, fov, aspect, near, far):
        self.zero()
        h = math.tan(fov * 0.5)
        self[0][0] = 1.0 / (h * aspect)
        self[1][1] = 1.0 / h
        far_inf = far > 0 and math.isinf(far)
        near_inf = near > 0 and math.isinf(near)
        if far_inf:
            e = 1E-6
            self[2][2] = e - 1.0
            self[2][3] = (e - 2.0) * near
        elif near_inf:
            e = 1E-6
            self[2][2] = 1.0 - e
            self[2][3] = (2.0 - e) * far
        else:
            self[2][2] = (far + near) / (near - far)
            self[2][3] = (far + far) * near / (near - far)
        self[3][2] = -1.0

    def translate(self, x, y, z):
        m1 = Mat4()
        m1.mat4[0] = self[0]
        m1.mat4[1] = self[1]
        m1.mat4[2] = self[2]
        m1.mat4[3] = self[3]

        m2 = Mat4()
        m2.ident()
        m2[0][3] = x
        m2[1][3] = y
        m2[2][3] = z
        m1 *= m2

        self.mat4[0] = m1[0]
        self.mat4[1] = m1[1]
        self.mat4[2] = m1[2]
        self.mat4[3] = m1[3]
        return

        self[0][3] = fma(self[0][0], x, fma(self[0][1], y, fma(self[0][2], z, self[0][3])))
        self[1][3] = fma(self[1][0], x, fma(self[1][1], y, fma(self[1][2], z, self[1][3])))
        self[2][3] = fma(self[2][0], x, fma(self[2][1], y, fma(self[2][2], z, self[2][3])))
        self[3][3] = fma(self[3][0], x, fma(self[3][1], y, fma(self[3][2], z, self[3][3])))

    def rotate_x(self, angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        lm10 = self[0][1]
        lm11 = self[1][1]
        lm12 = self[2][1]
        lm13 = self[3][1]
        lm20 = self[0][2]
        lm21 = self[1][2]
        lm22 = self[2][2]
        lm23 = self[3][2]
        self[0][2] = fma(lm10, -sin, lm20 * cos)
        self[1][2] = fma(lm11, -sin, lm21 * cos)
        self[2][2] = fma(lm12, -sin, lm22 * cos)
        self[3][2] = fma(lm13, -sin, lm23 * cos)
        self[0][1] = fma(lm10, cos, lm20 * sin)
        self[1][1] = fma(lm11, cos, lm21 * sin)
        self[2][1] = fma(lm12, cos, lm22 * sin)
        self[3][1] = fma(lm13, cos, lm23 * sin)

    def rotate_y(self, angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        nm00 = fma(self[0][0], cos, self[0][2] * -sin)
        nm01 = fma(self[1][0], cos, self[1][2] * -sin)
        nm02 = fma(self[2][0], cos, self[2][2] * -sin)
        nm03 = fma(self[3][0], cos, self[3][2] * -sin)
        self[0][2] = fma(self[0][0], sin, self[0][2] * cos)
        self[1][2] = fma(self[1][0], sin, self[1][2] * cos)
        self[2][2] = fma(self[2][0], sin, self[2][2] * cos)
        self[3][2] = fma(self[3][0], sin, self[3][2] * cos)
        self[0][0] = nm00
        self[1][0] = nm01
        self[2][0] = nm02
        self[3][0] = nm03

    def rotate_z(self, angle):
        sin = math.sin(angle)
        cos = math.cos(angle)
        nm00 = fma(self[0][0], cos, self[0][1] * sin)
        nm01 = fma(self[1][0], cos, self[1][1] * sin)
        nm02 = fma(self[2][0], cos, self[2][1] * sin)
        nm03 = fma(self[3][0], cos, self[3][1] * sin)
        self[0][1] = fma(self[0][0], -sin, self[0][1] * cos)
        self[1][1] = fma(self[1][0], -sin, self[1][1] * cos)
        self[2][1] = fma(self[2][0], -sin, self[2][1] * cos)
        self[3][1] = fma(self[3][0], -sin, self[3][1] * cos)
        self[0][0] = nm00
        self[1][0] = nm01
        self[2][0] = nm02
        self[3][0] = nm03

    def move(self, position, rotation):
        self.ident()
        self.rotate_x(rotation.x())
        self.rotate_y(rotation.y())
        self.rotate_z(rotation.z())
        self.translate(position.x(), position.y(), position.z())


class Vec4:
    def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
        self.vec4 = [x, y, z, w]

    def __getitem__(self, item):
        return self.vec4[item]

    def x(self):
        return self.vec4[0]

    def y(self):
        return self.vec4[1]

    def z(self):
        return self.vec4[2]

    def w(self):
        return self.vec4[3]


class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.vec3 = [x, y, z]

    def __getitem__(self, item):
        return self.vec4[item]

    def x(self):
        return self.vec3[0]

    def y(self):
        return self.vec3[1]

    def z(self):
        return self.vec3[2]

    def set_x(self, val):
        self.vec3[0] = val

    def set_y(self, val):
        self.vec3[1] = val

    def set_z(self, val):
        self.vec3[2] = val

    def __add__(self, other):
        return Vec3(self.x() + other.x(), self.y() + other.y(), self.z() + other.z())

    def __sub__(self, other):
        return Vec3(self.x() - other.x(), self.y() - other.y(), self.z() - other.z())

    def __mul__(self, other):
        return Vec3(self.x() * other, self.y() * other, self.z() * other)

    def dot(self, other):
        return self.x() * other.x() + self.y() * other.y() + self.z() * other.z()

    def cross(self, other):
        return Vec3(self.y() * other.z() - self.z() * other.y(), self.z() * other.x() - self.x() * other.z(), self.x() * other.y() - self.y() * other.x())

    def normalize(self):
        length = math.sqrt(self.x() * self.x() + self.y() * self.y() + self.z() * self.z())
        self.set_x(self.x() / length)
        self.set_y(self.y() / length)
        self.set_z(self.z() / length)
        return self

    def distance(self, other):
        return math.sqrt(sq(other.x() - self.x()) + sq(other.y() - self.y()) + sq(other.z() - self.z()))

def sq(n):
    return n * n

class Vec2:
    def __init__(self, x=0.0, y=0.0):
        self.vec2 = [x, y]

    def __getitem__(self, item):
        return self.vec4[item]

    def x(self):
        return self.vec2[0]

    def y(self):
        return self.vec2[1]


class Model:
    def __init__(self):
        self.vertices = []
        self.indices = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_index(self, index):
        self.indices.append(index)

    def move(self, pos):
        self.vertices = [v + pos for v in self.vertices]

    def scale(self, factor):
        self.vertices = [v * factor for v in self.vertices]


def process_face(token, faces):
    line_token = token.split('/')
    pos = int(line_token[0]) - 1
    faces.append(pos)


def load_model(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        model = Model()
        faces = []
        for line in lines:
            tokens = line.strip().split(' ')
            match tokens[0]:
                case 'v':
                    model.add_vertex(Vec3(float(tokens[1]), float(tokens[2]) * -1, float(tokens[3])))
                case 'f':
                    process_face(tokens[1], faces)
                    process_face(tokens[2], faces)
                    process_face(tokens[3], faces)
                case _:
                    pass

        for face in faces:
            model.add_index(face)

        return model
