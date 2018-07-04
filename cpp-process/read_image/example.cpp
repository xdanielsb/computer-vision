#include "opencv2/core.hpp"
#include "opencv2/highgui.hpp"
using namespace cv;
int main(){
    cv::Mat image = cv::imread("../assets/hand.jpg");
    cv::namedWindow("Lena", cv::WINDOW_NORMAL);
    cv::imshow("Lena", image);
    cv::waitKey();
    return 0;
}
