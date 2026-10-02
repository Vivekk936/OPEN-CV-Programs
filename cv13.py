#CHANNEL-->0 to 255
import cv2
import numpy as np
img=cv2.imread("image1.jpg",0)

threshold_value=100
_,binary_threshold= cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold",binary_threshold)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
