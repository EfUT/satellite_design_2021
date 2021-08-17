from math import degrees, tan, acos, pi, sqrt
from typing import NoReturn


class PosData():
    def __init__(self, x: float, y: float, z: float, theta: float, phi: float, psi: float, alpha: float, beta: float, a: float) -> None:
        self.pos: tuple[float, float, float] = (x, y, z)
        self.angle: tuple[float, float, float] = (theta, phi, psi)
        self.grad: tuple[float, float] = (alpha, beta)
        self.a: float = a

    @staticmethod
    def sample_complete_data(x: float, y: float, z: float, alpha: float, beta: float, a: float) -> 'PosData':
        cos_theta = -((x-a)*tan(alpha) + y*tan(beta) - z) \
            / (sqrt(1 + tan(alpha)**2 + tan(beta)**2)
               * sqrt((x-a)**2 + y**2 + z**2))
        cos_phi = -((x+a)*tan(alpha) + y*tan(beta) - z) \
            / (sqrt(1 + tan(alpha) ** 2 + tan(beta)**2)
               * sqrt((x+a)**2 + y**2 + z**2))
        cos_psi = ((x*tan(beta)+y)**2 + (z*tan(alpha)+x)**2 - a**2
                   + (y*tan(alpha)-x*tan(beta))**2 - a**2*tan(beta)**2) \
            / (sqrt((z*tan(beta)+y)**2 + (z*tan(alpha)+x-a)**2
                    + (y*tan(alpha)-(x-a)*tan(beta))**2)
               * sqrt((z*tan(beta)+y)**2 + (z*tan(alpha)+x+a)**2
                      + (y*tan(alpha)-(x+a)*tan(beta))**2))

        theta = acos(cos_theta)
        phi = acos(cos_phi)
        psi = acos(cos_psi)

        if y + tan(beta) * z >= 0:
            psi = 2 * pi - psi

        theta = degrees(theta)
        phi = degrees(phi)
        psi = degrees(psi)

        return PosData(x, y, z, theta, phi, psi, alpha, beta, a)
