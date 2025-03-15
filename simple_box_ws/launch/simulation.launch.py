import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    package_share_directory = get_package_share_directory('simple_box_ws')

    world_file = os.path.join(package_share_directory, 'worlds', 'world.sdf')

    return LaunchDescription([
        
        ExecuteProcess(
            cmd=['gz', 'sim', world_file],
            output='screen'
        )
    ])
