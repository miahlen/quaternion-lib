from quaternion import Quaternion
from position import Position
from euler_angle import EulerAngle
import numpy as np

def get_quaternion_norm(q):
    return np.sqrt(q.w**2 + q.x**2 + q.y**2 + q.z**2)

def normalize_quaternion(q):
    norm = get_quaternion_norm(q)

    # Make sure norm is not zero before normalizing the quaternion
    if norm==0.0:
        raise Exception("Quaternion norm equals zero")

    q.w /= norm
    q.x /= norm
    q.y /= norm
    q.z /= norm
    return q
