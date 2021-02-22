#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from udm_tuto.msg import custom_msg

def talker():
    pub = rospy.Publisher('chatter', custom_msg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	message=custom_msg()
	message.header.stamp=rospy.Time.now()
	message.header.frame_id='hello'
	message.str.data='world'
	message.pose.linear.x=56
	message.pose.angular.x=64

        #hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
