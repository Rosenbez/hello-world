import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load a color image in grayscale
img = cv2.imread('../images/newspaper.jpg',0)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image', img)
cv2.imwrite('../images/newspaper.png',img)
kernel = np.ones((8,8),np.uint8)



cv2.namedWindow('edged', cv2.WINDOW_NORMAL)
gray = cv2.bilateralFilter(img,9,75,75)

mask = cv2.inRange(gray, 50, 100)
edged = cv2.Canny(gray, 20, 100)
#cv2.imshow('edged', np.hstack([img, gray, edged, mask]))

mask1 = cv2.inRange(gray, 0, 100)
mask2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
mask3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                              cv2.THRESH_BINARY,11,2)
mask4 = cv2.inRange(gray, 80, 170)
closing = cv2.morphologyEx(mask4, cv2.MORPH_CLOSE, kernel)

ret3,otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
edges = cv2.Canny(closing,50,150)

cv2.imwrite('../images/otsu.jpg', otsu)
cv2.imwrite('../images/closing.jpg', closing)


cv2.imshow('edged', np.hstack([gray, mask4, closing, otsu, edges]))



cv2.waitKey(0)
cv2.destroyAllWindows()

