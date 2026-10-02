import cv2#resize based on aspect ratio
img = cv2.imread("image1.jpg")
print(f"Dimensions of original images:{img.shape}")
scale=130
width=int(img.shape[1]*scale/100)
height=int(img.shape[0]*scale/100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
print(f"Dimensions of resized images:{resized.shape}")
cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
