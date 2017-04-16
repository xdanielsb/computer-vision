#include <opencv2/imgcodecs.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>
#include <stdio.h>

using namespace cv;
using namespace std;

int NUM_IMAGE = 0;
string window_name = "TRACKING PROJECT";
bool debug = false;
bool tracking = false;
bool paused = false;


int options(Mat frame){
    //cout << "LOL" << endl;
    char filename[200];
    char key = (char)waitKey(30);
    switch (key) {
    cout << key << endl;
    case 'q': //QUIT
    case 'Q': //QUIT
    case 27:  //escape key QUT
        return 0;
    case ' ': //Save an image
        sprintf(filename,"filename%.3d.jpg",NUM_IMAGE++);
        imwrite(filename,frame);
        cout << "Saved " << filename << endl;
        break;
    case 'd':
    case 'D':
        debug = !debug;
        printf(debug ? "Debug Mode Enable\n": "Debug Mode Disabled\n");
        fflush(stdout);
        break;
    case 't':
    case 'T':
        tracking = !tracking;
        printf(tracking ? "Tracking Mode Enable\n": "Tracking Mode Disabled\n");
        fflush(stdout);
        break;
    case 'p':
    case 'P':
        paused = !paused;
        printf(paused? "The pogram is Paused\n": "The program is running.\n");
        fflush(stdout);
        break;
    default:
        break;
    }
}



void show_frame(string window_name, Mat frame){
    imshow(window_name, frame);
}

void Start() {
    //Custom Video
    // string arg ="/home/daniel/Videos/version2.mkv";
    //Camera
    string arg ="0";

    VideoCapture capture(arg); //try to open string, this will attempt to open it as a video file or image sequence

    if (!capture.isOpened()) //if this fails, try to open as a video camera, through the use of an integer param
        capture.open(atoi(arg.c_str()));
    if (!capture.isOpened()) {
        cerr << "Failed to open the video device, video file or image sequence!\n" << endl;
    }
    int n = 0;
    
    cout << "Press space to save a picture. q or esc to quit" << endl;
    namedWindow(window_name, WINDOW_KEEPRATIO); //resizable window;
    //createTrackbar( "Min Threshold:", window_name, &lowThreshold, max_lowThreshold, CannyThreshold );
    Mat frame;

    for (;;) {
        capture >> frame;
        if (frame.empty())
            break;
        show_frame(window_name, frame);
        //delay N millis, usually long enough to display and capture input
        options(frame);
    }

}

int main() {
    
    Start();
    return 0;
}

