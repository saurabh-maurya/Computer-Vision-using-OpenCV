import cv2
import numpy as np

img = cv2.imread('shapes.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corner_det = cv2.goodFeaturesToTrack(img_gray, 50, 0.01, 10) # source, maxNoOfCorners, qualityLevel, minDistance
corner_det = np.int0(corner_det)

for i in corner_det:
	x, y = i.ravel()
	cv2.circle(img, (x, y), 3, (0,255,0), -1)

cv2.imshow('Corner Detection', img)

cv2.waitKey(0)
cv2.destroyAllWindows()