from cmath import pi
import numpy as np

def move(self, r, u, n):
    ''' 
    Move Robot motion, with separated control and perturbation  inputs.

    In:
        r: robot pose        r = [x; y; alpha]
        u: control signal    u = [d_x; d_alpha]
        n: perturbation, additive to control signal

    Out: 
        ro = updated robot pose
        RO_r: Jacobian   d(ro) / d(r)
        RO_n: Jacobian   d(ro) / d(n)

        "EKF-SLAM A Very Quick Guide by Joan Sola" C.2.1 Robot Motion
    '''
    