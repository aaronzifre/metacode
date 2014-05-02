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

typeof = type
import identifier
import node
import value

class IntegerTemplate(node.Node):
  def __init__(self, id, parent):
    self._id = id
    self._parent = parent
    self._mems = {}
    parent.add_member(self._id, self)
    self._dbw = 32
    self._dbt = IntegerType(self, self._dbw)
    self._dbt._id = value.IntegerValue(self._dbt, self._dbw)
    self._mems[self._dbt._id] = self._dbt

  def __str__(self):
    return "<template-integer: %s>.%s" % (self._id, self._parent)

  def default(self):
    return self._dbt

  def identifier(self):
    return self._id
    
  def parent(self):
    return self._parent
    
  def print_tree(self):
    R = "IntegerTemplate: %s" % self._id
    S = ''
    for mem in self._mems.values():
      S += mem.print_tree() + '\n'
    T = ''
    for line in S.splitlines():
      T += ' ' + line + '\n'
    T = T.rstrip(' ')
    return R + '\n' + T
    
  def specialization(self, id):
    if id in self._mems: return self._mems[id]
    
    if not isinstance(id, identifier.List): raise TypeError("id should be metacode.identifier.List")
    if not len(id) == 1: raise ValueError("id should contain one identifier")
    if not isinstance(id[0], value.IntegerValue): raise ValueError("the first and the only identifier should be a metacode.value.IntegerValue")
    nbw = id[0].value()
    nit = IntegerType(self, nbw)
    nit._id = id
    self._mems[id] = nit
    return nit

class IntegerType(node.Node):
  def __init__(self, parent, width):
    self._id = None
    self._parent = parent
    self._width = width

  def parent(self):
    return self._parent
    
  def identifier(self):
    return self._id
    
  def mangle(self):
    S = 'J'   # J is type of Integer value
    S += self.parent().mangle()
    S += hex(self._width)[2:]
    S += '.'
    return S
    
  def print_tree(self):
    return str(self)

  def __str__(self):
    return "<type-integer: %s>.%s" % (self._width, self._parent)


class FunctionTemplate(node.Node):
  def __init__(self, id, parent):
    self._id = id
    self._parent = parent
    self._mems = {}
    parent.add_member(self._id, self)
    
  def __str__(self):
    return "<template-function: %s>.%s" % (self._id, self._parent)
    
  def identifier(self):
    return self._id
  
  def parent(self):
    return self._parent
  
  def print_tree(self):
    R = "FunctionTemplate: %s" % self._id
    S = ''
    for mem in self._mems.values():
      S += mem.print_tree() + '\n'
    T = ''
    for line in S.splitlines():
      T += ' ' + line + '\n'
    T = T.rstrip(' ')
    return R + '\n' + T
      
  
  def specialization(self, id):
    if id in self._mems: return self._mems[id]
    
    if not isinstance(id, identifier.List): raise TypeError("id should be metacode.identifier.List")
    if not len(id) >= 1: raise ValueError("id should contain at least one identifier")
    
    ft = FunctionType(id, self, id[0], id[1:])
    self._mems[id] = ft
    return ft

class FunctionType(node.Node):
  def __init__(self, id, parent, ret, args):
    self._id = id
    self._parent = parent
    self._ret = ret
    self._args = args
    
  def __str__(self):
    return "<type-function: %s>.%s" % (self._id, self._parent)

  def identifier(self):
    return self._id
    
  def parent(self):
    return self._parent
    
  def print_tree(self):
    return str(self)
  