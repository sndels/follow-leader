import random
from parameters import PLeader
from math import pi
from vector import Vector2f, trunc, normalize
from graphics import drawArrow

class Leader():
    def __init__(self, params):
        self.params = params
        self.pos = Vector2f(0.0, 0.0)
        self.v = Vector2f(0.0000001, 0.0)
        self.orientation = 0.0
        self.cDist = 0.002
        self.cRad = 0.0005
        self.wAngle = 0.0
        self.wChange = 0.5

        random.seed(100)

    def getPos(self):
        return self.pos

    def getV(self):
        return self.v

    def move(self):
        wForce = normalize(self.v) * self.cDist
        rForce = normalize(self.v) * self.cRad
        rForce.rotate(self.wAngle)
        wForce += rForce
        if self.pos.x > 1.2:
            wForce += Vector2f(-1.0, 0.0) * self.pos.x * 0.002
        elif self.pos.x < -1.2:
            wForce += Vector2f(1.0, 0.0) * (1 - self.pos.x) * 0.002
        if self.pos.y > 0.7:
            wForce += Vector2f(0.0, -1.0) * self.pos.y * 0.002
        elif self.pos.y < -0.7:
            wForce += Vector2f(0.0, 1.0) * (1 - self.pos.y) * 0.002
        wForce.trunc(self.params.maxF)
        self.wAngle += (random.random() * 2 - 1) * self.wChange
        steering = wForce / self.params.mass
        self.v = trunc(self.v + steering, self.params.maxV)
        self.pos += self.v
        self.orientation = self.v.angle() * 180 / pi

    def render(self):
        drawArrow(self.pos, 0.02, -self.orientation, "RED")
