'''
Class for simulation Parameters

Holds all simulation parameters and handles changes to mutable ones
'''
class Parameters():
    def __init__(self):
        self.timeScale = 1.0

        self.leaderMass = 10
        self.leaderMaxV = 0.002
        self.leaderMaxF = 0.001
