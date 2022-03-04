#!/usr/bin/env python
import rospy
from turtlesim.srv import Spawn

def spawn(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        spawnTurtle = rospy.ServiceProxy('/spawn', Spawn)
        # spawnTurtle.
        spawnRes = spawnTurtle(x, y, ang, 'turtle2')
    except rospy.ServiceException as e:
        print(str(e))
        
if __name__ == "__main__":
    spawn(5,5,0)