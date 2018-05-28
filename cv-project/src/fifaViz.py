#fifa image analyzer 
import numpy as np
import cv2
from matplotlib import pyplot as plt

kernel = np.ones((8,8),np.uint8)

fifaorig = cv2.imread('../images/Post-match-stats.png', 0)



ret3,otsu = cv2.threshold(fifaorig,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imwrite('../images/fif-otsu.png', otsu)

mask3 = cv2.adaptiveThreshold(fifaorig,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#cv2.imwrite('../images/fifa-adapt-gaus.png', mask3)

#cv2.imshow('fifaorig', np.hstack([fifaorig, otsu, mask3]))

image, contours, hierarchy = cv2.findContours(otsu,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

fifaorig_cl = cv2.imread('../images/Post-match-stats.png',1)
print np.shape(contours)[0]

#for index,i in enumerate(contours):
#	print i.output(index)


#iterate through contours, drawing each one
for i in [0,np.shape(contours)[0]-1]:
	rect = cv2.minAreaRect(contours[i])
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	fifaorig_cl = cv2.drawContours(fifaorig_cl,[box],0,(0,200,0),5)
	
rect = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(rect)
box = np.int0(box)
fifaorig_cl = cv2.drawContours(fifaorig_cl,[box],0,(0,0,200),5)

cv2.imwrite('../images/fifaorig_boxed.png', fifaorig_cl)


cv2.waitKey(0)
