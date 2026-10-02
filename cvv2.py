import cv2
img=cv2.imread(r"D:\project jarvis\Images\1.jpg", 0)
cv2.imshow("window", img)
cv2.imwrite("2.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()