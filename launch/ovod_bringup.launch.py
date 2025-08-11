# ovod_bringup.launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    image_topic   = LaunchConfiguration('image_topic')
    camera_index  = LaunchConfiguration('camera_index')
    log_level     = LaunchConfiguration('log_level')

    return LaunchDescription([
        # 런치 인자
        DeclareLaunchArgument('image_topic',  default_value='/image',    description='Camera image topic'),
        DeclareLaunchArgument('camera_index', default_value='0',         description='OpenCV camera index'),
        DeclareLaunchArgument('log_level',    default_value='info',      description='rcl logging level'),

        # 1) 웹캠 퍼블리셔
        Node(
            package='ovod_llm',
            executable='webcam_publisher',   # setup.py console_scripts 이름
            name='webcam_publisher',
            output='screen',
            parameters=[{'camera_index': camera_index}],
            arguments=['--ros-args', '--log-level', log_level],
            remappings=[('/image', image_topic)],
            respawn=False
        ),

        # 2) 디텍션 노드
        Node(
            package='ovod_llm',
            executable='detection_node',
            name='detection_node',
            output='screen',
            arguments=['--ros-args', '--log-level', log_level],
            remappings=[('/image', image_topic)],
            respawn=False
        ),

        # 3) LLM 노드
        Node(
            package='ovod_llm',
            executable='llm_node',
            name='llm_node',
            output='screen',
            arguments=['--ros-args', '--log-level', log_level],
            # 필요 시 remappings/parameters 추가
            respawn=False
        ),
    ])