import numpy as np
import cv2

#bitwise operation is very useful whilw working with mask, indicates the pixel of binary image where operation is to be perfromed
img1 = np.zeros([250, 500, 3], np.uint8) #[y, x, #c]
img1 = cv2.rectangle(img1, (200, 0), (300,100), (255,255,255), -1)
img2 = cv2.imread('black_and_white.jpg', -1)
img2 = cv2.resize(img2, (500,250))

## bitwise operation
#bitAnd = cv2.bitwise_and(img2, img1) # bitwise AND operation on image 1 and 2
#bitOr= cv2.bitwise_or(img2, img1) # bitwise OR operation on image 1 and 2
#bitXor= cv2.bitwise_xor(img2, img1) # bitwise XOR operation on image 1 and 2
bitNot= cv2.bitwise_not(img2)

cv2.imshow('image 1', img1)
cv2.imshow('image 2', img2)
#cv2.imshow('bitAnd', bitAnd)
#cv2.imshow('bitOr', bitOr)
#cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot', bitNot)



cv2.waitKey(0)
cv2.destroyAllWindows()