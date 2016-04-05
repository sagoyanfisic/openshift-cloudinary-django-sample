from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6','MySQL-python','cloudinary']

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='cloudinary_example',
      version='1.0',
      description='test',
      author='Your Name',
      author_email='yancel moises',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

