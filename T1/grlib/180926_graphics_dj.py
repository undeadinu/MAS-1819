# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:42:29 2018

@author: jennyd
"""

import sys
sys.path.append('C:\\Users\\jennyd\\Documents\\DavidJenny\\GIT\\MAS-1819\\T1\\grlib')

from graphics import*

def main():
    win = GraphWin("Flag", 100, 100)
    win.setBackground("red")
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()
    
main()