from .point_vector import Point3D
from .geo_base import GeoObject
import numpy as np


class Sphere(GeoObject):
    def __init__(self, center, radius, material):
        self.center = Point3D(center)
        self.radius = np.double(radius)
        self.material = material

    def intersection_param(self, ray):
        oc = ray.origin.vector_to(self.center)
        v = oc*ray.direction
        discri = v*v - oc*oc + self.radius*self.radius

        if discri < 0:
            return None
        else:
            return v - (discri**0.5)

    def normal_vec_at(self, hitpoint):
        return self.center.vector_to(hitpoint).normalize()
