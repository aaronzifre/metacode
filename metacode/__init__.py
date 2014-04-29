#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#

"""
Main Metacode package for some most important things...
"""

__version__ = '0.0'


import type
import identifier

class Assembly:
  def __init__(self, name):
    self._name = name
    self._mems = {}
    self._inttemplate = type.IntegerTemplate(identifier.Name('UInt'), self)
    self._funtemplate = type.FunctionTemplate(identifier.Name('Func'), self)
    # TODO TODO TODO
    # create int type

  def print_tree(self):
    R = 'Assembly: %s' % self._name
    S = ''
    for mem in self._mems.values():
      S += mem.print_tree()
    T = ''
    for line in S.splitlines():
      T += ' ' + line + '\n'
    T = T.rstrip(' ')
    return R + '\n' + T

  def __getitem__(self, idx):
    return self._mems[idx]
    
  def __str__(self):
    return "<assembly: %s>" % self._name
    
  def add_member(self, identifier, node):
    self._mems[identifier] = node
    
  def mangle(self):
    return 'A' + '.'  # jak Assembly


