import cv2
img=cv2.imread("2.jpg")
print("dimension of image",img.shape)
width= 1000
height= 500
dim=(width,height)
resized=cv2.resize(img,dim)
print("dimension of resized image",resized.shape)
cv2.imshow("window",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()