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

def getContours(img, imgblur):
    x = y = w = h = 0 
    cont,a = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for con in cont:
        area = cv2.contourArea(con)
        ep = 0.048 * cv2.arcLength(con, True) - 0.7
        app = cv2.approxPolyDP(con, ep, True)
        x, y, w, h = cv2.boundingRect(app)
        if area>100:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            break
    return x,y,w,h

def color(lower, upper, lower2, upper2, img):

    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(imghsv, lower, upper)
    mask2 = cv2.inRange(imghsv, lower2, upper2)
    mask = mask1 + mask2
    kern1 = np.ones((5, 5), np.uint8)
    kern2 = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kern2)
    mask = cv2.dilate(mask, kern1)
    imggreen = cv2.bitwise_and(img, img, mask)
    imggreen[mask == 0] = (255, 255, 255)
    imgblur = cv2.GaussianBlur(imggreen, (3, 3), 0)
    x,y,w,h = getContours(mask, imgblur)
    return x+w/2
    
def findArucoMarkers(img, markerSize = 6, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arucoDict = aruco.Dictionary_get(cv2.aruco.DICT_5X5_100)
    arucoParam = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    aruco.drawDetectedMarkers(img, corners)
    if ids is not None:
#        print(ids)
#        print(corners[0][0][2][0])
        aid=[]
        ax=[]
        for i in range(5):
            aid.append(ids[i][0])
            orx=(corners[i][0][0][0]+corners[i][0][2][0])/2
            ax.append(orx)
        print(aid)
        print(ax)
        
    rx=color(np.array([0,150,0]),np.array([3,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    yx=color(np.array([24,238,112]),np.array([179,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    bx=color(np.array([90,127,85]),np.array([126,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    gx=color(np.array([38,207,98]),np.array([100,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    px=color(np.array([131,139,88]),np.array([164,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    mp=[]
    mindi=999
    for i in range(5):
       z=abs(rx-ax[i])
       if z<mindi:
          j=i
          mindi=z
    mp.insert(j,'red')
    mindi=999
    for i in range(5):
       z=abs(yx-ax[i])
       if z<mindi:
          mindi=z
          j=i
    mp.insert(j,'yellow')
    mindi=999
    for i in range(5):
       z=abs(bx-ax[i])
       if z<mindi:
          mindi=z
          j=i
    mp.insert(j,'blue')
    mindi=999
    for i in range(5):
       z=abs(gx-ax[i])
       if z<mindi:
          mindi=z
          j=i
    mp.insert(j,'green')
    mindi=999
    for i in range(5):
       z=abs(px-ax[i])
       if z<mindi:
          mindi=z
          j=i
    mp.insert(j,'purple')
    print(mp)
    return aid,mp

img = cv2.imread('img3.jpg')
aid,mp=findArucoMarkers(img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
