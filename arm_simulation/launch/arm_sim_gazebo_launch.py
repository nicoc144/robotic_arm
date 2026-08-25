import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

'''
    Launch file for Gazebo simulation only
'''

def generate_launch_description():

    arm_description_path = get_package_share_directory("arm_description")
    empty_world_path = os.path.join(arm_description_path, "sdf", "empty_world.sdf")
    arm_4dof_path = os.path.join(arm_description_path, "urdf/arm_4dof.urdf")

    gz_sim = ExecuteProcess(
        cmd = ["gz", "sim", "-r", empty_world_path], # cmd = [executable, arg1, arg2, ...]
        output = 'screen'
    )

    create_node = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-file", arm_4dof_path,
            "-name", "arm_4dof"
        ],
        output="screen"
    )

    return LaunchDescription([
        gz_sim,
        TimerAction(period=3.0, actions=[create_node]),
    ])