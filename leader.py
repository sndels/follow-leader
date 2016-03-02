from vector import Vector2f
from graphics import drawArrow

class Leader():
    def __init__(self, pos2f, params):
        self.pos = pos2f
        self.v = Vector2f(0.0000001, 0.0)
        self.orientation = 0
        self.params = params

    def render(self):
        drawArrow(self.pos, 0.05, self.orientation)
