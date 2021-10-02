import argparse
import imutils
import cv2
import cv2.aruco as aruco
import numpy as np
import sys


num_balls = 3

lowerr1 = np.array([100,150,0])
upperr1 = np.array([130,255,255])


lowerr2 = np.array([80,0,0])
upperr2 = np.array([100,50,100])


lowerr3 = np.array([0,0,50])
upperr3 = np.array([10,100,150])


lowerr4 = np.array([10,100,0])
upperr4 = np.array([50,255,100])


lowerr5 = np.array([0,50,50])
upperr5 = np.array([10,255,255])



def masking(img, lower, upper):  
      ## blurring the image - no_need  

    mask = cv2.inRange(img, lower, upper)
    return mask 

def findArucoMarkers(img, markerSize = 6, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arucoDict = aruco.Dictionary_get(cv2.aruco.DICT_5X5_100)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
    if ids is not None:
        for i, corners in zip(ids, bboxs):
            if i == num_balls:
                print('ID: {}; bbox: {}'.format(i, corners))
                req_x = (corners[0][0][0] + corners[0][1][0])/2
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                mask = masking(hsv, lowerr1, upperr1)
                countors, garbage = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
                if(len(countors) > 0):
                    cv2.imshow("mask_blue", mask)
                    countors = sorted(countors, key=lambda x:cv2.contourArea(x), reverse = True)
                    if cv2.contourArea(countors[0]) > 200:
                        M = cv2.moments(countors[0])
                        if M['m00'] != 0:
                            cx = int(M['m10']/M['m00'])
                            if abs(cx - req_x)<6:
                                print("blue detected for num balls = 1")
                                return lowerr1, upperr1

                mask = masking(img, lowerr2, upperr2)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                countors, garbage = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
                if(len(countors) > 0):
                    cv2.imshow("mask_purple", mask)
                    countors = sorted(countors, key=lambda x:cv2.contourArea(x), reverse = True)
                    if cv2.contourArea(countors[0]) > 200:
                        M = cv2.moments(countors[0])
                        if M['m00'] != 0:
                            cx = int(M['m10']/M['m00'])
                            if abs(cx - req_x)<6:
                                print("purple detected for num balls = 2")
                                return lowerr2, upperr2
                
                mask = masking(img, lowerr3, upperr3)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                countors, garbage = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
                if(len(countors) > 0):
                    cv2.imshow("mask_red", mask)
                    countors = sorted(countors, key=lambda x:cv2.contourArea(x), reverse = True)
                    if cv2.contourArea(countors[0]) > 200:
                        M = cv2.moments(countors[0])
                        if M['m00'] != 0:
                            cx = int(M['m10']/M['m00'])
                            if abs(cx - req_x)<6:
                                print("red detected for num balls = 0")
                                return lowerr3, upperr3

                mask = masking(img, lowerr4, upperr4)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                countors, garbage = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
                if(len(countors) > 0):
                    cv2.imshow("mask_green", mask)
                    countors = sorted(countors, key=lambda x:cv2.contourArea(x), reverse = True)
                    if cv2.contourArea(countors[0]) > 200:
                        M = cv2.moments(countors[0])
                        if M['m00'] != 0:
                            cx = int(M['m10']/M['m00'])
                            if abs(cx - req_x)<6:
                                print("green detected for num balls = 4")
                                return lowerr4, upperr4

                mask = masking(img, lowerr5, upperr5)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                countors, garbage = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
                if(len(countors) > 0):
                    cv2.imshow("mask_yellow", mask)
                    countors = sorted(countors, key=lambda x:cv2.contourArea(x), reverse = True)
                    if cv2.contourArea(countors[0]) > 200:
                        M = cv2.moments(countors[0])
                        if M['m00'] != 0:
                            cx = int(M['m10']/M['m00'])
                            if abs(cx - req_x)<6:
                                print(" Yellow detected for num balls = 3")
                                return lowerr5, upperr5

                print("none detected")
                return 0,0

    


img = cv2.imread('~/catkin_ws/img4.jpg')
lowerf, upperf = findArucoMarkers(img)
print(lowerf,upperf)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

