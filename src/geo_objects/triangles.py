from .geo_base import GeoObject
from .point_vector import Point3D


class Triangle(GeoObject):
    def __init__(self, point_a, point_b, point_c, material):
        self.a = Point3D(point_a)
        self.b = Point3D(point_b)
        self.c = Point3D(point_c)
        self.u = self.a.vector_to(self.b)
        self.w = self.a.vector_to(self.c)
        self.material = material

    def intersection_param(self, ray):
        pass
