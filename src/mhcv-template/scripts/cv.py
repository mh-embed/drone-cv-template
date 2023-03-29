#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16, Float32, Bool
import cv2

CV_RATE = 30

class CV_Node:

    # GLOBAL CONSANTS
    CV_NODE_UID = "TEMPLATE"            # Change This to Whatever You are Provided
    CV_RUNNING = False
    
    def __init__(self):
        # Placeholders
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

        # Initialize the Node
        rospy.init_node('cv'+self.CV_NODE_UID)

        self.register_subs()
        self.register_pubs()

    def register_subs(self):
        # Setup Subscribing
        # Setup Selector Bit 
        rospy.Subscriber('cv_selector/'+self.CV_NODE_UID, Bool, self.selector_bit_receiver)

    def register_pubs(self):
        # Setup Publishing
        ## TBD, Placeholder Publishers and Subscribers
        self.roll_pub = rospy.Publisher('cv_roll/' + self.CV_NODE_UID, Float32, queue_size=10)
        self.pitch_pub = rospy.Publisher('cv_pitch/' + self.CV_NODE_UID, Float32, queue_size=10)
        self.yaw_pub = rospy.Publisher('cv_yaw/' + self.CV_NODE_UID, Float32, queue_size=10)

    def pub_all(self):
        self.roll_pub.publish(self.roll)
        self.pitch_pub.publish(self.pitch)
        self.yaw_pub.publish(self.yaw)

    def is_running(self):
        return self.CV_RUNNING

    # Function to Initialize the node
    def init_cv(self):
        return

    # Function to restart CV
    def restart_cv(self):
        return

    # Function to pause CV
    def pause_cv(self):
        return

    # DO NOT CHANGE THIS BIT
    # The Main ROS Controller Needs to be able to Start and Pause 
    # your specific ROS instance. 

    # Selector Bit Pauses or Restarts Your CV Workflow
    def selector_bit_receiver(self, data):
        if self.CV_RUNNING != data:
            self.CV_RUNNING = data
            if not self.CV_RUNNING:
                self.pause_cv()
            else:
                self.restart_cv()



# Main Driver of CV
def main():    
    # Initialize a CV Node
    node = CV_Node()
    
    rate = rospy.Rate(CV_RATE)       # All CV Programs run at 30hz

    # Start CV
    node.init_cv()
    
    while not rospy.is_shutdown():

        # Subscribing is automatic, nothing needs to be done

        # ------------
        # Your Code May Start Here
        # ------------

        if node.is_running():
            print("CV Running!")           # Dummy
        
        else:
            print("CV Not Running!")           # Dummy

        # ------------
        # Remember to publish what you want to publish.
        # ------------

            node.pub_all()
        
        # Make sure your node runs at the proper frequency
        rate.sleep()


if __name__ == '__main__':
    main()
