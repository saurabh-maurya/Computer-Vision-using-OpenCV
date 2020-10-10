import numpy as np
import cv2

# img = cv2.imread('lena.jpg',-1)
img = np.zeros([512,512, 3], np.uint8) # used to create black image using numpy

img = cv2.line(img, (0, 0), (255,255), (0, 255, 0), 5) # used to draw line with color in BGR from here -> (0,255,0) and thikness of line is 5px
img = cv2.arrowedLine(img, (200, 0), (255, 155), (0, 0, 255), 5) # used to draw arrow line with color in BGR from here -> (0,255,0) and line of 5px

img = cv2.rectangle(img, (0, 255), (100,200), (255, 0, 0), 5) # used to draw rectangle with color in BGR from here -> (0,255,0) and line of 5px, if thickness = -1 then it will fill the box with color
img = cv2.circle(img, (255,255), 50, (100,220,80), 10) # used to draw circle iwth centre and radius , here raius = 50, with color in BGR from here -> (0,255,0) and line of 5px, if thickness = -1 then it will fill the circle with color

font = cv2.FONT_HERSHEY_SIMPLEX # used to create font face
img = cv2.putText(img, 'OpenCV', (20,400), font, 4, (0, 255, 255), 10, cv2.LINE_AA) # used to put text on image,starting point -> (20,400), font face fontsize ie 4 here, then color in BGR from here -> (0,0,0) thickness of line, thickness of line i.e. 10 and then line type i.e 
cv2.imshow('image_lena', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
