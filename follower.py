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
        self.loc = Vector2f(floor(self.pos.x / 32), floor(self.pos.y / 32))
        self.v = Vector2f(0.0001, 0.0)
        self.orientation = 0.0
        self.leader = leader

    def getPos(self):
        return self.pos

    def calcRepulsion(self, followers):
        repulsionF = Vector2f(0.0, 0.0)
        for i in self.grid.getNeighbours(self.loc.x, self.loc.y):
                d = distance(self.pos, i.pos)
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
        repulsionF = self.calcRepulsion(followers)
        steer = trunc(steer + repulsionF, self.params.maxF)
        acc = steer / self.params.mass * self.gParams.speed
        self.v = trunc(self.v + acc, self.params.maxV)
        dist = distance(self.pos, target)
        if dist < self.params.slowingD:
            self.v *= dist / self.params.slowingD
        self.pos += self.v * self.gParams.speed
        self.loc = Vector2f(floor(self.pos.x / 32), floor(self.pos.y / 32))
        self.orientation = self.v.angle() * 180 / pi

    def render(self):
        drawArrow(self.pos, 0.012, self.orientation, "WHITE")
