from utils import *
import cv2
w, h = 360, 240
pid = [0.5, 0.5, 0]
pError = 0
myDrone = initTello()

while True:

    img = telloGetImage(myDrone, w, h)

    img, info = findFace(img)

    print(info[0][0])

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # quit
        myDrone.land()
        break
