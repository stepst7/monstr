#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Monstr',
      version='1.0',
      description='Monitoring Framework for Tier1',
      author='JINR',
      author_email='gavelock@gmail.com',
      url='https://www.python.org',
      #packages=['Monstr'],
#      package_data={'': ['*.html', '*.css', '*.js']},
      include_package_data = True,
      packages=find_packages(),
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
     )
