# importing necessary packages
import numpy as np
import cv2
import imutils as im
import argparse

class DetectSkin:
    def __init__(self):
        """Constructor for the DetectSkin Class
        """
        self.min_HSV = np.array([0, 48, 80], dtype = "uint8")
        self.max_HSV = np.array([20, 255, 255], dtype = "uint8")

    def run(self):
        # start the webcam
        camera = cv2.VideoCapture(0)

        if not camera.isOpened():
            raise IOError("cannot open webcam")


        while True:
            ret, frame = camera.read()

            frame = im.resize(frame, width= 400)
            cv2.imwrite("./images/rgb.png", frame)

            #convert_to_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
            convert_to_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imwrite("./images/hsv.png", convert_to_HSV)
            dmask = cv2.inRange(convert_to_HSV, self.min_HSV, self.max_HSV)
            
            dmask = cv2.GaussianBlur(dmask, (3,3), 0)
            cv2.imwrite("./images/yao.png", dmask)

            skin = cv2.bitwise_and(frame, frame, mask= dmask)

            cv2.imshow('images', np.hstack([frame, skin]))

            cv2.imwrite("./images/test.png", skin)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()


