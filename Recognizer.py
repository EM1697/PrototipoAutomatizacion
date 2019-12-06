import cv2,  numpy as np, sqlite3

#recognizer = cv2.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

def getProfile(Id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * from People WHERE id_person = " + str(Id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

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
        profile = getProfile(Id)
        if profile != None:
            #cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
            cv2.putText(img,profile[1],(x,y+h),font,2,(255,0,0),3);
        else:
            Id="Unknown"
    cv2.imshow('img',img) 
    if cv2.waitKey(10)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
