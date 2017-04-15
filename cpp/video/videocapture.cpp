#include <opencv2/imgcodecs.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>
#include <stdio.h>

using namespace cv;
using namespace std;

int cont = 0;
string window_name = "video | q or esc to quit";


int options(char key, Mat frame){
    char filename[200];
    switch (key) {
    case 'q':
    case 'Q':
    case 27: //escape key
        return 0;
    case ' ': //Save an image
        sprintf(filename,"filename%.3d.jpg",cont++);
        imwrite(filename,frame);
        cout << "Saved " << filename << endl;
        break;
    default:
        break;
    }
}



void show_frame(string window_name, Mat frame){
     /// Convert the image to grayscale
    Mat  src_gray, detected_edges, dst;
    //to gray
    cvtColor( frame, src_gray, CV_BGR2GRAY );
    //blur
    blur( src_gray, detected_edges, Size(3,3) );
    
    //Now canny filter
    int lowThreshold =0;
    int const max_lowThreshold = 100;
    int ratio  = 3;
    int kernel_size  = 3;

    /// Using Canny's output as a mask, we display our result
    dst = Scalar::all(0);
    frame.copyTo( dst, detected_edges);

    Canny( detected_edges, detected_edges, lowThreshold, lowThreshold*ratio, kernel_size );

    imshow(window_name, detected_edges);
}

int process(VideoCapture& capture) {
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
        
        char key = (char)waitKey(30); //delay N millis, usually long enough to display and capture input
        options(key, frame);

    }
    return 0;
}



void addTrackBar(int, void*){
    
      createTrackbar( "Min Threshold:", window_name, &lowThreshold, max_lowThreshold, CannyThreshold );
    
}

int main(int ac, char** av) {
    
    cv::CommandLineParser parser(ac, av, "{help h||}{@input||}");
    std::string arg = parser.get<std::string>("@input");
    if (arg.empty()) {
        cout << "Write your options user." << endl;
        return 1;
    }
    VideoCapture capture(arg); //try to open string, this will attempt to open it as a video file or image sequence
    if (!capture.isOpened()) //if this fails, try to open as a video camera, through the use of an integer param
        capture.open(atoi(arg.c_str()));
    if (!capture.isOpened()) {
        cerr << "Failed to open the video device, video file or image sequence!\n" << endl;
        return 1;
    }
    process(capture);

    return 0;
}

