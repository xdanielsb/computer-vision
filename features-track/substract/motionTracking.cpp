#include <opencv2/imgcodecs.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <iostream>

using namespace std;
using namespace cv;
const static int SENSITIVITY_VALUE = 20;
const static int BLUR_SIZE = 10;
int theObject[2] = {
  0,
  0
};
Rect objectBoundingRectangle = Rect(0, 0, 0, 0);
string intToString(int number) {
  std::stringstream ss;
  ss << number;
  return ss.str();
}

void searchForMovement(Mat thresholdImage, Mat & cameraFeed) {

  bool objectDetected = false;
  Mat temp;
  thresholdImage.copyTo(temp);
  vector < vector < Point > > contours;
  vector < Vec4i > hierarchy;
  findContours(temp, contours, hierarchy, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE); // retrieves external contours
  if (contours.size() > 0) {
    objectDetected = true;
  } else {
    objectDetected = false;
  }
  if (objectDetected) {
    vector < vector < Point > > largestContourVec;
    largestContourVec.push_back(contours.at(contours.size() - 1));
    objectBoundingRectangle = boundingRect(largestContourVec.at(0));
    int xpos = objectBoundingRectangle.x + objectBoundingRectangle.width / 2;
    int ypos = objectBoundingRectangle.y + objectBoundingRectangle.height / 2;
    theObject[0] = xpos, theObject[1] = ypos;
  }
  int x = theObject[0];
  int y = theObject[1];
  circle(cameraFeed, Point(x, y), 20, Scalar(0, 255, 0), 2);
  line(cameraFeed, Point(x, y), Point(x, y - 25), Scalar(0, 255, 0), 2);
  line(cameraFeed, Point(x, y), Point(x, y + 25), Scalar(0, 255, 0), 2);
  line(cameraFeed, Point(x, y), Point(x - 25, y), Scalar(0, 255, 0), 2);
  line(cameraFeed, Point(x, y), Point(x + 25, y), Scalar(0, 255, 0), 2);
  putText(cameraFeed, "Tracking object at (" + intToString(x) + "," + intToString(y) + ")", Point(x, y), 1, 1, Scalar(255, 0, 0), 2);
}
int main() {
  bool objectDetected = false;
  bool debugMode = false;
  bool trackingEnabled = false;
  bool pause = false;
  Mat frame1, frame2;
  Mat grayImage1, grayImage2;
  Mat differenceImage;
  Mat thresholdImage;
  VideoCapture capture;
  while (1) {
    capture.open("bouncingBall.avi");
    if (!capture.isOpened()) {
      cout << "ERROR ACQUIRING VIDEO FEED\n";
      getchar();
      return -1;
    }
    while (capture.get(CV_CAP_PROP_POS_FRAMES) < capture.get(CV_CAP_PROP_FRAME_COUNT) - 1) {
      capture.read(frame1);
      cvtColor(frame1, grayImage1, COLOR_BGR2GRAY);
      capture.read(frame2);
      cvtColor(frame2, grayImage2, COLOR_BGR2GRAY);
      absdiff(grayImage1, grayImage2, differenceImage);
      threshold(differenceImage, thresholdImage, SENSITIVITY_VALUE, 255, THRESH_BINARY);
      if (debugMode == true) {
        namedWindow("Difference Image", WINDOW_KEEPRATIO);
        namedWindow("Threshold Image", WINDOW_KEEPRATIO);
        imshow("Difference Image", differenceImage);
        imshow("Threshold Image", thresholdImage);
      } else {
        try {
          destroyWindow("Difference Image");
          destroyWindow("Threshold Image");
        } catch (cv::Exception & e) {
          const char * err_msg = e.what();
          std::cout << "exception caught: " << err_msg << std::endl;
        }
      }
      blur(thresholdImage, thresholdImage, Size(BLUR_SIZE, BLUR_SIZE));
      threshold(thresholdImage, thresholdImage, SENSITIVITY_VALUE, 255, THRESH_BINARY);
      if (debugMode == true) {
        namedWindow("Final Threshold Image", WINDOW_KEEPRATIO);
        imshow("Final Threshold Image", thresholdImage);
      } else {
        try {
          destroyWindow("Final Threshold Image");
        } catch (cv::Exception & e) {
          const char * err_msg = e.what();
          std::cout << "exception caught: " << err_msg << std::endl;
        }
      }
      if (trackingEnabled) {
        searchForMovement(thresholdImage, frame1);
      }
      imshow("Frame1", frame1);
      switch (waitKey(10)) {
      case 27: //'esc' key has been pressed, exit program.
        return 0;
      case 116: //'t' has been pressed. this will toggle tracking
        trackingEnabled = !trackingEnabled;
        if (trackingEnabled == false) cout << "Tracking disabled." << endl;
        else cout << "Tracking enabled." << endl;
        break;
      case 100: //'d' has been pressed. this will debug mode
        debugMode = !debugMode;
        if (debugMode == false) cout << "Debug mode disabled." << endl;
        else cout << "Debug mode enabled." << endl;
        break;
      case 112: //'p' has been pressed. this will pause/resume the code.
        pause = !pause;
        if (pause == true) {
          cout << "Code paused, press 'p' again to resume" << endl;
          while (pause == true) {
            //stay in this loop until 
            switch (waitKey()) {
              //a switch statement inside a switch statement? Mind blown.
            case 112:
              //change pause back to false
              pause = false;
              cout << "Code resumed." << endl;
              break;
            }
          }
        }
      }
    }
    capture.release();
  }
  return 0;

}
