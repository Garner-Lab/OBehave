import cv2
import numpy as np

from kiralux_cam import KiraluxCamera
from kiralux_utilities import configure_path

configure_path()

mycam = KiraluxCamera(23234)

with mycam:
    mycam.begin_record()
    while(True):
        print('Recording...')
        image = mycam.cam.get_pending_frame_or_null()

        if image is not None:
            buf = image.image_buffer
            img = np.array(buf,dtype=float)/float(1023)
            cv2.imshow("image", img)
            cv2.waitKey(1)
        else:
            raise ValueError('Null frame acquired.')

     

