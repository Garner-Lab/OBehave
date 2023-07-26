# behavior-tracker

This repository contains a Python-based behavioral tracker with custom algorithms for detecting the eyes, whiskers, and body position of lab mice suspended in a simulated environment. The project is in development for the Garner Lab in the Department of Neurobiology at Harvard Medical School.

Device Setup:

THORLABS KIRALUX

The Python SDK supports Thorlabs scientific-camera series CC215, CS126, CS135, CS165, CS2100, CS235, CS505, and CS895. 

The Python SDK is a wrapper around the native SDK, which means python applications need access to the native camera DLLs.

To install the Python SDK, please follow these directions:

1. Install ThorCam and the appropriate drivers. The installer can be found at Thorlabs.com on any of the camera pages. Click on the Software tab, then on the Software button.

2. The Python SDK is provided both as an installable package and as source files. To install the Python SDK in your environment, use a package manager such as pip to install from the package file. Note that the Python SDK package must be located in your environment for installation to proceed.

 Example install command: 'python.exe -m pip install thorlabs_tsi_camera_python_sdk_package.zip'  

 Note: The Python SDK can be retrieved from the directory where Thorlabs software was originally installed on your machine.
 Example: C:\Program Files\Thorlabs\Scientific Imaging\Scientific Camera Support\Scientific Camera Interfaces\SDK\Python Toolkit

3. For this application the 64-bit DLLs are included under Devices\Cameras\THORLABS\Library_X64 and the kiralux_utils.configure_path method is used to initialize the libraries.

Alternatively, you can copy the managed DLLs from

 Scientific Camera Interfaces\SDK\DotNet Toolkit\dlls\Managed_32_lib\*.dll (for 32-bit LabVIEW)
 or
 Scientific Camera Interfaces\SDK\DotNet Toolkit\dlls\Managed_64_lib\*.dll (for 64-bit LabVIEW)