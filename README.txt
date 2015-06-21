This is a set of python and shell scripts for keeping track of time and to-do
lists, based on google calendar. 

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
**) Make it so that when we install, it puts the location of the python binary into scripts like atp.py so that we can run them without the python prefix on the command line.
**) Have the setup.py script make links to the appropriate scripts in the appropriate bin directory.  Right now I just put a link to the current directory in my path.
**) We must store the credential information required by google to authenticate in a file.
The file location is currently hardcoded to /Users/pf98/gcaltimetracker.dat in two places.
We need to fix this.
