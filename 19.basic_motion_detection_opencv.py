import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
	frame_difference = cv2.absdiff(frame1, frame2)
	gray_frame_diff = cv2.cvtColor(frame_difference, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray_frame_diff, (5, 5), 0)
	_, thrsh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	dilate = cv2.dilate(thrsh, None, iterations = 3)
	contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	# cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
	for contour in contours: # drawing rectangle
		(x, y, w, h) = cv2.boundingRect(contour)
		if cv2.contourArea(contour) < 700: # avoideing small area i.e noise
			continue
		cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)


	cv2.imshow('video frame', frame1)

	frame1 = frame2
	ret, frame2 = cap.read()

	if cv2.waitKey(60) == ord('q'):
		break
		
cv2.destroyAllWindows()