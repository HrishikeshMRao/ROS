# ROS
#!/usr/bin/env 
import rospy
from std_msgs.msg import Int16
S=1
def callback1(N):
 A=N            
 rospy.loginfo(N)
 return(N)
def callback2(M):
 B=M   
 rospy.loginfo(M)
 rospy.loginfo(A+B) 
 return(M)           
rospy.init_node('emitter', anonymous=True)
rub = rospy.Publisher('incrementB', int, queue_size=10)
pub = rospy.Publisher('incrementA', int, queue_size=10)
rospy.Subscriber("incrementA", int, callback1)
rospy.Subscriber("incrementB", int, callback2)
rate = rospy.Rate(10) 
while not rospy.is_shutdown():
    A=A+S
    B=B+S
    pub.publish(A)
    rub.publish(B)
    rate.sleep()
