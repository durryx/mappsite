from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='mappsite',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Giovanni Durante',
    author_email='giovanni3durante@gmail.com',
    url='',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[

    ]
)