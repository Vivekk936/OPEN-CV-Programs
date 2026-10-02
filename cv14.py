import cv2
img=cv2.imread("image1.jpg")
resized=cv2.resize(img,(640,640))
ksize=(7,7)
sigmax= 0
sigmay= 0
blur = cv2.GaussianBlur(resized,ksize,sigmax)
cv2.imshow("Original",resized)
cv2.imshow("Blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()