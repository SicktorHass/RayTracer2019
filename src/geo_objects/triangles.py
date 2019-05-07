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
        p = self.a.vector_to(ray.origin)
        dw = ray.direction % self.w
        dwu = dw * self.u

        if dwu == 0:
            return None
        pu = p % self.u
        r = dw * p / dwu
        s = pu * ray.direction / dwu
        if 0 <= r and r <= 1 and 0 <= s and s <= 1 and r+s <= 1:
            return pu * self.w / dwu
        else:
            return None

    def normal_vec_at(self, p):
        return (self.u % self.w).normalize()
