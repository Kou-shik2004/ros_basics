#include "rclcpp/rclcpp.hpp"


class MyCppNode : public rclcpp::Node{
    public:
        MyCppNode() : Node("my_cpp_ros2_node"),counter(0)
        {
            RCLCPP_INFO(this->get_logger(),"Welcome to Ros 2 Cpp ");
            timer_=this->create_wall_timer(std::chrono::seconds(2),std::bind(&MyCppNode::timer_cb,this));
        }
    private:
        void timer_cb(){
            counter++;
            RCLCPP_INFO(this->get_logger(),"Hello World %d",counter);
        }
    rclcpp::TimerBase::SharedPtr timer_; //initializes a timer object using  ros2 lib
    int counter;
};
int main(int argc,char** argv){
    rclcpp::init(argc,argv);

    auto node=std::make_shared<MyCppNode>();



    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}


