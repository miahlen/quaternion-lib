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

    def test_sub(self):
        """Test operator overloading method __sub__"""
        # Create instances of class Position to subtract
        p1 = Position(0.9, -1, -0.4)
        p2 = Position(0.3, 1.3, 0.2)

        # Function call (to function to test)
        p = p1 - p2

        # Create oracle
        p_oracle = Position(0.6, -2.3, -0.6)

        # Assert expected behaviour
        self.assertAlmostEqual(p.x, p_oracle.x)
        self.assertAlmostEqual(p.y, p_oracle.y)
        self.assertAlmostEqual(p.z, p_oracle.z)

    def test_str(self):
        """Test operator overloading method __str__"""
        # Create instance of class Position to get string of
        p1 = Position(0.9, -1, -0.4)

        # Function call (to function to test)
        s = str(p1)

        # Create oracle
        s_oracle = "(0.9, -1, -0.4)"

        # Assert expected behaviour
        self.assertEqual(s, s_oracle)


if __name__ == '__main__':
    unittest.main()
