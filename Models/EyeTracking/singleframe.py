# %%timeit -n 100

from frr import FastReflectionRemoval

import cv2
import numpy as np
from math import pi, sqrt

filepath = "//research.files.med.harvard.edu/Neurobio/GarnerLab/Aux_Code/Ethans_Code/python_eye_tracking/movies/cropped_repo6"
filename = "retouched2.png"

outputfilepath = "//research.files.med.harvard.edu/Neurobio/GarnerLab/Aux_Code/Ethans_Code/python_eye_tracking/movies/filtered_repo6"

# for i in range(155):
#     frame = cv2.imread(f"{filepath}/frame_{i}.png")
#     cropped_image = frame[500:710, 550:800]
#     cv2.imwrite(f"{outputfilepath}/cropped_frame_{i}.png", cropped_image)
#     print(i)

frame = cv2.imread(f"{outputfilepath}/{filename}")

cv2.imshow("original", frame)

(h, w) = frame.shape[:2]

red = frame[:, :, 2]
equred = cv2.equalizeHist(red)
reds = np.hstack((red,equred)) #stacking images side-by-side
cv2.imshow("red", reds)

blue = frame[:, :, 0]
equblue = cv2.equalizeHist(blue)
blues = np.hstack((blue, equblue)) #stacking images side-by-side
cv2.imshow("blue", blues)

green = frame[:, :, 1]
equgreen = cv2.equalizeHist(green)
greens = np.hstack((green, equgreen)) #stacking images side-by-side
cv2.imshow("green", greens)


# cv2.imshow("dereflected", green)

# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# res = np.hstack((green, gray)) #stacking images side-by-side
# cv2.imshow("initial equalization",res)

# # cv2.imshow("repaired", result)

# newmask = cv2.inRange(green, 18, 255)

# cv2.imshow("newmask", newmask)

# green[newmask == 255] = 0

# cv2.imshow("masked green", green)

# repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,5))
# result = 255 - cv2.morphologyEx(255 - green, cv2.MORPH_CLOSE, repair_kernel, iterations=1)

# cv2.imshow("repaired green", result)

# reduced_noise = cv2.GaussianBlur(result, (7,7), 0)

# cv2.imshow("blurred repaired green", reduced_noise)

#create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(green) 
cv2.imshow('clahe_2.jpg',cl1)

equ = cv2.equalizeHist(green)
res = np.hstack((equ,cl1)) #stacking images side-by-side

clahe2 = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl2 = clahe.apply(equ) 
cv2.imshow('clahe_2.jpg',cl2)

equ2 = cv2.equalizeHist(cl1)
res = np.hstack((res, equ2, cl2)) #stacking images side-by-side
cv2.imshow("initial equalization",res)

reduced_noise = cv2.medianBlur(cl2, 3, 3)
cv2.imshow("Blurred equalization",reduced_noise)


# cv2.imwrite(f"{outputfilepath}/blurred_frame_0.png", reduced_noise)

# define the contrast and brightness value
# contrast = 5. # Contrast control ( 0 to 127)
# brightness = 2. # Brightness control (0-100)

# # call addWeighted function. use beta = 0 to effectively only
# # operate on one image
# # out = cv2.addWeighted(frame, contrast, frame, 0, brightness)

# # reduced_noise = cv2.GaussianBlur(out, (31,31), 0)

# # cv2.imshow("postblur", reduced_noise)

# cv2.imshow("out", frame)

# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# cv2.imshow("gray", gray)

#  # create a CLAHE object (Arguments are optional).
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(gray) 
# # cv2.imwrite('clahe_2.jpg',cl1)

# equ = cv2.equalizeHist(gray)
# res = np.hstack((equ,cl1)) #stacking images side-by-side
# cv2.imshow("initial equalization",equ)

# reduced_noise = cv2.GaussianBlur(equ, (15,15), 0)

# cv2.imshow("blur", reduced_noise)

# equ2 = cv2.equalizeHist(reduced_noise)
# cv2.imshow("double equalization",equ2)


# # threshold
# lower = (252)
# upper = (255)
# thresh = cv2.inRange(equ2, lower, upper)

# # apply morphology close and open to make mask
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
# morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
# morph = cv2.morphologyEx(morph, cv2.MORPH_DILATE, kernel, iterations=1)

# # floodfill the outside with black
# black = np.zeros([h + 2, w + 2], np.uint8)
# mask = morph.copy()
# mask = cv2.floodFill(mask, black, (0,0), 0, 0, 0, flags=8)[1]

# cv2.imshow("mask", mask)

# equ2[mask == 255] = (10)

# # use mask with input to do inpainting
# result1 = cv2.inpaint(equ2, mask, 900, cv2.INPAINT_TELEA)
# result2 = cv2.inpaint(equ2, mask, 900, cv2.INPAINT_NS)
# result3 = cv2.imshow("result3", equ2)
# cv2.imshow("result1", result1)
# cv2.imshow("result2", result2)


#  # create a CLAHE object (Arguments are optional).
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(result2) 
# # cv2.imwrite('clahe_2.jpg',cl1)

# equ = cv2.equalizeHist(result2)
# res = np.hstack((equ,cl1)) #stacking images side-by-side
# cv2.imshow("post glare equalization",equ)

# reduced_noise = cv2.GaussianBlur(equ, (15,15), 0)

# cv2.imshow("post glare blur", reduced_noise)

# equ2 = cv2.equalizeHist(reduced_noise)
# cv2.imshow("post glare double equalization",equ2)


cv2.waitKey(0)
cv2.destroyAllWindows