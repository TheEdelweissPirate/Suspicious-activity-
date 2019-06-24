import cv2
import numpy as np
import winsound
import time
people_cascade = cv2.CascadeClassifier('cascadG.xml')
head_cascade = cv2.CascadeClassifier('cascadeH5.xml')
cap = cv2.VideoCapture('HD CCTV People.mp4')
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    people=people_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in people:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,"Someone's there",(x,y), font, 1, (200,255,155), 2, cv2.LINE_AA)
        
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 
