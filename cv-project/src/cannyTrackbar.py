#Canny track bar
import cv2
import numpy as np

def nothing(x):
	pass

otsu = cv2.imread('../images/otsu.jpg')
closing = cv2.imread('../images/closing.jpg')

cv2.namedWindow('Canny Test',)

#create upper and lower bound trackbars
cv2.createTrackbar('Lower', 'Canny Test', 0, 255, nothing)
cv2.createTrackbar('Upper', 'Canny Test', 0, 255, nothing)
low = 50
upper = 150

while(1):
	canny = cv2.Canny(otsu, low, upper)
	cv2.imshow('Canny Test', canny)
	
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	
	#get trackbar pos
	low = cv2.getTrackbarPos('Lower', 'Canny Test')
	upper = cv2.getTrackbarPos('Upper', 'Canny Test')

cv2.imwrite('../images/otsuCanny.jpg', canny)
cv2.destroyAllWindows()


