#square triange shape recognition

import numpy as np
import cv2

sqrtrg_bgr = cv2.imread('../images/SqTrg.png')

sqrtrg = cv2.cvtColor(sqrtrg_bgr, cv2.COLOR_BGR2HSV)

#define red hsv color range
lower_red = np.array([0,50,50])
upper_red = np.array([15,255,255])

#define blue hsv color range
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

sqthresh = cv2.inRange(sqrtrg, lower_red, upper_red)

trgthresh = cv2.inRange(sqrtrg, lower_blue, upper_blue)

cv2.imwrite('../images/sqthresh.png', sqthresh)
cv2.imwrite('../images/trgthresh.png', trgthresh)

trgimage, trgcontours, trghierarchy = cv2.findContours(trgthresh ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
tcnt= trgcontours[0]


rect = cv2.minAreaRect(tcnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
trgimage = cv2.drawContours(sqrtrg_bgr,[box],0,(0,200,0),5)
cv2.imwrite('../images/trgbox.png', trgimage)

cv2.waitKey(0)