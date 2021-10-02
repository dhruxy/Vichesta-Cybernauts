#!/usr/bin/env python3
import rospy
import actionlib
import roslib
roslib.load_manifest('takshak')
import sys
import cv2
import cv2.aruco as aruco
import numpy as np
from std_msgs.msg import Float64
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal
from cmvision.msg import Blobs

rospy.init_node("mynode")
navclient=actionlib.SimpleActionClient('move_base',MoveBaseAction)
navclient.wait_for_server()
goal=MoveBaseGoal()

def active_cb():
  rospy.loginfo("Goal being processed")
def feedback_cb(feedback):
#  rospy.loginfo("Current="+str(feedback))
  pass
def done_cb(status,result):
  if status==3:
     rospy.loginfo("Goal reached")
  elif status==2 or status==8:
     rospy.loginfo("Goal cancelled")
  elif status==4:
     rospy.loginfo("Goal aborted")

def getContours(img, imgblur):
    x = y = w = h = 0 
    cont, a = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
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

col=[]
def gatecolor(img):
 global col
 hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# light_blue = np.array([90,127,0])
# dark_blue = np.array([126,255,255])

# light_green = np.array([45,208,0])
# dark_green = np.array([179,255,255])

# light_purple= np.array([128,136,0])
# dark_purple= np.array([179,255,255])

# light_yellow = np.array([21,239,0])
# dark_yellow = np.array([179,255,255])

# light_red = np.array([0,150,0])
# dark_red = np.array([3,255,255])


 light_blue = np.array([88,173,50])
 dark_blue = np.array([124,255,255])

 light_green = np.array([30,214,0])
 dark_green = np.array([62,255,255])

 light_purple= np.array([131,121,59])
 dark_purple= np.array([151,255,255])

 light_yellow = np.array([0,245,92])
 dark_yellow = np.array([179,255,255])

 light_red = np.array([0,230,0])
 dark_red = np.array([5,255,255])

 try:
  mask = cv2.inRange(hsv, light_blue, dark_blue)
  output = cv2.bitwise_and(img,img, mask= mask)
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  c = max(contours, key = cv2.contourArea)
  cv2.drawContours(img, c, -1, (0, 255, 0), 3)
  M = cv2.moments(c)
  cX_blue = int(M["m10"] / M["m00"])
  cY_blue = int(M["m01"] / M["m00"])
  cv2.circle(img, (cX_blue,cY_blue), 5, (255, 255, 255), -1)
  #cv2.imshow("Color Detected", np.hstack((img,output)))


  mask = cv2.inRange(hsv, light_green, dark_green)
  output = cv2.bitwise_and(img,img, mask= mask)
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  c = max(contours, key = cv2.contourArea)
  cv2.drawContours(img, c, -1, (0, 255, 0), 3)
  M = cv2.moments(c)
  cX_green = int(M["m10"] / M["m00"])
  cY_green = int(M["m01"] / M["m00"])
  cv2.circle(img, (cX_green,cY_green), 5, (255, 255, 255), -1)
 # cv2.imshow("Color Detected", np.hstack((img,output)))


  mask = cv2.inRange(hsv, light_purple, dark_purple)
  output = cv2.bitwise_and(img,img, mask= mask)
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  c = max(contours, key = cv2.contourArea)
  cv2.drawContours(img, c, -1, (0, 255, 0), 3)
  M = cv2.moments(c)
  cX_purple = int(M["m10"] / M["m00"])
  cY_purple = int(M["m01"] / M["m00"])
  cv2.circle(img, (cX_purple,cY_purple), 5, (255, 255, 255), -1)
 #cv2.imshow("Color Detected", np.hstack((img,output)))


  mask = cv2.inRange(hsv, light_yellow, dark_yellow)
  output = cv2.bitwise_and(img,img, mask= mask)
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  c = max(contours, key = cv2.contourArea)
  cv2.drawContours(img, c, -1, (0, 255, 0), 3)
  M = cv2.moments(c)
  cX_yellow = int(M["m10"] / M["m00"])
  cY_yellow = int(M["m01"] / M["m00"])
  cv2.circle(img, (cX_yellow,cY_yellow), 5, (255, 255, 255), -1)
