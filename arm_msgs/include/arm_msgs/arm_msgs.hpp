#pragma once

#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/quaternion.hpp>
#include <sensor_msgs/msg/joint_state.hpp>
#include <cmath>
#include <thread>
#include <chrono>

class StatePublisher : public rclcpp::Node {
    public:
        StatePublisher();
    
    private:
        std::shared_ptr<rclcpp::Publisher<sensor_msgs::msg::JointState>> joint_publisher_;
        std::shared_ptr<rclcpp::TimerBase> timer_;

        void publish();
};
