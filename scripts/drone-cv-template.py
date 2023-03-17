#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16, Float32, String, Bool
import cv2

# GLOBAL VARIABLES
CV_NODE_UID = "TEMPLATE"            # Change This to Whatever You are Provided
CV_RUNNING = False
CV_RATE = 30


# Placeholders
self.roll = 0.0
self.pitch = 0.0
self.yaw = 0.0

# Function to Initialize the node
def init_cv(self):
    return

# Function to restart CV
def restart_cv(self):
    return

# Function to pause CV
def pause_cv(self):
    return


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
    cv_roll_pub = rospy.Publisher('cv-roll-' + CV_NODE_UID, Float32, queue_size=10)
    cv_pitch_pub = rospy.Publisher('cv-pitch-' + CV_NODE_UID, Float32, queue_size=10)
    cv_yaw_pub = rospy.Publisher('cv-yaw-' + CV_NODE_UID, Float32, queue_size=10)

    # Setup Subscribing
    # Setup Selector Bit 
    rospy.Subscriber('cv-selector-'+CV_NODE_UID, Bool, selector_bit_receiver)

    # Setup Spin Rate
    rate = rospy.Rate(CV_RATE)       # All CV Programs run at 30hz

    # Initialize CV
    init_cv()




    
    while not rospy.is_shutdown():

        # Your Code May Start Here



        # Remember to publish what you want to publish.
        cv_roll_pub.publish(roll)
        rate.sleep()


if __name__ == '__main__':
    main()
