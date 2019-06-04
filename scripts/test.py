#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

tasknum_pub=rospy.Publisher("/patient_reach",String,queue_size=10)

if __name__ == '__main__':
    rospy.init_node("test")
    
    content="1"
    tasknum_pub.publish(content)
    