import cv2
import datetime
## video is nothing but sequence or frames

## read and show an images
cap = cv2.VideoCapture(0) # used to read videos using filename or pass value 0|-1 -> CAMERA CAPTURE , other interger for different camera if attached

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # it is used to get different porperty of cap
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # more about properties->  https://docs.opencv.org/master/d4/d15/group__videoio__flags__base.html

# we can also use no. associated to property to do our bidings
cap.set(3, 720) # used to set value of image property, associated no. with cv2.CAP_PROP_FRAME_WIDTH is 3
cap.set(4, 720) #  associated no. with cv2.CAP_PROP_FRAME_HEIGHT is 4
# if we are using camera to capture then camera will automatically cange the resolution to nearest possible resolution

print(cap.get(3))
print(cap.get(4))


print(cap.isOpened()) # isOpened return True if video is availabe when filename is given or camera is available else return False
while(cap.isOpened()): # infinite loop to read frame
	ret, frame = cap.read() # it is ued to store frame matrix in frame variable and ret is used here to store True if frame available else False 
	
	if ret == True:
				
		date = str(datetime.datetime.now())
		font = cv2.FONT_HERSHEY_SIMPLEX # used to create font face
		img = cv2.putText(frame, date, (20,20), font, .5, (0, 255, 255), 1, cv2.LINE_AA) # used to put text on image,starting point -> (20,400), font face fontsize ie 4 here, then color in BGR from here -> (0,0,0) thickness of line, thickness of line i.e. 10 and then line type i.e 
		
		cv2.imshow('VideoImage', img) # show image for split of sec.
		if cv2.waitKey(1) == ord('q'): # wait for milisecond before disappering, if value 0 -> we have to close image or press any key
			break # break from sequetial image capture
	else:
		break


cap.release() # release all resources
cv2.destroyAllWindows() # used to distroy all window that created, can use distroyWindow() for distroying single window 