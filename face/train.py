import cv2 as cv
import cv2
import numpy as np
import os

def rescale(img, scale):
    w = img.shape[1]
    h = img.shape[0]
    dim = ((int)(w*scale), (int)(h*scale))
    return cv.resize(img, dim, cv.INTER_AREA)

haar_face = cv.CascadeClassifier(r'C:\Users\huydo\Downloads\archive\haar_face.xml')
people = []

dir = r'C:\Users\huydo\Downloads\archive\trains'

features = []
labels = []

for i in os.listdir(dir):
    people.append(i)
for i in people:
    path = os.path.join(dir, i)
    label = people.index(i)

    for j in os.listdir(path):
        img_path = os.path.join(path,j)
        img = cv.imread(img_path)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        face_rect = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

        for (x,y,w,h) in face_rect:
            cv.rectangle(img, (x+20, y-20), (x+w-20,y+h+20), (250,0,0), thickness=2)
            face_roi = gray[y:y+h, x:x+w]
            features.append(face_roi)
            labels.append(label)

        cv.putText(img,'Training:' + str(len(features)),(20,40), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,1), 2)
        cv.putText(img, str(people[label]), (x+20, y-30), cv.FONT_HERSHEY_COMPLEX, 1,(250,0,0), 2)   
        cv.imshow('Picture', img)
        cv.waitKey(2)

print('Numner of Features:' + str(len(features)) + '----- Number of labels: ' + str(len(labels)))

features = np.array(features, dtype='object')
labels =np.array(labels)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save('C:/Users/huydo/Downloads/archive/face_train.yml')
np.save('C:/Users/huydo/Downloads/archive/features.npy', features)
np.save('C:/Users/huydo/Downloads/archive/labels.npy', labels)

    
