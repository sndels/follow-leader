'''
Classes for simulation Parameters
'''
class PLeader():
    def __init__(self):
        self.mass = 40
        self.maxV = 0.8
        self.maxF = 0.4

    def setMaxV(self, newMaxV):
        self.maxV = newMaxV / 10.0
        self.maxF = newMaxV / 2.0

class PFollower():
    def __init__(self):
        self.num = 100
        self.mass = 40
        self.maxV = 0.8
        self.maxF = 0.1
        self.followDist = 40
        self.slowingD = 20
        self.separationD = 30

    def setNum(self, newNum):
        self.num = newNum

    def setMaxV(self, newMaxV):
        self.maxV = newMaxV / 10.0
        self.maxF = newMaxV / 2.0

    def setSeparation(self, newSeparationD):
        self.separationD = newSeparationD

    def setFollowDist(self, newFollowDist):
        self.followDist = newFollowDist

class PGlobal():
    def __init__(self):
        self.speed = 1.0

    def setSpeed(self, newSpeed):
        self.speed = newSpeed / 10.0

class PInfo():
    def __init__(self):
        self.frameTime = [0, 0, 0, 0, 0]
        self.lastFrame = 0.0
        self.collisionChecks = [0, 0, 0, 0, 0]
        self.computeTime = [0, 0, 0, 0, 0]
