class EulerAngle():
    """ Form an euler angle.

    A class with instance variables roll, pitch and yaw,
    representing Euler angles. All angles are given in
    radians and the order of rotation is ZYX.

    Attributes:
        roll: A float representing the rotation around the x axis (pointing forward) in radians.
        pitch: A float representing the rotation around the y axis (pointing left) in radians.
        yaw: A float representing the rotation around the z axis (pointing upward) in radians.
    """

    def __init__(self, roll=0.0, pitch=0.0, yaw=0.0):
        """Inits EulerAngle with angles roll, pitch and yaw."""
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def __eq__(self, e2):
        return self.roll==e2.roll and self.pitch==e2.pitch and self.yaw==e2.yaw

    def __str__(self):
        return "("+str(self.roll)+", "+str(self.pitch)+", "+str(self.yaw)+")"

    def __mul__(self, val):
        return EulerAngle(self.roll*val, self.pitch*val, self.yaw*val)
