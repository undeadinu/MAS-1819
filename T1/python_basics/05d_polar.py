#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:28:02 2018

@author: bernham
"""

#from grlib.graphics import *
import grlib.graphics as gr
from PIL import Image
import math

#def main():
width = 800
height = 800
win = gr.GraphWin("art",width,height)

numrings = 20
dr = width/2.0 / numrings

for r in range(1,numrings):
    circum = r*dr*2*math.pi
    numrays = int(circum/dr)
    da = math.pi*2/numrays
    for a in range(numrays):
        px = width/2 + r*dr * math.cos(a*da)
        py = height/2 + r*dr * math.sin(a*da)
        c = gr.Circle(gr.Point(px,py),10)
        c.setFill('black')
        c.setWidth(0)
        c.draw(win)
    
win.getMouse()
win.close()
    
#main()
