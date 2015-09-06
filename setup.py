# -*- coding: utf-8 -*-
"""
In order to create a link in your site package dir. run 'python setup.py develop'
Or 'python setup.py install' when one is not in dev mode
"""
from setuptools import setup, find_packages

setup(
    name = "qsforex",
    version = "0.0",
    packages = find_packages() +  ['resources'],
    include_package_data = True
)