class Phong(object):
    def __init__(self, color):
        self.ka = 0.5
        self.kd = 0.6
        self.ks = 0.4
        # specular highlight size; bigger exp = less highlight
        self.phong_exponent = 3
        self.base_color = color

    def base_color_at(self, hitpoint):
        return self.base_color
