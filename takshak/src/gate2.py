import cv2
import numpy as np


image = cv2.imread("gates.jpg")                
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

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


def blue():
	mask = cv2.inRange(hsv, light_blue, dark_blue)
	output = cv2.bitwise_and(image,image, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
	cX=[]
	cY=[]
	for c in contours:
		M = cv2.moments(c)
		cX.append(int(M["m10"] / M["m00"]))
		cY.append(int(M["m01"] / M["m00"]))
	x=np.sum(cX)/len(contours)
	y=np.sum(cY)/len(contours)
	
	cv2.circle(image, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((image,output)))
	return x

def green():
	mask = cv2.inRange(hsv, light_green, dark_green)
	output = cv2.bitwise_and(image,image, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
	cX=[]
	cY=[]
	for c in contours:
		M = cv2.moments(c)
		cX.append(int(M["m10"] / M["m00"]))
		cY.append(int(M["m01"] / M["m00"]))
	x=np.sum(cX)/len(contours)
	y=np.sum(cY)/len(contours)
	
	cv2.circle(image, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((image,output)))
	return x

def purple():
	mask = cv2.inRange(hsv, light_purple, dark_purple)
	output = cv2.bitwise_and(image,image, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
	cX=[]
	cY=[]
	for c in contours:
		M = cv2.moments(c)
		cX.append(int(M["m10"] / M["m00"]))
		cY.append(int(M["m01"] / M["m00"]))
	x=np.sum(cX)/len(contours)
	y=np.sum(cY)/len(contours)
	
	cv2.circle(image, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((image,output)))
	return x

def yellow():
	mask = cv2.inRange(hsv, light_yellow, dark_yellow)
	output = cv2.bitwise_and(image,image, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
	cX=[]
	cY=[]
	for c in contours:
		M = cv2.moments(c)
		cX.append(int(M["m10"] / M["m00"]))
		cY.append(int(M["m01"] / M["m00"]))
	x=np.sum(cX)/len(contours)
	y=np.sum(cY)/len(contours)

	cv2.circle(image, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((image,output)))
	return x

def red():
	mask = cv2.inRange(hsv, light_red, dark_red)
	output = cv2.bitwise_and(image,image, mask= mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

	cX=[]
	cY=[]
	for c in contours:
		M = cv2.moments(c)
		cX.append(int(M["m10"] / M["m00"]))
		cY.append(int(M["m01"] / M["m00"]))
	x=np.sum(cX)/len(contours)
	y=np.sum(cY)/len(contours)
	
	cv2.circle(image, (int(x), int(y)), 5, (255, 255, 255), -1)
	cv2.imshow("Color Detected", np.hstack((image,output)))
	return x

ans = red()
# print(ans)

if ans >75 and ans <125:
	end = 7.92303
elif ans > 150 and ans < 200:
	end = 5.410655
elif ans > 240 and ans < 290:
	end = 2.89836
elif ans > 360 and ans < 410:
	end = 0.3833055
else:
	end = -2.1358

print(end)



cv2.waitKey(0)
cv2.destroyAllWindows()
