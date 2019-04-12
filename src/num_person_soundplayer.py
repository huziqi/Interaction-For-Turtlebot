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
    if data.data=="0":
        msg="there is no person"
    else:
        msg="i see "+data.data+"person"
    soundhandle.say(msg)
    sleep(5)
    print "say the words !!!!!!!"


if __name__=='__main__':
    rospy.init_node('soundplay_test',anonymous=True)
    voice = rospy.get_param("~voice", "voice_don_diphone")
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.Subscriber("chatter", String, callback)
    soundhandle=SoundClient()
    rate=rospy.Rate(10)

    rospy.spin()
