cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

# default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(ros2_cpp_node src/my_cpp_node.cpp)

ament_target_dependencies(ros2_cpp_node rclcpp)

install(TARGETS
  ros2_cpp_node
  DESTINATION lib/${PROJECT_NAME})