import cv2
img=cv2.imread("image1.jpg")
row=img.shape[1]
column=img.shape[0]

centre=(column/2,row/2)
angle=180  

r=cv2.getRotationMatrix2D(centre,angle,1)
rotate=cv2.warpAffine(img,r,(column,row))



cv2.imshow("Original",img)
cv2.imshow("Rotated",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()