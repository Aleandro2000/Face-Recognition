import cv2
import sys

import os
from os import path

open=True

while open==True:
    name = input("Write the name of png image with its extension from 'faces' folder: ")
    imagePath = "./faces/"+name
    cascPath = "./database/defaultfaces.xml"

    imagePath_recover = "../faces/"+name
    cascPath_recover = "../database/defaultfaces.xml"

    if path.exists(imagePath)==False and path.exists(imagePath_recover)==False:
        print('ERROR! FILE DOES NOT EXIST!')
        if input("Do you want to exit? Type EXIT if you want!\n*")=="EXIT":
            open=False
        else:
            os.system("@cls||clear")
        continue
    elif path.exists(imagePath_recover)==False:
        faceCascade = cv2.CascadeClassifier(cascPath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        print("Found {0} faces! Type EXIT to close!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imwrite("./faces_recognition/face_recognition.png",image)

        if input("*")=="EXIT":
            open=False
        else:
            os.system("@cls||clear")
    else:
        faceCascade = cv2.CascadeClassifier(cascPath_recover)
        image = cv2.imread(imagePath_recover)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        print("Found {0} faces! Type EXIT to close!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imwrite("./faces_recognition/face_recognition.png",image)

        if input("*")=="EXIT":
            open=False
        else:
            os.system("@cls||clear")
