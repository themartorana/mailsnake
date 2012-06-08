#!/usr/bin/env python
from setuptools import setup, find_packages

import mailsnake

setup(
    name='mailsnake',
    version=mailsnake.__version__,
    description='MailChimp API v1.3 wrapper for Python.',
    long_description=open('README.rst').read(),
    author=mailsnake.__author__,
    url='https://github.com/michaelhelmick/python-mailsnake',
    packages=find_packages(),
    download_url='http://pypi.python.org/pypi/mailsnake/',
    keywords='mailsnake mailchimp api wrapper 1.3',
    zip_safe=True,
    install_requires=['simplejson'],
    py_modules=['mailsnake'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
