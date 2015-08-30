This is a set of python and shell scripts for keeping track of time and to-do
lists, based on google calendar. 

I use it day-to-day to figure out how much I worked on different projects,
and to figure out whether I can meet deadlines in the future.

Requires the following python packages:
python-gflags
datetime
httplib2
apiclient
oauth2client
matplotlib
urllib3
google-api-python-client
gcalcli

To do:
*) Create a setup.py
*) Make it so that when we install, it puts the location of the python binary into scripts like atp.py so that we can run them without the python prefix on the command line.
*) Have the setup.py script make links to the appropriate scripts in the appropriate bin directory.  Right now I just put a link to the current directory in my path.
