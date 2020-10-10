import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 200, 255, 0)
contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # source, contour mode, contour approx method
print('No. of contour present : ', len(contour))

cv2.drawContours(img, contour, -1, (255, 255, 0), 3) # source, contour, indexofcontour, color, thickness
# it will draw contour on source image

cv2.imshow('image', img)
#cv2.imshow('image gray', imgray) # rec, e, n, ein, p, pin, V, C

cv2.waitKey(0)
cv2.destroyAllWindows()