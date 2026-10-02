#canny Edge Detection
#1 Noise Reduction
#2 Intensity of the gradient
#3 Non-Maximum suppression
#4 Thresholding

import cv2


img=cv2.imread("image1.png",0)
resized=cv2.resize(img,(520,520))
min_thres=100
max_thres=200
edges=cv2.Canny(resized,min_thres,max_thres)
cv2.imshow("edges",edges)





cv2.imshow("original",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()