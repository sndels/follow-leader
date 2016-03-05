'''
Class for simulation Parameters

Holds all simulation parameters and handles changes to mutable ones
'''
class PLeader():
    def __init__(self):
        self.mass = 10
        self.maxV = 0.002
        self.maxF = 0.001

class PFollower():
    def __init__(self):
        self.mass = 10
        self.maxV = 0.0025
        self.maxF = 0.0015
        self.followDist = 0.01
        self.slowingD = 0.1
