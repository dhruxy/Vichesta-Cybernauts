import cv2
import numpy as np


img = cv2.imread("gates.jpg")                
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


mask = cv2.inRange(hsv, light_blue, dark_blue)
output = cv2.bitwise_and(img,img, mask= mask)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = max(contours, key = cv2.contourArea)
cv2.drawContours(img, c, -1, (0, 255, 0), 3)
M = cv2.moments(c)
cX_blue = int(M["m10"] / M["m00"])
cY_blue = int(M["m01"] / M["m00"])
cv2.circle(img, (cX_blue,cY_blue), 5, (255, 255, 255), -1)
cv2.imshow("Color Detected", np.hstack((img,output)))


mask = cv2.inRange(hsv, light_green, dark_green)
output = cv2.bitwise_and(img,img, mask= mask)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = max(contours, key = cv2.contourArea)
cv2.drawContours(img, c, -1, (0, 255, 0), 3)
M = cv2.moments(c)
cX_green = int(M["m10"] / M["m00"])
cY_green = int(M["m01"] / M["m00"])
cv2.circle(img, (cX_green,cY_green), 5, (255, 255, 255), -1)
cv2.imshow("Color Detected", np.hstack((img,output)))


mask = cv2.inRange(hsv, light_purple, dark_purple)
output = cv2.bitwise_and(img,img, mask= mask)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = max(contours, key = cv2.contourArea)
cv2.drawContours(img, c, -1, (0, 255, 0), 3)
M = cv2.moments(c)
cX_purple = int(M["m10"] / M["m00"])
cY_purple = int(M["m01"] / M["m00"])
cv2.circle(img, (cX_purple,cY_purple), 5, (255, 255, 255), -1)
cv2.imshow("Color Detected", np.hstack((img,output)))


mask = cv2.inRange(hsv, light_yellow, dark_yellow)
output = cv2.bitwise_and(img,img, mask= mask)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = max(contours, key = cv2.contourArea)
cv2.drawContours(img, c, -1, (0, 255, 0), 3)
M = cv2.moments(c)
cX_yellow = int(M["m10"] / M["m00"])
cY_yellow = int(M["m01"] / M["m00"])
cv2.circle(img, (cX_yellow,cY_yellow), 5, (255, 255, 255), -1)
cv2.imshow("Color Detected", np.hstack((img,output)))


mask = cv2.inRange(hsv, light_red, dark_red)
output = cv2.bitwise_and(img,img, mask= mask)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = max(contours, key = cv2.contourArea)
cv2.drawContours(img, c, -1, (0, 255, 0), 3)
M = cv2.moments(c)
cX_red = int(M["m10"] / M["m00"])
cY_red = int(M["m01"] / M["m00"])
cv2.circle(img, (cX_red,cY_red), 5, (255, 255, 255), -1)
cv2.imshow("Color Detected", np.hstack((img,output)))


pos = np.array([cX_blue, cX_green, cX_purple, cX_yellow, cX_red])
pos = np.sort(pos)
color = []
for i in range(len(pos)):
	if pos[i]==cX_purple:
		color.append('purple')
	elif pos[i]==cX_green:
		color.append('green')
	elif pos[i]==cX_blue:
		color.append('blue')
	elif pos[i]==cX_yellow:
		color.append('yellow')
	else:
		color.append('red')

print(color)


cv2.waitKey(0)
cv2.destroyAllWindows()
