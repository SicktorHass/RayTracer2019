import math as m
from geo_objects.point_vector import *


class PinholeCamera(object):

    def __init__(self, location, center, up, fov, resolution):

        # extrinsische Parameter
        self.origin = Point3D(location)
        # z-axis
        self.f = self.origin.vector_to(Point3D(center)).normalize()
        # commutation matters: alters the direction
        # x-axis
        self.u = (Vector3D(up) % self.f).normalize()
        # y-axis
        self.s = self.u % self.f

        # intrinsische Parameter TODO numpy
        self.fov = fov
        self.res_w = resolution[0]
        self.res_h = resolution[1]
        self.alpha = m.radians(self.fov/2)
        self.aspect_ratio = self.res_w / self.res_h
        self.view_plane_height = 2*m.tan(self.alpha)
        self.view_plane_width = self.aspect_ratio * self.view_plane_height
        self.pixel_w = self.view_plane_width / (self.res_w-1)
        self.pixel_h = self.view_plane_height / (self.res_h-1)

    def __repr__(self):
        return "f: {}, u: {}, s: {}".format(self.f, self.u, self.s)
