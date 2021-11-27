# importing necessary packages
import numpy as np
import cv2
import argparse

# parse command line arguments if any
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to video (optional)")
args = vars(ap.parse_args())

# setting the upper and lower boundaries of the HSV pixels
lower = np.array([0, 48, 80])
upper = np.array([0, 48, 80])

