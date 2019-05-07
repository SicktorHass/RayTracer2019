from geo_objects.point_vector import Vector3D


class Checkerboard(object):
    def __init__(self):
        self.base_color = (1., 1., 1.)
        self.other_color = (0., 0., 0.)
        self.ka = 0.9
        self.kd = 0.1
        self.ks = 0.9
        self.phong_exponent = 10
        self.check_size = 4
        self.reflection = 0.4

    def base_color_at(self, hitpoint_data):
        """
        l = hitpoint_data['hitpoint'].vector_to(hitpoint_data['light'].posi).normalize()
        hitpoint_data['l'] = l
        r = l.rotate_pi(hitpoint_data['normal'])
        phi = l * hitpoint_data['normal']
        theta = (hitpoint_data['ray'].direction * -1) * r
        a = self.compute_ambient(hitpoint_data)
        d = self.compute_diffuse(phi, hitpoint_data['light'].color)
        s = self.compute_specular(theta, hitpoint_data['light'].color)
        return tuple([x+y+z for x, y, z in zip(a, d, s)])
        """
        return self.checker_color(hitpoint_data)

    def compute_ambient(self, hitpoint_data):
        base_color = self.checker_color(hitpoint_data)
        return [c*self.ka for c in base_color]

    def compute_diffuse(self, phi, light_col):
        return [c*self.kd*phi for c in light_col]

    def compute_specular(self, theta, light_col):
        theta_n = theta**self.phong_exponent
        return [c*self.ks*theta_n for c in light_col]

    def checker_color(self, hitpoint_data):
        l = hitpoint_data['hitpoint'].vector_to(hitpoint_data['light'].posi).normalize()
        hitpoint_data['l'] = l
        p = hitpoint_data['hitpoint']
        v = Vector3D((p.x, p.y, p.z))
        v*(1/self.check_size)
        if (int(abs(v.x) + 0.5) + int(abs(v.y) + 0.5) + int(abs(v.z) + 0.5)) % 2:
            return self.other_color
        return self.base_color
