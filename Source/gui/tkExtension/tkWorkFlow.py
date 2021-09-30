#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########
# IMPORT #
##########
# Systeem
import sys
from sys import platform as _platform

import time

# SQL
#import sqlite3

# GUI - TKInter
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import Text

# GUI - Extensions
from gui.tkExtension import tkSimpleDialog

###########
# CLASSES #
###########

### CLASS: __workflowAPP ###
class workFlow(tk.Tk):
    def __init__(self, notebooks, about, help = None, sleep = 0):
        tk.Tk.__init__(self)
 
        self.about = about # list of about values
        self.help = help # can be empty
        
        # create GUI for workflow
        s = ttk.Style()
 
        if _platform == "win32":
            s.theme_use("vista")
        elif _platform in [ "linux", "linux2" ]:
            s.theme_use("alt")
        elif _platform == "darwin":
            s.theme_use("aqua")
  
        self.title(about.get('title'))
        self.resizable(False, False)
        
        _menubar(self, self.about, self.help)
        _workflowGUI(self, notebooks) 

        # self.deiconify()

### CLASS: _menubar ###
class _menubar(tk.Menu):
    def __init__(self, parent, about, help):
        tk.Menu.__init__(self, parent)

        self.parent = parent # Needed dialogboxes
        
        self.__createMenubar()
        
        self.parent.config(menu=self)
        
    def __createMenubar(self):
        # menu bar
        # OPTIONS <TODO>

        # HELP
        helpmenu = tk.Menu(self, tearoff=0)
        
        if (not self.parent.help == None):
            helpmenu.add_command(label="Help", command=self.__showHelpDialog)
            
        
        helpmenu.add_command(label="About", command=self.__showAboutDialog, accelerator="F1")
        self.bind_all("<F1>", lambda e: self.__showAboutDialog())  # Implement accelerator
        
        self.add_cascade(label="Help", menu=helpmenu)
        
    def __showAboutDialog(self):
        _aboutDialog(self.parent)
        
    def __showHelpDialog(self):
        _helpDialog(self.parent)
        
### CLASS: _workflowGUI ###
class _workflowGUI(ttk.Frame):
    
    def __init__(self, parent, notebooks):
        ttk.Frame.__init__(self, parent)

        #self.parent = parent # Needed for exit
        self.notebooks = notebooks # hookback to main function for creation of notebooks
        
        
        self.__createWidgets()
        self.grid()
        
    def __createWidgets(self):

        # Top buttons: About, Exit
        tFrame = ttk.Frame(self)

        #ttk.Button(tFrame, text='About', command=self.__showAboutDialog).grid(row=0, column=0,padx=10,pady=10)
        
        #if (not self.help == None):
        #    ttk.Button(tFrame, text='Help', command=self.__showHelpDialog).grid(row=0, column=1,padx=10,pady=10)
            
        # ttk.Button(tFrame, text='Exit', command=self.parent.destroy).grid(row=0, column=2,padx=10,pady=10)

        #tFrame.grid(sticky=tk.E)
        
        #tFrame = ttk.Frame(self)

        # Tabs
        notebook = ttk.Notebook(tFrame)
        notebook.enable_traversal()

        notebook.grid(padx=10,pady=10,sticky=tk.W)

        tFrame.grid(sticky=tk.W)

        # add notebooks
        self.notebooks(notebook)

class _helpDialog(tkSimpleDialog.SimpleDialog):

    """ Help dialog. Based upon standard simple dialog.
    """
                    
    def __init__(self, parent, title = None):
    
        super().__init__(parent, title)
        
    def body(self, parent):
        # overwrite standard body
        tFrame = ttk.Frame(self)
        
        ttk.Label(tFrame, text=self.parent.help, wraplength=440).grid(row=0, pady=5, sticky=tk.W)
                           
        tFrame.grid(padx=10,pady=10, row=0, column=0, sticky=tk.W)
        
    def buttonbox(self):
        # override standaard buttons

        tFrame = ttk.Frame(self)

        ttk.Button(tFrame, text="OK", width=10, command=self.cancel, default=tk.ACTIVE).grid(row=0, column=0, padx=10, pady=10)

        self.bind("<Return>", self.cancel)
        self.bind("<Escape>", self.escape)

        tFrame.grid()
        
class _aboutDialog(tkSimpleDialog.SimpleDialog):

    """ About dialog. Based upon standard simple dialog.
    """
                    
    def __init__(self, parent, title = None):   
        super().__init__(parent, title)
        
    def body(self, parent):
        # overwrite standard body

        appHighlightFont = font.Font(family='TkDefaultFont', weight='bold')
    
        tFrame = ttk.Frame(self)

        ttk.Label(tFrame, text="Program", font=appHighlightFont).grid(row=0, column=0, pady=5, sticky=tk.W )
        ttk.Label(tFrame, text=str.format("Title" )).grid(row=1, column=0, padx=10, sticky=tk.W)
        ttk.Label(tFrame, text=str.format(" : %s" % (self.parent.about.get('title'),))).grid(row=1, column=1, padx=10, sticky=tk.W)       
        ttk.Label(tFrame, text=str.format("Version" )).grid(row=2, column=0, padx=10, sticky=tk.W)
        ttk.Label(tFrame, text=str.format(" : %s" % (self.parent.about.get('version'),))).grid(row=2, column=1, padx=10, sticky=tk.W)
     
        ttk.Label(tFrame, text="Enviroment", font=appHighlightFont).grid(row=3, column=0, pady=5, sticky=tk.W ) 
        ttk.Label(tFrame, text=str.format("Platform")).grid(row=4, column=0, padx=10, sticky=tk.W)
        ttk.Label(tFrame, text=str.format(" : %s" % (_platform,))).grid(row=4, column=1, padx=10, sticky=tk.W)
        ttk.Label(tFrame, text=str.format("Python Version")).grid(row=5, column=0, padx=10, sticky=tk.W)
        ttk.Label(tFrame, text=str.format(" : %s" % (sys.version_info,))).grid(row=5, column=1, padx=10, sticky=tk.W)

        # If more then version and title in about dictionaty, print the values
        if(len(self.parent.about) > 2):
            
            ttk.Label(tFrame, text="Other", font=appHighlightFont).grid(row=6, column=0, pady=5, sticky=tk.W)

            row = 7

            for key,value in self.parent.about.items():
                if (not (key == 'version' or key == 'title')):
                            ttk.Label(tFrame, text=str.format(key)).grid(row=row, column=0, padx=10, sticky=tk.W)
                            ttk.Label(tFrame, text=str.format(" : %s" % (value,))).grid(row=row, column=1, padx=10, sticky=tk.W)
                            
                            row += 1
                    
        tFrame.grid(padx=10,pady=10, row=0, column=0, sticky=tk.W)
        
    def buttonbox(self):
        # override standaard buttons

        tFrame = ttk.Frame(self)

        ttk.Button(tFrame, text="OK", width=10, command=self.cancel, default=tk.ACTIVE).grid(row=0, column=0, padx=10, pady=10)

        self.bind("<Return>", self.cancel)
        self.bind("<Escape>", self.escape)

        tFrame.grid()                          
