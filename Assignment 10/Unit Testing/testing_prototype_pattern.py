import unittest
import Circle             # from prototype

class TestPrototypePattern(unittest.TestCase):
    def test_shape_prototype(self):
        circle1 = Circle(5)
        circle2 = circle1.clone()
        
        self.assertEqual(circle1.radius, circle2.radius)
        self.assertIsNot(circle1, circle2)  