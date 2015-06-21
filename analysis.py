# This script creates a histogram of hours worked per day, based on
# covariates. It can then be used to determine how many hours are predicted
# to be available for work.

# Feature request: combine this script with atp.py, as there is code that is
# copied and pasted.

# Feature request: do better handling of time zones.

import gflags
import httplib2
from datetime import tzinfo, datetime, timedelta, date

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

import dateutil.parser

import matplotlib.pyplot as plt

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
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
# Feature: Don't hardcode the location of gcaltimetracker.dat
storage = Storage('/Users/pf98/gcaltimetracker.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google Developers Console
# to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http,
       developerKey='YOUR_DEVELOPER_KEY')

# List of calendars to get events from.
# Feature request: allow the user to specify these calendars on the command
# line, and to do it via their descriptions rather than their ids.
calendars = {'primary'}

# Feature request: allow changing from the default via arguments on the command line.
start = date(year=2014,month=1,day=1)
end   = date(year=2014,month=12,day=31)

ndays = (end-start).days+1 # We add 1 because our search is inclusive
elapsed = [timedelta(0) for i in range(ndays)]# We will store the total time for each day in an array

# Create strings in ISO format encoding midnight on the start and end-days, in the appropriate time zone.
# Feature request: don't hardcode the timezone.  Where to get it?  Maybe the calendar itself.
class TZ(tzinfo):
  # Use GMT-5, which is the US Eastern time zone.
  def utcoffset(self, dt): return timedelta(hours=-5)
start_iso = datetime(year=start.year, month=start.month, day=start.day, hour=0, minute=0, second=0, tzinfo=TZ()).isoformat()
end_iso = datetime(year=end.year, month=end.month, day=end.day, hour=0, minute=0, second=0, tzinfo=TZ()).isoformat()

# First, go through all of the calendars and calculate the total time worked on each day.

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
      # include them in elapsed In the future, we can allow the user to provide
      # a more generic regular expression, or set of inclusions and exclusions.
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
      print event['summary'] + ' ' + str(event_elapsed)

    page_token = events.get('nextPageToken')
    if not page_token:
      break

print total
for i in range(ndays):
    print str(start+timedelta(days=i)) + ' ' + str(elapsed[i])

elapsed_hours = [td.total_seconds()/3600 for td in elapsed]

def accumu(lis):
    total = lis
    for i in range(len(lis)-1):
        total[i+1] = total[i]+lis[i+1]
    return total

capacity = [(i+1)*hours_per_day for i in range(ndays)]

# Plot everything
plt.plot(range(ndays),accumu(elapsed_hours),range(ndays),capacity)
plt.show()
