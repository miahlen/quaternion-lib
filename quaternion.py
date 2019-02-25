import numpy as np

class Quaternion():
    """ Form an Quaternion.

    A class with instance variables w, x, y and z, representing
    a quaternion. The w is the scalar part and (x,y,z) the vector
    part of the quaternion.

    Attributes:
        w: A float representing the w component of the quaternion.
        x: A float representing the x component of the quaternion.
        y: A float representing the y component of the quaternion.
        z: A float representing the z component of the quaternion.
    """

    def __init__(self, w=1.0, x=0.0, y=0.0, z=0.0):
        """Inits Quaternion class."""
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, q2):
        return self.w==q2.w and self.x==q2.x and self.y==q2.y and self.z==q2.z

    def __str__(self):
        return "("+str(self.w)+", "+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"

    def get_quaternion_norm(self):
        return np.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def normalize_quaternion(self):
        norm = self.get_quaternion_norm()

        # Make sure norm is not zero before normalizing the quaternion
        if norm==0.0:
            raise Exception("Quaternion norm equals zero")

        self.w /= norm
        self.x /= norm
        self.y /= norm
        self.z /= norm
        return self

    def get_quaternion_conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)
