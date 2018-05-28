import numpy as np
import cv2

def nothing(x):
	pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')

#create upper and lower bound trackbars
# cv2.createTrackbar('Lower', 'frame', 0, 255, nothing)
# cv2.createTrackbar('Upper', 'frame', 0, 255, nothing)
# low = 50
# upper = 150

while(True):
	# capture frame-by-frame
	ret, frame = cap.read()
	
	#get trackbar positions
	low = cv2.getTrackbarPos('Lower', 'Canny Test')
	upper = cv2.getTrackbarPos('Upper', 'Canny Test')
	
	#our operations on the frame come here
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	mask = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
	mask1 = cv2.inRange(gray, low, upper)
	mask2 = cv2.inRange(gray, 50, 150)
	
	#Display frame 
	cv2.imshow('frame', mask2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#When everything done, release capture 
cap.release()
cv2.destroyAllWindows()