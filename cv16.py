import cv2#Bilateral Filter
img=cv2.imread("image1.jpg")
resized=cv2.resize(img,(500,500))
d=7
sigmacolor=100
sigmaspace=100
b=cv2.bilateralFilter(img,d,sigmacolor,sigmaspace)

cv2.imshow("original",resized)
cv2.imshow("Output",b)
cv2.waitKey(0)
cv2.destroyAllWindows()