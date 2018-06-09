import numpy
import cv2

cap = cv2.VideoCapture(1)

ret = cap.set(3,640) # WIDTH
ret = cap.set(4,360) # Height 
ret = cap.set(5,60) # FPS Frame rate


while(True):
    ret, frame = cap.read()
    cv2.imshow('raw',frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
