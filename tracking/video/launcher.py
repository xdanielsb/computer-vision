"""
    Hello User!!!
    I'm daniel this software track an object in a
    video in real time, using C, bash, dynamic
    libraries, techniques of BigData, Complex
    variables, Mathematics and Machine Vision.

    Commands
    Key         Function
    T           Tracking
    D           Debug Activated
    F           Finish the program
    P           Pause the camera
    W           Save the image
    O           Activate tracking method 1
    U           Activate tracking method 2
    S           Activate tracking method 3
    M           Visualize tracking methods
    F           Follow the track object

"""
from video import video_capture

if (__name__ == "__main__"):
    print(__doc__)
    video_capture()
