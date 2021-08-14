from math import pi, cos, sqrt, radians, atan, acos, tan
import numpy as np
import os


def calc_position(a: float, theta: float, phi: float, psi: float):
    """
    Calculate the position of satellite by given parameters.

    parameters:
    a: a distance between the origin and the beacon (unit: m)
    theta: an angle between a line SA and the direction of gravity (unit: deg)
    phi: an angle between a line SB and the direction of gravity (unit: deg)
    psi: an angle between a line SA and SB (unit: deg)

    (S means the point of satellite, A the point of a beacon, and B the point of the other beacon)

    return:
    x, y, z: the position of satellite (unit: m)

    """

    r_theta = radians(theta)
    r_phi = radians(phi)
    r_psi = radians(psi)

    x: float
    y: float
    z: float

    A = tan(r_theta) ** 2 + tan(r_phi) ** 2 - 2 * \
        tan(r_theta) * tan(r_phi) * cos(r_psi)

    z = 2 * a / sqrt(A)

    x = (tan(r_theta) ** 2 - tan(r_phi) ** 2) * a / A

    y = sqrt(z ** 2 * tan(r_theta) ** 2 - (x + a) ** 2)

    return x, y, z


def calc_angle(a, x, y, z):
    theta = atan(sqrt((x + a) ** 2 + y ** 2) / z)
    phi = atan(sqrt((x - a) ** 2 + y ** 2) / z)
    gamma = acos((x ** 2 + y ** 2 - a ** 2) /
                 sqrt((x ** 2 + y ** 2 + a ** 2) ** 2 - 4 * a ** 2 * x ** 2))
    return theta * 180 / pi, phi * 180 / pi, gamma * 180 / pi


def calc_velocity(x: float, y: float, z: float, new_x: float, new_y: float, new_z: float, time_duration: float):
    """
    Calculate the velocity of satellite by given parameters.

    parameters:
    x, y, z: the previous position
    new_x, new_y, new_z: the newer position
    time_duration: the duration between two observations

    return:
    vx, vy, vz = the velocity of satellite

    """

    vx = (new_x - x) / time_duration
    vy = (new_y - y) / time_duration
    vz = (new_z - z) / time_duration

    return vx, vy, vz


# the distance between the origin and the beacon
a = 1000


if __name__ == '__main__':
    os.system('cls')
    try:
        while(True):
            print('x,y,z -> ', end='')
            x, y, z = (int(n) for n in input().split(','))
            theta, phi, gamma = calc_angle(a, x, y, z)
            print('theta, gamma, gamma = {}, {}, {}'.format(theta, phi, gamma))
    except KeyboardInterrupt:
        pass

    print()
    os.system('cls')

    try:
        while(True):
            print('initial theta, phi, psi -> ', end='')
            theta, phi, gamma = (float(n) for n in input().split(','))
            x, y, z = calc_position(a, theta, phi, gamma)
            print('x, y, z = {}, {}, {}'.format(x, y, z))
            print()

            print('final theta, phi, psi -> ', end='')
            theta, phi, gamma = ((float(n) for n in input().split(',')))
            fx, fy, fz = calc_position(a, theta, phi, gamma)
            print('x, y, z = {}, {}, {}'.format(fx, fy, fz))
            print()

            i = np.array([x, y, z])
            f = np.array([fx, fy, fz])

            dist = np.linalg.norm(f - i)

            print('distance: {} m'.format(dist))
            print()
            print('----------------------------------')
            print()
    except KeyboardInterrupt:
        pass
