# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:57:51 2018

@author: jennyd
"""

from graphics import*

def main():
    s_w = 800
    s_h = 800
    win = GraphWin("RGB", s_w, s_h)
    win.setBackground(color_rgb(0,0,0))
    
    div_1 = 68
    div_2 = 60
    for i in range(div_1):
        for j in range(div_2):
            c = Circle(Point(i*int(s_w/div_1),j*2*int(s_h/div_2)),10)
            c.setFill(color_rgb(i*255/div_1,j *255/div_1,0))
            c.draw(win)
            
        
    win.getMouse()  # Pause to view result.
    win.close()     # Close window when done.

main()