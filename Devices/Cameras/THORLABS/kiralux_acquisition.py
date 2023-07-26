
import numpy as np
import cv2


from kiralux_utils import KiraluxUtilities

u = KiraluxUtilities()

u.configure_path()

with TLCameraSDK() as sdk:
    print(sdk.discover_available_cameras())
    with sdk.open_camera('23234') as cam:
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