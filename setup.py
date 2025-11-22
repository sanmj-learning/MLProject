from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
            
        return requirements
    

setup(
    name="MLProject",
    version="0.0.1",
    author="Santosh Pusparaj",
    author_email="sanmj.learning@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)