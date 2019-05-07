from scene import World
from geo_objects.geo_base import Ray
from geo_objects.point_vector import *
from math import radians, degrees, cos
import time
import threading

if __name__ == "__main__":
    world = World()
    start = time.ctime()
    image = world.render_scene()
    image.save('ende.jpg')
    end = time.ctime()
    print(start, end)
