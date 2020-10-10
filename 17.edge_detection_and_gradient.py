import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('messi5.jpg', 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F) # simple gradient
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, 5) # gradient for x-> source, depth, x, y, kernelSize
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, 5) # gradient for y-> source, depth, x, y, kernelSize

canny = cv2.Canny(img, 50, 255) # edge detector -?> source, threshold 1, threshold 2

titles = ['image', 'laplacian', 'sobelX', 'sobelY', 'edge']
images = [img, laplacian, sobelX, sobelY, canny]

for i in range(5):
	plt.subplot(2, 3, i+1) # create subplot of rows, cols
	plt.imshow(images[i], 'gray') # threshold images tkaes gray image
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])
plt.show()