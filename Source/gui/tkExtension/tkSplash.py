#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__   = "1.0.0"

__author__    = "Rob de Bruin"
__copyright__ = "Copyright 2018, Koninklijke Bibliotheek"

__docformat__ = 'reStructuredText en'

"""
::todo: capture and handle errors.

"""

##########
# IMPORT #
##########
import tkinter as tk
from tkinter import ttk

# from PIL import Image, ImageTk

#########
# CLASS #
#########

### CLASS: __Splash ###
class Splash(tk.Toplevel):
    def __init__(self, parent, splash_image, splash_text):
        tk.Toplevel.__init__(self, parent)

        self.parent = parent
        self.splash_image = splash_image
        self.splash_text = splash_text

        self.__initWindow()
        self.__createWidgets()

        self.update()

    def __initWindow(self):
        self.overrideredirect(True)

        self.geometry("+%d+%d" % (self.parent.winfo_rootx()+50,
                                  self.parent.winfo_rooty()+50))

    def __createWidgets(self):

        # logo
        # img = ImageTk.PhotoImage(Image.open(self.splash_image))

        # logo=tk.Label(self, image=img)
        # logo.image = img
        # logo.grid(row=0, column=0, padx=10, pady=10)

        # banner
        banner = tk.Label(self, text=self.splash_text, font=("TkDefaultFont", 20)).grid(row=1, column=0, padx=10, pady=10)
