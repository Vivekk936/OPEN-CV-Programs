import cv2
import numpy as np
img=cv2.imread("image1.jpg")
width=600
height=850
dim=(width,height)
resized=cv2.resize(img,dim)
kernel=np.ones((5,5),dtype='uint8')
opening=cv2.morphologyEx(resized,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel)
cv2.imshow("Original",resized)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)   
cv2.waitKey(0)
cv2.destroyAllWindows()
