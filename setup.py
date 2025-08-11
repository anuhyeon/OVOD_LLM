from setuptools import setup

package_name = 'ovod_llm'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ######################추가 launch로 한번에 실행####################
        ('share/' + package_name + '/launch', ['launch/ovod_bringup.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rcv',
    maintainer_email='rcv@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detection_node = ovod_llm.detection_node:main',
            'webcam_publisher = ovod_llm.camera_node:main',
            'llm_node = ovod_llm.llm_node:main'

        ],
    },
)
