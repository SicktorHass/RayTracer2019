from .geo_base import GeoObject
from .point_vector import *


class Plane(GeoObject):

    def __init__(self, point, normal, material):
        self.point = Point3D(point)
        self.normal = Vector3D(normal).normalize()
        self.material = material

    def intersection_param(self, ray):
        op = ray.origin.vector_to(self.point)
        a = op * self.normal
        b = ray.direction * self.normal

        if b < 0:
            return a / b
        else:
            return None

    def normal_vec_at(self, hitpoint=None):
        return self.normal
