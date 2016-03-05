'''
Class for simulation Parameters

Holds all simulation parameters and handles changes to mutable ones
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
        self.maxF = 0.4
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
