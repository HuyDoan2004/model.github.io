import cv2
import numpy as np
from PIL import Image
import os

# Path for face image database
path = r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\dataset'
trainer_path = r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\trainer\trainer.yml'
cascadePath = r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\haarcascade_frontalface_default.xml'

face_detector = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.face.LBPHFaceRecognizer_create()

def capture_faces():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    face_id = input('\n enter user id end press <return> ==>  ')

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    count = 0

    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            file_path = os.path.join(path, f'User.{face_id}.{count}.jpg')
            if os.path.exists(file_path):
                os.remove(file_path)
            cv2.imwrite(file_path, gray[y:y + h, x:x + w])
            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 200:  # Take 200 face samples and stop video
            break

    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

def train_faces():
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = face_detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)

        return faceSamples, ids

    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    if os.path.exists(trainer_path):
        os.remove(trainer_path)
    recognizer.write(trainer_path)

    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

def recognize_faces():
    recognizer.read(trainer_path)
    names = ['None', 'HUY', 'GIAP', 'TOAN']

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if confidence < 100:
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break

    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

def main():
    while True:
        print("\nChoose an option:")
        print("1. Capture Faces")
        print("2. Train Faces")
        print("3. Recognize Faces")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            capture_faces()
        elif choice == '2':
            train_faces()
        elif choice == '3':
            recognize_faces()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
