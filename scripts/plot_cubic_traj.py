#! /usr/bin/env python3

# imports
import rospy
import numpy as np
from std_msgs.msg import Float64
from ar_week8_test.msg import cubic_traj_coeffs

# method for calculating the position
def position(t, coefficients):
    # equation: p(t) = a0 + a1*t + a2*t^2 + a3*t^3
    return coefficients[0] + coefficients[1]*(t) + coefficients[2]*(t**2) + coefficients[3]*(t**3)

# method for calculating the velocity
def velocity(t, coefficients):
    # equation: v(t) = a1 + 2*a2*t + 3*a3*t^2
    return coefficients[1] + 2*coefficients[2]*t + 3*coefficients[3]*(t**2)

# method for calculating the acceleration
def acceleration(t, coefficients):
    # equation: alpha(t) = 2*a2 + 6*a3*t
    return 2*coefficients[2] + 6*coefficients[3]*t


def callback(data):
    coefficients = [data.a0, data.a1, data.a2, data.a3]
    times = [data.t0, data.tf]
   
    # time steps
    dt = (times[1]-times[0]) / 100

    for t in np.arange(0, times[1], dt):
        # publisher for position values
        pos = position(t, coefficients)
        position_pub.publish(pos)

        # publisher for velocity values
        vel = velocity(t, coefficients)
        velocity_pub.publish(vel)

        # publisher for acceleration values
        acc = acceleration(t, coefficients)
        acceleration_pub.publish(acc)

        rospy.sleep(dt)

    # output in terminal to know which stage reached
    rospy.loginfo('Position, velocity and acceleration published')

def plot_cubic_traj():
    # creating node
    rospy.init_node('plot_traj', anonymous=True)
    # subscribing to the topic Coefficients of type cubic_traj_coeffs
    rospy.Subscriber("Coefficients", cubic_traj_coeffs, callback)
    rospy.spin()

if __name__ == "__main__":
    # creating publishers globally to prevent redundant overheadds in the callbacks
    position_pub = rospy.Publisher("trajPos", Float64, queue_size=10)
    velocity_pub = rospy.Publisher("trajVel", Float64, queue_size=10)
    acceleration_pub = rospy.Publisher("trajAcc", Float64, queue_size=10)
    
    plot_cubic_traj()