#!/usr/bin/env python
# -*- coding: utf-8 -*-

# job file
jobfile = "/robocopy.rcj"

# log folder
log_folder = "/log"

# command for robocopy /k
cmdline = "start cmd /c robocopy.exe /LOG:{logfile} /JOB:\"{jobfile}\" \"{source}\" \"{destination}\" &"

# Minimal length for source and destination
label_length = -100

# delim
delim_path = "/"

# info
info = { 'RI1' : 'RoboCopy started'
       }
       
# errors
errors = {'R1' : 'No batch folder selected as source.',
          'R2' : 'No folder selected as destination.',
          'R3' : 'Source and destination folder must be different.',
          'R4' : 'Destination cannot be part of source',
          'R5' : 'No robocopy job file found:\n%s'
         }
         
