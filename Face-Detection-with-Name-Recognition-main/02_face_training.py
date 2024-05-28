# import cv2
# import numpy as np
# from PIL import Image
# import os

# # Path for face image database
# path = r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\dataset'

# recognizer = cv2.face.LBPHFaceRecognizer_create()
# detector = cv2.CascadeClassifier(r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\haarcascade_frontalface_default.xml');

# # function to get the images and label data
# def getImagesAndLabels(path):

#     imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
#     faceSamples=[]
#     ids = []

#     for imagePath in imagePaths:

#         PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
#         img_numpy = np.array(PIL_img,'uint8')

#         id = int(os.path.split(imagePath)[-1].split(".")[1])
#         faces = detector.detectMultiScale(img_numpy)

#         for (x,y,w,h) in faces:
#             faceSamples.append(img_numpy[y:y+h,x:x+w])
#             ids.append(id)

#     return faceSamples,ids

# print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
# faces,ids = getImagesAndLabels(path)
# recognizer.train(faces, np.array(ids))

# # Save the model into trainer/trainer.yml
# recognizer.write(r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\trainer\trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# # Print the numer of faces trained and end program
# print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))




import cv2
import numpy as np
from PIL import Image
import os

# Path for face image database
path = r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\haarcascade_frontalface_default.xml')

# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)

            # Construct file path
            file_path = os.path.join(path, f'User.{id}.{len(faceSamples)}.jpg')

            # Check if file already exists and delete if it does
            if os.path.exists(file_path):
                os.remove(file_path)

            # Save the captured image into the dataset folder
            cv2.imwrite(file_path, img_numpy[y:y+h, x:x+w])

    return faceSamples, ids

print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
trainer_path = r'C:\Users\huydo\Downloads\Face-Detection-with-Name-Recognition-main-20240505T234037Z-001\Face-Detection-with-Name-Recognition-main\trainer\trainer.yml'
if os.path.exists(trainer_path):
    os.remove(trainer_path)
recognizer.write(trainer_path)

# Print the number of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
