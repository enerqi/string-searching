# python2 & 3 compatibility
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type # make all classes new-style in python2

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='stringsearching',
    version='0.1.0',
    description='String searching algorithms',
    long_description=readme,
    url='https://github.com/enerqi/string-searching',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
