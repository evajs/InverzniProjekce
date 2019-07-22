# I suppose that
#   the photo is xy plane having z=0.
#   coordinates of a point of laser plane having laser_position=0 are (p_1, p_2, p_3).
#   normal vector of laser plane is (n_1, n_2, n_3).
#   focus is in (-width/2, -heigth/2, -f).

import numpy

#normal vector of laser plane in photo coordinates (Z axis of cuboid)
n_1 = 0
n_2 = 0
n_3 = 1
# a point of laser plane 0
p_1 = 0
p_2 = 0
p_3 = 1
# photo size
width = 2
heigth = 2
# focus
f = 1

normal = numpy.array([n_1, n_2, n_3])
normal_unit = normal/ numpy.linalg.norm(normal)
base_point = numpy.array([p_1, p_2, p_3])
focus = numpy.array([width/2, heigth/2, -f])


def get3D(photo_x, photo_y, laser_position):
    laser_point = base_point + laser_position * normal_unit # is a point in laser plane
    photo_point = numpy.array([photo_x, photo_y, 0])
    line_direction = photo_point - focus
    # line containing points photo_point and focus has equation focus + line_param * line_direction
    # laser plane has equation normal.(x, y, z) - normal.laser_point = 0, so the intersection is defined by
    line_param = (numpy.dot(normal_unit,laser_point) - numpy.dot(normal_unit,focus))/(numpy.dot(normal_unit, line_direction))

    coordinates = focus + line_param * line_direction
    return coordinates

# point over base point (point of Y axis in cuboid)
u_1 = 0
u_2 = 1
u_3 = 0
up = numpy.array([u_1, u_2, u_3])
up_unit = up/numpy.linalg.norm(up)

# axis X is orthogonal to Y and Z
axis_x = numpy.cross(up_unit, normal_unit)
axis_x_unit = axis_x/numpy.linalg.norm(axis_x)


def coordinate_change(old_coordinates):
    # from photo coordinates the cuboid coordinates are obtained using change of basis matrix
    new_basis = numpy.transpose(numpy.array([axis_x, up, normal]))
    print(new_basis)
    new_basis_inversion = numpy.linalg.inv(new_basis)
    print(new_basis_inversion)
    new_coordinates = numpy.dot(new_basis_inversion, old_coordinates)
    return new_coordinates

print(coordinate_change(get3D(1/2, 1/2, 1)))
