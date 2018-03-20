import unittest
from speed_calculation import SpeedCalculation



class TestSpeedCalculation(unittest.TestCase):
    def test_speed_calculation_point_number(self):
        v1 = 8.63
        v2 = 3.82
        speed = SpeedCalculation(v1, v2).speed_calculation()
        self.assertAlmostEquals(speed, 8.132984293)

    def test_speed_calculation_minus_number(self):
        v1 = -2
        v2 = 2
        speed = SpeedCalculation(v1, v2).speed_calculation()
        self.assertAlmostEquals(speed, -3.6)

if __name__ == '__main__':
    unittest.main()