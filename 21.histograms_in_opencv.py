import numpy as np
import cv2
import matplotlib.pyplot as plt

# img = np.zeros((200 , 200), np.uint8)
img = cv2.imread('lena.jpg', 0)
#b, g, r = cv2.split(img)

# historgarm using cv2
hist = cv2.calcHist([img], [0], None, [256], [0, 256]) # source, channel, mask, no_of_bins, range
plt.plot(hist)

cv2.imshow('image', img)
#cv2.imshow('red', r)
#cv2.imshow('green', g)
#cv2.imshow('blue', b)

 # histogam using matplotlib
#plt.hist(img.ravel(), 256, [0,256]) #greyscale mode
#plt.hist(b.ravel(), 256, [0,256])
#plt.hist(g.ravel(), 256, [0,256])
#plt.hist(r.ravel(), 256, [0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()