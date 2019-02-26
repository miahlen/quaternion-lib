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

    def test_mul(self):
        """Test operator overloading method __mul__"""
        # Create instance of class EulerAngle to be multiplied by value
        e_in = EulerAngle(0.9, -1, -0.4)

        # Create value for EulerAngle instance to be multiplied by
        val = 2.0

        # Function call (to function to test)
        e = e_in*val

        # Create oracle
        e_oracle = EulerAngle(0.9 * val, -1 * val, -0.4 * val)

        # Assert expected behaviour
        self.assertTrue(e == e_oracle)
        self.assertFalse(e_in == e_oracle)


if __name__ == '__main__':
    unittest.main()
