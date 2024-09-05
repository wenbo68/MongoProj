from setuptools import setup, find_packages
from typing import List

Hyphen_e = '-e .'

# def get_requirements(filename: str) -> List[str]:
#     requirements = []
#     with open(filename) as obj:
#         requirements = obj.readlines()
#         requirements = [req.replace("\n", "") for req in requirements]
        
#         if Hyphen_e in requirements:
#             requirements.remove(Hyphen_e)
    
#     return requirements

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="mongodb_connect_wenboliu",
    version="0.1.0",
    author="Wenbo",
    author_email="wenboliu68@gmail.com",
    long_description=long_description,
    # install_requires=get_requirements("requirements.txt"),
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
