import unittest
from euler_angle import EulerAngle

class TestEulerAngle(unittest.TestCase):

    def test_eq(self):
        """Test operator overloading method __eq__"""
        # Create instances of class EulerAngle to compare
        e1 = EulerAngle(0.9, -1, -0.4)
        e2 = EulerAngle(0.9, -1, -0.4)
        e3 = EulerAngle(0.9, -1.1, -0.4)

        # Assert expected behaviour
        self.assertTrue(e1 == e2)
        self.assertFalse(e1 == e3)


if __name__ == '__main__':
    unittest.main()
