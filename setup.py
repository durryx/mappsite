from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='mappsite',
    version='0.1.0',
    description='provide the tree hierarchical view of a given website',
    long_description=readme,
    author='Giovanni Durante',
    author_email='giovanni3durante@gmail.com',
    url='',
    packages=find_packages(exclude=('test', 'docs')),
    install_requires=[

    ]
)