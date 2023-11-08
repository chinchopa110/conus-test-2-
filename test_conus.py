import unittest
from conus import Conus

class TestConus(unittest.TestCase):

    def test_area(self):
        radius = 3
        height = 4
        conus = Conus(radius, height)
        result = conus.area()
        self.assertAlmostEqual(result, 75.39815999999999)
    def test_sum(self):
        radius = 3
        height = 4
        conus = Conus(radius, height)
        result = conus.sum()
        self.assertAlmostEqual(result, 7)



if __name__ == '__main__':
    unittest.main()