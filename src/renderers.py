from PIL import Image
from geo_objects.geo_base import Ray
import math as m
import threading
BACKGROUND_COLOR = (0, 0, 0)
EPSILON = 0.0001


class PrimitiveRenderer(object):
    def __init__(self, camera, objects, lights, resolution):
        self.cam = camera
        self.lights = lights
        self.objects = objects
        self.image = Image.new('RGB', (resolution[0], resolution[1]), BACKGROUND_COLOR)
        self.max_level = 3

    def start_render(self, start):
        for y in range(start, self.image.height, 4):
            for x in range(self.image.width):
                ray = self.cast_cam_ray(x, y)
                color = self.trace_ray(1, ray)
                color = tuple([int(x*255) if x <= 1 else 1*255 for x in color])
                self.image.putpixel((x, y), color)
        print('Thread "{}" finished rendering!'.format(start))

    def intersect(self, ray):
        hitpoint_data = {}
        maxdist = float('inf')
        for obj in self.objects:
            hitdist = obj.intersection_param(ray)
            if hitdist and hitdist > 0:
                if hitdist < maxdist:
                    maxdist = hitdist
                    hitpoint_data['hitdist'] = hitdist
                    hitpoint_data['hitobj'] = obj
                    hitpoint_data['ray'] = ray
                    hitpoint_data['hitpoint'] = ray.point_at_t(hitdist)
                    hitpoint_data['light'] = self.lights
                    hitpoint_data['normal'] = obj.normal_vec_at(hitpoint_data['hitpoint'])
        return hitpoint_data

    def trace_ray(self, level, ray):
        hitpoint_data = self.intersect(ray)
        color = BACKGROUND_COLOR
        if level <= self.max_level:
            if hitpoint_data:
                color = self.shade(level, hitpoint_data)
        return color

    def shade(self, level, hitpoint_data):
        direct_color = hitpoint_data['hitobj'].material.base_color_at(hitpoint_data)
        direct_color = self.cast_shadow(hitpoint_data, direct_color)
        reflected_ray = self.calc_reflected_ray(hitpoint_data)
        reflect_color = self.trace_ray(level+1, reflected_ray)
        reflect_color = tuple(map(lambda x: x*(hitpoint_data['hitobj'].material.reflection/level), reflect_color))
        return self.add_colors(direct_color, reflect_color)

    def calc_reflected_ray(self, hitpoint_data):
        d_inverse = hitpoint_data['ray'].direction * -1
        direction = d_inverse.rotate_pi(hitpoint_data['normal'])
        return Ray(hitpoint_data['hitpoint'], direction)

    def add_colors(self, ct1, ct2):
        return (ct1[0]+ct2[0], ct1[1]+ct2[1], ct1[2]+ct2[2])

    def cast_shadow(self, hitpoint_data, direct_color):
        light_ray = Ray(hitpoint_data['hitpoint'], hitpoint_data['l'])
        for o in self.objects:
            if o is hitpoint_data['hitobj']:
                continue
            hit = o.intersection_param(light_ray)

            # 16.4 THE EPSILON FACTOR -SALT AND PEPPER NOISE
            # fraglich ist: warum passiert es nie auf den oberseiten??
            # es müsste mit der gleichen wahrscheinlichkeit auf der oberseite
            # punkte innerhalb der sphäre geben, für die ein hit gemeldet wird,
            # sodass fälschlicherweise geshadet wird, diese treten jedoch nie auf
            # da wir nach den nächstgelegensten hit suchen und die punkte
            # manchmal (leider) INNERHALB der sphäre liegen, was in negativen
            # 't' resultiert gibt es hier eine kleine, hässliche toleranz für
            # marginal negative 't'

            if hit:     # no direct light at this point
                if hit > -EPSILON:
                    return tuple(map(lambda x: x*0.5, direct_color))
        return direct_color

    def cast_cam_ray(self, x, y):
        x_comp = self.cam.u*(x*self.cam.pixel_w - self.cam.view_plane_width/2)
        y_comp = self.cam.s*(y*self.cam.pixel_h - self.cam.view_plane_height/2)
        return Ray(self.cam.origin, self.cam.f+x_comp+y_comp)
