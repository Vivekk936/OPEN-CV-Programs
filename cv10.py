import cv2
import numpy as np
#img = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)
img=np.zeros((600,800,3),np.uint8)#Black space
img.fill(255)#background white
cv2.line(img,(0,0),(150,150),(255,0,0),2)
cv2.rectangle(img,(200,150),(250,300),(0,255,0),3)
cv2.circle(img,(300,75),70,(255,0,255),3)
pts_polygon=np.array([[100,50],[100,300],[500,50],[500,300]],np.int32)
cv2.polylines(img,[pts_polygon],True,(0,0,255),3)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,"Hello",(10,500),font,2,(34,160,255),2,cv2.LINE_AA)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()