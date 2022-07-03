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



v = Vector(1,2,3)
w = Vector(2,-3,2)

assert v != w
assert v + w == Vector(3,-1,5)
assert v - w == Vector(-1,5,1)
assert v * w == 2
assert v.cross(w) == Vector(13,4,-7)
assert v.length() == math.sqrt(14)
S = set([v,v,w])
assert len(S) == 2

print('Tests passed!')
