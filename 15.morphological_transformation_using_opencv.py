import cv2
import matplotlib.pyplot as plt
import numpy as np

# morphological transformation are some simple operation based on the image shape, it is normally performed on binary image
img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE) # or use 0
_, mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

# morphological tranformation
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations = 1)
erotion = cv2.erode(mask, kernel, iterations = 1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # erosion then dilation is performed
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # dilation then erosion is performed
# can use many morphology using morphologyEx 

titles = ['image', 'mask', 'dilation', 'erotion', 'opening', 'closing']
images = [img, mask, dilation, erotion, opening, closing]

for i in range(6):
	plt.subplot(2, 3, i+1) # create subplot of rows, cols
	plt.imshow(images[i], 'gray') # threshold images tkaes gray image
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()