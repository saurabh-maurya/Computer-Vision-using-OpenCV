import cv2

## read and show an images
img = cv2.imread('lena.jpg', 0) # used to read images and value -1,0,1 -> color,greyscale, unchanged
print(img) # print matrix of image
cv2.imshow('image', img) # show image for split of sec.
k = cv2.waitKey(5000) # wait for milisecond before disappering, if value 0 -> we have to close image or press any key

## saVe on 's' key press and distory window on 'esc' key press
if k == 27 : # 27 is value for esc ky
	cv2.destroyAllWindows() # used to distroy all window that created, can use distroyWindow() for distroying single window 
elif k == ord('s') or k == ord('S'): #ord takes one value and return in ascii value
	## write an image
	cv2.imwrite('lena_copy.png', img) #  used to write image in any image format
	cv2.destroyAllWindows()




