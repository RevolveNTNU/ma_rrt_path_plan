from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(packages=["ma_rrt_path_plan"], package_dir={"": "src"})

setup(**d)