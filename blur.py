import cv2
import numpy as np

img = cv2.imread('a/1.jpg')
img = cv2.resize(img, (300, 300))   
median = cv2.medianBlur(img,15)
cv2.imshow("Result", np.hstack([img, median]))
cv2.waitKey(0)