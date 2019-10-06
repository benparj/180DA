#Code edited from: https://github.com/kevinam99/capturing-images-from-webcam-using-opencv-python/blob/master/webcam-capture-v1.01.py
#review credits for Mark Geha8

import cv2

webcam = cv2.VideoCapture(0)
if True:

    check, frame = webcam.read()
    print(check) #true(webcamcheck)
    print(frame) #writes matrix values of each framecd
    cv2.imwrite(filename='saved_img.jpg', img=frame)
