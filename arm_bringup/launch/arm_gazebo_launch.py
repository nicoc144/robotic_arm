import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

'''
    Launch file for Gazebo, related nodes, drivers, etc.
'''

def generate_launch_description():

    arm_simulation_path = get_package_share_directory("arm_simulation")
    arm_gazebo_launch_path = os.path.join(arm_simulation_path, "launch")
    
    arm_gazebo_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(
    os.path.join(arm_gazebo_launch_path, "arm_sim_gazebo_launch.py")))

    return LaunchDescription([
        arm_gazebo_launch,
    ])