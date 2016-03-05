import random
import parameters
from graphics import drawArrow
from leader import Leader
from math import pi, floor
from vector import Vector2f, normalize, trunc, distance

class Follower():
    def __init__(self, leader, params, grid):
        self.params = params
        self.grid = grid
        self.pos = Vector2f(random.random() * 1280, random.random() * 720)
        self.loc = self.calcLoc()
        self.grid.insert(self, self.loc.x, self.loc.y)
        self.v = Vector2f(0.0001, 0.0)
        self.orientation = 0.0
        self.leader = leader

    def calcLoc(self):
        return Vector2f(floor(self.pos.x / 40), floor(self.pos.y / 40))

    def getPos(self):
        return self.pos

    def move(self, followers):
        target = self.leader.getPos() - normalize(self.leader.getV()) * self.params.followDist
        steer = trunc(target - self.pos, self.params.maxF)
        separationF = Vector2f(0.0, 0.0)
        for i in self.grid.getNeighbours(self.loc.x, self.loc.y):
            d = distance(i.getPos(), self.pos)
            if d < self.params.separationD and d != 0:
                separationF += (self.pos - i.getPos()) * self.params.separationD / d
        steer = trunc(steer + separationF, self.params.maxF)
        acc = steer / self.params.mass
        self.v = trunc(self.v + acc, self.params.maxV)
        dist = distance(self.pos, target)
        if dist < self.params.slowingD:
            self.v *= dist / self.params.slowingD
        self.pos += self.v
        newLoc = self.calcLoc()
        if newLoc.x != self.loc.x or newLoc.y != self.loc.y:
            self.grid.pop(self, self.loc.x, self.loc.y)
            self.loc = newLoc
            self.grid.insert(self, self.loc.x, self.loc.y)
        self.orientation = self.v.angle() * 180 / pi

    def render(self):
        drawArrow(self.pos, 0.012, -self.orientation, "WHITE")
