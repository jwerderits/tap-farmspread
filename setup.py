#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-farmspread',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Farmspread API',
      author='Jacob Werderits',
      url='http://github.com/jwerderits',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_farmspread'],
      install_requires=[
          'tap-framework==0.0.4',
      ],
      entry_points='''
          [console_scripts]
          tap_farmspread=tap_farmspread:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_farmspread': [
              'schemas/*.json'
          ]
      })
