#To install the package is necesary pre-install setuptools in your environment
#When you did the last, type: "pip install -e" in the terminal to finish the installation 

from setuptools import setup
import os

#requirements.txt lecture
REQUIREMENTS_PATH = os.path.join(os.path.curdir,'requirements.txt')
with open(REQUIREMENTS_PATH, 'r') as f:
    requires=[]
    for i in range(len(f)): 
        requires.append(f.read())

#setup
setup(
   name={{ cookiecutter.project_slug }},
   version={{ cookiecutter.project_version }},
   description={{ cookiecutter.project_description }},
   author={{ cookiecutter.project_author_name }},
   author_email={{ cookiecutter.project_author }},
   packages= [{{ cookiecutter.project_slug }}],  # would be the same as name
   install_requires=requires #external packages acting as dependencies
)