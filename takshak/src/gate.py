import cv2
import numpy as np


img = cv2.imread("gates.jpg")                
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

light_blue = np.array([90,127,0])
dark_blue = np.array([126,255,255])

light_green = np.array([45,208,0])
dark_green = np.array([179,255,255])

light_purple= np.array([128,136,0])
dark_purple= np.array([179,255,255])

light_yellow = np.array([21,239,0])
dark_yellow = np.array([179,255,255])

light_red = np.array([0,150,0])
dark_red = np.array([3,255,255])

def blue(img):
	mask = cv2.inRange(hsv, light_blue, dark_blue)
	output = cv2.bitwise_and(img,img, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
	i=0
	cX=[0,0]
	cY=[0,0]
	for c in contours:
		   M = cv2.moments(c)
		   cX[i] = int(M["m10"] / M["m00"])
		   cY[i] = int(M["m01"] / M["m00"])
		   i=i+1
	x=(cX[0]+cX[1])/2
	y=(cY[0]+cY[1])/2
	
	cv2.circle(img, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((img,output)))
	return x,y

def green(img):
	mask = cv2.inRange(hsv, light_green, dark_green)
	output = cv2.bitwise_and(img,img, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
	i=0
	cX=[0,0]
	cY=[0,0]
	for c in contours:
		   M = cv2.moments(c)
		   cX[i] = int(M["m10"] / M["m00"])
		   cY[i] = int(M["m01"] / M["m00"])
		   i=i+1
	x=(cX[0]+cX[1])/2
	y=(cY[0]+cY[1])/2
	
	cv2.circle(img, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((img,output)))
	return x,y

def purple(img):
	mask = cv2.inRange(hsv, light_purple, dark_purple)
	output = cv2.bitwise_and(img,img, mask= mask)
	cv2.imshow("out",output)
	cv2.waitKey(0)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
	for con in contours:
         area = cv2.contourArea(con)
         ep = 0.048 * cv2.arcLength(con, True) - 0.7
         app = cv2.approxPolyDP(con, ep, True)
         x, y, w, h = cv2.boundingRect(app)
         if area>100:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            break
	cv2.circle(img, (x, y), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((img,output)))
	return x,y

def yellow(img):
	mask = cv2.inRange(hsv, light_yellow, dark_yellow)
	output = cv2.bitwise_and(img,img, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
	i=0
	cX=[0,0]
	cY=[0,0]
	for c in contours:
		   M = cv2.moments(c)
		   cX[i] = int(M["m10"] / M["m00"])
		   cY[i] = int(M["m01"] / M["m00"])
		   i=i+1
	x=(cX[0]+cX[1])/2
	y=(cY[0]+cY[1])/2
	
	cv2.circle(img, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((img,output)))
	return x,y

def red(img):
	mask = cv2.inRange(hsv, light_red, dark_red)
	output = cv2.bitwise_and(img,img, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
	i=0
	cX=[0,0]
	cY=[0,0]
	for c in contours:
		   M = cv2.moments(c)
		   cX[i] = int(M["m10"] / M["m00"])
		   cY[i] = int(M["m01"] / M["m00"])
		   i=i+1
	x=(cX[0]+cX[1])/2
	y=(cY[0]+cY[1])/2
	
	cv2.circle(img, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((img,output)))
	return x,y

ans = purple(img)
print(ans)

cv2.waitKey(0)
cv2.destroyAllWindows()
