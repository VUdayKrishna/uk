import cv2
import winsound
cam=cv2.VideoCapture(0)
while True:
    _,im1=cam.read()
    _,im2=cam.read()
    diff=cv2.absdiff(im1,im2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    _,thresh=cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        winsound.Beep(500,100)
    cv2.imshow("security camera",thresh)
    if cv2.waitKey(10)==27:
        break
cam.release()
cv2.destriyAllWindows()