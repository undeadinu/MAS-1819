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

numx = 40
numy = 40
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
        px = x*dx+dx/2
        py = y*dy+dy/2
        c = gr.Circle(gr.Point(px,py),dx/2)
        #col = img.getPixel(int(x*icx),int(y*icy))
        col = pixel_values[int(x*icx),int(y*icy)]
        c.setFill(gr.color_rgb(col[0],col[1],col[2]))
        c.setWidth(0)
        c.draw(win)
    
win.getMouse()
win.close()
    
#main()
