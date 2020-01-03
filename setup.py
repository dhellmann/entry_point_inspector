#!/usr/bin/env python

PROJECT = 'entry_point_inspector'

# Change docs/source/conf.py too!
VERSION = '0.1.2'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Tool for looking at the entry point plugins on a system',
    long_description=long_description,

    author='Doug Hellmann',
    author_email='doug@doughellmann.com',

    license='ASL 2.0',

    url='https://github.com/dhellmann/entry_point_inspector',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],

    platforms=['Any'],

    scripts=[],

    provides=['entry_point_inspector',
              ],
    install_requires=[
        'cliff',
    ],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'epi = entry_point_inspector.app:main',
        ],
        'epi.commands': [
            'group_list = entry_point_inspector.group:GroupList',
            'group_show = entry_point_inspector.group:GroupShow',
            'ep_show = entry_point_inspector.ep:EntryPointShow',
        ],
    },

    zip_safe=False,
)
