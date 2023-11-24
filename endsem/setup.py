from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'endsem'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('urdf/*')),
        (os.path.join('share', package_name), glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shravya',
    maintainer_email='shravya@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            'square_turtle = endsem.square_drawer:main',
            'circle_turtle = endsem.circle_drawer:main',
            'spiral_turtle = endsem.spiral_drawer:main',
            'triangle_turtle = endsem.triangle_drawer:main',
            'concircle = endsem.continue_circle:main',
            'turtlesim_controller = endsem.turtle_controller:main',
            'add_two_ints_server = endsem.add_two_ints_server:main',
            'add_two_ints_client = endsem.add_two_ints_client:main',
            'tri_continue = endsem.continous_triangle:main',
            'squa_continue = endsem.continous_square:main',
            
        ],
    },
)
