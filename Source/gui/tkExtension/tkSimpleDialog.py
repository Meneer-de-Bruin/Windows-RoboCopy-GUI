import tkinter as tk
from tkinter import ttk

import os

#from functions import generic as gF

# FROM: http://effbot.org/tkinterbook/tkinter-dialog-windows.htm
# Adjusted slightlty to use ttk for style issues
# moved to grid instead of pack
# added result (True, False, None)

class SimpleDialog(tk.Toplevel):

    def __init__(self, parent, title = None):

        tk.Toplevel.__init__(self, parent)
        
        self.transient(parent)

        self.parent = parent # To enanble return of focus
        
        if title:
            self.title(title)

        self.result = None
        
        self.__createWidgets()

        self.wait_window(self)

    def __createWidgets(self):
        body = ttk.Frame(self)
        self.initial_focus = self.body(body)
        
        body.grid()

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.escape)

        self.geometry("+%d+%d" % (self.parent.winfo_rootx()+50,
                                  self.parent.winfo_rooty()+50))

        self.initial_focus.focus_set()
        
    #
    # construction hooks


    def body(self, parent):
        # create dialog body.  return widget that should have
        # initial focus.  this method must be overridden

        pass # default - no message only ok / cancel button

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = ttk.Frame(self)

        ttk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE).grid(row=0, column=0, padx=10, pady=10)
        #ttk.Button(box, text="Annuleren", width=10, command=self.cancel).grid(row=0, column=1, padx=10, pady=10)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.escape)

        box.grid()

    #
    # standard button semantics

    def ok(self, event=None):
        self.result = True
        
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        # put focus back to the parent window
        self.escape()

    def cancel(self, event=None):
        self.result = False
        
        # put focus back to the parent window
        self.escape()
        
    def escape(self, event=None):
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override
