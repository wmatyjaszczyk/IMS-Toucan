from setuptools import setup, find_packages
import os

with open('requirements.txt', encoding="utf8", errors='ignore') as f:
    required = f.read().splitlines()

setup(
    name='IMS-Toucan',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
)
