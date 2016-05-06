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
        self.loc = Vector2f(floor(self.pos.x / 32)+1, floor(self.pos.y / 32)+1)
        self.grid.insert(self, self.loc.x, self.loc.y)
        self.repulsionF = Vector2f(0.0, 0.0)
        self.v = Vector2f(0.0001, 0.0)
        self.orientation = 0.0
        self.leader = leader

    def getPos(self):
        return self.pos

    def calcRepulsion(self, followers):
        self.repulsionF = Vector2f(0.0, 0.0)
        collisionChecks = 0
        # Calculate evasion from neighbours that are too close
        for i in self.grid.getNeighbours(self.loc.x, self.loc.y):
                d = distance(self.pos, i.pos)
                collisionChecks += 1
                if d < self.params.separationD and d != 0.0:
                    self.repulsionF += (self.pos - i.getPos()) * self.params.separationD / d
        # Evade leader if necessary
        fLeader = self.leader.getPos() + normalize(self.leader.getV()) * self.params.followDist
        d = distance(self.pos, fLeader)
        if d < self.params.followDist and d != 0.0:
            self.repulsionF += (self.pos - fLeader) * self.params.followDist / d
        d = distance(self.pos, self.leader.getPos())
        if d < self.params.followDist and d != 0.0:
            self.repulsionF += (self.pos - self.leader.getPos()) * 2 * self.params.followDist / d
        return collisionChecks

    def move(self):
        # Get target from behind the leader
        target = self.leader.getPos() - normalize(self.leader.getV()) * self.params.followDist
        # Calculate desired direction
        steer = trunc(target - self.pos, self.params.maxF)
        # Truncate final steering vector and convert to acceleration
        steer = trunc(steer + self.repulsionF, self.params.maxF)
        acc = steer / self.params.mass * self.gParams.speed
        # Truncate final speed, slow down if necessary
        self.v = trunc(self.v + acc, self.params.maxV)
        dist = distance(self.pos, target)
        if dist < self.params.slowingD:
            self.v *= dist / self.params.slowingD
        # Calculate new position
        self.pos += self.v * self.gParams.speed
        # Update grid if necessary
        newLoc = Vector2f(floor(self.pos.x / 32)+1, floor(self.pos.y / 32)+1)
        if newLoc.x != self.loc.x or newLoc.y != self.loc.y:
            self.grid.remove(self, self.loc.x, self.loc.y)
            self.loc = newLoc
            self.grid.insert(self, self.loc.x, self.loc.y)
        # Set current angle for drawing
        self.orientation = self.v.angle() * 180 / pi

    def render(self):
        drawArrow(self.pos, 0.012, self.orientation, "WHITE")