# cv2.imshow("Color Detected", np.hstack((img,output)))


  mask = cv2.inRange(hsv, light_red, dark_red)
  output = cv2.bitwise_and(img,img, mask= mask)
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  c = max(contours, key = cv2.contourArea)
  cv2.drawContours(img, c, -1, (0, 255, 0), 3)
  M = cv2.moments(c)
  cX_red = int(M["m10"] / M["m00"])
  cY_red = int(M["m01"] / M["m00"])
  cv2.circle(img, (cX_red,cY_red), 5, (255, 255, 255), -1)
 #cv2.imshow("Color Detected", np.hstack((img,output)))


  pos = np.array([cX_blue, cX_green, cX_purple, cX_yellow, cX_red])
  pos = np.sort(pos)
  for i in range(len(pos)):
        if pos[i]==cX_purple:
           col.append('purple')
        elif pos[i]==cX_green:
           col.append('green')
        elif pos[i]==cX_blue:
           col.append('blue')
        elif pos[i]==cX_yellow:
           col.append('yellow')
        else:
           col.append('red')
  col.reverse()
  print("Gate colors from left to right of world= ",col)
 except:
    col=['red','yellow','blue','green','purple']

def move(gx,gy,oz,ow):
 goal.target_pose.pose.position.x = gx
 goal.target_pose.pose.position.y = gy
 goal.target_pose.pose.orientation.z = oz
 goal.target_pose.pose.orientation.w = ow
 navclient.send_goal(goal,done_cb,active_cb,feedback_cb) 
 finished=navclient.wait_for_result()

 if not finished:
  rospy.logerr("Action server not avalaible")
  sys.exit()
 else:
  rospy.loginfo(navclient.get_result())


goal.target_pose.header.seq = 1
goal.target_pose.header.stamp = rospy.Time.now()
goal.target_pose.header.frame_id = "map"
goal.target_pose.pose.orientation.x = 0.0
goal.target_pose.pose.orientation.y = 0.0
count,count1,count2,count3=0,0,0,0
aid=[]

def findArucoMarkers(img, markerSize = 6, totalMarkers=250, draw=True):
    global aid,mp
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arucoDict = aruco.Dictionary_get(cv2.aruco.DICT_5X5_100)
    arucoParam = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    aruco.drawDetectedMarkers(img, corners)
    if ids is not None:
