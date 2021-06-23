import sympy as sp
from sympy import diff, atan, acos, sqrt, Abs
from math import pi



th = sp.Symbol('θ')
ph = sp.Symbol('φ')
ps = sp.Symbol('Ψ')

dth = sp.Symbol('Δθ')
dph = sp.Symbol('Δφ')
dps = sp.Symbol('ΔΨ')

x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')

a = sp.Symbol('a')



fth = atan(sqrt((x + a) ** 2 + y ** 2) / z)

fph = atan(sqrt((x - a) ** 2 + y ** 2) / z)

fps = acos((x ** 2 + y ** 2 - a ** 2) / sqrt((x ** 2 + y ** 2 + a ** 2) ** 2 - 4 * a ** 2 * x ** 2))



dfthdx = diff(fth, x)
dxdfth = 1 / dfthdx

dfthdy = diff(fth, y)
dydfth = 1 / dfthdy

dfthdz = diff(fth, z)
dzdfth = 1 / dfthdz


dfphdx = diff(fph, x)
dxdfph = 1 / dfphdx

dfphdy = diff(fph, y)
dydfph = 1 / dfphdy

dfphdz = diff(fph, z)
dzdfph = 1 / dfphdz


dfpsdx = diff(fps, x)
dxdfps = 1 / dfpsdx

dfpsdy = diff(fps, y)
dydfps = 1 / dfpsdy

dzdfps = 0

eval_func = sqrt((Abs(dxdfth * dth) + Abs(dxdfph * dph) + Abs(dxdfps * dps)) ** 2
                 + (Abs(dydfth * dth) + Abs(dydfph * dph) + Abs(dydfps * dps)) ** 2
                 + (Abs(dzdfth * dth) + Abs(dzdfph * dph) + Abs(dzdfps * dps)) ** 2)

v_dth = pi / 1800
v_dph = pi / 1800
v_dps = pi / 1800

v_a = 10000

original_eval_func = eval_func.subs([(dth, v_dth), (dph, v_dph), (dps, v_dps), (a, v_a)])

with open('precision_table.txt', 'w') as f:
        for v_z in range(1000, 2 * v_a, 1000):
            for v_y in range(1000, 2 * v_a, 1000):
                for v_x in range(-v_a * 2, v_a * 2, 1000):
                    try:
                        pos = '{} {} {} {}\n'.format(v_x, v_y, v_z, original_eval_func.subs([(x, v_x), (y, v_y), (z, v_z)]).evalf())
                        print(pos)
                        f.write(pos)
                    except ZeroDivisionError:
                        continue




