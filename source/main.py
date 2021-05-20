from math import sin, cos, sqrt, pow, radians
import time
from typing import Tuple
import traceback


def calc_position(a: float, theta: float, phi: float, gamma: float) -> Tuple(float, float, float):
    """
    Calculate the position of satellite by given parameters.
    
    parameters:
    a: a distance between the origin and the beacon (unit: m)
    theta: an angle between a line SA and the direction of gravity (unit: deg)
    phi: an angle between a line SB and the direction of gravity (unit: deg)
    gamma: an angle between a line SA and SB (unit: deg)
    
    (S means the point of satellite, A the point of a beacon, and B the point of the other beacon)
    
    return:
    x, y, z: the position of satellite (unit: m)
    
    """
    
    r_theta = radians(theta)
    r_phi = radians(phi)
    r_gamma = radians(gamma)
    
    x: float
    y: float
    z: float
    
    A = pow(cos(r_theta), 2) + pow(cos(r_phi), 2) - 2 * cos(r_theta) * cos(r_phi) * cos(r_gamma)
    
    x = (pow(cos(r_phi), 2) - pow(cos(r_theta), 2)) * a / A
    
    y = 2 * a * cos(r_theta) * cos(r_phi) * sqrt(pow(sin(r_theta), 2) - pow(cos(r_phi), 2) - pow(cos(r_gamma), 2) + 2 * cos(r_theta) * cos(r_phi) * cos(r_gamma)) / A
    
    z = 2 * a * cos(r_theta) * cos(r_phi) / sqrt(A)
    
    
    return x, y, z



def calc_velocity(x: float, y: float, z: float, new_x: float, new_y: float, new_z: float, time_duration: float) -> Tuple(float, float, float):
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
a = 2000


def run():
    
    x, y, z = 0, 0, 0
    clock: float = time.perf_counter()
    
    try:
        while True:
            theta, phi, gamma = get_angles_from_sensors() # TODO: implement
            
            
            # calculate the position
            new_x, new_y, new_z = calc_position(a, theta, phi, gamma)
            
            
            # if the duration between observations is less than 1ms, wait until 1ms passes
            new_clock = time.perf_counter()
            duration = new_clock - clock
            
            if duration < 0.001:
                time.sleep(0.001 - duration)
                duration = time.perf_counter() - clock
            
            clock = new_clock
            
            
            # calculate the velocity
            vx, vy, yz = calc_velocity(x, y, z, new_x, new_y, new_z, duration)
            
            
            do_some_actions(x, y, z, vx, vy, yz) # TODO: implement
            
            x, y, z = new_x, new_y, new_z
    
    except:
        # do some cleanup actions
        traceback.format_exc()



if __name__ == '__main__':
    run()
