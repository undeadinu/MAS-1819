#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 09:35:35 2018

@author: harley_quinn
"""

#my_list=range(0,10)
#print my_list[3]
#
#my_list[0] = [0,1,2] 
#print my_list[0][2]

import sys
import math as m
import random as r



sys.path.append("..")
#print sys.path

from grlib.graphics import *

#Circles, Rectangles, Oval, Polygons, Text, Entry, Images

#def main():
#    
#    
#    sizeWidth = 1000
#    sizeHeight = 600
#    
#    
#    win = GraphWin("My Drawing", sizeWidth,sizeHeight) 
#    win.setBackground(color_rgb(100,150,150))
#    
#    c= Circle(Point(sizeWidth/2,sizeHeight/2), 50)
#    c.setFill(color_rgb(150,0,0))
#    c.setOutline(color_rgb(250,250,250))
#    c.setWidth(5)
#    c.draw(win)
#    
#    r = Rectangle(Point(100,100), Point(400,400))
#    
#    r.setFill(color_rgb(50,50,50))
#    r.setOutline(color_rgb(250,250,250))
#    r.setWidth(5)
#    r.draw(win)
#    
#    win.getMouse()
#    win.close()
#    
#  
#main()



def main():
    
    sizeW = 1000
    sizeH = 1000
    
    win = GraphWin("Swiss Flag", sizeW, sizeH)
    win.setBackground(color_rgb(250,0,0))
    
# =============================================================================
#     my_objects =[]
#     
#     
#     r1 =  Rectangle(Point(sizeW*2/5,sizeH/5), Point(sizeW*3/5, sizeH*4/5))
#     my_objects.append(r1)
#     
# #    r1.setFill(color_rgb(255,255,255))
# #    r1.setOutline(color_rgb(255,255,255))
# #    r1.setWidth(0)
# #    r1.draw(win)
#     
#     r2 = Rectangle(Point(sizeW/5, sizeH*2/5), Point(sizeW*4/5, sizeH*3/5))
#     my_objects.append(r2)
# #    r2.setFill(color_rgb(255,255,255))
# #    r2.setOutline(color_rgb(255,255,255))
# #    r2.setWidth(0)
# #    r2.draw(win)
#     
#     c=  Circle(Point(200,400), 100)
#     my_objects.append(c)
#     
# =============================================================================
    
    
# =============================================================================
#     def my_display(objects):
#     
#         for i in range(len(objects)):
#             objects[i].setFill(color_rgb(80*i,50*i,255))
#             objects[i].setOutline(color_rgb(50*i,50*i,255))
#             objects[i].setWidth(2)
#             objects[i].draw(win)
#     
#     my_display(my_objects)
#     
#     for j in range(10):
#         for i in range(len(my_objects)):
#             my_objects[i].move(20*i,50*i)
# =============================================================================
    num_x = 1
    num_y = 10
    my_circles = []
    
    for x in range (num_x):
        for y in range(num_y):
            c= Circle(Point(r.randint(0,sizeW),r.randint(0,sizeH)), r.randint(10,150))
            c.setFill(color_rgb(r.randint(0,255),r.randint(0,255),r.randint(0,255)))
            c.draw(win)
            
    win.getMouse()
    win.setBackground("yellow")      
    
    t = Text(Point(500,500),"There is no flag anymore")
    t.setFill("green")
    t.setStyle("bold")
    t.setSize(24)
    t.draw(win)
    
    
    
    
    
    

# =============================================================================
#     my_Star= Polygon(Point(100,10), Point(115,10), Point(120,0), Point(125,10), Point(140,10),Point(130,20), Point(135,35),Point(120,25), Point(105,35), Point(110,20))
#     my_Star.setFill("yellow")
#     my_Star.setOutline("yellow")
#     my_Star.draw(win)
#     
# =============================================================================
    
    
    
#    l1 = Polygon(Point(100,10),Point(115,10), Point(120,0), Point(125,10), Point(140,10),Point(130,20), Point(135,35),Point(120,25), Point(105,35), Point(110,20))
#    l1.move(100,300)
#    l1.setFill("yellow")
#    l1.setWidth(3)
#    l1.draw(win)
    
    win.getMouse()
    win.close()
    
"""    
    my_objects= []
    my_objects.append(r1)
    my_objects.append(r2)
    
    for i in range(len(my_objects)):
        my_objects[i].setFill(color_rgb(255,255,255))
        my_objects[i].setWidth(0)
        my_objects[i].draw(win)
"""        
#    my_plgn = Polygon
#    alpha = 2* m.pi /10
#    radius  = 12
#    starXY = [500,500]
    
    
#    p = []
#    print p.type()
#    for i in range(11):
#        r = radius*(i % 2 + 1)/2
#        omega=alpha*i
#        p.append((Point((r * m.sin(omega) + starXY[0]), ((r * m.cos(omega)) + starXY[1]) ) )
#    
    
#    for i in range(len(p)-1):
#        myLine= Line(p[i], p[i+1])
#        myLine.draw(win)
# =============================================================================
#     r1.move(100,100)
#     r2.move(100,100)
# =============================================================================
"""

    for i in range(60):
        r1.move(10,10)
        r2.move(10,10)
    
    t = Text(Point(500,500), "FLAG IS GONE")
    t.setFill("green")
    t.setStyle("bold")
    t.setSize(24)
    t.draw(win)
"""    
    
    
    
main()