#!/usr/bin/env python3

# imports
import rospy
import random
from ar_week8_test.msg import cubic_traj_params

# function for generating the points and publishing to the topic
def points_generator():
    # initializing node
    rospy.init_node("points_generator", anonymous=True)
    # 20 seconds = 0.05 Hz
    rate = rospy.Rate(0.05)

    # parameter object
    params = cubic_traj_params()
    
    while not rospy.is_shutdown():
        # initial position generated in range of -10 to 10
        params.p0 = random.uniform(-10,10)
        # final position generated in range of -10 to 10
        params.pf = random.uniform(-10,10)
        # initial velocity generated in range of -10 to 10
        params.v0 = random.uniform(-10,10)
        # final velocity generated in range of -10 to 10
        params.vf = random.uniform(-10,10)
        # initial time set to 0
        params.t0 = 0
        # generate random time step in range of 5 to 10
        dt = random.uniform(5,10)
        # final time is calculated by adding the initial time with the random var dt
        params.tf = params.t0 + dt

        # output in terminal to know which stage reached
        rospy.loginfo('Points Generated')
        pub.publish(params)
        rate.sleep()

if __name__ == '__main__':
    try:
        # creating publisher globally to prevent repeated overheads
        pub = rospy.Publisher("Points", cubic_traj_params, queue_size=10)
        # calling function defined above
        points_generator()

    except rospy.ROSInterruptException:
        pass

