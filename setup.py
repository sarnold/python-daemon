# -*- coding: utf-8 -*-

__version__ = '0.2.3'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="python-daemon",
    packages=['daemon'],
    version=__version__,
    author="Server Density",
    license="http://creativecommons.org/licenses/by-sa/3.0/",
    url="https://github.com/sarnold/python-daemon",
    description="Python daemonizer for Unix, Linux and OS X",
    platforms=["any"],
    test_suite='daemon',
    classifiers=[
        "License :: OSI Approved :: Attribution Assurance License",
        'Intended Audience :: Developers',
        'Environment :: No Input/Output (Daemon)',
        'Development Status :: 4 - Beta',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
)
