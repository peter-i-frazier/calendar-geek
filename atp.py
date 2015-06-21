#!/Users/pfrazier/Library/Enthought/Canopy_64bit/User/bin/python

import gflags
import httplib2
from datetime import tzinfo, datetime, timedelta, date

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

import dateutil.parser
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import argparse

parser = argparse.ArgumentParser(description='Time planning google calendar script.')
def mkdate(datestr):
    return dateutil.parser.parse(datestr).date()
parser.add_argument('--start',dest='start',type=mkdate,default=date.today(),
                    help='Start date in YYYY-MM-DD format (default: today)')
parser.add_argument('--ndays',dest='ndays',default=30,type=int,metavar='n',
                    help='Duration in days (default: 30)')
parser.add_argument('--no-plot',dest='do_plot',action='store_false',default=True,
                    help='Turn off plotting (default: on)')
parser.add_argument('--no-summary',dest='do_summary',action='store_false',default=True,
                    help='Turn off hours per day summary (default: on)')
parser.add_argument('--details',dest='do_details',action='store_true',default=False,
                    help='Turn on detailed list of all events (default: off)')

args = parser.parse_args()
ndays = args.ndays
start = args.start

# The following parameter should go into a configuration file

# File that google uses to store authentication information.  Should be
# readable and writable.
credential_file = '/Users/pfrazier/calendar.dat'

# List of calendars to get events from.
# Feature request: allow the user to specify these calendars on the command
# line, and to do it via their descriptions rather than their ids.
calendars = {'bu7c7742dbv9v4daqmqqcsqo5k@group.calendar.google.com',  # todo calendar
            'i304j8vnu0tdi6rhj9ip3nlj74@group.calendar.google.com', #Floating calendar
             '4m9g61tcu5bsj4rcfp4ilvb23g@group.calendar.google.com', #to-do-repeat calendar
             'primary'}

# Number of hours of capacity that I can work per day.
hours_per_day = 55.0 / 7
# Feature request: allow the user to specify my capacity in a more dynamic way,
# e.g., days that I am available on conference.  A clean way to do this would
# be to have an additional calendar, maybe called "capacity", that would have
# time that I can work.  Or, it could be specified in the config file.  Could
# have a different time for weekdays and weekends, etc.


FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret can be found in Google Developers Console
FLOW = OAuth2WebServerFlow(
    client_id='497551361623-87u6em4sdk4qk4bpga39b8jgvfum67b1.apps.googleusercontent.com',
    client_secret='o6-tK2NE_mk5inQNzAhvwRqg',
    scope='https://www.googleapis.com/auth/calendar',
    user_agent='Peter-calendar-script/0.1')

# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good Credentials
# will get written back to a file.
storage = Storage(credential_file)
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit the Google
# Developers Console to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http,
       developerKey='YOUR_DEVELOPER_KEY')

end = start + timedelta(days=ndays)
elapsed = [timedelta(0) for i in range(ndays)]# We will store the total time for each day in an array

# Create strings in ISO format encoding midnight on the start and end-days, in the appropriate time zone.
# Feature request: don't hardcode the timezone.  Where to get it?  Maybe the calendar itself.
class TZ(tzinfo):
  # Use GMT-5, which is the US Eastern time zone.
  def utcoffset(self, dt): return timedelta(hours=-5)
start_iso = datetime(year=start.year, month=start.month, day=start.day, hour=0, minute=0, second=0, tzinfo=TZ()).isoformat()
end_iso = datetime(year=end.year, month=end.month, day=end.day, hour=0, minute=0, second=0, tzinfo=TZ()).isoformat()

page_token = None
total = timedelta(0)
for cal_id in calendars:
  while True:
    events = service.events().list(calendarId=cal_id, timeMin=start_iso, timeMax=end_iso, singleEvents=True, orderBy='startTime', pageToken=page_token).execute()
    for event in events['items']:

      # Read in the start and end times for the event, and calculate time elapsed
      if 'dateTime' in event['end']:
          event_end = dateutil.parser.parse(event['end']['dateTime'])
      else:
          event_end = dateutil.parser.parse(event['end']['date'])

      if 'dateTime' in event['start']:
          event_start = dateutil.parser.parse(event['start']['dateTime'])
      else:
          event_start = dateutil.parser.parse(event['start']['date'])

      event_elapsed = event_end - event_start

      # if the strings "#home" or "#note" appear in the description, do not
      # include them in elapsed
      # Feature request: allow the user to provide a more generic regular
      # expression, or set of inclusions and exclusions.
      if '#home' in event['summary']:
        continue
      if '#note' in event['summary']:
        continue

      # PF: feature request: break events that span multiple days across those
      # days, rather than just attributing them to one day.

      # Record the elapsed time in the dictionary for the appropriate start day
      event_start_day = date(year=event_start.year, month=event_start.month, day=event_start.day)
      i = (event_start_day - start).days
      elapsed[i] = elapsed[i] + event_elapsed
      total += event_elapsed

      if args.do_details:
        print str(event_start_day) + ' ' + str(event_elapsed) + ' ' + event['summary']

    page_token = events.get('nextPageToken')
    if not page_token:
      break

print 'Total: ' + str(total)
if args.do_summary:
    for i in range(ndays):
      print str(start+timedelta(days=i)) + ' ' + str(elapsed[i])

elapsed_hours = [td.total_seconds()/3600 for td in elapsed]

def accumu(lis):
    total = lis
    for i in range(len(lis)-1):
        total[i+1] = total[i]+lis[i+1]
    return total

capacity = [(i+1)*hours_per_day for i in range(ndays)]

if args.do_plot:
    # Plot everything
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    x= [start+timedelta(days=n) for n in range(ndays)]
    plt.plot(x,accumu(elapsed_hours),x,capacity)
    plt.gcf().autofmt_xdate()
    plt.show()
