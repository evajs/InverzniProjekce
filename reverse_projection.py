import numpy




class ReverseProjection:
    """
    I suppose that
    the photo is xy plane having z=0.
    coordinates of a point of laser plane having laser_position=0 are (p_1, p_2, p_3).
    normal vector of laser plane is (n_1, n_2, n_3).
    focus is in (width/2, heigth/2, -f).
    """

    def __init__(self, laser_plane_normal, a_point_at_laser_plane, photo_size_px, up, focal_point_z):
        self.laser_plane_normal = laser_plane_normal
        self.a_point_at_laser_plane = a_point_at_laser_plane
        self.photo_size = photo_size_px
        # focal point
        self.focal_point = numpy.array([photo_size_px[0]/2, photo_size_px[1]/2, focal_point_z])
        self.normal_unit = laser_plane_normal / numpy.linalg.norm(laser_plane_normal)
        self.up = up
        # Normalized up vector
        self.up_unit = up / numpy.linalg.norm(up)
        # axis X is orthogonal to Y and Z
        self.axis_x = numpy.cross(self.up_unit, self.normal_unit)
        self.axis_x_unit = self.axis_x / numpy.linalg.norm(self.axis_x)

    def get3D(self, photo_x, photo_y, laser_position):
        """

        :param photo_x:
        :param photo_y:
        :param laser_position:
        :return:
        """
        laser_point = self.a_point_at_laser_plane + laser_position * self.normal_unit # is a point in laser plane
        photo_point = numpy.array([photo_x, photo_y, 0])
        line_direction = photo_point - self.focal_point
        # line containing points photo_point and focus has equation focus + line_param * line_direction
        # laser plane has equation normal.(x, y, z) - normal.laser_point = 0, so the intersection is defined by
        line_param = (numpy.dot(self.normal_unit,laser_point) - numpy.dot(self.normal_unit, self.focal_point)) / (numpy.dot(self.normal_unit, line_direction))

        coordinates = self.focal_point + line_param * line_direction
        return coordinates

    def coordinate_change(self, old_coordinates):
        """

        :param old_coordinates:
        :return:
        """
        # from photo coordinates the cuboid coordinates are obtained using change of basis matrix
        new_basis = numpy.transpose(numpy.array([self.axis_x, self.up, self.laser_plane_normal]))
        print(new_basis)
        new_basis_inversion = numpy.linalg.inv(new_basis)
        print(new_basis_inversion)
        new_coordinates = numpy.dot(new_basis_inversion, old_coordinates)
        return new_coordinates
