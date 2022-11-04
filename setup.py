from setuptools import setup, find_packages

setup(
    author='Levent Soykan',
    description='Package of helper tools for data science and python',
    name='leventools',
    version='0.1.0',
    packages=find_packages(include=['leventools', 'leventools.*'])
)
