#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#

'''
Identifier classes
'''

class Name:
  def __init__(self, name):
    self._name = name

  def __str__(self):
    return '"%s"' % self._name

class List:
  def __init__(self, ids):
    pass
