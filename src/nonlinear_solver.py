from math import cos, sqrt, tan, radians
from scipy import optimize
import time

from src.sampling_complete_data import PosData


def _generate_func(data: PosData):
    theta = radians(data.angle[0])
    phi = radians(data.angle[1])
    psi = radians(data.angle[2])
    alpha = radians(data.grad[0])
    beta = radians(data.grad[2])
    a = data.a

    def func(x):
        return [((x[0]-a)*tan(alpha) + x[1]*tan(beta) - x[2])
                / (sqrt(1 + tan(alpha)**2 + tan(beta)**2)
                   * sqrt((x[0]-a)**2 + x[1]**2 + x[2]**2)) + cos(theta),
                ((x[0]+a)*tan(alpha) + x[1]*tan(beta) - x[2])
                / (sqrt(1 + tan(alpha) ** 2 + tan(beta)**2)
                   * sqrt((x[0]+a)**2 + x[1]**2 + x[2]**2)) + cos(phi),
                ((x[0]*tan(beta)+x[1])**2 + (x[2]*tan(alpha)+x[0])**2 - a**2
                 + (x[1]*tan(alpha)-x[0]*tan(beta))**2 - a**2*tan(beta)**2)
                / (sqrt((x[2]*tan(beta)+x[1])**2 + (x[2]*tan(alpha)+x[0]-a)**2
                        + (x[1]*tan(alpha)-(x[0]-a)*tan(beta))**2)
                   * sqrt((x[2]*tan(beta)+x[1])**2
                          + (x[2]*tan(alpha)+x[0]+a)**2
                          + (x[1]*tan(alpha)-(x[0]+a)*tan(beta))**2))
                - cos(psi)]
    return func


def solve_nonlin(data: PosData, includeWrong: bool = False):
    root_set = set()
    initial_time = time.time()

    for init_x in range(-10000, 10000, 1000):
        for init_y in range(-10000, 10000, 1000):
            for init_z in range(0, 10000, 1000):
                if any((init_x, init_y, init_z) == (data.a, 0, 0),
                       (init_x, init_y, init_z) == (-data.a, 0, 0)):
                    continue

                result = optimize.root(
                    _generate_func(data), [init_x, init_y, init_z],
                    method='broyden1',
                    options={
                        "maxiter": 30
                    })
                if(result['success']):
                    root_set.add(tuple([round(n)
                                 for n in result['x'].tolist()]))
                    if not includeWrong:
                        break
                    if len(root_set) == 2:
                        break
            else:
                continue
            break
        else:
            continue
        break

    final_time = time.time()

    return {
        "pos": root_set,
        "correct": data.pos in root_set,
        "time": final_time - initial_time,
    }
