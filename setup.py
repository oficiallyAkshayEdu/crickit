from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='crickit',
    version='0.0.2',
    packages=['crickit'],
    url="https://github.com/oficiallyAkshayEdu/crickit",
    license='MITa',
    author='Akshay Agrawal',
    author_email='',
    description='Text based Cricket Simulator in Python',
    long_description = readme()
)
