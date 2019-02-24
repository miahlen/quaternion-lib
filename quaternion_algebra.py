from quaternion import Quaternion
from position import Position
from euler_angle import EulerAngle
import numpy as np

def get_quaternion_norm(q):
    return np.sqrt(q.w**2 + q.x**2 + q.y**2 + q.z**2)
