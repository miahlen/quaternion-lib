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


if __name__ == '__main__':
    unittest.main()
