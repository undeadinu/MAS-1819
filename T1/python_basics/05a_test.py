#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:28:02 2018

@author: bernham
"""

#from grlib.graphics import *
import grlib.graphics as gr
import random
import math

#def main():
width = 800
height = 800
win = gr.GraphWin("art",width,height)

numx = 20
numy = 20
dx = float(width)/numx
dy = float(height)/numy

for y in range(numy):
    for x in range(numx):
        px = x*dx+dx/2
        py = y*dy+dy/2
        rad = 1+ (x*y)/10.0
        #rrad = 1+random.random()*19
        c = gr.Circle(gr.Point(px,py),rad)
        c.setFill('black')
        c.draw(win)
    
win.getMouse()
win.close()
    
#main()
