#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#

'''
Assembly object representation
'''

import types
import identifiers

class Assembly:
  def __init__(self, name):
    self._name = name
    self._mems = {}
    self._inttemplate = types.IntegerTemplate(identifiers.Name('UInt'), self)
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

  def __str__(self):
    return "<assembly: %s>" % self._name
    
  def add_member(self, identifier, node):
    self._mems[identifier] = node
