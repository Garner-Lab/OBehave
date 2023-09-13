
import cv2

import pandas as pd
import numpy as np
from math import sqrt, pi

from os import listdir


def captureEye(filename, filepath):

    frame = cv2.imread(f"{filepath}/{filename}")
    initial_mask = np.full(frame.shape[:2], 0, dtype="uint8")
    cv2.circle(initial_mask, (275, 210), 120, 255, -1)
    frame = cv2.bitwise_and(frame, frame, mask=initial_mask)

    # converts the BGR color space of image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold of gray in HSV space
    lower = np.array([0, 0, 0])
    upper = np.array([0, 100, 100])

    # preparing the mask to overlay
    mask = cv2.inRange(hsv, lower, upper)

    # The black region in the mask has the value of 0,
    # so when multiplied with original image removes masked out regions
    _ = cv2.bitwise_and(frame, frame, mask = mask)

    # otsu threshold
    thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

    # apply morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)

    # invert image and calculate pupil pixels
    morph = cv2.bitwise_not(morph)
    pupil_size = np.sum(morph == 255)

    # calculate moments of binary image
    M = cv2.moments(morph)
        
    # calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    radius = sqrt(pupil_size / pi)

    return (cX, cY, radius)


csv_name = "testsheet.csv"
# filename = "grayeye.png"
filepath = "//research.files.med.harvard.edu/Neurobio/GarnerLab/Aux_Code/Ethans_Code/python_eye_tracking/movies/repo6"

df = pd.DataFrame(columns=["Pupil X", "Pupil Y", "Pupil Radius"])

count = 0
for file in listdir(filepath):
    cX, cY, radius = captureEye(file, filepath)
    print(cX, cY, radius)


