class Position():
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, p2):
        return self.x==p2.x and self.y==p2.y and self.z==p2.z

    def __add__(self, p2):
        return Position(self.x+p2.x, self.y+p2.y, self.z+p2.z)
