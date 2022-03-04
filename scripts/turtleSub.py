#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo(data.x)
    
def pose():
    rospy.init_node('poseSub', anonymous=False)
    rospy.Subscriber("turtle1/pose", Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    pose()