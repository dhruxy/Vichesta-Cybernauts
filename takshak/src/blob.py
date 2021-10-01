#!/usr/bin/env python3
import rospy
import actionlib
import roslib
roslib.load_manifest('takshak')
from cmvision.msg import Blobs

def callback(data):
 rospy.loginfo(data.blob_count)
 
rospy.init_node('listener', anonymous=True)
rospy.Subscriber("/blobs", Blobs, callback)
rospy.spin()
