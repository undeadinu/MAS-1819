#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:28:02 2018

@author: bernham
"""

#from grlib.graphics import *
import grlib.graphics as gr
from PIL import Image

#def main():
width = 800
height = 800
win = gr.GraphWin("art",width,height)

numx = 70
numy = 70
dx = float(width)/numx
dy = float(height)/numy

#img = gr.Image(gr.Point(width/2,height/2),"pics/cow.png")
img = Image.open('pics/cow.jpg')
pixel_values = img.load()
#randpixel = img.getPixel(20,20)
#img.draw(win)

iw = img.width #img.getWidth()
ih = img.height #img.getHeight()
print iw,ih
icx = float(iw)/numx
icy = float(ih)/numy

for y in range(numy):
    for x in range(numx):
        
        col = pixel_values[int(x*icx),int(y*icy)]
        rad = 0.3*col[0] + 0.59*col[1] + 0.11*col[2]
        rad = rad/255
        rad = 1-rad
        rad = rad*dx/2
        
        px = x*dx+dx/2
        py = y*dy+dy/2
        c = gr.Circle(gr.Point(px,py),rad)
        c.setFill('black')
        
        c.setWidth(0)
        c.draw(win)
    
win.getMouse()
win.close()
    
#main()
