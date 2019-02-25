class Position():
    """ Form an 3D position.

    A class with instance variables x, y and z, representing
    a 3D position in meters. If used to represent the position
    of a robot, x points East, y points North and z points Up.
    If instead used to represent position offset on robot,
    x axis points forward, y axis points to the left and z axis
    points upwards, relative to the ego robot pose.

    Attributes:
        x: A float representing the x component of the position in meters.
        y: A float representing the y component of the position in meters.
        z: A float representing the z component of the position in meters.
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """Inits Position class with 3D position x,y,z."""
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, p2):
        return self.x==p2.x and self.y==p2.y and self.z==p2.z

    def __add__(self, p2):
        return Position(self.x+p2.x, self.y+p2.y, self.z+p2.z)

    def __sub__(self, p2):
        return Position(self.x-p2.x, self.y-p2.y, self.z-p2.z)

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"
