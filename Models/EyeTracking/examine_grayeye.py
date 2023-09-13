

import cv2
import numpy as np

frame = cv2.imread("frames/grayeye.png")
cv2.imshow("gray eye", frame)

initial_mask = np.full(frame.shape[:2], 0, dtype="uint8")
cv2.circle(initial_mask, (275, 210), 120, 255, -1)
frame = cv2.bitwise_and(frame, frame, mask=initial_mask)

cv2.imshow("mask", frame)

(h, w) = frame.shape[:2]

# converts the BGR color space of image to HSV color space
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

print(hsv[0][0])

# Threshold of gray in HSV space
lower = np.array([0, 0, 0])
upper = np.array([0, 100, 100])

# preparing the mask to overlay
mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(frame, frame, mask = mask)

cv2.imshow("mask", mask)
cv2.imshow("post-mask", result)

# display pixel format
print(frame[0][0])

cv2.waitKey(0)
cv2.destroyAllWindows