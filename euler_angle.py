class EulerAngle():
    def __init__(self, roll=0.0, pitch=0.0, yaw=0.0):
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def __str__(self):
        return "("+str(self.roll)+", "+str(self.pitch)+", "+str(self.yaw)+")"
