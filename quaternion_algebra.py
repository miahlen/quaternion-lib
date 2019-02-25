from quaternion import Quaternion
from position import Position
from euler_angle import EulerAngle
import numpy as np

def get_quaternion_norm(q):
    return np.sqrt(q.w**2 + q.x**2 + q.y**2 + q.z**2)

def get_quaternion_conjugate(q):
    return Quaternion(q.w, -q.x, -q.y, -q.z)

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

def multiply_quaternions(q1, q2):
    q_out = Quaternion()
    q_out.w = q1.w*q2.w  -  q1.x*q2.x  -  q1.y*q2.y  -  q1.z*q2.z
    q_out.x = q1.w*q2.x  +  q1.x*q2.w  +  q1.y*q2.z  -  q1.z*q2.y
    q_out.y = q1.w*q2.y  -  q1.x*q2.z  +  q1.y*q2.w  +  q1.z*q2.x
    q_out.z = q1.w*q2.z  +  q1.x*q2.y  -  q1.y*q2.x  +  q1.z*q2.w
    return q_out

# input v is of class Position
def rotate_vector_by_quaternion(v,q):
    vq = Quaternion(0.0, v.x, v.y, v.z)
    q_conjugate = get_quaternion_conjugate(q)
    q_out = multiply_quaternions(multiply_quaternions(q, vq), q_conjugate)
    return Position(q_out.x, q_out.y, q_out.z)

def quaternion_to_euler(q):
    # roll (rotation around x-axis pointing forward)
    roll = np.arctan2(2.0 * (q.w*q.x + q.y*q.z), 1.0 - 2.0 * (q.x**2 + q.y**2))

    # pitch (rotation around y-axis pointing to the left)
    sinp = 2.0 * (q.w * q.y - q.z * q.x)
    if sinp >= 1:
        pitch = np.pi / 2 # use 90 degrees if out of range
    elif sinp <= -1:
        pitch = - np.pi / 2 # use -90 degrees if out of range
    else:
        pitch = np.arcsin(sinp)

    # yaw (rotation around z-axis pointing upward)
    yaw = np.arctan2( 2.0 * (q.w*q.z + q.x*q.y), 1.0 - 2.0 * (q.y**2 + q.z**2))
    euler = EulerAngle()
    euler.roll = roll
    euler.pitch = pitch
    euler.yaw = yaw
    return euler

def get_quaternion_from_vectors(u, v):
    cross_u_v = np.cross(u,v)
    if np.all(cross_u_v == 0.0):
        if all([ui+vi==0.0 for ui,vi in zip(u,v)]):
            return Quaternion(0.0, 0.0, 0.0, -1.0)
        else:
            return Quaternion(1.0, 0.0, 0.0, 0.0)
    u_norm = np.sqrt(u[0]**2 + u[1]**2 + u[2]**2)
    u = [ui/u_norm for ui in u]
    v_norm = np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    v = [vi/v_norm for vi in v]
    cos_theta = np.dot(u,v)
    half_cos = np.sqrt(0.5 * (1.0 + cos_theta))
    half_sin = np.sqrt(0.5 * (1.0 - cos_theta))

    cros_norm = np.sqrt(cross_u_v[0]**2 + cross_u_v[1]**2 + cross_u_v[2]**2)
    w = [cross_i/cros_norm for cross_i in cross_u_v]

    q_out = Quaternion()
    q_out.w = half_cos
    q_out.x = half_sin * w[0]
    q_out.y = half_sin * w[1]
    q_out.z = half_sin * w[2]
    return q_out

def get_quaternion_from_vector(v):
    u = [1.0, 0.0, 0.0]
    return get_quaternion_from_vectors(u,v)
