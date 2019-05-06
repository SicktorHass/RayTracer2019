from cameras import PinholeCamera
from geo_objects.geo_base import *
from geo_objects.point_vector import *
from geo_objects.plane import *
from geo_objects.spheres import *
from geo_objects.triangles import *
from lights import PointLight
from materials import phong as p
from materials import checkerboard as ch
from renderers import PrimitiveRenderer

# *** DEFINITIONS ***
# -- Camera --
C_LOC = (0, 8, -10)
C_CENTER = (0, 5, 5)
C_UP = (0, 6, 0)
# -- Colors --
RED = (1., 0., 0.)
GREEN = (0., 1., 0.)
BLUE = (0., 0., 1.)
GREY = (.5, .5, .5)
YELLOW = (1., 1., 0.)
WHITE = (1., 1., 1.)
# -- Light --
LIGHT = PointLight((7, 30, 7.5), WHITE)
# -- Materials --

# -- Scene Objects --
biggi = Sphere((0, 10, 12), 4, p.Phong(YELLOW))
s1 = Sphere((0, 5, 5), 1.5, p.Phong(BLUE))  # mitte, fokus
s2 = Sphere((-2.5, 7.5, 5), 1.5, p.Phong(GREEN))  # links oben
s3 = Sphere((2.5, 7.5, 5), 1.5, p.Phong(RED))    # rechts oben
p = Plane((0, 0, 0), (0, 1, 0), ch.Checkerboard())
OBJECTS = [p, s1, s2, s3, biggi]
# -- Image --
IMAGEWIDTH = 1920
IMAGEHEIGHT = 1080


class World(object):
    def __init__(self):
        self.camera = PinholeCamera(C_LOC, C_CENTER, C_UP, 60, (IMAGEWIDTH, IMAGEHEIGHT))
        self.light = LIGHT
        self.objects = OBJECTS
        self.renderer = PrimitiveRenderer(self.camera, self.objects, self.light, (IMAGEWIDTH, IMAGEHEIGHT))

    def render_scene(self):
        image = self.renderer.start_render()
        return image
