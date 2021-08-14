from sympy import Symbol, tan, cos, sqrt, diff, Abs, init_printing, pi
from math import atan, acos
import math

init_printing()

th = Symbol('θ')
ph = Symbol('φ')
ps = Symbol('Ψ')

dth = Symbol('Δθ')
dph = Symbol('Δφ')
dps = Symbol('ΔΨ')

a = Symbol('a')


A = tan(th) ** 2 + tan(ph) ** 2 - 2 * tan(th) * tan(ph) * cos(ps)

z = 2 * a / sqrt(A)

x = (tan(ph) ** 2 - tan(th) ** 2) * a / A

y = sqrt(z ** 2 * tan(th) ** 2 - (x - a) ** 2)

dxdth = diff(x, th)
dxdph = diff(x, ph)
dxdps = diff(x, ps)

dydth = diff(y, th)
dydph = diff(y, ph)
dydps = diff(y, ps)

dzdth = diff(z, th)
dzdph = diff(z, ph)
dzdps = diff(z, ps)

dl = sqrt((Abs(dxdth * dth) + Abs(dxdph * dph) + Abs(dxdps * dps)) ** 2
          + (Abs(dydth * dth) + Abs(dydph * dph) + Abs(dydps * dps)) ** 2
          + (Abs(dzdth * dth) + Abs(dzdph * dph) + Abs(dzdps * dps)) ** 2)

v_dth = v_dph = 0.176 * pi / 180
v_dps = 0.224 * pi / 180
v_a = 2000

dl = dl.subs([(dth, v_dth), (dph, v_dph), (dps, v_dps), (a, v_a)])
print(dl)


def convert_pos_to_angle(x, y, z, a):
    theta = atan(math.sqrt((x - a) ** 2 + y ** 2) / z)
    phi = atan(math.sqrt((x + a) ** 2 + y ** 2) / z)
    psi = acos((x ** 2 + y ** 2 - a ** 2) /
               math.sqrt((x**2 + y ** 2 + a ** 2) ** 2 - 4 * a ** 2 * x ** 2))
    return theta, phi, psi


def calculate(theta, phi, psi):
    from math import sqrt, tan, sin, cos
    return sqrt((100*pi*abs((tan(theta)**2 - tan(phi)**2)*sin(psi)*tan(theta)*tan(phi)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2)/9 + pi*abs(1000*(2*(tan(theta)**2 + 1)*cos(psi)*tan(phi) - (2*tan(theta)**2 + 2)*tan(theta))*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2 + 1000*(2*tan(theta)**2 + 2)*tan(theta)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2))/180 + pi*abs(1000*(2*(tan(phi)**2 + 1)*cos(psi)*tan(theta) - (2*tan(phi)**2 + 2)*tan(phi))*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2 - 1000*(2*tan(phi)**2 + 2)*tan(phi)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2))/180)**2 + (100*pi*abs(sin(psi)*tan(theta)*tan(phi))/(9*abs((-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**(3/2))) + pi*abs(1000*(tan(theta)**2 + 1)*cos(psi)*tan(phi) - 500*(2*tan(theta)**2 + 2)*tan(theta))/(90*abs((-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**(3/2))) + pi*abs(1000*(tan(phi)**2 + 1)*cos(psi)*tan(theta) - 500*(2*tan(phi)**2 + 2)*tan(phi))/(90*abs((-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**(3/2))))**2 + (pi*abs((1000*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2) + 1000)*(2000*(2*(tan(phi)**2 + 1)*cos(psi)*tan(theta) - (2*tan(phi)**2 + 2)*tan(phi))*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2 - 2000*(2*tan(phi)**2 + 2)*tan(phi)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2))/2 - 2000000*(2*(tan(phi)**2 + 1)*cos(psi)*tan(theta) - (2*tan(phi)**2 + 2)*tan(phi))*tan(theta)**2/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2)/(180*abs(sqrt(-(1000*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2) + 1000)**2 + 4000000*tan(theta)**2/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)))) + pi*abs(2000*(1000*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2) + 1000)*(tan(theta)**2 - tan(phi)**2)*sin(psi)*tan(theta)*tan(phi)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2 - 4000000*sin(psi)*tan(theta)**3*tan(phi)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2)/(180*abs(sqrt(-(1000*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2) + 1000)**2 + 4000000*tan(theta)**2/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)))) + pi*abs(-(1000*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2) + 1000)*(2000*(2*(tan(theta)**2 + 1)*cos(psi)*tan(phi) - (2*tan(theta)**2 + 2)*tan(theta))*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2 + 2000*(2*tan(theta)**2 + 2)*tan(theta)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2))/2 + 2000000*(2*(tan(theta)**2 + 1)*cos(psi)*tan(phi) - (2*tan(theta)**2 + 2)*tan(theta))*tan(theta)**2/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)**2 + 2000000*(2*tan(theta)**2 + 2)*tan(theta)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2))/(180*abs(sqrt(-(1000*(tan(theta)**2 - tan(phi)**2)/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2) + 1000)**2 + 4000000*tan(theta)**2/(-2*cos(psi)*tan(theta)*tan(phi) + tan(theta)**2 + tan(phi)**2)))))**2)


with open('precision_table_2km_0.3515deg.txt', 'w') as f:
    for v_z in range(v_a // 10, 5 * v_a, v_a // 10):
        for v_y in range(v_a // 10, 5 * v_a, v_a // 10):
            for v_x in range(-5 * v_a, 5 * v_a, v_a // 10):
                try:
                    theta, phi, psi = convert_pos_to_angle(v_x, v_y, v_z, v_a)
                    pos = '{} {} {} {}\n'.format(
                        v_x, v_y, v_z, calculate(theta, phi, psi))
                    print(pos)
                    f.write(pos)
                except ZeroDivisionError:
                    continue

'''
print('{} {} {} => {} {} {}'.format(1000, 1000, 100,
      *convert_pos_to_angle(1000, 1000, 100, 2000)))


print()

'''
