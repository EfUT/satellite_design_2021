from math import sqrt, pow, pi


a = 1000  # m


def xthetaf(x, y, z):
    return ((x + a) ** 2 + y ** 2 + z ** 2) * sqrt((x + a) ** 2 + y ** 2) / (z * (x + a))


def xphif(x, y, z):
    return ((x + a) ** 2 + y ** 2 + z ** 2) * sqrt((x + a) ** 2 + y ** 2) / (z * y)


def xgammaf(x, y, z):
    return -((x + a) ** 2 + y ** 2 + z ** 2) / sqrt((x + a) ** 2 + y ** 2)


def ythetaf(x, y, z):
    return ((x - a) ** 2 + y ** 2 + z ** 2) * sqrt((x - a) ** 2 + y ** 2) / (z * (x - a))


def yphif(x, y, z):
    return ((x - a) ** 2 + y ** 2 + z ** 2) * sqrt((x - a) ** 2 + y ** 2) / (z * y)


def ygammaf(x, y, z):
    return -((x - a) ** 2 + y ** 2 + z ** 2) / sqrt((x + a) ** 2 + y ** 2)


def zthetaf(x, y, z):
    return -((x ** 2 + y ** 2 + z ** 2 + a ** 2) ** 2 - 4 * a ** 2 * x ** 2) / (4 * a * x * y)


def zphif(x, y, z):
    return ((x ** 2 + y ** 2 + a ** 2) ** 2 - 4 * a ** 2 * x ** 2) / 2 * a * y * (x ** 2 - y ** 2 - z ** 2 - a ** 2)


def zgammaf(x, y, z):
    return 0


def eval_func(x, y, z):
    xtheta = abs(xthetaf(x, y, z))
    xphi = abs(xphif(x, y, z))
    xgamma = abs(xgammaf(x, y, z))

    ytheta = abs(ythetaf(x, y, z))
    yphi = abs(yphif(x, y, z))
    ygamma = abs(ygammaf(x, y, z))

    ztheta = abs(zthetaf(x, y, z))
    zphi = abs(zphif(x, y, z))
    zgamma = abs(zgammaf(x, y, z))

    return sqrt(pow(xtheta + xphi + xgamma, 2) + pow(ytheta + yphi + ygamma, 2) + pow(ztheta + zphi + zgamma, 2))


if __name__ == '__main__':
    try:
        while(True):
            print('x,y,z ->', end='')
            x, y, z = (int(n) for n in input().split(','))

            delta_theta = pi / 180

            eval = eval_func(x, y, z)

            print('precision: about {} m'.format(eval * delta_theta))

    except KeyboardInterrupt:
        pass
    except ZeroDivisionError:
        print('devided by zero')
