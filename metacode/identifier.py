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

import base64
'''
import base64
.b64encode(s, altchrs)
.b64decode(s, altchrs)
altchrs to zamienne znaki dla + i /
'''

class Name:
  def __init__(self, name):
    self._name = name

  def __cmp__(self, other):
    return cmp(self.mangle(), other.mangle())
    
  def __hash__(self):
    return hash(self.mangle())
    
  def __str__(self):
    return '"%s"' % self._name
    
  def mangle(self):
    S = 'S'   # jak Symbol (N jest zarezerwowane dla Node)
    S += base64.b64encode(self._name, ['_', '$'])
    S += '.'
    return S

class List:
  def __init__(self, ids):
    self._ids = ids

  def __cmp__(self, other):
    return cmp(self.mangle(), other.mangle())
    
  def __getitem__(self, idx):
    return self._ids[idx]
    
  def __hash__(self):
    return hash(self.mangle())
    
  def __len__(self):
    return len(self._ids)
        
  def __str__(self):
    return '%s' % self._ids
    
  def mangle(self):
    S = 'L'   # jak List
    for id in self._ids:
      S += id.mangle() + '.'
    S += '.'
    return S

