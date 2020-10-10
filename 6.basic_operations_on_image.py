import numpy as np
import cv2

img = cv2.imread('messi5.jpg', 1)
img2 = cv2.imread('opencv-logo.png', 1)

print(img.shape) # number of rows, columns , channels
print(img.size) # total number of pixels
print(img.dtype) # data type of image

b, g, r = cv2.split(img)  # split channels of image
img = cv2.merge((b, g, r)) # merge channel of image

# find out the coordinates fo ball using mouse click event or mouse_event_in_open_cv , here ball is our ROI
ball = img[280:340, 330:390]
img[273:333, 120:180] = ball

# resizing image 
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# for adding two images they must be of same size
#dst = cv2.add(img, img2) # adding two images
dst = cv2.addWeighted(img, .9, img2, .1, 0) # adding two images with weight, alpha(here = .9 ) is weight for image 1, beta(here = .1) is weight for image 2, gamma(here = 0) is the scalar value, weight must be in between 0 to 1

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()