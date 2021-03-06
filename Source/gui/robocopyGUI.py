#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########
# IMPORT #
##########

# tkinter #
import tkinter as tk
from tkinter import ttk, HORIZONTAL
from tkinter import filedialog
from tkinter import messagebox

# system #
import os
import subprocess
import pathlib

# date and time
from datetime import datetime

# configuration #
from config import robocopy_config as cfg

###########
# CLASSES #
###########    
        
### CLASS: robocopyGUI ###
class robocopyGUI(ttk.Frame):
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
      
        self.parent = parent
        
        self.sourcePath = tk.StringVar()
        self.destPath = tk.StringVar()
        
        self.__createWidgets()
        self.grid()

        self.update()
              
    def __createWidgets(self):

        ### Source ###
        tFrame = ttk.Frame(self)
         
        ttk.Label(tFrame, text="Source", width=10).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        ttk.Label(tFrame, textvariable=self.sourcePath, borderwidth=2, width=cfg.label_length).grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)
        
        ttk.Button(tFrame, text="Source", command=self.__selectSource).grid(row=0, column=2, sticky=tk.E, padx=10, pady=10)
        
        tFrame.grid(sticky=tk.W)
       
        ### Destination ###
        tFrame = ttk.Frame(self)
         
        ttk.Label(tFrame, text="Destination", width=10).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        ttk.Label(tFrame, textvariable=self.destPath, borderwidth=2, width=cfg.label_length).grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)
        
        ttk.Button(tFrame, text="Destination", command=self.__selectDest).grid(row=0, column=2, sticky=tk.E, padx=10, pady=10)
        
        tFrame.grid(sticky=tk.W)
        
        ### Action ###
        tFrame = ttk.Frame(self)
        
        ### Start robocopy button ###
        ttk.Button(tFrame, text="Start RoboCopy", command=self.__startRobocopy).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        tFrame.grid(sticky=tk.W)
       

    # BUTTON COMMANDS
    def __startRobocopy(self):
        # check src folder selected
        src = self.sourcePath.get()
        
        if (not src):
            self.__showError(cfg.errors['R1'])
            return
        
        # batch (src folder - without path)
        batch = src.split(cfg.delim_path)[-1]
        
        # check if a folder was selected - batch must be filled
        if (batch == ""):
            self.__showError(cfg.errors['R1'])
            return 
            
        # check dst folder selected
        dst = self.destPath.get()
        
        if (not dst):
            self.__showError(cfg.errors['R2'])
            return
        
        # add batch to destination
        dst += '/' + batch
        
        # check that src and dst are not the same
        if (src == dst):
            self.__showError(cfg.errors['R3'])
            return        
        
        # check if src folder not part of dst
        if (src in dst):
            self.__showError(cfg.errors['R4'])
            return  
                   
        # check if dst already exists
        # give warning an option to stop
        if(os.path.isdir(dst)):
            # give warning
            if(self.__showQuestion(cfg.errors['R6'], dst) == False):
                return
        
        # determine logfile
        # determine and check log_path
        home_path = os.getcwd()
        log_path = home_path+cfg.log_folder+'/'
        
        # check if log directory exists if not make it
        if (not os.path.isdir(log_path)):
            try:
                os.makedirs(log_path)
            except Exception as e:
                self.__showError(str(e))
                return
            
        # date_time
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")

        logfile = '"'+log_path+date_time+'_'+batch+'.log"'

        # determine jobfile
        jobfile = home_path+cfg.jobfile
                
        # check if job file exists
        if (not os.path.isfile(jobfile)):
            self.__showError(cfg.errors['R5'], jobfile)
            return

        # copy to log directory
        log_jobfile=log_path+date_time+'_'+batch+'.rcj'
    
        # copy file with own function check if returns True

        try:
            self.__copyrcj(jobfile, log_jobfile)
        except Exception as e:
            self.__showError(str(e))
            return
        
        # construct cmdline
        cmdline = cfg.cmdline.format(logfile=logfile, jobfile=log_jobfile, source=src, destination=dst)

            
        # check if robocopy OK - and start or stop    
        if( self.__showQuestion("Start :\n"+cmdline) == True):
            # OK - run robocopy
            try:
                subprocess.run(cmdline, shell=True)
            except Exception as e:
                self.__showError(str(e))
                return
            
            # clear source - ready for next batch selection
            self.sourcePath.set('')
          
        # else
          # NOK
          # no action - return (automatic)

    def __copyrcj(self, src, dst):
        # open src for reading
        try:
            f_src = open(src, "r")
        except Exception as e:
            raise
        
        # open dst for writing
        try:
            f_dst = open(dst, "w")
        except Exception as e:
            raise
 
        try: 
            # write /NOSD and /NODD to dst
            f_dst.write("/NOSD\n")
            f_dst.write("/NODD\n")
            
        except Exception as e:
            raise
        
        # for all lines in src -> write to dst
        for line in f_src:
            # if line contains /NOSD or /NODD then skip
            if ("/NOSD" not in line and "/NODD" not in line):
                try:
                    f_dst.write(line)
                except Exception as e:
                    raise
        
        f_src.close()
        f_dst.close()
        
    def __selectSource(self):
        filename = filedialog.askdirectory()
        
        self.sourcePath.set(filename)
        
    def __selectDest(self):
        filename = filedialog.askdirectory()
        
        self.destPath.set(filename)
        
    def __showInfo(self, msg_string, *args):
      msg = str.format(msg_string % (args))

      tk.messagebox.showinfo("Info", msg) 

    def __showError(self, msg_string, *args):
      msg = str.format(msg_string % (args))

      tk.messagebox.showerror("Error", msg)
      
    def __showQuestion(self, msg_string, *args):
        msg = str.format(msg_string % (args))
        
        MsgBox = tk.messagebox.askquestion ("Info", msg)
        if (MsgBox == 'yes'):
            return True
        else:
            return False