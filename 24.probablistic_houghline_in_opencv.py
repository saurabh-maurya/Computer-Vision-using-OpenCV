import cv2
import numpy as np

##_____STEPS_____##
#1 Edge Detection
#2 Mapping of Edges to the Hough Space and store in accumulator
#3 Intepretation of accumulator to yield lines of infinte length
#4 Conversion of Infonte line to finite line

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 0, 150, apertureSize = 3)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength = 100, maxLineGap = 50)

for line in lines:
	x1, y1, x2, y2 = line[0]
	cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('image', img)
cv2.imshow('Canny Edge', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()