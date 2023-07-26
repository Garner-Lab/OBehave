
import numpy as np

from thorlabs_tsi_sdk.tl_camera import TLCameraSDK

class KiraluxCamera:
    """_summary_
    """
    def __init__(self, serialnumber: int):
        """ Initializes an interactable instance of a Thorlabs Kiralux camera with the given serial number,
        if it exists.

        Args:
            serialnumber (int): The serial number of the camera which you are attempting to connect to.

        Raises:
            ValueError: If the provided serial number does not match any Thorlabs device connected to the computer.
        """
        with TLCameraSDK() as sdk: # type: ignore
            available = sdk.discover_available_cameras()
            helpstring = ''
            if str(serialnumber) not in available:
                if len(available) > 0:
                    helpstring += 'Detected cameras of the following Serial Numbers:\n'
                    for sn in available:
                        helpstring += f'{sn}\n'
                else:
                    helpstring = 'No cameras were detected.'
                raise ValueError(f'Camera of SN: {serialnumber} not detected, see below for list of detected cameras:\n' + helpstring)
        self.serialnumber = serialnumber

    def acquire_frame(self):
        """ Connects to and captures a single frame of a Kiralux Camera, will likely be replaced by __enter__ and __exit__ commands.

        Raises:
            ValueError: If the frame acquired from the camera is Null.

        Returns:
            Numpy Array: The image data captured from the frame.
        """
        with TLCameraSDK() as sdk: # type: ignore
            with sdk.open_camera(str(self.serialnumber)) as cam:
                print(f'Opening camera model {cam.model} with SN {self.serialnumber}...')
                cam.operation_mode = 0
                cam.frames_per_trigger_zero_for_unlimited = 0
                cam.arm(10)
                cam.issue_software_trigger()
                image = cam.get_pending_frame_or_null()

                if image is not None:
                    buf = image.image_buffer
                    img = np.array(buf,dtype=float)/float(1023)
                    return img
                else:
                    raise ValueError('Null frame acquired.')
                





    



