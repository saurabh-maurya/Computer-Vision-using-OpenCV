import cv2
import numpy as np

## process oh thresholding is segementation technique ,widley used in seprating image from background

img = cv2.imread('gradient.png', -1)

# threshold is use to acces required object of image
_, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # in binary threshold, if image value in between threshold if assign 0 else 1 to image  making it back and white image
_, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # it is inverse binary threshold
_, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) # upto threshold value image will not change ,if it is in between threshold value then it will change to lower value of thershold 
_, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # when value is less than threshold it will assign 0 to it , if it is in threshold then it will be same 
_, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # it will be inverse of TOZERO threshold


cv2.imshow('Image', img)
cv2.imshow('threshold 1', thr1)
cv2.imshow('threshold 2', thr2)
cv2.imshow('threshold 3', thr3)
cv2.imshow('threshold 4', thr4)
cv2.imshow('threshold 5', thr5)


cv2.waitKey(0)

cv2.destroyAllWindows()