#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#

'''
Type system package
'''

import identifier
import node
import type

class Function(node.Node):
  def __init__(self, id, parent):
    self._id = id
    self._parent = parent
    parent.add_member(id, self)
    self._mems = {}
      
  def add_member(self, id, overload):
    self._mems[id] = overload
      
  def identifier(self):
    return self._id
  
  def parent(self):
    return self._parent
  
  class Overload(node.Node):
    def __init__(self, parent, ret, args):
      self._id = identifier.List( [ret] + [ a.type() for a in args ] )
      self._parent = parent
      parent.add_member(self._id, self)
      self._ret = ret
      self._args = args
      self.code = None    # instructions to call
      self.name = None    # native name of this overload [usually a result of mangle()]
    
    def identifier(self):
      return self._id
  
    def parent(self):
      return self._parent
    
    def type(self):
      a = self.assembly()
      f = a[identifier.Name('Func')]
      s = f.specialization(self._id)
      return s
