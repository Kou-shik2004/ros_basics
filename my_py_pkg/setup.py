from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='koushik',
    maintainer_email='koushik20040804@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ "first_py_node=my_py_pkg.my_sample_node:main","simple_publisher=my_py_pkg.my_simple_publisher:main","simple_subscriber=my_py_pkg.my_simple_subscriber:main",
        "simple_service=my_py_pkg.simple_service_server:main","simple_client=my_py_pkg.simple_service_client:main",
        ],
    },
)
