from djitellopy import Tello
import cv2
import numpy as np


def initTello():
    myDrone = Tello()
    myDrone.connect()

    # set the speeds
    myDrone.speed = 0

    # print the battery percentage
    print(myDrone.get_battery())
    myDrone.streamoff()  # if not off already
    myDrone.streamon()
    #myDrone.takeoff()
    return myDrone


def telloGetImage(myDrone, w=360, h=240):
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (w, h))  # so that it can be used for tracking
    return img


def findFace(img):
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 4)

    myFaceListC = []
    myFaceListArea = []  # closest face has largest area

    # find all the faces & draw the largest one

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        myFaceListArea.append(area)
        myFaceListC.append([cx, cy])

    if len(myFaceListC) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]  # return the largest face
    else:
        return img, [[0, 0], 0]


def trackFace(myDrone, info, x, y):
    if info[0][0] != 0:
        print(info[0][0], info[0][1])
        if info[0][1] > (y // 2 - 20):
            myDrone.move_up(20)
        else:
            myDrone.move_down(20)
        if info[0][0] > (x // 2 - 20):
            myDrone.move_right(20)
        else:
            myDrone.move_left(20)

