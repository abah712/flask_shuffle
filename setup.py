import os
from setuptools import setup

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VERSION')) as version_file:
    version = version_file.read().strip()
    
setup(
    name='flask_shuffle',
    version=version,
    author='luciano de falco alfano',
    url='https://github.com/l-dfa/flask_shuffle',
    packages=['flask_shuffle'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

