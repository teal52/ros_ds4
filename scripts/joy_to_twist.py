#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def joy_to_twist(msg , twist_pub):
    L_horizontal = msg.axes[0]
    L_vertical = msg.axes[1]
    circle = msg.buttons[13]
    velocity = [L_horizontal*(1+circle),L_vertical*(1+circle)]

    t = Twist()

    t.angular.z, t.linear.x = velocity

    twist_pub.publish(t)


if __name__ == '__main__':
    rospy.init_node('joy_to_twist')
    twist_pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1)

    rospy.Subscriber('/joy',Joy,joy_to_twist,twist_pub)

    rospy.spin()
