import cv2
import numpy as np


def trackbarValue(x):
	print(x)

cap = cv2.VideoCapture(0)

cv2.namedWindow('Trackbar')

cv2.createTrackbar('hue_lower', 'Trackbar', 0, 255, trackbarValue)
cv2.createTrackbar('saturation_lower', 'Trackbar', 0, 255, trackbarValue)
cv2.createTrackbar('value_lower', 'Trackbar', 0, 255, trackbarValue)

cv2.createTrackbar('hue_upper', 'Trackbar', 255, 255, trackbarValue)
cv2.createTrackbar('saturation_upper', 'Trackbar', 255, 255, trackbarValue)
cv2.createTrackbar('value_upper', 'Trackbar', 255, 255, trackbarValue)


while(1):
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	hl = cv2.getTrackbarPos('hue_lower', 'Trackbar')
	sl = cv2.getTrackbarPos('saturation_lower', 'Trackbar')
	vl = cv2.getTrackbarPos('value_lower', 'Trackbar')

	hu = cv2.getTrackbarPos('hue_upper', 'Trackbar')
	su = cv2.getTrackbarPos('saturation_upper', 'Trackbar')
	vu = cv2.getTrackbarPos('value_upper', 'Trackbar')

	l_b = np.array([[hl, sl, vl]]) # it is lower bound for color in hsv color format
	u_b = np.array([[hu , su, vu]]) # its is upper bound for  color

	mask = cv2.inRange(hsv, l_b, u_b) # collect the value between l_b and u_b having in image 
	res = cv2.bitwise_and(frame, frame, mask = mask)

	cv2.imshow('image', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	k = cv2.waitKey(1) # remeber to change image per mili second
	if k == 27:
		break



cap.release()
cv2.destroyAllWindows()