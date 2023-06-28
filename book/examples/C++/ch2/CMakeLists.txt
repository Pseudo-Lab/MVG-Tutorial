cmake_minimum_required(VERSION 3.5)

project(ch2)

find_package( OpenCV REQUIRED )
find_package (Eigen3 REQUIRED)

add_executable(ch2 test.cpp)
target_link_libraries(${PROJECT_NAME}
${OpenCV_LIBS}
${EIGEN3_LIBS}
${Eigen_LIBRARIES}
)
