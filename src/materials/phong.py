class Phong(object):
    def __init__(self, color):
        self.ka = 0.8
        self.kd = 0.6
        self.ks = 0.4
        # specular highlight size; bigger exp = less highlight
        self.phong_exponent = 3
        self.base_color = color
        self.reflection = 0.2

    def base_color_at(self, hitpoint_data):
        l = hitpoint_data['hitpoint'].vector_to(hitpoint_data['light'].posi).normalize()
        hitpoint_data['l'] = l
        r = l.rotate_pi(hitpoint_data['normal'])
        phi = l * hitpoint_data['normal']
        theta = (hitpoint_data['ray'].direction * -1) * r
        a = self.compute_ambient()
        d = self.compute_diffuse(phi, hitpoint_data['light'].color)
        s = self.compute_specular(theta, hitpoint_data['light'].color)
        return tuple([x+y+z for x, y, z in zip(a, d, s)])

    def compute_ambient(self):
        return [c*self.ka for c in self.base_color]

    def compute_diffuse(self, phi, light_col):
        return [c*self.kd*phi for c in light_col]

    def compute_specular(self, theta, light_col):
        theta_n = theta**self.phong_exponent
        return [c*self.ks*theta_n for c in light_col]
