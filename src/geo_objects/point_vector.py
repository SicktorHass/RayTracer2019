import numpy as np
import math as m
from pyquaternion import Quaternion


class Point3D(object):
    def __init__(self, coord_tup):
        self.x = np.double(coord_tup[0])
        self.y = np.double(coord_tup[1])
        self.z = np.double(coord_tup[2])
        #self.coords = np.nd

    def __repr__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    # evtl. nicht ständig neue vektoren erzeugen
    def __add__(self, vec):
        assert(isinstance(vec, Vector3D))
        return Point3D((
            self.x + vec.x,
            self.y + vec.y,
            self.z + vec.z))

    def vector_to(self, point_b):
        assert(isinstance(point_b, Point3D))
        return Vector3D((
            point_b.x - self.x,
            point_b.y - self.y,
            point_b.z - self.z))


class Vector3D(object):
    def __init__(self, coord_tup):
        self.x = np.double(coord_tup[0])
        self.y = np.double(coord_tup[1])
        self.z = np.double(coord_tup[2])
        self.len = (self * self)**np.double(0.5)

    def __repr__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        assert(isinstance(other, Vector3D))
        product = (self.x+other.x, self.y+other.y, self.z+other.z)
        return Vector3D(product)

    def __sub__(self, other):
        assert(isinstance(other, Vector3D))
        product = (self.x-other.x, self.y-other.y, self.z-other.z)
        return Vector3D(product)

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            r = self.x*other.x + self.y*other.y + self.z*other.z
            return r
        else:
            s = np.double(other)
            return Vector3D((self.x*s, self.y*s, self.z*s))

    def __truediv__(self, scalar):
        s = np.double(scalar)
        # TODO eventuell problematische division
        return Vector3D((self.x/s, self.y/s, self.z/s))

    def __mod__(self, other):
        assert(isinstance(other, Vector3D))
        return Vector3D((
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x))

    def normalize(self):
        return self/self.len

    def angle_with(self, other):
        assert(isinstance(other, Vector3D))
        angle = m.acos(self * other)
        return angle

    def rotate_pi(self, normal):
        v = [self.x, self.y, self.z]
        axis = [normal.x, normal.y, normal.z]
        theta = m.pi
        rotated = Quaternion(axis=axis, angle=theta).rotate(v)
        return Vector3D((rotated[0], rotated[1], rotated[2]))
