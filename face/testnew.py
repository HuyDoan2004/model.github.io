# import cv2 as cv
# import cv2
# import numpy as np
# import os

# def rescale(img, scale):
#     w = img.shape[1]
#     h = img.shape[0]
#     dim = ((int)(w*scale), (int)(h*scale))
#     return cv.resize(img, dim, cv.INTER_AREA)

# haar_face = cv.CascadeClassifier(r'C:\Users\huydo\Downloads\archive\haar_face.xml')
# people = []

# dir = r'C:\Users\huydo\Downloads\archive\trains'

# features = []
# labels = []

# for i in os.listdir(dir):
#     people.append(i)
# for i in people:
#     path = os.path.join(dir, i)
#     label = people.index(i)

#     for j in os.listdir(path):
#         img_path = os.path.join(path,j)
#         img = cv.imread(img_path)

#         gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#         face_rect = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

#         for (x,y,w,h) in face_rect:
#             cv.rectangle(img, (x+20, y-20), (x+w-20,y+h+20), (250,0,0), thickness=2)
#             face_roi = gray[y:y+h, x:x+w]
#             features.append(face_roi)
#             labels.append(label)

#         cv.putText(img,'Training:' + str(len(features)),(20,40), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,1), 2)
#         cv.putText(img, str(people[label]), (x+20, y-30), cv.FONT_HERSHEY_COMPLEX, 1,(250,0,0), 2)   
#         cv.imshow('Picture', img)
#         cv.waitKey(2)

# print('Numner of Features:' + str(len(features)) + '----- Number of labels: ' + str(len(labels)))

# features = np.array(features, dtype='object')
# labels =np.array(labels)

# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.train(features, labels)

# face_recognizer.save('C:/Users/huydo/Downloads/archive/face_train.yml')
# np.save('C:/Users/huydo/Downloads/archive/features.npy', features)
# np.save('C:/Users/huydo/Downloads/archive/labels.npy', labels)

    
import numpy as np
import cv2 as cv
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs

people = ['DoanHuy', 'HuuGiap', 'TienToan']

haar_cascade = cv.CascadeClassifier(r'C:\Users\huydo\Downloads\archive\haar_face.xml')
features = np.load(r'C:\Users\huydo\Downloads\archive\features.npy', allow_pickle=True)
labels = np.load(r'C:\Users\huydo\Downloads\archive\labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\huydo\Downloads\archive\face_train.yml')

class Main(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Processing Image (T-H)")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu = menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpenColor)
        fileMenu.add_command(label="Save", command=self.onSave)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.quit)    

        Recognizer = Menu(menubar)
        Recognizer.add_command(label="Recognizer", command=self.Recognizer)
        Recognizer.add_command(label="AutoRecognizer", command=self.AutoRecognizer)
        Recognizer.add_command(label="RecognizerWebcam", command=self.RecognizerWebcam)

        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Recognizer", menu=Recognizer)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpenColor(self):
        global ftypes
        ftypes = [('Images', '*jpg *.tif *.bmp *.gif *.png')]
        dlg = Open(self, filetypes = ftypes)

        fl = dlg.show()

        if fl != '':
            global imgin
            imgin = cv.imread(fl,cv.IMREAD_GRAYSCALE)
            imgin = cv.imread(fl,cv.IMREAD_COLOR)
            cv.namedWindow("Picture", cv.WINDOW_AUTOSIZE)
            cv.imshow("Picture", imgin)

    def onSave(self):
        dlg = SaveAs(self, filetypes = ftypes)
        fl = dlg.show()
        if fl != '':
            cv.imwrite(fl,imgout)

    def Recognizer(self):
        pass

    def AutoRecognizer(self):
        pass

    def RecognizerWebcam(self):
        cap = cv.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                label, confidence = face_recognizer.predict(face_roi)

                cv.putText(frame, f"Predicted: {people[label]}, Confidence: {confidence}", (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv.imshow('Webcam', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

def main():
    root = Tk()
    root.geometry("600x450")
    app = Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
