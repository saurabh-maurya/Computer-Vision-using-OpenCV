import cv2
from matplotlib import pyplot as plt
import numpy as np

# common use of smoothing is to remove noise from images
img = cv2.imread('lena.jpg', -1) # halftone-eye.jpg -> all, water.png -> salt and paper, lena.jpg -> preserve edges
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
hm_filter = cv2.filter2D(img, -1, kernel) # homogeneous filter, mean of the kernel

# lpf helps in edge finding , hpf helps in smoothing and bluring -> high and low pass filter
blur = cv2.blur(img, (5,5)) # blur image source, kernel , it is also called averaging
gblur = cv2.GaussianBlur(img, (5,5), 0)# designed specially for rm highFreqNoise using differnt values in x and y direction, middle elemnet of kernel is having highest weight
mblur = cv2.medianBlur(img, 5) # designed specially for rm salt and paper noise, kernel size must be odd except 1
#in all above we smoothed the image as well as edges
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)# use to preserve edges-> source, diameterof echpixel neighbour 9, sigma colour, sigma space

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'MedianBlur', 'bilateralFilter']
images = [img, hm_filter, blur, gblur, mblur, bilateralFilter]


for i in range(6):
	plt.subplot(2, 3, i+1) # create subplot of rows, cols
	plt.imshow(images[i], 'gray') # threshold images tkaes gray image
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])
plt.show()