import unittest
from math import pi, sqrt, atan2
from vector import Vector2f

class Test(unittest.TestCase):
    def test_add(self):
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(0.7543, 0.4432)
        vecResult = vec1 + vec2
        self.assertEqual(vecResult.x, 1.2543 + 0.7543, "Adding positive x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432 + 0.4432, "Adding positive y coordinate failed")
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(-0.7543, -0.4432)
        vecResult = vec1 + vec2
        self.assertEqual(vecResult.x, 1.2543 - 0.7543, "Adding negative x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432 - 0.4432, "Adding negative y coordinate failed")
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(0.0, 0.0)
        vecResult = vec1 + vec2
        self.assertEqual(vecResult.x, 1.2543, "Adding zero x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432, "Adding zero y coordinate failed")

    def test_sub(self):
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(0.7543, 0.4432)
        vecResult = vec1 - vec2
        self.assertEqual(vecResult.x, 1.2543 - 0.7543, "Subtracting positive x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432 - 0.4432, "Subtracting positive y coordinate failed")
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(-0.7543, -0.4432)
        vecResult = vec1 - vec2
        self.assertEqual(vecResult.x, 1.2543 + 0.7543, "Subtracting negative x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432 + 0.4432, "Subtracting negative y coordinate failed")
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(0.0, 0.0)
        vecResult = vec1 - vec2
        self.assertEqual(vecResult.x, 1.2543, "Subtracting zero x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432, "Subtracting zero y coordinate failed")

    def test_mul(self):
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(0.7543, 0.4432)
        vecResult = vec1 * vec2
        self.assertEqual(vecResult.x, 1.2543 * 0.7543, "Multiplying with positive x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432 * 0.4432, "Multiplying with positive y coordinate failed")
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(-0.7543, -0.4432)
        vecResult = vec1 * vec2
        self.assertEqual(vecResult.x, 1.2543 * (-0.7543), "Multiplying with negative x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432 * (-0.4432), "Multiplying with negative y coordinate failed")
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(0.0, 0.0)
        vecResult = vec1 * vec2
        self.assertEqual(vecResult.x, 0.0, "Multiplying with zero x coordinate failed")
        self.assertEqual(vecResult.y, 0.0, "Multiplying with zero y coordinate failed")

    def test_div(self):
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(0.7543, 0.4432)
        vecResult = vec1 / vec2
        self.assertEqual(vecResult.x, 1.2543 / 0.7543, "Division with positive x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432 / 0.4432, "Division with positive y coordinate failed")
        vec1 = Vector2f(1.2543, 1.2432)
        vec2 = Vector2f(-0.7543, -0.4432)
        vecResult = vec1 / vec2
        self.assertEqual(vecResult.x, 1.2543 / (-0.7543), "Division with negative x coordinate failed")
        self.assertEqual(vecResult.y, 1.2432 / (-0.4432), "Division with negative y coordinate failed")

    def test_len(self):
        vec1 = Vector2f(1.0, 0.0)
        length = vec1.len()
        self.assertEqual(length, 1.0, "Unit vector failed")
        vec1 = Vector2f(1.0, 1.0)
        length = vec1.len()
        self.assertEqual(length, sqrt(2), "[1.0,1.0] vector failed")
        vec1 = Vector2f(0.0, 0.0)
        length = vec1.len()
        self.assertEqual(length, 0.0, "[0.0,0.0] vector failed")
        vec1 = Vector2f(-1.0, 0.0)
        length = vec1.len()
        self.assertEqual(length, 1.0, "[-1.0,0.0] vector failed")
        vec1 = Vector2f(21.234234, 15.345323)
        length = vec1.len()
        self.assertEqual(round(length,5), 26.19870, "[21.234234,15.345323] vector failed")

    def test_angle(self):
        vec1 = Vector2f(1.0, 0.0)
        self.assertEqual(vec1.angle(), 0.0, "0 degrees failed")
        vec1 = Vector2f(0.0, 1.0)
        self.assertEqual(vec1.angle(), pi/2, "90 degrees failed")
        vec1 = Vector2f(-1.0, 0.0)
        self.assertEqual(vec1.angle(), pi, "180 degrees failed")
        vec1 = Vector2f(0.0, -1.0)
        self.assertEqual(vec1.angle(), 3*pi / 2, "270 degrees failed")
        vec1 = Vector2f(0.234522, 0.123477)
        self.assertEqual(round(vec1.angle(), 5), round(atan2(vec1.y, vec1.x), 5), "22.76703 degrees failed")
        vec1 = Vector2f(-0.234522, -0.123477)
        self.assertEqual(round(vec1.angle(), 5), round(atan2(vec1.y, vec1.x) + 2 * pi, 5), "202.76703 degrees failed")

    def test_dist(self):
        vec1 = Vector2f(1.0, 0.0)
        vec2 = Vector2f(0.0, 1.0)
        self.assertEqual(vec1.dist(vec2), sqrt(2), "Dist1 failed")
        vec1 = Vector2f(0.0, 0.0)
        vec2 = Vector2f(0.0, 0.0)
        self.assertEqual(vec1.dist(vec2), 0.0, "Dist2 failed")
        vec1 = Vector2f(0.2314320, 0.3242123)
        vec2 = Vector2f(-0.2342343, 0.0324121)
        self.assertEqual(round(vec1.dist(vec2), 5), 0.54954, "Dist3 failed")

if __name__ == '__main__':
    unittest.main()
