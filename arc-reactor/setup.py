from setuptools import find_packages, setup
from update import update

with open("README.md", "r") as fh:
    long_description = fh.read()

update()

setup(
    name='arc-reactor',  
    version='1.0.10',
    author="Abhishek Ghosh",
    author_email="ghoshabhishek1640@gmail.com",
    description="A custom framework for python",
    long_description=long_description,
    install_requires=[
        'setuptools',
        'pyzip',
        'pyfolder',
        'colorama'
    ],
    long_description_content_type="text/markdown",
    url="https://github.com/Abhishek1009/python-projects/tree/master/arc-reactor",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
    'console_scripts': [
        'arc-reactor=arc_reactor.__main__:main'
        ]
    }
 )
