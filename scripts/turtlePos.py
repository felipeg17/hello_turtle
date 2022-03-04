#!/usr/bin/env python
import rospy
from turtlesim.srv import TeleportAbsolute
import argparse
def teleport(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
        print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type = float, default = 5.0)
    parser.add_argument('--y', type = float, default = 5.0)
    parser.add_argument('--ang', type = float, default = 0)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    teleport(args.x, args.y, args.ang)