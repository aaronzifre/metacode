#
# Copyright (C) 2014 Aaron Zifre <aaron.zifre@gmail.com>
#
# This file is a part of 'Metacode' project
# Distributed under GPLv3 license.
# See: LICENSE or http://www.gnu.org/licenses/
#


class Node:
  def __cmp__(self, other):
    return cmp(self.mangle(), other.mangle())
    
  def __hash__(self):
    return hash(self.mangle())
  
  def assembly(self):
    return self.parent().assembly()
  
  def mangle(self):
    S = 'N'   # N jak Node
    S += self.parent().mangle()
    S += self.identifier().mangle()
    S += '.'
    return S
