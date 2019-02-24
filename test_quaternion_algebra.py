import unittest
import quaternion_algebra
from quaternion import Quaternion
from position import Position
import numpy as np

class TestQuaternionAlgebra(unittest.TestCase):

    def test_normalize_quaternion(self):
        q = Quaternion(-2.1,0.0,0.0,0.0)
        q = quaternion_algebra.normalize_quaternion(q)
        self.assertTrue(np.sqrt(q.w**2 + q.x**2 + q.y**2 + q.z**2) == 1)
        self.assertTrue(q == Quaternion(-1.0, 0.0, 0.0, 0.0))

    # Perform rotation of vector (of class Position) with quaternion.
    def test_rotate_vector_by_quaternion(self):
        # Vector to rotate
        v = Position(1.2, 2.8, -1.0)

        # Quaternion which represent rotation
        theta = -79 * np.pi/180.0
        qv = [np.sin(theta/2.0)*vi for vi in [-0.4,1.3,4.1]]
        q = Quaternion(np.cos(theta/2.0), qv[0], qv[1], qv[2])
        q = quaternion_algebra.normalize_quaternion(q)

        # Rotate vector with function to test
        v = quaternion_algebra.rotate_vector_by_quaternion(v,q)

        # Assert excepted behaviour
        self.assertAlmostEqual(v.x, 0.552995401929)
        self.assertAlmostEqual(v.y, -3.05678095585)
        self.assertAlmostEqual(v.z, 0.79390570814)

    # Perform rotation with quaternion which represents no rotation
    # Expected behaviour is that no change has been made to vector
    def test_rotate_vector_by_no_rot_quaternion(self):
        # Vector to rotate
        v = Position(1.2, 2.8, -1.0)

        # Quaternion which represent no rotation
        q = Quaternion(1, 0, 0, 0)
        q = quaternion_algebra.normalize_quaternion(q)

        # Rotate vector with function to test
        v = quaternion_algebra.rotate_vector_by_quaternion(v,q)

        # Assert excepted behaviour
        self.assertTrue(v == Position(1.2, 2.8, -1.0))


if __name__ == '__main__':
    unittest.main()
