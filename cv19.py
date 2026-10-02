import cv2
video=cv2.VideoCapture("video1.mp4")
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
output=cv2.VideoWriter("output.mp4",fourcc,60,(1080,1920))
while video.isOpened():
    ret,frame=video.read()
    if ret:
        output.write(frame)
        cv2.imshow("output",frame)
        if cv2.waitKey(10)  == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()

