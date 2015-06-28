#!/usr/bin/env python
from setuptools import setup

setup(
    name='scrst',
    version='1.0.0',
    description='Upload screenshot to AWS S3',
    author='Vladimir Rudnyh',
    author_email='dreadatour@gmail.com',
    url='https://github.com/dreadatour/scrst',
    install_requires=["Pillow", "boto"],
    scripts=['bin/scrst']
)
