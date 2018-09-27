#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:28:02 2018

@author: bernham
"""

#from grlib.graphics import *
import grlib.graphics as gr
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
        #rad = 20*math.sin(float(x)/numx*math.pi + float(y)/numy*math.pi)
        lx = px-width/2
        ly = py-height/2
        d = math.sqrt(lx*lx+ly*ly)/50 
    
#        if d<0:
#            rad = 15
#        else:
#            rad = 1
        c = gr.Circle(gr.Point(px,py),d)
        c.setFill('black')
        c.draw(win)
    
win.getMouse()
win.close()
    
#main()
