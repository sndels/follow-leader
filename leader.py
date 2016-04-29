import random
from parameters import PLeader
from math import pi, floor
from vector import Vector2f, trunc, normalize
from graphics import drawArrow, drawDiamond

class Leader():
    def __init__(self, params, gParams):
        self.params = params
        self.gParams = gParams
        self.pos = Vector2f(random.random() * 1024, random.random() * 768)
        self.v = Vector2f(0.0000001, 0.0)
        self.orientation = 0.0
        self.cDist = 0.8
        self.cRad = 0.8
        self.wAngle = 0.0
        self.wChange = 0.5
        self.target = Vector2f(0.0, 0.0)
        self.controlled = False
        self.seeking = False

        random.seed(100)

    def getPos(self):
        return self.pos

    def getV(self):
        return self.v

    def isControlled(self):
        return self.controlled

    def toggleControl(self):
        self.controlled = not self.controlled

    def goTo(self, target):
        self.target = target
        self.seeking = True

    def turn(self, direction):
        if direction == 'L':
            self.v.rotate(0.05)
        elif direction == 'R':
            self.v.rotate(-0.05)

    def wander(self):
        wForce = normalize(self.v) * self.cDist
        rForce = normalize(self.v) * self.cRad
        rForce.rotate(self.wAngle)
        wForce += rForce
        if self.pos.x > 1100:
            wForce += Vector2f(-1.0, 0.0) * self.pos.x /100 * self.params.maxF
        elif self.pos.x < 100:
            wForce += Vector2f(1.0, 0.0) * (1280 - self.pos.x) /100 * self.params.maxF
        if self.pos.y > 650:
            wForce += Vector2f(0.0, -1.0) * self.pos.y /100 * self.params.maxF
        elif self.pos.y < 70:
            wForce += Vector2f(0.0, 1.0) * (720 - self.pos.y) /100 * self.params.maxF
        wForce.trunc(self.params.maxF)
        self.wAngle += (random.random() * 2 - 1) * self.wChange
        steering = wForce / self.params.mass * self.gParams.speed
        self.v = trunc(self.v + steering, self.params.maxV)

    def seek(self):
        pass

    def move(self):
        if self.controlled:
            pass
        elif self.seeking:
            self.seek()
        else:
            self.wander()
        self.pos += self.v * self.gParams.speed
        self.orientation = self.v.angle() * 180 / pi

    def render(self):
        drawArrow(self.pos, 0.02, self.orientation, "RED")
        if self.seeking:
            drawDiamond(self.target, 0.015)
