import os
import sys

from thorlabs_tsi_sdk.tl_camera import TLCameraSDK

class KiraluxUtilities:

    def __init__(self):
        self.sdk = TLCameraSDK()

    def configure_path(self):
        """ 
        Adds THORLABS library path to current environment PATH
        Note: Assumes DLLs are contained in Library_X64 subdirectory of current directory
        """
        # is_64bits = sys.maxsize > 2**32
        relative_path_to_dlls = '.' + os.sep + 'Library_X64' + os.sep

        # if is_64bits:
        #     relative_path_to_dlls += '64_lib'
        # else:
        #     relative_path_to_dlls += '32_lib'

        absolute_path_to_file_directory = os.path.dirname(os.path.abspath(__file__))

        absolute_path_to_dlls = os.path.abspath(absolute_path_to_file_directory + os.sep + relative_path_to_dlls)

        os.environ['PATH'] = absolute_path_to_dlls + os.pathsep + os.environ['PATH']
        self.dllpath = absolute_path_to_dlls + os.pathsep + os.environ['PATH']

        try:
            # Python 3.8 introduces a new method to specify dll directory
            os.add_dll_directory(absolute_path_to_dlls)
        except AttributeError:
            pass



