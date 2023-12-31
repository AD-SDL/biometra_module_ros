import os
from setuptools import setup, find_packages
from glob import glob

package_name = 'biometra_client'

setup(
    name='biometra_client',
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=[],
    zip_safe=True,
    python_requires=">=3.8",
    maintainer='',
    maintainer_email='ravescovi@anl.gov',
    description='',
    url='https://github.com/AD-SDL/biometra_module.git', 
    license='MIT License',
    entry_points={ 
        'console_scripts': [
            'biometra_client = biometra_client.biometra_client:main',
        ]
    },
)
