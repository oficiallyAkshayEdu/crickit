'''
Setup Script which TRAVIS-CI runs to test project
'''

import os
import sys
# imports distribution metadata declaration method 'setup'
from distutils.core import setup

# if last argument is 'travis'
if sys.argv[-1] == 'travis':

    result = os.system("python crickit/tests/tests_overall.py")

    # WHEN and IFF previous 'if' commands execute without error
    if result == 0:
        os.system("coverage run crickit/tests/tests_overall.py")
        os.system("coverage report")
        sys.exit()

    if result == 1: # if process fails
        sys.exit()

if sys.argv[-1] == 'localtest':
    # no special parameters needed for local testing yet
    pass

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
