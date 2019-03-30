#!/usr/bin/env python

import rospy, os, sys 
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

def sleep(t):
    try:
        rospy.sleep(t)
    except:
        pass


if __name__=='__main__':
    rospy.init_node('soundplay_test',anonymous=True)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    soundhandle=SoundClient()
    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        hello_str="hello"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


    rospy.sleep(1)

    soundhandle.stopAll()

