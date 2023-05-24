from setuptools import setup

package_name = 'py_image_flip'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools','rclpy', 'sensor_msgs', 'cv2','cv_bridge'],
    zip_safe=True,
    maintainer='gabriel',
    maintainer_email='brinkmanngabriel@yahoo.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_flip_node = py_image_flip.image_flip_node:main'
        ],
    },
)
