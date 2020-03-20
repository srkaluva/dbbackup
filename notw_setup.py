from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='dbbackup',
    version='0.1.0',
    author='Santosh Kaluva',
    author_email='skaluva16@gmail.com',
    description='utility for backing up db(Postgres)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/srkaluva/dbbackup',
    packages=find_packages('src'),
    package_dir={' ':'src'},
    install_requires=['boto3'],
    entry_points={'console_scripts': ['dbbackup=dbbackup.cli:main']},

  )

