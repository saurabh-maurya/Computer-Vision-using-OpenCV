import cv2
## video is nothing but sequence or frames

## read and show an images
cap = cv2.VideoCapture(0) # used to read videos using filename or pass value 0|-1 -> CAMERA CAPTURE , other interger for different camera if attached
fourcc = cv2.VideoWriter_fourcc(*'XVID') # used to det fourcc code
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) # used to save video , here 20.0 is frames per second anad (640,480) is size of frames

print(cap.isOpened()) # isOpened return True if video is availabe when filename is given or camera is available else return False
while(cap.isOpened()): # infinite loop to read frame
	ret, frame = cap.read() # it is ued to store frame matrix in frame variable and ret is used here to store True if frame available else False 
	
	if ret == True:
		print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # it is used to get different porperty of cap
		print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # more about properties->  https://docs.opencv.org/master/d4/d15/group__videoio__flags__base.html

		out.write(frame) # used to write frame value to variable out

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # it is used to covet into different color image, by default our image is in BGR format
		cv2.imshow('VideoImage', gray) # show image for split of sec.
		if cv2.waitKey(1) == ord('q'): # wait for milisecond before disappering, if value 0 -> we have to close image or press any key
			break # break from sequetial image capture
	else:
		break

		
cap.release() # release all resources
out.release()
cv2.destroyAllWindows() # used to distroy all window that created, can use distroyWindow() for distroying single window 