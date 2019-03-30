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

def callback(data):
    # s=soundhandle.voiceSound(data)
    # s.play()
    soundhandle.say(data.data)
    sleep(3)
    print "say the words !!!!!!!"


if __name__=='__main__':
    rospy.init_node('soundplay_test',anonymous=True)
    voice = rospy.get_param("~voice", "voice_don_diphone")
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.Subscriber("chatter", String, callback)
    soundhandle=SoundClient()
    rate=rospy.Rate(10)
    
    # while not rospy.is_shutdown():
    #     hello_str="hello jeffery"
    #     rospy.loginfo(hello_str)
    #     pub.publish(hello_str)
    #     rate.sleep()
    rospy.spin()

    # rospy.sleep(1)

    #soundhandle.stopAll()

    # s3 = soundhandle.voiceSound("Testing the new A P I")
    # s3.repeat()
    # sleep(3)