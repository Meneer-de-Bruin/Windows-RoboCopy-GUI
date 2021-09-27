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
          'R5' : 'No robocopy job file found:\n%s',
          'R6' : 'Destination folder %s already exists'
         }
         
#help text
help = 'RoboCopy GUI is a simpel frontend to RoboCopy\n\
\n\
The application uses a RoboCopy jobfile named "robocopy.rcj" which must be in the same \
directory as the application itself. This jobfile contains all options that are given to \
RoboCopy. The first two rows of the jobfile must contain the following:\n\
  /NOSD\n\
  /NODD\n\
\n\
A default RoboCopy jobfile has been added to the distribution.\n\
\n\
When starting RoboCopy command the application makes a directory in the destination folder that \
which is equal to the source folder name. If this folder already exists files within it may be overwritten. \n\
\n\
Also the application makes a log which has the following name: <systemdate/time>_<source folder name>.log\n\
\n\
After having started a RoboCopy job, you can immediately start the next RoboCopy job. Each job uses resources so starting \
too many jobs may adversely effect other running jobs or Window processes.'