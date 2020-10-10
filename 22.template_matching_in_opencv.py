import cv2
import numpy as np

img_bgr = cv2.imread('messi5.jpg', -1)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('messi_face.jpg', 0)

w, h = template.shape[::-1]

matching_template = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9

loc = np.where(matching_template >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

cv2.imshow('Template Matching', img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()