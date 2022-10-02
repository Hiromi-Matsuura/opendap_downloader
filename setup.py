from setuptools import setup, find_packages

setup(
    name='opendap',
    version='0.0.1',
    lincense='MIT',
    description='This package wraps ncks command to download OISST/AVHRR data through OPeNDAP',
    author='Hiromi-Matsuura',
    packages=find_packages(),
)