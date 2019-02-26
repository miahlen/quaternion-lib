import unittest
from position import Position

class TestPosition(unittest.TestCase):

    def test_eq(self):
        """Test operator overloading method __eq__"""
        # Create instances of class Position to compare
        p1 = Position(0.9, -1, -0.4)
        p2 = Position(0.9, -1, -0.4)
        p3 = Position(0.9, -1.1, -0.4)

        # Assert expected behaviour
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_add(self):
        """Test operator overloading method __add__"""
        # Create instances of class Position to add
        p1 = Position(0.9, -1, -0.4)
        p2 = Position(0.3, 1.3, 0.2)

        # Function call (to function to test)
        p = p1 + p2

        # Create oracle
        p_oracle = Position(1.2, 0.3, -0.2)

        # Assert expected behaviour
        self.assertAlmostEqual(p.x, p_oracle.x)
        self.assertAlmostEqual(p.y, p_oracle.y)
        self.assertAlmostEqual(p.z, p_oracle.z)


if __name__ == '__main__':
    unittest.main()
