from scene import World
from geo_objects.geo_base import Ray
from geo_objects.point_vector import *
from math import radians, degrees, cos

if __name__ == "__main__":
    world = World()
    image = world.render_scene()
    image.save('phongtestfullhd.jpg')

    """
    hitpoint = Point3D((0, 0, 0))
    ray = Ray(hitpoint, raydirection)
    ray.calculate_reflected_ray(hitpoint, normal)
    print(ray)

    normal = Vector3D((0, 1, 0)).normalize()
    raydirection = Vector3D((1, 1, 0)).normalize()
    acos = normal.angle_with(raydirection)
    dot = normal * raydirection
    c = cos(acos)
    print(acos)
    print(dot)
    print(c)
    print(degrees(acos))
    #print(degrees(dot))
    print(degrees(c))
    c1 = (0.2, 0.3, 0.4)
    c2 = (0.3, 0.4, 0.5)
    c3 = (0.6, 0.3, 0.1)
    r = tuple([x+y+z for x, y, z in zip(c1, c2, c3)])
    print(r)
    """
