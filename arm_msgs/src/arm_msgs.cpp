#include <arm_msgs/arm_msgs.hpp>

using namespace std::chrono_literals;

StatePublisher::StatePublisher() : Node("state_publisher") {

    joint_publisher_ = this->create_publisher<sensor_msgs::msg::JointState>("joint_states", 10);

    RCLCPP_INFO(this->get_logger(), "Starting state_publisher node.");

    timer_ = this->create_wall_timer(33ms, [this](){ this->publish(); });
};

void StatePublisher::publish() {

    sensor_msgs::msg::JointState joint_state;

    const auto ts = this->get_clock()->now();

    joint_state.name = {"shoulder_joint_yaw", "shoulder_joint_pitch", "elbow_joint", "wrist_joint"};
    joint_state.position = {shoulder_joint_yaw, shoulder_joint_pitch, elbow_joint, wrist_joint};

    joint_publisher_->publish(joint_state);

    RCLCPP_INFO_THROTTLE(this->get_logger(), *this->get_clock(), 1000, "Publishing joint_state on joint_states topic.");
}

int main(int argc, char ** argv) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<StatePublisher>());
  rclcpp::shutdown();
  return 0;
}