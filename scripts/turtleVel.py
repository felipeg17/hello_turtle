#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 

def pubVel():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        vel.linear.x = 2
        vel.angular.z = 1
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        pubVel()
    except rospy.ROSInterruptException:
        pass