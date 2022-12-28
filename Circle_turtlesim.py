#!/usr/bin/env 
import rospy
import time
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose

rospy.init_node('revolver')
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
twist = Twist()
V = 4.0
Z = 1.0
twist.linear.x = V 
twist.angular.z = Z
rate = rospy.Rate(10)
tim = rospy.get_time()
def calculator(Z):
    t = (2*3.14/Z)-0.75
    stptim = tim + t
    return stptim
cmp = calculator(Z)    
while not (tim >= cmp):
    tim = rospy.get_time()
    pub.publish(twist)
    rate.sleep()
