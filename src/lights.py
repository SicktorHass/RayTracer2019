from geo_objects.point_vector import Point3D


class PointLight(object):
    def __init__(self, posi, color):
        self.posi = Point3D(posi)
        self.color = color
