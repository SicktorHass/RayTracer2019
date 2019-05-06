from PIL import Image
from geo_objects.geo_base import Ray
import math as m
import threading
BACKGROUND_COLOR = (0, 0, 0)
EPSILON = 0.000001


class PrimitiveRenderer(object):
    def __init__(self, camera, objects, lights, resolution):
        self.cam = camera
        self.lights = lights
        self.objects = objects
        self.image = Image.new('RGB', (resolution[0], resolution[1]), BACKGROUND_COLOR)

    def start_render(self):
        for y in range(self.image.height):
            for x in range(self.image.width):
                ray = self.cast_cam_ray(x, y)
                maxdist = float('inf')
                color = BACKGROUND_COLOR
                for obj in self.objects:
                    hitdist = obj.intersection_param(ray)
                    if hitdist:
                        if hitdist < maxdist:
                            maxdist = hitdist
                            hitpoint = ray.point_at_t(hitdist)
                            color = self.color_at(ray, hitpoint, obj)
                            color = tuple([int(x*255) if x <= 1 else 1*255 for x in color])
                self.image.putpixel((x, y), color)
        print('Done Rendering')
        return self.image

    def cast_cam_ray(self, x, y):
        x_comp = self.cam.u*(x*self.cam.pixel_w - self.cam.view_plane_width/2)
        y_comp = self.cam.s*(y*self.cam.pixel_h - self.cam.view_plane_height/2)
        return Ray(self.cam.origin, self.cam.f+x_comp+y_comp)

    def color_at(self, ray, hitpoint, hit_obj):

        l = hitpoint.vector_to(self.lights.posi).normalize()  # vector in light direction
        n = hit_obj.normal_vec_at(hitpoint)  # normal of the surface that got hit
        r = l.rotate_pi(n)  # direction of the reflected light
        d_inverse = ray.direction*-1
        # TODO: c_a is probably self color + a bit of other objects/ c_in is light, WHEN NO LIGHT only other objects, maybe shadow
        # quadratische abnahme des einflusses auf die farbe, je weiter das objekt weg ist
        c_a = hit_obj.material.base_color_at(hitpoint)
        c_in = self.lights.color
        phi = l*n
        theta_n = (r*d_inverse)**hit_obj.material.phong_exponent
        # compute environment light; ambient part; kommt aus allen richtungen
        ambient = [c*hit_obj.material.ka for c in c_a]
        # diffuse part; wie schräg fällt die lichtquelle auf das objekt/den punkt
        diffuse = [c*hit_obj.material.kd*phi for c in c_in]
        # specular part; abhängigkeit vom reflexionswinkel, senkrecht = 0, gleiche richtung = 1
        # TODO: entferne specular von unterseite
        specular = [c*hit_obj.material.ks*theta_n for c in c_in]
        color = tuple([x+y+z for x, y, z in zip(ambient, diffuse, specular)])
        light_ray = Ray(hitpoint, l)
        for o in self.objects:
            # 16.4 THE EPSILON FACTOR -SALT AND PEPPER NOISE
            # fraglich ist: warum passiert es nie auf den oberseiten??
            # es müsste mit der gleichen wahrscheinlichkeit auf der oberseite
            # punkte innerhalb der sphäre geben, für die ein hit gemeldet wird,
            # sodass fälschlicherweise geshadet wird, diese treten jedoch nie auf

            hit = o.intersection_param(light_ray)
            # da wir nach den nächstgelegensten hit suchen und die punkte
            # manchmal (leider) INNERHALB der sphäre liegen, was in negativen
            # 't' resultiert gibt es hier eine kleine, hässliche toleranz für
            # marginal negative 't'

            if hit:     # no direct light at this point
                if hit > -EPSILON:
                    return map(lambda x: x*0.66, color)
            else:       # direct light shining hitting object
                pass

        return color

        def near_object_color(self, point):
            # caste rays in hemishpere
            return ()

        def check_shadow(self, point, calcuated_color):
            # senke die farbe, wenn
            pass
