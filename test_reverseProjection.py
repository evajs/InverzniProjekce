from unittest import TestCase
import numpy
from reverse_projection import ReverseProjection

class TestReverseProjection(TestCase):
    def test_get3D(self):
        # normal vector of laser plane in photo coordinates (Z axis of cuboid)
        laser_plane_normal = numpy.array([0, 0, 1])
        # a point of laser plane 0
        a_point_at_laser_plane = numpy.array([0, 0, 1])
        # photo size
        photo_size = [2, 2]

        # Necessary to specify coordinates of laser plane
        # Up defines direction of y axis of laser plane in the captured image
        up = numpy.array([0, 1, 0])

        projection = ReverseProjection(laser_plane_normal, a_point_at_laser_plane, photo_size, up, -1)

        assert projection.coordinate_change(projection.get3D(1 / 2, 1 / 2, 1)) == numpy.array([0, 0, 0])

    def test_coordinate_change(self):
        self.fail()
