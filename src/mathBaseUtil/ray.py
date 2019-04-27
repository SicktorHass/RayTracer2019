import numpy as np

class Vector3D(object):
    

    def __init__(self, coord_tup):
        self.x = np.double(coord_tup[0])
        self.y = np.double(coord_tup[1])
        self.z = np.double(coord_tup[2])

    def __repr__(self):
        return "Xcomp: {} Ycomp: {} Zcomp: {}".format(self.x, self.y, self.z)
    
    def __add__(self, other):
        assert(isinstance(other, type(self)))
        product = (self.x+other.x, self.y+other.y, self.z+other.z)
        return Vector3D(product)

    def __sub__(self, other):
        assert(isinstance(other, type(self)))
        product = (self.x-other.x, self.y-other.y, self.z-other.z)
        return Vector3D(product)

    def __mul__(self, other):
        if isinstance(other, type(self)):
            product = np.double(self.x*other.x + self.y*other.y + self.z*other.z)
            return product
        else:
            s = np.double(other)
            return Vector3D((self.x*s, self.y*s, self.z*s))

    def __truediv__(self, scalar):
        s = np.double(scalar)
        return Vector3D((self.x/s, self.y/s, self.z/s))

    def __mod__(self, other):
        assert(isinstance(other, type(self)))
        return Vector3D((
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x))

    def castRay(self, origin, direction):
        pass