#include <opencv2/opencv.hpp>
#include <eigen3/Eigen/Dense>
#include <iostream>

int main()
{
	std::cout << "OpenCV version : " << CV_VERSION << std::endl;

	cv::Mat img; 
	img = cv::imread("../../images/Lenna.png");

	
	if (img.empty())
	{
		std::cerr << "Image load failed" << std::endl;
		return -1;
	}
    Eigen::MatrixXd matrix_input_a;


	cv::namedWindow("image"); 
	cv::imshow("image", img); 

	cv::waitKey(); 

	return 0;
}