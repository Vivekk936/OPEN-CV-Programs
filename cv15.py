import cv2
img = cv2.imread("image1.jpg")
resized=cv2.resize(img,(600,600))
kernel=3
blur=cv2.medianBlur(img,kernel)
cv2.imshow("blur",blur)

cv2.imshow("Original",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()