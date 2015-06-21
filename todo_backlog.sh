#!/bin/sh

# This shell script calculates how many hours of work is backlogged in the todo
# calendar. It takes an optional argument, which is the last day of the range
# to look over.  If this is not specified, then today is used.

if [ $# -eq 0 ]
then
    END_DAY='today'
elif [ $# -eq 1 ]
then
    END_DAY=$1
else
    echo 'usage: todo_backlog.sh [END_DAY]'
    echo 'This script calculates how many hours of work are backlogged, from 1/1/2000 up to END_DAY.'
    echo 'It looks only at the todo calendar.'
    echo 'If END_DAY is not specified, then it is set to today.'
    echo 'Dates should be specified in mm/dd/yyyy format.'
    exit
fi

# This is set to something really early, essentially to -infinity.
START_DAY='1/1/2000'

gcalcli --nocache --cal=todo --tsv agenda $START_DAY $END_DAY | gcalcli_count.py
