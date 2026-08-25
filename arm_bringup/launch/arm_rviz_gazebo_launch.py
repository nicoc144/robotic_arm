import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

'''
    Launch file for Gazebo and Rviz along with related nodes, drivers, etc.
'''

def generate_launch_description():

    arm_description_path = get_package_share_directory("arm_description")
    arm_urdf_path = os.path.join(arm_description_path, "urdf", "arm_4dof.urdf")
    rviz_arm_config = os.path.join(arm_description_path, "rviz", "arm_config.rviz")

    arm_simulation_path = get_package_share_directory("arm_simulation")
    arm_gazebo_launch_path = os.path.join(arm_simulation_path, "launch")

    arm_gazebo_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(
        os.path.join(arm_gazebo_launch_path, "arm_sim_gazebo_launch.py")))

    with open(arm_urdf_path, "r") as f:
        urdf_file = f.read()

    state_publish = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen", # Print INFO/WARN/ERROR to console
        parameters=[{"robot_description": urdf_file}]
    )
    
    joint_state_publish = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        output="screen" # Print INFO/WARN/ERROR to console
    )
    
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_arm_config],
        output="screen" # Print INFO/WARN/ERROR to console
    )

    return LaunchDescription([
        state_publish,
        joint_state_publish,
        rviz,
        arm_gazebo_launch,
    ])