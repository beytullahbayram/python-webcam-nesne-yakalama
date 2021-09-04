import cv2
import numpy as np

cap = cv2.VideoCapture(0)  #görüntü alma
mycascade = cv2.CascadeClassifier("C:\mycascade\classifier\\cascade.xml")  #\\ önceki yer cascade dosya yolu

font1=cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    sigara = mycascade.detectMultiScale(gray,1.3,7)
    for (x,y,w,h) in sigara:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,"SIGARA",(x,y),font1,1,(255,0,0), cv2.LINE_4)

        cv2.imshow("sigara",frame)

        if cv2.waitKey(1) & 0xFF==ord("q"):
            break


cap.release()
cv2.destryoAllWindows()


