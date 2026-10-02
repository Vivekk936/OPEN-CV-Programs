import cv2#flip image


img = cv2.imread("image1.jpg")
width = 600
height = 850 
dim = (width, height)
resized = cv2.resize(img, dim)
print(f"Size in bytes:{img.size}")
flip_horizontal = cv2.flip(resized, 1)
flip_vertical = cv2.flip(resized, 0)
flip_back = cv2.flip(resized, -1)
cv2.imshow("Original", resized)
cv2.imshow("Flipped-H", flip_horizontal)
cv2.imshow("Flipped-V", flip_vertical)
cv2.imshow("Flip-Back", flip_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
