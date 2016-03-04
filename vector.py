from math import sqrt, sin, cos, atan2, pi
'''
2d-vector

Stores values x and y
'''
class Vector2f():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2f(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2f(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2f(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Vector2f(self.x / other.x, self.y / other.y)

    def __truediv__(self, other):
        return Vector2f(self.x / other.x, self.y / other.y)

    def len(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def angle(self):
        if self.x == 0.0 and self.y == 0:
            return 0.0
        angle = atan2(self.y, self.x)
        if angle < 0:
            angle += 2 * pi
        return angle

    def dist(self, vec):
        return sqrt(pow(self.x - vec.x, 2) + pow(self.y - vec.y, 2))

    def getNormalized(self):
        l = sqrt(pow(self.x, 2) + pow(self.y, 2))
        return Vector2f(self.x / l, self.y / l)

    def getTrunc(self, max_l):
        l = sqrt(pow(self.x, 2) + pow(self.y, 2))
        if l > max_l:
            return Vector2f(self.x * max_l / l, self.y * max_l / l)
        return Vector2f(self.x, self.y)

def distance(vec1, vec2):
    return sqrt(pow(vec1.x - vec2.x, 2) + pow(vec1.y - vec2.y, 2))

def normalize(vec):
    l = sqrt(pow(vec.x, 2) + pow(vec.y, 2))
    return Vector2f(vec.x / l, vec.y / l)

def trunc(vec, max_l):
    l = sqrt(pow(vec.x, 2) + pow(vec.y, 2))
    if l > max_l:
        return Vector2f(vec.x * max_l / l, vec.y * max_l / l)
    return vec
