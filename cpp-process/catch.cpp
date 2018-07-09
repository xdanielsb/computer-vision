#include "opencv2/core.hpp"
#include "opencv2/highgui.hpp"
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
int main(){
  try{
  }
  catch( cv::Exception& e ){
      const char* err_msg = e.what();
      std::cout << "exception caught: " << err_msg << std::endl;
  }
}
