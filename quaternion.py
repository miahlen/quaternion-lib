class Quaternion():
    def __init__(self, w=1.0, x=0.0, y=0.0, z=0.0):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, q2):
        return self.w==q2.w and self.x==q2.x and self.y==q2.y and self.z==q2.z

    def __str__(self):
        return "("+str(self.w)+", "+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"
