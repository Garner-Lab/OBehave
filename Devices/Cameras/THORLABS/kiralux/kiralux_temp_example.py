

import cv2

from kiralux_cam import KiraluxCamera
from kiralux_utilities import configure_path

configure_path()

mycam = KiraluxCamera(23234)
image = mycam.acquire_frame()
cv2.imshow('frame', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

