from math import pi, sqrt, tan, cos
from main import calc_angle


def cnt_theta_diff_times_d(f, a, theta, phi, psi, d_theta):
    return (f(a, theta + d_theta, phi, psi) - f(a, theta - d_theta, phi, psi)) / 2


def cnt_phi_diff_times_d(f, a, theta, phi, psi, d_phi):
    return (f(a, theta, phi + d_phi, psi) - f(a, theta, phi - d_phi, psi)) / 2


def cnt_psi_diff_times_d(f, a, theta, phi, psi, d_psi):
    return (f(a, theta, phi, psi + d_psi) - f(a, theta, phi, psi - d_psi)) / 2


def A(theta, phi, psi):
    return tan(theta) ** 2 + tan(phi) ** 2 - 2 * tan(theta) * tan(phi) * cos(psi)


def z_pos(a, theta, phi, psi):
    return 2 * a / sqrt(A(theta, phi, psi))


def x_pos(a, theta, phi, psi):
    return (tan(theta) ** 2 - tan(phi) ** 2) * a / A(theta, phi, psi)


def y_pos(a, theta, phi, psi):
    return sqrt(z_pos(a, theta, phi, psi) ** 2 * tan(theta) ** 2 - (x_pos(a, theta, phi, psi) + a) ** 2)


def evaluate(d_theta, d_phi, d_psi, a, theta, phi, psi):
    return sqrt((abs(cnt_theta_diff_times_d(x_pos, a, theta, phi, psi, d_theta)) + abs(cnt_phi_diff_times_d(x_pos, a, theta, phi, psi, d_phi)) + abs(cnt_psi_diff_times_d(x_pos, a, theta, phi, psi, d_psi))) ** 2
                + (abs(cnt_theta_diff_times_d(y_pos, a, theta, phi, psi, d_theta)) + abs(cnt_phi_diff_times_d(y_pos,
                                                                                                              a, theta, phi, psi, d_phi)) + abs(cnt_psi_diff_times_d(y_pos, a, theta, phi, psi, d_psi))) ** 2
                + (abs(cnt_theta_diff_times_d(z_pos, a, theta, phi, psi, d_theta)) + abs(cnt_phi_diff_times_d(z_pos,
                                                                                                              a, theta, phi, psi, d_phi)) + abs(cnt_psi_diff_times_d(z_pos, a, theta, phi, psi, d_psi))) ** 2
                )


if __name__ == '__main__':

    a = 3000  # m

    d_theta = d_phi = d_psi = pi / 180

    with open('precision_table_3km.txt', 'w') as f:
        for x in range(-2 * a, 2 * a, a // 10):
            for y in range(a // 10, 2 * a, a // 10):
                for z in range(a // 10, 2 * a, a // 10):

                    theta, phi, psi = calc_angle(a, x, y, z)
                    eval_value = evaluate(
                        d_theta, d_phi, d_psi, a, theta, phi, psi)

                    print(theta, phi, psi, '=>', x, y, z, eval_value)
                    f.write('{} {} {} {}\n'.format(x, y, z, eval_value))
