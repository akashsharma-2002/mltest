from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        # Read lines and remove newline characters
        requirements = file_obj.read().splitlines()
    # Remove any editable install entries (e.g., '-e .')
    requirements = [req for req in requirements if req.strip() != '-e .']
    return requirements

setup(
    name='ML_PROJECT',
    version='0.0.1',
    author='Akash',
    author_email='akashbest2002@gmail.com',
    packages=find_packages(),  # Corrected: use 'packages' instead of 'package'
    install_requires=get_requirements('requirements.txt')  # Corrected key name
)
