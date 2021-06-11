#!/usr/bin/python3

import cv2

def open_image():
    img = cv2.imread("fischl_see_this_shit.png")
    while True:
        cv2.imshow(("Fischl!"), img)
        if cv2.waitKey(33) == ord("q"):
            break
    cv2.destroyAllWindows()

def open_camera():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
    #Check error
        if not ret:
            print("Unable to open camera\n")
            break
        #Show camera
        cv2.imshow("idk", frame)
        #Close the window
        if cv2.waitKey(33) == ord("q"):
            break
    cv2.destroyAllWindows()

open_camera()