import cv2
import numpy as np

img = cv2.imread('sudoku.png', 0)

# every image have different illuminati region but when we use simple tresholding it will apply globally
# so we use adaptive thresholding to use thresholding based on the region

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# two types of adaptive thresholding
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) # threshold value is the mean of neighbour area -> source, max_value, type of calc, typeofthreshold , block size, value of C
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#cv2.imshow('image', img)
cv2.imshow('Binary threshold of image', th1)
cv2.imshow('adaptiveThreshold using meanC', th2)
cv2.imshow('adaptiveThreshold using gaussianC', th3)


cv2.waitKey(0)
cv2.destroyAllWindows()
