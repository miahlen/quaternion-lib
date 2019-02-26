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


if __name__ == '__main__':
    unittest.main()
