from pynput.keyboard import Key, Listener
import rospy
from geometry_msgs.msg import Twist 

def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

def on_press(key):
    if key == Key.space:
        pubVel(0,1,2.2)

def on_release(key):
    if key == Key.esc:
        return False

if __name__ == '__main__':
    pubVel(0,0,0.1)
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except rospy.ROSInterruptException:
        pass