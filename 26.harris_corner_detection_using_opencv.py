import cv2
import numpy as np

img = cv2.imread('chessboard.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray = np.float32(img_gray)

corner_det = cv2.cornerHarris(img_gray, 2, 3, 0.04)
corner_det = cv2.dilate(corner_det, None)

img[corner_det > 0.01 * corner_det.max()] = [0, 0, 255]

cv2.imshow('Corner Detection', img)

cv2.waitKey(0)
cv2.destroyAllWindows()