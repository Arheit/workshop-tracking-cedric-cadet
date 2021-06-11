#!/usr/bin/python3

import cv2
import mediapipe as mp

def open_image():
    img = cv2.imread("fischl_see_this_shit.png")
    while True:
        cv2.imshow(("Fischl!"), img)
        if cv2.waitKey(33) == ord("q"):
            break
    cv2.destroyAllWindows()

def open_camera():
    cam = cv2.VideoCapture(0)
    mpHand = mp.solutions.hands
    hand = mpHand.Hands()
    while True:
        ret, frame = cam.read()
    #Check error
        if not ret:
            print("Unable to open camera\n")
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hand.process(rgb)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, handLms, mpHand.HAND_CONNECTIONS)
        #Show camera
        cv2.imshow("idk", frame)
        #Close the window
        if cv2.waitKey(33) == ord("q"):
            break
    cv2.destroyAllWindows()

open_camera()