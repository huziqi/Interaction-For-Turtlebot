#!/usr/bin/env python

import cv2
import dlib
from skimage import io
import rospy, os, sys 
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

pub = rospy.Publisher('chatter', String, queue_size=10)

def face_detector():
    detector=dlib.get_frontal_face_detector()
    cap=cv2.VideoCapture(0)
    cap.set(3,960)
    while cap.isOpened():
        flag,img_rd=cap.read()
        k=cv2.waitKey(1)
        img_gray=cv2.cvtColor(img_rd,cv2.COLOR_RGB2GRAY)
        faces=detector(img_gray,0)

        if k==ord('q'):
            break
        else:
            if len(faces)!=0:
                faces_start_width=0;
                for face in faces:
                    # draw square
                    cv2.rectangle(img_rd, tuple([face.left(), face.top()]), tuple([face.right(), face.bottom()]),
                                (0, 255, 255), 2)

                    height = face.bottom() - face.top()
                    width = face.right() - face.left()
        pub.publish(str(len(faces)))

        cv2.namedWindow("camera", 1)
        cv2.imshow("camera", img_rd)

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    rospy.init_node('face_detect',anonymous=True)
    rate=rospy.Rate(10)
    face_detector()
    # while not rospy.is_shutdown():
    #     hello_str="hello"
    #     rospy.loginfo(hello_str)
    #     pub.publish(hello_str)
    #     rate.sleep()