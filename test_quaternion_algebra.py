import unittest
import quaternion_algebra
from quaternion import Quaternion
import numpy as np

class TestQuaternionAlgebra(unittest.TestCase):

    def test_normalize_quaternion(self):
        q = Quaternion(-2.1,0.0,0.0,0.0)
        q = quaternion_algebra.normalize_quaternion(q)
        self.assertTrue(np.sqrt(q.w**2 + q.x**2 + q.y**2 + q.z**2) == 1)
        self.assertTrue(q == Quaternion(-1.0, 0.0, 0.0, 0.0))
        
if __name__ == '__main__':
    unittest.main()