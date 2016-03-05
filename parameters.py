'''
Class for simulation Parameters

Holds all simulation parameters and handles changes to mutable ones
'''
class PLeader():
    def __init__(self):
        self.mass = 20
        self.maxV = 0.8
        self.maxF = 0.4

class PFollower():
    def __init__(self):
        self.num = 100
        self.mass = 20
        self.maxV = 0.8
        self.maxF = 0.4
        self.followDist = 10
        self.slowingD = 20
        self.separationD = 30
