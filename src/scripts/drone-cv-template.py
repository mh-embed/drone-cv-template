#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16, Float32, String, Bool
import cv2

# GLOBAL VARIABLES
CV_NODE_UID = "TEMPLATE"            # Change This to Whatever You are Provided
CV_RUNNING = False
CV_RATE = 30


# Placeholders
roll = 0.0
pitch = 0.0
yaw = 0.0


# Function to Initialize the node
def init_cv():
    return

# Function to restart CV
def restart_cv():
    return

# Function to pause CV
def pause_cv():
    return


# DO NOT CHANGE THIS BIT
# The Main ROS Controller Needs to be able to Start and Pause 
# your specific ROS instance. 

# Selector Bit Pauses or Restarts Your CV Workflow
def selector_bit_receiver(data):
    if CV_RUNNING != data:
        CV_RUNNING = data
        if not CV_RUNNING:
            pause_cv()
        else:
            restart_cv()



# Main Driver of CV
def main():

    # Initialize the Node
    rospy.init_node('cv'+CV_NODE_UID)

    # Setup Publishing
    ## TBD, Placeholder Publishers and Subscribers
    cv_roll_pub = rospy.Publisher('cv_roll_' + CV_NODE_UID, Float32, queue_size=10)
    cv_pitch_pub = rospy.Publisher('cv_pitch_' + CV_NODE_UID, Float32, queue_size=10)
    cv_yaw_pub = rospy.Publisher('cv_yaw_' + CV_NODE_UID, Float32, queue_size=10)

    # Setup Subscribing
    # Setup Selector Bit 
    rospy.Subscriber('cv_selector/'+CV_NODE_UID, Bool, selector_bit_receiver)

    # Initialize Your CV Program
    init_cv()
    rate = rospy.Rate(CV_RATE)       # All CV Programs run at 30hz
    
    while not rospy.is_shutdown():

        # ------------
        # Your Code May Start Here
        # ------------

        if CV_RUNNING:
            i = 0           # Dummy


        # ------------
        # Remember to publish what you want to publish.
        # ------------

            cv_roll_pub.publish(roll)
        
        # Make sure your node runs at the proper frequency
        rate.sleep()


if __name__ == '__main__':
    main()
