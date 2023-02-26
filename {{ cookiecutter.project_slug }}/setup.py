#IMPORTANT:
#To install the package is necessary pre-install setuptools in your environment
#When you did the last, type: "pip install -e <directory-of-your-package>" in the terminal to finish the installation 
#It's necessary have the requirements.txt archive before the installation

from setuptools import setup
import os

#requirements.txt lecture
REQUIREMENTS_PATH = os.path.join(os.path.curdir,'requirements.txt')
with open(REQUIREMENTS_PATH, 'r') as f:
    requires = f.readlines()
    for i in range(len(requires)):
        requires[i] = requires[i].replace('\n','')

#setup
setup(
   name='{{ cookiecutter.project_slug }}',
   version='{{ cookiecutter.project_version }}',
   description='{{ cookiecutter.project_description }}',
   author='{{ cookiecutter.project_author_name }}',
   author_email='{{ cookiecutter.project_author_email }}',
   packages= [os.path.abspath(os.getcwd())],  # would be the same as name
   install_requires=requires #external packages acting as dependencies
)