#! /usr/bin/env python3

# imports
import rospy
import numpy as np
from ar_week8_test.srv import compute_cubic_traj, compute_cubic_trajResponse

def callback(data):

    # Using equation: a = M^-1 c
    # c = [p0,v0,pf,vf]

    c = np.array([[data.p0],[data.v0],[data.pf],[data.vf]])

    # M = [[1,  t0, t0^2,   t0^3], 
    #      [0,  1,  2t0,    3t0^2],
    #      [1,  tf, tf^2,   tf^3],
    #      [0,  1,  2tf,    3t0^2]]

    M = np.array([[1, data.t0, (data.t0)**2, (data.t0)**3],
                [0, 1, 2*data.t0, 3*((data.t0)**2)],
                [1, data.tf, (data.tf)**2, (data.tf)**3],
                [0, 1, 2*data.tf, 3*((data.tf)**2)]])
    
    # a = [a0,a1,a2,a3]
    a = np.linalg.solve(M, c)

    # output in terminal to know which stage reached
    rospy.loginfo("Coefficients a0, a1, a2, a3 Computed")
    return compute_cubic_trajResponse(a[0], a[1], a[2], a[3])
    
def compute_cubic_coeffs():
    # creating node for service
    rospy.init_node("computer_cubic_traj_Service", anonymous=True)
    service = rospy.Service("compute_cubic_traj", compute_cubic_traj, callback)
    rospy.spin()

if __name__ == "__main__":
    compute_cubic_coeffs()