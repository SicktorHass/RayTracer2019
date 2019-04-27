import numpy as np

class Point3D(object):


    def __init__(self, coord_tup):
        self.x = np.double(coord_tup[0])
        self.y = np.double(coord_tup[1])
        self.z = np.double(coord_tup[2])

    def __repr__(self):
        return "X_coord:{} Y_coord:{} Z_coord:{}".format(self.x, self.y, self.z)