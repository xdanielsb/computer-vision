#include <stdio.h>
#include <iostream>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <opencv2/nonfree/features2d.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/nonfree/features2d.hpp> //Thanks to Alessandro
using namespace cv;
void readme();
int main(  ){
  const cv::Mat input = cv::imread("input.jpg", 0); //Load as grayscale
  cv::SiftFeatureDetector detector;
  std::vector<cv::KeyPoint> keypoints;
  detector.detect(input, keypoints);
  cv::Mat output;
  cv::drawKeypoints(input, keypoints, output);
  cv::imwrite("sift_result.jpg", output);
  return 0;
}
