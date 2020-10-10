import cv2
import numpy as np

img = cv2.imread('smarties.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_blur = cv2.medianBlur(img_gray, 5)

circles = cv2.HoughCircles(img_gray_blur, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 0, maxRadius = 0)
detected_circles = np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :]:
	cv2.circle(img, (x, y), r, (255, 255, 0), 3)
	cv2.circle(img, (x, y), 2, (0, 255, 255), 3)

cv2.imshow('Circle Detected', img)

cv2.waitKey(0)
cv2.destroyAllWindows()