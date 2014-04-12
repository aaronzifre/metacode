# -*- coding: utf-8 -*-

#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#

'''
Integer value object
'''

class IntegerValue:
  def __init__(self, itype, data):
    self._type = itype
    self._data = data

  def __str__(self):
    return "<value-integer: %s of %s>" % self._data, self._type
