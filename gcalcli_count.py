#!/usr/local/bin/python

import sys
import string
import datetime

total_hours = 0
for line in sys.stdin:
    # We expect that each input line is the output of gcalcli agenda --tsv
    # Example input is:
    # 2015-08-10    08:00   2015-08-10  09:30   Jialei & Peter, to work on Nature SI
    try:
        fields = string.split(line,'\t')

        # Extract the contents from this line.
        # The elements of list fields are as follows:
        # [0] start date, [1] start time, [2] end date, [3] end time,
        # [4] description
        # From this, we calculate the start time of the event, the end-time of
        # the event, and the description.
        start = datetime.datetime.strptime(fields[0] + " " + fields[1], '%Y-%m-%d %H:%M')
        end   = datetime.datetime.strptime(fields[2] + " " + fields[3], '%Y-%m-%d %H:%M')
        description = fields[4]
    except:
        print "gcalcli_count.py: Error, Could not parse the following input line, will skip it and keep going."
        print line
        continue


    # Get the duration, expressed in hours as a real number
    duration = end - start
    hours = duration.days * 24 + float(duration.seconds + duration.microseconds / 10**6) /3600
    total_hours += hours

    print str(hours) + " " + description
print "Total Hours:", total_hours
