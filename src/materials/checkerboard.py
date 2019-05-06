from geo_objects.point_vector import Vector3D


class Checkerboard(object):
    def __init__(self):
        self.base_color = (1., 1., 1.)
        self.other_color = (0., 0., 0.)
        self.ka = 1.
        self.kd = 0.1
        self.ks = 0.2
        self.phong_exponent = 20
        self.check_size = 4

    def base_color_at(self, p):
        v = Vector3D((p.x, p.y, p.z))
        v*(1/self.check_size)
        if (int(abs(v.x) + 0.5) + int(abs(v.y) + 0.5) + int(abs(v.z) + 0.5)) % 2:
            return self.other_color
        return self.base_color
