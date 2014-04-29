#!/usr/bin/env python

#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#

from distutils.core import setup
from distutils.extension import Extension

setup(
  name='metacode',
  version='0.0',
  description='Metacode: high-level code generator',
  author='Aaron Zifre',
  author_email='aaron.zifre@gmail.com',
  maintainer='Aaron Zifre',
  maintainer_email='aaron.zifre@gmail.com',
  #url='',
  packages=['metacode'],
  ext_modules=[
    Extension('llvm',
              ['llvm/llvm.cpp'],
              libraries = ['boost_python', 'python2.7'],
              extra_compile_args = ['-std=c++11', '-stdlib=libc++'],
              extra_link_args = ['-std=c++11', '-stdlib=libc++'],
             )
  ],
  long_description='',
  license='GPLv3',
  platforms=['any'],
)

