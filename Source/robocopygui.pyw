#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" RoboCopy

This programma allows the user to choose the source and destination
directory via browsing and then start RoboCopy in a coomand window.
"""

__author__    = "R.J.L. de Bruin"
__copyright__ = "Copyright 2021, R.J.L. de Bruin"
__license__   = "MIT"

__version__   = "0.9.0"

__docformat__ = 'reStructuredText en'

##########
# IMPORT #
##########

# GUI - TKInter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

# Config
from config import robocopy_config as cfg

# GUI
from gui.tkExtension import tkWorkFlow

from gui import robocopyGUI

###########
# CLASSES #
###########
        
### CLASS: __workflowAPP ###
class workFlowAPP(tkWorkFlow.workFlow):

    def __init__(self):
        about = {} # init
        about['title'] = 'RoboCopy GUI'
        about['version'] = __version__
        about['author'] = __author__
        about['copyright'] = __copyright__
        about['license'] = __license__
     
                    
        super().__init__(self.notebooks, about, cfg.help)

    def notebooks(self, notebook):
        theFrame = ttk.Frame()
        robocopyGUI.robocopyGUI(theFrame)
        
        notebook.add(theFrame, text='File Selection')

########
# MAIN #
########
def main():
   
    app = workFlowAPP()
    
    # This application always, always stays on top
    app.attributes('-topmost',True)
    
    app.mainloop()

# Can be imported (needed for pydoc), but not meant to be.
if __name__ == '__main__':
  main()