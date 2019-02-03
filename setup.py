from os import path
from setuptools import setup

# read the contents of your README file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='readableID',
    version='0.0.3',
    description='Transform integer ids into readable, nonconsecutive ids',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/nziehn/readableID',
    author='Nils Ziehn',
    author_email='nziehn@mail.com',
    license='MIT',
    packages=['readableID'],
    zip_safe=False
)