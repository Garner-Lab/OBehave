import cv2
import numpy as np

from kiralux_cam import KiraluxCamera
from kiralux_utilities import configure_path

configure_path()

mycam = KiraluxCamera(23234)

with mycam:
    mycam.cam.roi = [500, 0, 1080, 1240]
    # mycam.begin_record()
    counter = 0
    mycam.cam.operation_mode = 0
    mycam.cam.frames_per_trigger_zero_for_unlimited = 1
    mycam.cam.arm(10)
    # mycam.cam.exposure_time_us = 5000
    mycam.cam.image_poll_timeout_ms = 0

    while(True):
        # print('Recording...')
        mycam.cam.issue_software_trigger()
        image = mycam.cam.get_pending_frame_or_null()

        # print(mycam.cam.get_measured_frame_rate_fps())
        if image is not None:
            print(image.image_buffer[0][0])
            buf = image.image_buffer
            img = np.array(buf,dtype=float)/float(1023)
            cv2.imshow("image", img)
            cv2.waitKey(1)
            # print(counter)
            counter += 1
            
        else:
            print('null')

     

