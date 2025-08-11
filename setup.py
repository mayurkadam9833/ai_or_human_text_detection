import os 
from typing import List 
from setuptools import setup,find_packages


def get_requirements()->List[str]:
    requiremnets_lst:List[str]=[]
    try:
        with open("requirements.txt","r")as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement != "-e .":
                    requiremnets_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt not found !!!!!!!!")

    return requiremnets_lst


setup(version="0.0.1",
    author="Mayur",
    packages=find_packages(),
    install_requires=get_requirements())
