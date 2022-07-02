import math
class Vector:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({},{},{})".format(self.x,self.y,self.z)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == other.z 

    def __ne__(self,other):
        return not self == other

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y,self.z + other.z)

    def __sub__(self,other):
        return Vector(self.x - other.x,self.y - other.y,self.z - other.z)

    def __mul__(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self,other):
        return Vector(self.y*other.z-other.y*self.z,-self.x*other.z+other.x*self.z, self.x*other.y-other.x*self.y)

    def length(self):
        return math.sqrt(self*self)

    def __hash__(self):
        return hash((self.x, self.y, self.z))
