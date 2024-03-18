#!/usr/bin/env python3

# imports
import rospy
import random
from ar_week8_test.msg import cubic_traj_params, cubic_traj_coeffs
from ar_week8_test.srv import compute_cubic_traj

def callback(data):
    # calling service and waiting until it is available
    rospy.wait_for_service("compute_cubic_traj")

    try:
        # using the handle as a function and passing the points retrieved
        coeffients_response = compute_traj_service(data.p0,data.pf,data.v0,data.vf,data.t0,data.tf)

        # creating the coeffs object
        # unpacking response to the object
        coeffs = cubic_traj_coeffs()
        coeffs.a0 = coeffients_response.a0
        coeffs.a1 = coeffients_response.a1
        coeffs.a2 = coeffients_response.a2
        coeffs.a3 = coeffients_response.a3
        coeffs.t0 = data.t0
        coeffs.tf = data.tf

        # publish the values for the coefficients and time
        coeff_pub.publish(coeffs)
        
        # output in terminal to know which stage reached
        rospy.loginfo("Coefficients Published")

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def cubic_traj_planner():
    # creating node
    rospy.init_node('cubic_traj_planner', anonymous=True)
    # subscribing to the topic Points of type cubic_traj_params (points from generator.py file)
    rospy.Subscriber("Points", cubic_traj_params, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        # publisher created globally to prevent repeated overheads
        # create publisher to send coefficients to cubic_traj_coeffs topic
        coeff_pub = rospy.Publisher("Coefficients", cubic_traj_coeffs, queue_size=10)
        # handle for calling service
        compute_traj_service = rospy.ServiceProxy("compute_cubic_traj", compute_cubic_traj)

        cubic_traj_planner()
        
    except rospy.ROSInterruptException:
        pass