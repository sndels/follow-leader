import random
import parameters
from graphics import drawArrow
from leader import Leader
from math import pi
from vector import Vector2f, normalize, trunc, distance

class Follower():
    def __init__(self, leader, params):
        self.params = params
        self.pos = Vector2f(random.random(), random.random())
        self.v = Vector2f(0.0001, 0.0)
        self.speed = Vector2f(0.000001, 0.0)
        self.orientation = 0.0
        self.leader = leader

    def move(self):
        target = self.leader.getPos() - normalize(self.leader.getV()) * self.params.followDist
        steer = trunc(target - self.pos, self.params.maxF)
        acc = steer / self.params.mass
        self.v = trunc(self.v + acc, self.params.maxV)
        dist = distance(self.pos, target)
        if dist < self.params.slowingD:
            self.v *= dist / self.params.slowingD
        self.pos += self.v
        self.orientation = self.v.angle() * 180 / pi

    def render(self):
        drawArrow(self.pos, 0.02, -self.orientation, "WHITE")
