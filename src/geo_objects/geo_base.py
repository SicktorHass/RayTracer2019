from .point_vector import *
from abc import ABC, abstractmethod


class GeoObject(ABC):

    def __init__(self, material):
        self.normal = None
        self.material = material

    def intersection_param(self, ray):
        assert(isinstance(ray, Ray))

    def normal_vec_at(self, hitpoint):
        assert(isinstance(hitpoint, Point3D))


class Ray(object):

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def point_at_t(self, t):
        return self.origin + self.direction*t
    """
    def create_rotation_plane(self, vec):
        pl_point = self.origin
        pl_normal = (self.direction % vec).normalize()
        return pl_normal
    """
    def __repr__(self):
        return 'Ray(%s,%s)' % (repr(self.origin), repr(self.direction))
