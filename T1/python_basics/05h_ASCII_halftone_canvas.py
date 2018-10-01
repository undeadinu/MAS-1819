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

numx = 30
numy = 30
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

charlist = [' ','.',',','n','o','#','@']
sampletuple = ()

for y in range(numy):
    for x in range(numx):
        
        col = pixel_values[int(x*icx),int(y*icy)]
        val = 0.3*col[0] + 0.59*col[1] + 0.11*col[2]
        val = val/255
        val = 1-val
        idx = int(val*(len(charlist)-1))
        #print idx
        c = charlist[idx]
        
        px = x*dx+dx/2
        py = y*dy+dy/2
        
        t = gr.Text(gr.Point(px,py),c)
        t.setSize(int(dx))
        t.draw(win)
    
win.getMouse()
win.close()
    
#main()
