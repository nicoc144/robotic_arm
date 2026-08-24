import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import FileContent, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    arm_description_path = get_package_share_directory('arm_description')
    arm_4dof_path = os.path.join(arm_description_path, 'urdf/arm_4dof.urdf')
    
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    return LaunchDescription([
        Node(
            package = 'robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': arm_4dof_path}],
            arguments=[arm_4dof_path],
        ),
        Node(
            package='arm_msgs',
            executable='arm_msgs',
            name='arm_msgs',
            output='screen'
        ),
    ])