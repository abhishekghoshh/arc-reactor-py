from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='arc-reactor-utility',  
    version='1.0.0',
    author="Abhishek Ghosh",
    author_email="ghoshabhishek1640@gmail.com",
    description="Utility functions for python",
    long_description=long_description,
    install_requires=[

    ],
    long_description_content_type="text/markdown",
    url="https://github.com/Abhishek1009/python-projects/tree/master/arc-reactor-utility",
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
        ]
    }
 )
