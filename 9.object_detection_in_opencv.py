import cv2
import numpy as np


def trackbarValue(x):
	print(x)

cv2.namedWindow('Tracking')

cv2.createTrackbar('hue_lower', 'Tracking', 0, 255, trackbarValue)
cv2.createTrackbar('saturation_lower', 'Tracking', 0, 255, trackbarValue)
cv2.createTrackbar('value_lower', 'Tracking', 0, 255, trackbarValue)

cv2.createTrackbar('hue_upper', 'Tracking', 255, 255, trackbarValue)
cv2.createTrackbar('saturation_upper', 'Tracking', 255, 255, trackbarValue)
cv2.createTrackbar('value_upper', 'Tracking', 255, 255, trackbarValue)


while(1):
	img = cv2.imread('smarties.png', 1)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	hl = cv2.getTrackbarPos('hue_lower', 'Tracking')
	sl = cv2.getTrackbarPos('saturation_lower', 'Tracking')
	vl = cv2.getTrackbarPos('value_lower', 'Tracking')

	hu = cv2.getTrackbarPos('hue_upper', 'Tracking')
	su = cv2.getTrackbarPos('saturation_upper', 'Tracking')
	vu = cv2.getTrackbarPos('value_upper', 'Tracking')

	l_b = np.array([[hl, sl, vl]]) # it is lower bound for color in hsv color format
	u_b = np.array([[hu , su, vu]]) # its is upper bound for  color

	mask = cv2.inRange(hsv, l_b, u_b) # collect the value between l_b and u_b having in image 
	res = cv2.bitwise_and(img, img, mask = mask)

	cv2.imshow('image', img)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	k = cv2.waitKey(1) # remeber to change image per mili second
	if k == 27:
		break




cv2.destroyAllWindows()