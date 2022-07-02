from vector3D import Vector

def find_axis(v1, v2):
    v = v1.cross(v2)
    N = v.length()
    if N == 0:
        raise ValueError('The vectors v1 and v2 are parallel')
    else:
        axis = Vector(v.x/N, v.y/N, v.z/N)
        print('The axis of the vectors v1 and v2 is: {}'.format(axis))
    

V1 = Vector(1,2,-3)
V2 = Vector(3,1,-5)
find_axis(V1,V2)

