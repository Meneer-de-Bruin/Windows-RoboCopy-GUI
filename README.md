# Windows RoboCopy GUI

RoboCopy GUI is a simple frontend to RoboCopy.

The application uses a RoboCopy jobfile named "robocopy.rcj" which must be in the same directory as the application itself. This jobfile contains all options that are given to
RoboCopy. The first two rows of the jobfile must contain the following:
  /NOSD
  /NODD

A default RoboCopy jobfile has been added to the distribution.

When starting RoboCopy command the application makes a directory in the destination folder that which is equal to the source folder name. If this folder already exists files within it may be overwritten.

Also the application makes a log which has the following name: <systemdate/time>_<source folder name>.log

After having started a RoboCopy job, you can immediately start the next RoboCopy job. Each job uses resources so starting too many jobs may adversely effect other running jobs or Window processes.

# Prerequisites
RoboCopy must be installed on your machine and it must be runable from the commandline. 

The distribution was specificly made for Windows 7.

# Installation
You can download the source and make your own distribution, or you can download all files from the distribution directory and place them on your own machine. Downloading only works for windows machines. 

# Distribution
The distribution was created by running pyinstaller from the commandline in the source directory, as follows:  
python -O -m PyInstaller --clean --onefile --distpath ..\Distribution robocopygui.pyw

# Support
As  my time is extremly limited I can offer no support what-so-ever. But hey, it's free.
