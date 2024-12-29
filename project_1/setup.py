from setuptools import find_packages, setup
from typing import List
import os

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the given file path.
    It also removes the '-e .' line if present, which indicates editable installations.
    '''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = [req.strip() for req in file_obj.readlines() if req.strip()]
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("Requirements:", requirements)  # Debugging output
    return requirements

long_description = ""
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    print("Warning: README.md file not found.")

# Debugging output
print("Reading requirements from requirements.txt...")
if os.path.exists('requirements.txt'):
    print("requirements.txt found.")
else:
    print("requirements.txt not found.")

requirements = get_requirements('requirements.txt')
print("Requirements read:", requirements)  # Debugging output

setup(
    name='mlprojects',
    version='0.0.1',
    author='bhupen',
    author_email='bhupenparmar192@gmail.com',
    description="A machine learning project",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bhupencoD3/ds-portfolio/blob/main/project_1',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)