from utils import *
import cv2
w, h = 360, 240 # the dimensions for the screen
pid = [0.5, 0.5, 0]
pError = 0
myDrone = initTello()  # before starting the tracking, make sure the drone takes off

while True:

    img = telloGetImage(myDrone, w, h)

    img, info = findFace(img)
    if info[0][0] != 0:  # there exists a face
        print(info[0][0], info[0][1], "area of ", info[1])

    trackFace(myDrone, info, w, h)  # in progress: currently only works when drone is at the height of the face

    cv2.imshow('Image', img) # start the display of the image

    if cv2.waitKey(1) & 0xFF == ord('q'):  # quit
        myDrone.land()
        break
    if cv2.waitKey(1) & 0xFF == ord('w'): # go up
        myDrone.move_up(20)

    if cv2.waitKey(1) & 0xFF == ord('s'):  # go down
        myDrone.move_down(20)


