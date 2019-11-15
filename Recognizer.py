import cv2
import numpy as np

#recognizer = cv2.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_COMPLEX;
while True:
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        #print (Id)
        if(conf<50):
            if(Id==1):
                Id="Enrique"
            elif(Id==2):
                Id="Melissa"
            elif(Id==3):
                Id="Sofia"
            elif(Id==4):
                Id="Gema"
        else:
            Id="Unknown"
        #cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        cv2.putText(img,str(Id),(x,y+h),font,2,(255,0,0),3);
    cv2.imshow('img',img) 
    if cv2.waitKey(10)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
