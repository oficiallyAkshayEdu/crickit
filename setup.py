'''
Setup Script which TRAVIS-CI runs to test project
'''

import os
import sys
# imports distribution metadata declaration method 'setup'
from distutils.core import setup

# if last argument is 'travis'
if sys.argv[-1] == 'travis':
    # invoke python interpeter and execute this file
    # store result state (1 = error, 0 = all good)

    result = os.system("python crickit/PlayCricket.py")

    # following IF statement will be executed in sequential order

    # if any stage fails what is happening?
    # IFF the above thing does not result in error
    if result == 0:
        result = os.system("python crickit/simulate.py")
    if result == 0:
        result = os.system("python crickit/tests/tests.py")

    # WHEN and IFF previous 'if' commands execute without error
    if result == 0:

        # run coverage on simulate file
        os.system("coverage run crickit/simulate.py")
        # Generate report
        os.system("coverage report")
        sys.exit()
    if result == 1: #process fails
        sys.exit()

# if testing locally
# todo find usage
if sys.argv[-1] == 'localtest':
    result = os.system("python")


def readme():
    thefile = open('docs/README.rst')
    return thefile.read()


setup(
        name = 'crickit',
        version = '0.0.126',
        # packages=['crickit, '],
        url = "https://github.com/oficiallyAkshayEdu/crickit",
        license = 'MIT',
        author = 'Akshay Agrawal',
        author_email = '',
        description = 'Text based Cricket Simulator in Python',
        long_description = readme(),
        packages = ['crickit', 'crickit/classes', 'crickit/tests']
        )
