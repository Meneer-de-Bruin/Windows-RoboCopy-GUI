# Windows-RoboCopy-GUI

# RoboCopy GUI
RoboCopy GUI is a simpel frontend to RoboCopy.

The application uses a RoboCopy jobfile named "robocopy.rcj" which must be in the same directory as the application itself. This jobfile contains all options that are given to
RoboCopy. The first two rows of the jobfile must contain the following:
  /NOSD
  /NODD

A default RoboCopy jobfile has been added to the distribution.

When starting RoboCopy command the application makes a directory in the destination folder that which is equal to the source folder name. If this folder already exists files within it may be overwritten.

Also the application makes a log which has the following name: <systemdate/time>_<source folder name>.log

After having started a RoboCopy job, you can immediately start the next RoboCopy job. Each job uses resources so starting too many jobs may adversely effect other running jobs or Window processes.

# Prerequisites
RoboCopy must be installed on your Windows machine and it must be runable from the commandline.

# Distirbution
The distrobution was create by running pyinstaller from the commandline in the source directory:
python -O -m PyInstaller --clean --onefile --distpath ..distpath ..\Distribution robocopygui.pyw
