#!/usr/bin/python3

import cv2
#Open camera
img = cv2.imread("fischl_see_this_shit.png")

while True:
    cv2.imshow(("Fischl!"), img)
    if cv2.waitKey(33) == ord("q"):
        break

cv2.destroyAllWindows()
#     #Check error
#     if not [...]:
#         print("Unable to open camera\n")
#         break
#     #Show camera
#     cv2.[...]("Name", [...])
#     #Close the window
#     if cv2.waitKey([...]) = ord([...]):
#     cv2.destroyAllWindows()