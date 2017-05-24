"""
    Hello User!!!
    Commands
    Key         Function
    T           Tracking
    D           Debug Activated
    F           Finish the program
    P           Pause the camera
    W           Save the image
    O           Activate ORB method
    U           Activate SURF method
    S           Activate SIFT method
    M           Visualize tracking methods

"""
from video import video_capture

if (__name__ == "__main__"):
    print(__doc__)
    video_capture()
