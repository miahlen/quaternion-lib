import unittest
import quaternion_algebra
from quaternion import Quaternion
from position import Position
from euler_angle import EulerAngle
import numpy as np

class TestQuaternionAlgebra(unittest.TestCase):

    # Perform rotation of vector (of class Position) with quaternion.
    def test_rotate_vector_by_quaternion(self):
        # Vector to rotate
        v = Position(1.2, 2.8, -1.0)

        # Quaternion which represent rotation
        theta = -79 * np.pi/180.0
        qv = [np.sin(theta/2.0)*vi for vi in [-0.4,1.3,4.1]]
        q = Quaternion(np.cos(theta/2.0), qv[0], qv[1], qv[2])
        q.normalize()

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
        q.normalize()

        # Rotate vector with function to test
        v = quaternion_algebra.rotate_vector_by_quaternion(v,q)

        # Assert excepted behaviour
        self.assertTrue(v == Position(1.2, 2.8, -1.0))

    # Rotate a zero vector with a quaterion. Expected behaviour is that no
    # change has been made to vector after function call rotate_vector_by_quaternion
    def test_rotate_zero_vector_by_quaternion(self):
        # Vector to rotate
        v = Position(0.0, 0.0, 0.0)

        # Quaternion which represent rotation
        theta = 79 * np.pi/180.0
        qv = [np.sin(theta/2.0)*vi for vi in [-0.4,0.7,0.4]]
        q = Quaternion(np.cos(theta/2.0), qv[0], qv[1], qv[2])
        q.normalize()

        # Rotate vector with function to test
        v = quaternion_algebra.rotate_vector_by_quaternion(v,q)

        # Assert excepted behaviour
        self.assertTrue(v == Position(0.0, 0.0, 0.0))

    def test_quaternion_to_euler(self):
        # Quaternion to convert
        q = Quaternion(0.670, 0.394, 0.511, -0.368)
        q.normalize()

        # The expected output (OBS, in degrees)
        euler_oracle = EulerAngle(42.118,  76.921, -23.544)

        # Function call
        euler = quaternion_algebra.quaternion_to_euler(q)
        # Convert to degrees for comparison
        euler *= 180/np.pi

        # Assert expected behaviour to the third decimal
        self.assertAlmostEqual(euler.roll, euler_oracle.roll, 3)
        self.assertAlmostEqual(euler.pitch, euler_oracle.pitch, 3)
        self.assertAlmostEqual(euler.yaw, euler_oracle.yaw, 3)

    def test_get_quaternion_from_vector(self):
        # Input variables to function
        v = [0, 0.2, 0]

        # Function call
        q = quaternion_algebra.get_quaternion_from_vector(v)

        # The expected output (rotation 90 degrees around z axis)
        q_oracle = Quaternion(np.cos(90 / 2.0 * np.pi/180), 0.0, 0.0, 1.0 * np.sin(90 / 2.0 * np.pi/180))

        # Assert expected behaviour
        self.assertAlmostEqual(q.w, q_oracle.w)
        self.assertAlmostEqual(q.x, q_oracle.x)
        self.assertAlmostEqual(q.y, q_oracle.y)
        self.assertAlmostEqual(q.z, q_oracle.z)

    def test_get_quaternion_from_vectors(self):
        # Input variables to function
        u = [1.2, 0, 0]
        v = [0, 0.2, 0]

        # Function call
        q = quaternion_algebra.get_quaternion_from_vectors(u, v)

        # The expected output (rotation 90 degrees around z axis)
        q_oracle = Quaternion(np.cos(90 / 2.0 * np.pi/180), 0.0, 0.0, 1.0 * np.sin(90 / 2.0 * np.pi/180))

        # Assert expected behaviour
        self.assertAlmostEqual(q.w, q_oracle.w)
        self.assertAlmostEqual(q.x, q_oracle.x)
        self.assertAlmostEqual(q.y, q_oracle.y)
        self.assertAlmostEqual(q.z, q_oracle.z)

    def test_get_quaternion_from_antiparallel_vectors(self):
        # Input variables to function
        u = [1.2, -0.1, 0.9]
        v = [-1.2, 0.1, -0.9]

        # Function call
        q = quaternion_algebra.get_quaternion_from_vectors(u, v)

        # The expected output
        q_oracle = Quaternion(0.0, 0.0, 0.0, -1.0)

        # Assert expected behaviour
        self.assertTrue(q == q_oracle)

    def test_get_quaternion_from_equal_vectors(self):
        # Input variables to function
        u = [0.1, -0.2, 0.9]
        v = [0.1, -0.2, 0.9]

        # Function call
        q = quaternion_algebra.get_quaternion_from_vectors(u, v)

        # The expected output
        q_oracle = Quaternion(1, 0, 0, 0)

        # Assert expected behaviour
        self.assertTrue(q == q_oracle)


if __name__ == '__main__':
    unittest.main()
