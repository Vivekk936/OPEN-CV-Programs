import cv2
import numpy as np
img=cv2.imread("image1.jpg")
width=600
height=850
dim=(width,height)
resized=cv2.resize(img,dim)
kernel=np.ones((5,5),dtype='uint8')
erosion=cv2.erode(resized,kernel,iterations=1)
dilation=cv2.dilate(resized,kernel,iterations=1)
cv2.imshow("Original",resized)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
