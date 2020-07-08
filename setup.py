#!/usr/bin/env python

from setuptools import setup
import behave_rest


long_description = open('README.rst', 'r').read()

install_requires = [
    'behave>=1.2.5',
    'requests>=2.10.0',
]

setup(
    name='behave-rest',
    version=behave_rest.__version__,
    packages=['behave_rest', 'behave_rest.steps'],
    install_requires=install_requires,
    description="BDD-style Rest API testing tool",
    long_description=long_description,
    url='https://github.com/priyankathirumalai28/restful_api_testing',
    license='Apache Software License',
    author='priyanka',
    author_email='priyanka.thirumalai28@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
