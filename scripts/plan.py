#!/usr/bin/env python

"""
    arm.py - move by the input coor

"""

import rospy
import math
from std_msgs.msg import String
from std_msgs.msg import Float64





def calculate(x,y):
	theta2=math.acos((x*x+y*y-0.145*0.145-0.15*0.15)/(2*0.145*0.15))
	A=0.145+0.15*math.cos(theta2)
	B=0.15*math.sin(theta2)
	theta1=math.acos(x/(math.sqrt(A*A+B*B)))-math.atan2(B,A)
	return theta1,theta2

if __name__=="__main__":
	rospy.init_node('arm')
	joint1 = rospy.Publisher('/shoulder_controller/command',Float64,queue_size=15)
	joint2 = rospy.Publisher('/elbow_controller/command',Float64,queue_size=15)
	pos1 = Float64()
	pos2 = Float64()
	x=input()
	y=input()
	pos1,pos2=calculate(x,y)
	while(1):
		joint1.publish(pos1)
		joint2.publish(pos2)
	print pos1
	print pos2

