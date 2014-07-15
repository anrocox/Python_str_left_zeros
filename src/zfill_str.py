#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

In python how to pad a numeric string with leading zeros?

En python ¿como rellenar de ceros a la izquierda un string numerico?
'''

#create a str with numbers
s = '2832'
print(s)

#generates a string of length defined, filling with zeroes the leading string
s_new = s.zfill(7)
print(s_new)

#another way is to use the rjust() method, indicating the '0' character as fill
s_new = s.rjust(7, '0')
print(s_new)
