# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:42:29 2018

@author: jennyd
"""

import sys
sys.path.append('C:\\Users\\jennyd\\Documents\\DavidJenny\\GIT\\MAS-1819\\T1\\grlib')

from graphics import*

# =============================================================================
# def main():
#     
#     size_width = 1000
#     size_height = 500
#     
#     win = GraphWin("Flag", size_width, size_height)
#     win.setBackground(color_rgb(100,150,150))
#     
#     c = Circle(Point(size_width/2,size_height/2), 50)
#     c.setFill(color_rgb(255,0,0))
#     c.setOutline(color_rgb(255,255,255))
#     c.draw(win)
#     
#     r = Rectangle(Point(100,100), Point(400,400))
#     r.setFill(color_rgb(100,100,100))
#     r.setOutline(color_rgb(200,200,200))
#     r.draw(win)
#     
#     win.getMouse()  # Pause to view result.
#     win.close()     # Close window when done.
#     
# main()
# =============================================================================


def main():
    s_w = 500
    s_h = 500
    len_edge = s_w * 2 / 3
    b = s_w/5
    
    
    win = GraphWin("CH-flag", s_w, s_h)
    win.setBackground(color_rgb(232,27,0))
    
    r_1 = Rectangle(Point(s_w/2 - len_edge/2, s_h/2 - b/2), Point(s_w/2 + len_edge/2,s_h/2 + b/2))
    r_1.setFill(color_rgb(255,255,255))
    r_1.setOutline(color_rgb(255,255,255))
    r_1.draw(win)
    
    r_2 = Rectangle(Point(s_w/2 - b/2, s_h/2 - len_edge/2), Point(s_w/2 + b/2, s_h/2 + len_edge/2))
    r_2.setFill(color_rgb(255,255,255))
    r_2.setOutline(color_rgb(255,255,255))
    r_2.draw(win)
    
    win.getMouse()  # Pause to view result.
    win.close()     # Close window when done.

main()