from math import sqrt, sin, cos, atan2, pi
'''
2d-vector

Stores values x and y
All functions use radians for angle
'''
class Vector2f():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2f(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2f(self.x - other.x, self.y - other.y)

    def __mul__(self, num):
        return Vector2f(self.x * num, self.y * num)

    def __div__(self, num):
        return Vector2f(self.x / num, self.y / num)

    def __truediv__(self, num):
        return Vector2f(self.x / num, self.y / num)

    def len(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def angle(self):
        if self.x == 0.0 and self.y == 0:
            return 0.0
        angle = atan2(self.y, self.x)
        if angle < 0:
            angle += 2 * pi
        return angle

    def rotate(self, angle):
        s = sin(angle)
        c = cos(angle)
        newX = self.x * c - self.y * s
        newY = self.x * s + self.y * c
        self.x = newX
        self.y = newY

    def trunc(self, max_l):
        l = self.len()
        if l > max_l:
            self.x *= max_l / l
            self.y *= max_l / l

    def normalize(self):
        if self.x != 0.0 or self.y != 0.0:
            l = sqrt(pow(self.x, 2) + pow(self.y, 2))
            self.x /= l
            self.y /= l

def distance(vec1, vec2):
    return sqrt(pow(vec1.x - vec2.x, 2) + pow(vec1.y - vec2.y, 2))

def trunc(vec, max_l):
    l = vec.len()
    if l > max_l:
        return Vector2f(vec.x * max_l / l, vec.y * max_l / l)
    return vec

def normalize(vec):
    if vec.x == 0.0 and vec.y == 0:
        return Vector2f(0.0, 0.0)
    l = sqrt(pow(vec.x, 2) + pow(vec.y, 2))
    return Vector2f(vec.x / l, vec.y / l)
