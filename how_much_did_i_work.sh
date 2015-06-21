#!/bin/sh

# This shell script calculates how much I worked on a day, or a range of days.
# It assumes that gcalcli_count.py is in the path.

# If they specify just one argument, make it the first and last days.
if [ $# -eq 1 ]
then
    START_DAY=$1
    END_DAY=$1
elif [ $# -eq 2 ]
then
    START_DAY=$1
    END_DAY=$2
else
    echo 'usage: how_much_did_i_work_sh START_DAY [END_DAY]'
    echo 'This script calculates the hours worked of over a specified period.'
    echo 'It looks at the Other Work, Research, and peter.i.frazier calendars, removing the #home and #note tags.'
    echo 'Dates should be specified in mm/dd/yyyy format.'
    echo 'If END_DAY is not specified, then it is set to START_DAY.'
    exit
fi

echo "START_DAY=$START_DAY, END_DAY=$END_DAY"

gcalcli --nocache --cal=peter.i.frazier --cal=Other --cal=ResearchPF --tsv agenda "12am $START_DAY" "11:59pm $END_DAY" | egrep -v '#home|#note' | gcalcli_count.py

# To do: make it easy to ask for a full week
