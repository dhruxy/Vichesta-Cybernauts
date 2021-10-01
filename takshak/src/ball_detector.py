#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('my_ball_detector')
import sys
import rospy
import cv2
import numpy as np
import message_filters
from std_msgs.msg import String
from std_msgs.msg import Int16
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class my_ball_detector:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.callback)
    self.pub = rospy.Publisher('/my_ball_detector/balls', Int16, queue_size=1)	

  def callback(self, rgb_data):
    
    try:
      img = self.bridge.imgmsg_to_cv2(rgb_data, "bgr8")
      # cv2.imwrite('img.jpg',img)
      # purple = (166, 143, 0, 167, 150, 255)
      # img = self.image_sub
      # lowHue = 166
      # lowSat = 143
      # lowVal = 0
      # highHue = 167
      # highSat = 150
      # highVal = 255
      # frameHSV = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2HSV)
      # colorLow = np.array([lowHue,lowSat,lowVal])
      # colorHigh = np.array([highHue,highSat,highVal])
      # mask = cv2.inRange(frameHSV, colorLow, colorHigh)
      # im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      # cv2.drawContours(img, contours, -1, (0,255,0), 3)
      count = 0
      hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      # Tunable parameters: Lower and upper bounds of yellow color of ball
      purpleLower = (166, 143, 0)
      purpleUpper = (167, 150, 255)
      mask = cv2.inRange(hsv, purpleLower, purpleUpper)
      contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      black_img = np.zeros(img.shape, 'uint8')
      for c in contours:
        area = cv2.contourArea(c)
        if area>200:
          count = count+1
        # ((x,y), radius) = cv2.minEnclosingCircle(c)
        # if (area > 5000):
        #   cv2.drawContours(img, [c], -1, (255,0,255), 2)
        #   cx, cy = self.get_contour_center(c)
        #   cv2.circle(img, (cx,cy), (int)(radius), (0,255,255), 3)
        #   cv2.circle(black_img, (cx,cy), (int)(radius), (0,255,255), 3)
        #   cv2.circle(black_img, (cx,cy), 5, (150,0,255), -1)
        print("Area: ", area)
      # cv2.imshow("Ball Tracking", img)
      # cv2.imshow("Black Background Tracking", black_img)


      # ball_cascade = cv2.CascadeClassifier('/home/bloisi/catkin_ws/src/ros_ball_detector/haarcascade/bottom_cascade.xml')
      # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      # balls = ball_cascade.detectMultiScale(gray, 1.2, 10)
      # for (x,y,w,h) in balls:
      #   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      #   roi_gray = gray[y:y+h, x:x+w]
      #   roi_color = img[y:y+h, x:x+w]
            
    except CvBridgeError as e:
      print(e)

    #convert opencv format back to ros format and publish result
    try:
      balls_message = self.bridge.cv2_to_imgmsg(img, "bgr8")
      print(count)
      self.pub.publish(count)
    except CvBridgeError as e:
    	print(e)
    

def main(args):
  rospy.init_node('ros_ball_node', anonymous=True)
  fd = my_ball_detector()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
