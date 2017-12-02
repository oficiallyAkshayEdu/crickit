from setuptools import setup

def readme():
    thefile = open('README.rst')
    return thefile.read()

setup(
    name='crickit',
    version='0.0.1',
    packages=['crickit'],
    url="https://github.com/oficiallyAkshayEdu/crickit",
    license='MITa',
    author='Akshay Agrawal',
    author_email='',
    description='Text based Cricket Simulator in Python',
    long_description = readme()
)