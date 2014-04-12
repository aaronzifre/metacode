# -*- coding: utf-8 -*-

#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#

'''
Integer type object
'''

import metacode.value as value

class IntegerTemplate:
  def __init__(self, identifier, parent):
    self._id = identifier
    self._parent = parent
    self._mems = {}
    parent.add_member(self._id, self)
    self._dbw = 32
    self._dbt = IntegerType()
    self._dbt._width = self._dbw
    self._dbt._id = value.IntegerValue(self._dbt, [self._dbw])
    self._mems[self._dbt._id] = self._dbt


  def print_tree(self):
    R = "IntegerTemplate: %s" % self._id
    S = ''
    for mem in self._mems.values():
      S += mem.print_tree()
    T = ''
    for line in S.splitlines():
      T += ' ' + line + '\n'
    T = T.rstrip(' ')
    return R + '\n' + T

  def __str__(self):
    return "<template-integer: %s>" % self._id

  def get_default_type(self):
    pass

  def specialization(self, id):
    pass

class IntegerType:
  def __init__(self):
    self._id = None
    self._width = 0
    pass

  def print_tree(self):
    return str(self)

  def __str__(self):
    return "<type-integer: %s>" % self._width

