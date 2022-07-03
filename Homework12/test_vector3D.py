# EXERCISE 12.1
# -----------------------------------------------
print('Exercise 12.1')
print('------------')

from vector3D import Vector
import pytest
import math


def test_operations():
    v = Vector(1,2,3)
    w = Vector(2,-3,2)
    assert v!=w
    assert v + w == Vector(3,-1,5)
    assert v - w == Vector(-1,5,1)
    assert v * w == 2
    assert v.cross(w) == Vector(13,4,-7)
    assert v.length() == math.sqrt(14)
    S = set([v,v,w])
    assert len(S) == 2

if __name__=="__main__":
    pytest.main()
