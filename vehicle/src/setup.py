from setuptools import setup

package_name = 'vehicle_pkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Denis Darquennes, Sebastien Dupont',
    author_email='denis.darquennes@cetic.be, sebastien.dupont@cetic.be',
    maintainer='Denis Darquennes, Sebastien Dupont',
    maintainer_email='denis.darquennes@cetic.be, sebastien.dupont@cetic.be',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='MUT4SEC Demo test mutation.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vehicle = vehicle_pkg.vehicle:main'
            ],
    },
)
