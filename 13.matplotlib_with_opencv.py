import cv2
from matplotlib import pyplot as plt

## 1
#img = cv2.imread('lena.jpg', -1)
#cv2.imshow('image', img)
#img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#plt.imshow(img) # image show using matplotlib difference in output image -> cv read image in BGR and matplotlib in RGB
#plt.imshow(img_rgb)
#plt.xticks([]), plt.yticks([]) # assign value to x, y ticks if empty list passed it will hide ticks
#plt.show()


## 2
img_thr = cv2.imread('gradient.png', -1)

_, thr1 = cv2.threshold(img_thr, 127, 255, cv2.THRESH_BINARY) # in binary threshold, if image value in between threshold  assign 0 else 1 to image  making it back and white image
_, thr2 = cv2.threshold(img_thr, 127, 255, cv2.THRESH_BINARY_INV) # it is inverse binary threshold
_, thr3 = cv2.threshold(img_thr, 127, 255, cv2.THRESH_TRUNC) # upto threshold value image will not change ,if it is in between threshold value then it will change to lower value of thershold 
_, thr4 = cv2.threshold(img_thr, 127, 255, cv2.THRESH_TOZERO) # when value is less than threshold it will assign 0 to it , if it is in threshold then it will be same 
_, thr5 = cv2.threshold(img_thr, 127, 255, cv2.THRESH_TOZERO_INV) # it will be inverse of TOZERO threshold

titles = ['Original', 'Binary', 'BinaryInv', 'Trunc', 'ToZero', 'ToZeroInv']
images = [img_thr, thr1, thr2, thr3, thr4, thr5]

for i in range(6):
	plt.subplot(2, 3, i+1) # create subplot of rows, cols
	plt.imshow(images[i], 'gray') # threshold images tkaes gray image
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()