#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#

'''
Value system package
'''

class IntegerValue:
  def __init__(self, type, value):
    if value < 0: raise ValueError('metacode.type.IntegerValue can contain only non-negative integers')
    self._type = type
    self._value = value

  def __repr__(self): return str(self)
    
  def __str__(self):
    return "<value-integer: %s of %s>" % (self._value, self._type)

  def mangle(self):
    return 'I' + self._type.mangle() + hex(self._value)[2:] + '.'
    
  def value(self):
    return self._value