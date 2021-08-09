from math import cos, tan, pi


def checkTheta(x, y, z, a, alpha, beta, theta):
    return not ((cos(theta) >= 0) ^ (((a - x) * tan(alpha) - y * tan(beta) + z) >= 0))


def checkPhi(x, y, z, a, alpha, beta, phi):
    return not ((cos(phi) >= 0) ^ (((-a - x) * tan(alpha) - y * tan(beta) + z) >= 0))


def checkPsi(x, y, z, a, alpha, beta, psi):
    return not ((cos(psi) >= 0) ^ (((z*tan(beta) + y)**2 + (z * tan(alpha) + x)**2 - a**2 + (y*tan(alpha) - x*tan(beta))**2 - a**2 * tan(beta) ** 2) >= 0))


def sign_of_sinpsi(x, y, z, alpha, beta):
    return (tan(beta) * z + y) >= 0


xdata = [2016, 2016, 2016, 2016, 1734, 1734, 1734, 1734,
         1000, 1000, 1000, 1000, 1655, 1655, 1655, 1655, ]
ydata = [-541, 422, -541, 422, -536, 425, -536, 425, -
         1282, 1000, -1282, 1000, -1672, 1328, -1672, 1328]
zdata = [252, 422, 252, 422, 228, 398, 228, 398,
         598, 1000, 598, 1000, 712, 1241, 712, 1241, ]

a = 2000
alpha = 10 * pi / 180
beta = 10 * pi / 180

theta = 0.976174218673598
phi = 1.48447620740614
psi = 1.84362216783075

if __name__ == '__main__':
    for i in range(16):
        print(
            f'{xdata[i]}, {ydata[i]}, {zdata[i]} => {checkTheta(xdata[i], ydata[i], zdata[i], a, alpha, beta, theta) and checkPhi(xdata[i], ydata[i], zdata[i], a, alpha, beta, phi) and checkPsi(xdata[i], ydata[i], zdata[i], a, alpha, beta, psi)}')
        # print(
        #     f'checksign => {sign_of_sinpsi(xdata[i], ydata[i], zdata[i], 0, 0)}')
        # print('------------------------------')