#        print(ids)
        if len(ids)!=5:
            return False
        aid=[]
        ax=[]
        for i in range(5):
            aid.append(ids[i][0])
            orx=(corners[i][0][0][0]+corners[i][0][2][0])/2
            ax.append(orx)
        print("Aruco ids= ",aid)
        print("Aruco x coordinates= ",ax)
        
    rx=color(np.array([0,150,0]),np.array([3,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    yx=color(np.array([24,238,112]),np.array([179,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    bx=color(np.array([90,127,85]),np.array([126,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    gx=color(np.array([38,207,98]),np.array([100,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    px=color(np.array([131,139,88]),np.array([164,255,255]),np.array([1,0,0]),np.array([0,0,0]),img)
    mp={}
    mindi=999
    for i in range(5):
       z=abs(rx-ax[i])
       if z<mindi:
          j=i
          mindi=z
    mp[aid[j]]="red"
    mindi=999
    for i in range(5):
       z=abs(yx-ax[i])
       if z<mindi:
          mindi=z
          j=i
    mp[aid[j]]="yellow"
    mindi=999
    for i in range(5):
       z=abs(bx-ax[i])
       if z<mindi:
          mindi=z
          j=i
    mp[aid[j]]='blue'
    mindi=999
    for i in range(5):
       z=abs(gx-ax[i])
       if z<mindi:
          mindi=z
          j=i
    mp[aid[j]]='green'
    mindi=999
    for i in range(5):
       z=abs(px-ax[i])
       if z<mindi:
          mindi=z
          j=i
    mp[aid[j]]='purple'
    print("Map of id vs color= ",mp)
    return True
    
def get_img(i):
   global count1,count2,count3,redx,redy,yellowx,yellowy,bluex,bluey,green
   bridge=CvBridge()
   data = rospy.wait_for_message("/camera/color/image_raw",Image)
   data = rospy.wait_for_message("/camera/color/image_raw",Image)
   data = rospy.wait_for_message("/camera/color/image_raw",Image)
   try:
     img = bridge.imgmsg_to_cv2(data, "bgr8")
     if i==1:
       blo=rospy.wait_for_message("/blobs",Blobs)
       count1=max(count1,blo.blob_count)
       print("Count1=",count1)
#     cv2.imwrite("img{}.jpg".format(j),img)
     elif i==2:
         blo=rospy.wait_for_message("/blobs",Blobs)
         count2=max(count2,blo.blob_count)
         print("Count2=",count2)
     elif i==0:
        t=findArucoMarkers(img)
        if t==False:
          data = rospy.wait_for_message("/camera/color/image_raw",Image)
          img = bridge.imgmsg_to_cv2(data, "bgr8")
          t=findArucoMarkers(img)
     elif i==4:
         gatecolor(img)
         cv2.imwrite("gates.jpg",img)
     elif i==3:
         blo=rospy.wait_for_message("/blobs",Blobs)
         count3=max(count3,blo.blob_count)
         print("Count3=",count3)
   except CvBridgeError as e:
      print(e)

c=0
def callback(data):
     global count3,c
     if data.blob_count>count3:
        c+=1
     else:
        c=0
     if c>10:
       count3=max(count3,data.blob_count)
       c=0
     print("Count3=",count3)
       
try:
    move(6.084538459777832,-4.636813163757324,-0.9997343077043511,0.02305024943252807)
    get_img(1)
    move(1.4062520265579224,-8.341598510742188,0.741779729145153,0.6706435964275984)
    get_img(1)
    move(-0.36798763275146484,-8.188644409179688, 0.999997709942646,0.0021401190302485695)
    get_img(2)
    move(-3.658727836608887,-4.558456134796143,-0.7087644218845909,0.7054452454093101)
    get_img(2)
    move(-10.380690574645996,-2.2751665115356445,0.5212666074192941,0.8533938856059256)
    get_img(0)
    move(1.9723916053771973,-0.35726332664489746,0.17674310097774856,0.9842570173774579)
    get_img(4)
    blo_sub=rospy.Subscriber("/blobs",Blobs,callback)
    move(1.389301061630249,-0.6601300239562988,0.621855439574967,0.7831320528946727)
#    get_img(3)
#    move(3.5313239097595215,0.8491373062133789,0.7159773738002765,0.6981234849265989)
#    get_img(3)
    move(5.929654769897461,4.787042331695557,-0.9999896192038987,0.004556477196423803)
#    get_img(3)
    move(5.921184062957764,7.6609578132629395,-0.9382660843857703,0.34591437508637096)
#    get_img(3)
    move(5.637727737426758,5.230498123168945,0.0,0.1)
    blo_sub.unregister()
    count=count1+count2+count3
    print("Final Count= ",count)
    count=count%5
    print("Required gate color= ",mp[count])
    #col=['red','yellow','blue','green','purple']
    gates=[-2.151081085205078,0.21936416625976562,2.6673340797424316,5.252288818359375,7.8068037033081055,-2.3645496368408203,0.4780440330505371,2.924586057662964,5.667872428894043,8.082221984863281]
    if mp[count]=='red':
      ind=col.index('red')
      move(8.999160766601562,gates[ind],0.015599107972384582,0.9998783265130142)
      move(11.855231285095215,gates[ind+5],0.13901939821610043,0.9902896580898103)
    elif mp[count]=='yellow':
      ind=col.index('yellow')
      move(8.999160766601562,gates[ind],0.015599107972384582,0.9998783265130142)
      move(12.011744499206543,gates[ind+5],0.02098140376705208,0.9997798661185191)
    elif mp[count]=='blue':
      ind=col.index('blue')
      move(8.999160766601562,gates[ind],0.015599107972384582,0.9998783265130142)
      move(12.011744499206543,gates[ind+5],0.02098140376705208,0.9997798661185191)
    elif mp[count]=='green':
      ind=col.index('green')
      move(8.999160766601562,gates[ind],0.015599107972384582,0.9998783265130142)
      move(12.011744499206543,gates[ind+5],0.02098140376705208,0.9997798661185191)
    elif mp[count]=='purple':
      ind=col.index('purple')
      move(9.664801597595215,gates[ind],0.015599107972384582,0.9998783265130142)
      move(12.011744499206543,gates[ind+5],0.02098140376705208,0.9997798661185191)
    rospy.loginfo("Task completed")
    rospy.spin()
except KeyboardInterrupt:
    print("Shutting down")
    cv2.destroyAllWindows()
