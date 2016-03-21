import random
from parameters import PFollower, PGlobal
from graphics import drawArrow
from leader import Leader
from math import pi, floor
from vector import Vector2f, normalize, trunc, distance

class Follower():
    def __init__(self, leader, params, gParams, grid):
        self.params = params
        self.gParams = gParams
        self.grid = grid
        self.pos = Vector2f(random.random() * 1024, random.random() * 768)
        self.loc = Vector2f(0, 0)
        self.calcLoc()
        self.grid.insert(self, self.loc.x, self.loc.y)
        self.v = Vector2f(0.0001, 0.0)
        self.orientation = 0.0
        self.leader = leader

    def getPos(self):
        return self.pos

    def calcLoc(self):
        newLoc = Vector2f(int(floor(self.pos.x / 32)), int(floor(self.pos.y / 32)))
        if newLoc.x != self.loc.x or newLoc.y != self.loc.y:
            self.grid.remove(self, self.loc.x, self.loc.y)
            self.loc = newLoc
            self.grid.insert(self, self.loc.x, self.loc.y)

    def calcRepulsion(self):
        repulsionF = Vector2f(0.0, 0.0)
        for i in self.grid.getNeighbours(self.loc.x, self.loc.y):
            d = distance(i.getPos(), self.pos)
            if d < self.params.separationD and d != 0:
                repulsionF += (self.pos - i.getPos()) * self.params.separationD / d
        fLeader = self.leader.getPos() + normalize(self.leader.getV()) * self.params.followDist
        d = distance(self.pos, fLeader)
        if d < self.params.followDist:
            repulsionF += (self.pos - fLeader) * self.params.followDist / d
        d = distance(self.pos, self.leader.getPos())
        if d < self.params.followDist:
            repulsionF += (self.pos - self.leader.getPos()) * 2 * self.params.followDist / d
        return repulsionF

    def move(self, followers):
        target = self.leader.getPos() - normalize(self.leader.getV()) * self.params.followDist
        steer = trunc(target - self.pos, self.params.maxF)
        repulsionF = self.calcRepulsion()
        steer = trunc(steer + repulsionF, self.params.maxF)
        acc = steer / self.params.mass * self.gParams.speed
        self.v = trunc(self.v + acc, self.params.maxV)
        dist = distance(self.pos, target)
        if dist < self.params.slowingD:
            self.v *= dist / self.params.slowingD
        self.pos += self.v * self.gParams.speed
        newLoc = self.calcLoc()
        self.orientation = self.v.angle() * 180 / pi

    def render(self):
        drawArrow(self.pos, 0.012, -self.orientation, "WHITE")
