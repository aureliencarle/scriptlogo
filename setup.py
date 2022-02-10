#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
    
setup(
    name='scriptsplash',
    version='1.0',
    plateformes = 'LINUX',
    packages=find_packages(),
    packages_dir = {'' : 'scriptsplash'},
    author='aureliencarle',
    description='Python Splash for Scripts',
    url='',
    download_url='https://github.com/aureliencarle/scriptsplash.git',
    license='GPL Version 3',
    keywords = ['scripts', 'ascii', 'tools', 'log'],
    classifiers = [ 'Programming Language :: Python :: 3',
                    'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                    'Operating System :: Debian',
                    'Topic :: Software Development :: User Interfaces'],
    long_description=open('README.md').read()
    )

