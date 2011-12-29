#!/usr/bin/env python

from setuptools import setup

setup(
    name="Slushbox",
    version="0.2.1",
    author="John J. Workman",
    author_email="workman@alumni.duke.edu",
    url="https://github.com/workmajj/slushbox",
    description="Reloads web pages when files in local directories change.",
    license = "BSD 3-Clause <http://www.opensource.org/licenses/BSD-3-Clause>",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities'
    ],
    scripts=['bin/slushbox'],
    install_requires=['MacFSEvents>=0.2.4'],
    packages=['slushbox']
)
