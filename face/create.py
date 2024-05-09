import numpy as np
import cv2 as cv
import os
from random import randint

# os.mkdir(r'C:\Users\huydo\Downloads\archive' + "\\" + 'trains')
# os.mkdir(r'C:\Users\huydo\Downloads\archive' + "\\" + 'tests')
# # Đường dẫn đến thư mục chứa dữ liệu huấn luyện và kiểm tra
# train_dir = r'C:\Users\huydo\Downloads\archive\trains'
# test_dir = r'C:\Users\huydo\Downloads\archive\tests'

# # Kiểm tra xem thư mục đã tồn tại chưa, nếu chưa thì tạo mới
# if not os.path.exists(train_dir):
#     os.mkdir(train_dir)

# if not os.path.exists(test_dir):
#     os.mkdir(test_dir)
directory = r'C:\Users\huydo\Downloads\archive\datatrain'
label = []

pathvideo = []
pathfolder = []
indexfolder = 0

for i in os.listdir(directory):

    label.append(i)

    path1 = os.path.join(directory, i)

    pathfolder.append(path1)

    for j in os.listdir(path1):

        path2 = os.path.join(path1, j)

        pathvideo.append(path2)
for i in pathvideo:
    os.mkdir(r'C:\Users\huydo\Downloads\archive\trains' + "\\" + str(label[indexfolder]))
    os.mkdir(r'C:\Users\huydo\Downloads\archive\tests' + "\\" + str(label[indexfolder]))

    capture = cv.VideoCapture(i)
    
    haar_face = cv.CascadeClassifier(r'C:\Users\huydo\Downloads\archive\haar_face.xml')

    cnt = 0

    while(1):

        isTrue,img = capture.read()

        cv.imshow('Video', img)

        if 50 <= cnt <= 250:
            cv.imwrite(r'C:\Users\huydo\Downloads\archive\trains' + "\\" + str(label[indexfolder]) + "\\" + 'fig' + str(cnt) + '.jpg', img)
        elif cnt < 50:
            cv.imwrite(r'C:\Users\huydo\Downloads\archive\tests' + "\\" + str(label[indexfolder]) + "\\" + 'fig' + str(cnt) + '.jpg', img)

        cnt = cnt + 1

        if cnt >= 250:
            indexfolder += 1
            break

        # Kết thúc vòng lặp nếu nhấn phím Esc
        if cv.waitKey(1) == 27:
            break

cv.destroyAllWindows()

