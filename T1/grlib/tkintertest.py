# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:04:57 2018

@author: jennyd
"""

from Tkinter import*


root = Tk() 							# Create the root (base) window 
w = Label(root, text="Hello, world!") 	# Create a label with words
w.pack() 								# Put the label into the window
root.mainloop() 						# Start the event loop