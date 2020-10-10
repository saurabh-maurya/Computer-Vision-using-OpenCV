import cv2
import numpy as np

def trackbarValue(x):
	print(x)

img = np.zeros([300, 512, 3], np.uint8)


cv2.namedWindow('image') # used to create window wth name , all imshow with name image will be loaded in this window

cv2.createTrackbar('B', 'image', 0, 255, trackbarValue) # used to create track bar, name of trackbar| window name| initial value| final value| call bak function  
cv2.createTrackbar('G', 'image', 0, 255, trackbarValue)
cv2.createTrackbar('R', 'image', 0, 255, trackbarValue)

switch = 'On/Off' # creating switch using trackbar
cv2.createTrackbar(switch, 'image', 0, 1, trackbarValue)

while(1):
	cv2.imshow('image', img)
	k = cv2.waitKey(1) # remeber to change image per mili second
	if k == 27:
		break
	b = cv2.getTrackbarPos('B', 'image') # get track bar value for name of trackabar
	g = cv2.getTrackbarPos('G', 'image')
	r = cv2.getTrackbarPos('R', 'image')
	s = cv2.getTrackbarPos(switch, 'image')
	
	if s == 0:
		img[:] = 0
	else:
		img[:] = [b, g, r]

cv2.destroyAllWindows()