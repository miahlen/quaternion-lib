import unittest
from quaternion import Quaternion

class TestQuaternion(unittest.TestCase):

    def test_eq(self):
        """Test operator overloading method __eq__"""
        # Create instances of class Quaternion to compare
        q1 = Quaternion(0.9, -1, -0.4, 0.1)
        q2 = Quaternion(0.9, -1, -0.4, 0.1)
        q3 = Quaternion(0.9, -1.1, -0.4, 0.1)

        # Assert expected behaviour
        self.assertTrue(q1 == q2)
        self.assertFalse(q1 == q3)

    def test_mul(self):
        """Test operator overloading method __mul__"""
        # Create instances of class Quaternion to be multiplied
        q1 = Quaternion(1, 2, 1, -3)
        q2 = Quaternion(2, -1, -3, 1)

        # Function call (to function to test)
        q = q1 * q2

        # Create oracle
        q_oracle = Quaternion(10, -5, 0, -10)

        # Assert expected behaviour
        self.assertTrue(q == q_oracle)

    def test_str(self):
        """Test operator overloading method __str__"""
        # Create instance of class Quaternion to get string of
        q = Quaternion(0.9, -1, -0.4, 0.1)

        # Function call (to function to test)
        s = str(q)

        # Create oracle
        s_oracle = "(0.9, -1, -0.4, 0.1)"

        # Assert expected behaviour
        self.assertEqual(s, s_oracle)


if __name__ == '__main__':
    unittest.main()
