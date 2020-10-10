import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i] # list out all event in cv2 directory
# print(events)

def mouse_click_event(event, x, y, flags, params):  #function to call on  mouse event
	if event == cv2.EVENT_LBUTTONDOWN: # check when left button is down i.e. initial stage of button click
		print(x, ',', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		x_y_cordinate = str(x) + ',' + str(y)
		cv2.putText(img, x_y_cordinate, (x, y), font, 0.5, (0, 255, 0), 1)
		cv2.imshow('Same Window Name', img)

	if event == cv2.EVENT_LBUTTONUP: # check when left button is up i.e. final stage of button click
		print(x, ',', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		x_y_cordinate = str(x) + ',' + str(y)
		cv2.putText(img, x_y_cordinate, (x, y), font, 0.5, (0, 255, 0), 1)
		cv2.imshow('Same Window Name', img)

	if event == cv2.EVENT_RBUTTONDOWN: # check when right button is down i.e. initial stage of button click
		blue = img[y, x, 0]
		green = img[y, x, 1]
		red = img[y, x, 2]
		font = cv2.FONT_HERSHEY_SIMPLEX
		bgr_value = str(blue) + ',' + str(green) + ',' + str(red)
		cv2.putText(img, bgr_value, (x, y), font, 0.5, (0, 255, 255), 1)
		cv2.imshow('Same Window Name', img)

def mouse_click_event_2(event, x, y, flags, params):  #function to call on  mouse event
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
		points.append((x, y))
		if len(points) >= 2:
			cv2.line(img, points[-1], points[-2], (0, 255, 255), 5)
		cv2.imshow('Same Window Name', img)

def mouse_click_event_3(event, x, y, flags, params):  #function to call on  mouse event
	if event == cv2.EVENT_LBUTTONDOWN:
		blue = img[y, x, 0]
		green = img[y, x, 1]
		red = img[y, x, 2]
		cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
		color_image = np.zeros([280, 280, 3], np.uint8)
		color_image[:] = [blue, green, red]
		cv2.imshow('color', color_image) # opens new window of name color


img = np.zeros([480, 680, 3], np.uint8)
#img = cv2.imread('lena.jpg', 1)
cv2.imshow('Same Window Name', img)

points = []
cv2.setMouseCallback('Same Window Name', mouse_click_event) # call back the function on every mouse event
#cv2.setMouseCallback('Same Window Name', mouse_click_event_2)
#cv2.setMouseCallback('Same Window Name', mouse_click_event_3)

cv2.waitKey(0)
cv2.destroyAllWindows()