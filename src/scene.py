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
import threading
import time

# *** DEFINITIONS ***
# -- Camera --
C_LOC = (0, 8, -10)
C_CENTER = (0, 5, 5)
C_UP = (0, 1, 0)
# -- Colors --
RED = (1., 0., 0.)
GREEN = (0., 1., 0.)
BLUE = (0., 0., 1.)
GREY = (.5, .5, .5)
YELLOW = (1., 1., 0.)
PURPLE = (1., 0., 1.)
CYAN = (0., 1., 1.)
WHITE = (1., 1., 1.)
# -- Light --
LIGHT = PointLight((7, 30, 7.5), WHITE)
# -- Materials --

# -- Scene Objects --
biggi = Sphere((0, 10, 9), 4, p.Phong(YELLOW))
s1 = Sphere((0, 5, 3), 1.5, p.Phong(BLUE))  # mitte, fokus
s2 = Sphere((-2.5, 7.5, 3), 1.5, p.Phong(GREEN))  # links oben
s3 = Sphere((2.5, 7.5, 3), 1.5, p.Phong(RED))    # rechts oben
pl = Plane((0, 0, 0), (0, 1, 0), ch.Checkerboard())
tr1 = Triangle((-3, 0, 5), (-1, 0, 6), (-2, 2, 5), p.Phong(PURPLE))
tr2 = Triangle((3, 0, 5), (1, 0, 6), (2, 2, 5), p.Phong(CYAN))
OBJECTS = [pl, s1, s2, s3, tr1, tr2, biggi]
# -- Image --
IMAGEWIDTH = 400
IMAGEHEIGHT = 400


class World(object):
    def __init__(self):
        self.camera = PinholeCamera(C_LOC, C_CENTER, C_UP, 60, (IMAGEWIDTH, IMAGEHEIGHT))
        self.light = LIGHT
        self.objects = OBJECTS
        self.renderer = PrimitiveRenderer(self.camera, self.objects, self.light, (IMAGEWIDTH, IMAGEHEIGHT))

    def render_scene_multi(self):
        t1 = threading.Thread(target=self.renderer.start_render, args=(0, 2), daemon=True)
        t2 = threading.Thread(target=self.renderer.start_render, args=(1, 2), daemon=True)
        print('starting rendering threads')
        t1.start()
        t2.start()
        while (not t1._is_stopped) and (not t2._is_stopped):
            print('rendering...')
            print(t1)
            print(t2)
            time.sleep(5)
        print('all threads are ready!')
        return self.renderer.image
    
    def render_scene_single(self):
        self.renderer.start_render(start=0, offset=1)
        return self.renderer.image
