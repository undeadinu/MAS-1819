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
#win = gr.GraphWin("art",width,height)

numx = 120
numy = 70
dx = float(width)/numx
dy = float(height)/numy

#img = gr.Image(gr.Point(width/2,height/2),"pics/cow.png")
img = Image.open('pics/blob.png')
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
    rowstring = ""
    for x in range(numx):
        
        col = pixel_values[int(x*icx),int(y*icy)]
        val = 0.3*col[0] + 0.59*col[1] + 0.11*col[2]
        val = val/255
        idx = int(val*(len(charlist)-1))
        #print idx
        c = charlist[idx]
        rowstring = rowstring+c
        
    print rowstring
#        px = x*dx
#        py = y*dy+dy/2
#        
#        l = gr.Line(gr.Point(px,py),gr.Point(px+dx,py))
#        l.draw(win)
#        l.setWidth(rad*2)
    
#win.getMouse()
#win.close()
    
#main()
