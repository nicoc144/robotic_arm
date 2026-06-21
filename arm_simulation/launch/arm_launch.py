import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    arm_description_path = get_package_share_directory('arm_description')
    empty_world_path = os.path.join(arm_description_path, 'sdf/empty_world.sdf')
    arm_4dof_path = os.path.join(arm_description_path, 'sdf/arm_4dof.sdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd = ['gz', 'sim', empty_world_path], # cmd = [executable, arg1, arg2, ...]
            output = 'screen'
        ),
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-file', arm_4dof_path,
                '-name', 'arm_4dof'
            ],
            output='screen'
        ),
    ])