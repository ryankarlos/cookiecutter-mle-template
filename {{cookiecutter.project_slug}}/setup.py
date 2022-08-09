
from setuptools import find_packages, setup
with open('requirements.txt', 'r') as f:
    req = [p.strip('\n') for p in f.readlines()]

with open('requirements_dev.txt', 'r') as f:
    opt = [p.strip('\n') for p in f.readlines()]

setup(
    name='src',
    packages=find_packages(),
    install_requires=req,
    extras_require ={'dev': opt},
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{{ cookiecutter.open_source_license }}'
)
