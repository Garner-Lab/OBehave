
import numpy as np
import cv2

from thorlabs_tsi_sdk.tl_camera import TLCameraSDK

class CameraInstance:

    def __init__(self, serialnumber: int):
        with TLCameraSDK() as sdk:
            available = sdk.discover_available_cameras()
            helpstring = ''
            if serialnumber not in available:
                if len(available) > 0:
                    helpstring += 'Detected cameras of the following Serial Numbers:\n'
                    for sn in available:
                        helpstring += f'{sn}\n'
                else:
                    helpstring = 'No cameras were detected.'
                raise ValueError(f'Camera of SN: {serialnumber} not detected, see below for list of detected cameras:\n' + helpstring)
        self.serialnumber = serialnumber

    def acquire_frame(self):
        with TLCameraSDK() as sdk:
            with sdk.open_camera(str(self.serialnumber)) as cam:
                print('inside open cam')
                cam.operation_mode = 0
                cam.frames_per_trigger_zero_for_unlimited = 0
                cam.arm(10)
                cam.issue_software_trigger()
                image = cam.get_pending_frame_or_null()

                if image is not None:
                    buf = image.image_buffer
                    img = np.array(buf,dtype=float)/float(1023)
                    print(image.image_buffer.shape)
                    print(type(buf[0][0]))
                    print(img)
                    
                    cv2.imshow("image", img)
                
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cam.disarm()
        


