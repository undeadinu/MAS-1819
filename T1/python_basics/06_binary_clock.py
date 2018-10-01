#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:15:11 2018

@author: bernham
"""

import time

#n = 5
#s = bin(n)
#
#for i in range(10):
#    print i, format(i, '#08b')[2:]
                    

current_time = time.asctime()
time_split = current_time.split(' ')
hms_string = time_split[3]
hms_split = hms_string.split(':')
hms_int = [int(x) for x in hms_split]

for e in hms_int:
    print e, format(e, '#08b')[2:]