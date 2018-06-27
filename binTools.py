# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:49:21 2018
@author: Joel Velez
"""
class binTools:
  #convert string to hex
  def strToBin(self, s):
    a_bytes = bytes(s, "ascii")
    b = ' '.join(["{0:b}".format(x) for x in a_bytes])
    return b
  
