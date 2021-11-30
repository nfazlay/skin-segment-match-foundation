# importing necessary packages
import numpy as np
import cv2
import imutils as im
import argparse

# parse command line arguments if any
# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", help = "path to video (optional)")
# args = vars(ap.parse_args())

# setting the upper and lower boundaries of the HSV pixels
# min_HSV = np.array([0, 133, 77], np.uint8)
# max_HSV = np.array([235, 173, 127], np.uint8)
min_HSV = np.array([0, 48, 80], dtype = "uint8")
max_HSV = np.array([20, 255, 255], dtype = "uint8")

# start the webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise IOError("cannot open webcam")


while True:
    ret, frame = camera.read()
    ret, frame = camera.read()
    dim = (400, 200)
    frame = im.resize(frame, width= 400)
    #resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    # frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation=cv2.INTER_AREA)
    #convert_to_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    convert_to_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dmask = cv2.inRange(convert_to_HSV, min_HSV, max_HSV)
    
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    # dmask = cv2.erode(dmask, kernel, iterations = 2)
    # dmask = cv2.dilate(dmask, kernel, iterations = 2)
    dmask = cv2.GaussianBlur(dmask, (3,3), 0)

    skin = cv2.bitwise_and(frame, frame, mask= dmask)

    cv2.imshow('images', np.hstack([frame, skin]))

    cv2.imwrite("./test.png", np.hstack([frame, skin]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()


