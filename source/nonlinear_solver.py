from math import cos, sqrt, tan, radians
from scipy import optimize
import time


def generate_func(theta, phi, psi, alpha, beta, a):
    theta = radians(theta)
    phi = radians(phi)
    psi = radians(psi)
    alpha = radians(alpha)
    beta = radians(beta)

    def func(x):
        return [((x[0]-a)*tan(alpha) + x[1]*tan(beta) - x[2]) / (sqrt(1 + tan(alpha)**2 + tan(beta)**2) * sqrt((x[0]-a)**2 + x[1]**2 + x[2]**2)) + cos(theta),
                ((x[0]+a)*tan(alpha) + x[1]*tan(beta) - x[2]) / (sqrt(1 + tan(alpha) **
                                                                      2 + tan(beta)**2) * sqrt((x[0]+a)**2 + x[1]**2 + x[2]**2)) + cos(phi),
                ((x[0]*tan(beta)+x[1])**2 + (x[2]*tan(alpha)+x[0])**2 - a**2 + (x[1]*tan(alpha)-x[0]*tan(beta))**2 - a**2*tan(beta)**2) / (sqrt((x[2]*tan(beta)+x[1])**2 + (x[2]*tan(alpha)+x[0]-a)**2 + (x[1]*tan(alpha)-(x[0]-a)*tan(beta))**2) * sqrt((x[2]*tan(beta)+x[1])**2 + (x[2]*tan(alpha)+x[0]+a)**2 + (x[1]*tan(alpha)-(x[0]+a)*tan(beta))**2)) - cos(psi)]
    return func


# (x, y, z) = (1000, 1000, 1000), alpha = beta = 10[deg] における連立非線形方程式の解法
theta, phi, psi = 55.93066279947788, 85.05422147195885, 105.63176923346151  # degree
a = 2000
alpha, beta = 10, 10  # degree

root_set = set()

initial_time = time.time()
for init_x in range(-10000, 10000, 1000):
    for init_y in range(-10000, 10000, 1000):
        for init_z in range(0, 10000, 1000):
            if (init_x, init_y, init_z) == (a, 0, 0) or (init_x, init_y, init_z) == (-a, 0, 0):
                continue

            result = optimize.root(generate_func(
                theta, phi, psi, alpha, beta, a), [init_x, init_y, init_z], method='broyden1', options={
                    "maxiter": 30
            })
            if(result['success']):
                root_set.add(tuple([round(n) for n in result['x'].tolist()]))
                if len(root_set) == 2:
                    break
        else:
            continue
        break
    else:
        continue
    break


final_time = time.time()


print(root_set)
print('Time:', final_time - initial_time)
