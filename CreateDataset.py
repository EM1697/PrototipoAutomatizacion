import cv2, sqlite3
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

def insertOrUpdateToDb(id, name):
    conn = sqlite3.connect('FaceBase.db')

    #Check if exists
    cmd = "SELECT * from People WHERE id_person = " + str(id)

    #Execute command and save all raws of request
    cursor = conn.execute(cmd)

    exists = False
    for row in cursor:
        exists = True

    if exists:
        cmd = "UPDATE People SET name = \'" + str(name) + "\' where id_person = " + str(id)
    else:
        cmd = 'INSERT INTO People (id_person, name) VALUES (' + str(id) + ', \'' + str(name) + '\')'

    conn.execute(cmd)
    conn.commit()
    conn.close()


Id = raw_input('Enter your Id: \n\r')
name = raw_input('Enter your name: \n\r')
insertOrUpdateToDb(Id, name)
sampleNum = 0
while (True):
    if Id.isdigit():
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            #incrementing sample number
            sampleNum = sampleNum + 1
            #saving the captured face in the dataset folder
            cv2.imwrite("dataset/User." + Id + '.' + str(sampleNum) + ".jpg",
                        gray[y:y + h, x:x + w])

            cv2.imshow('frame', img)
        #wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 20
        elif sampleNum > 50:
            break
    else:
        print('Just integers please.')
        break
cam.release()
cv2.destroyAllWindows()