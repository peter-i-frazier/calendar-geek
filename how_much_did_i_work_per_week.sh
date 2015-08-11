#!/bin/sh
# Calculates how many hours I worked per week, over a period of weeks,
# looking at a period in the summer of 2014.

total=0
n_weeks=0

#
# 2014
#

# how_much_did_i_work.sh 6/2  6/8 | grep 'Total Hours'
echo "6/02 to 6/08, Total Hours (cached): 56.0"
this_week=56
n_weeks=$((n_weeks+1))
total=$(($total+$this_week))

# how_much_did_i_work.sh 6/9  6/15 | grep 'Total Hours'
echo "6/09 to 6/15, Total Hours (cached): 88.5833333333"
this_week=89
n_weeks=$((n_weeks+1))
total=$((total+this_week))

#how_much_did_i_work.sh 6/16 6/22 | grep 'Total Hours'
echo "6/16 to 6/22, Total Hours (cached): 34.75"
this_week=35
n_weeks=$((n_weeks+1))
total=$((total+this_week))


#how_much_did_i_work.sh 6/23 6/29 | grep 'Total Hours'
echo "6/23 to 6/29, Total Hours (cached): 39.1666666667"
this_week=39
n_weeks=$((n_weeks+1))
total=$((total+this_week))

#how_much_did_i_work.sh 6/30 7/6 | grep 'Total Hours'
echo "6/20 to 7/06, Total Hours (cached): 33.25"
this_week=33
n_weeks=$((n_weeks+1))
total=$((total+this_week))


#how_much_did_i_work.sh 7/7  7/13 | grep 'Total Hours'
echo "7/07 to 7/13, Total Hours (cached): 35.9166666667"
this_week=36
n_weeks=$((n_weeks+1))
total=$((total+this_week))


#how_much_did_i_work.sh 7/14 7/20 | grep 'Total Hours'
echo "7/14 to 7/20, Total Hours (cached): 44.5833333333"
this_week=45
n_weeks=$((n_weeks+1))
total=$((total+this_week))


#how_much_did_i_work.sh 7/21 7/27 | grep 'Total Hours'
echo "7/21 to 7/27, Total Hours (cached): 51.75"
this_week=52
n_weeks=$((n_weeks+1))
total=$((total+this_week))


#how_much_did_i_work.sh 7/28 8/3 | grep 'Total Hours'
echo "7/28 to 8/03, Total Hours (cached): 54.5"
this_week=55
n_weeks=$((n_weeks+1))
total=$((total+this_week))


#how_much_did_i_work.sh 8/4  8/10 | grep 'Total Hours'
echo "8/04 to 8/10, Total Hours (cached): 45.3333333333"
this_week=45
n_weeks=$((n_weeks+1))
total=$((total+this_week))


#how_much_did_i_work.sh 8/11 8/17 | grep 'Total Hours'
echo "8/11 to 8/17, Total Hours (cached): 59.75"
this_week=60
n_weeks=$((n_weeks+1))
total=$((total+this_week))


#how_much_did_i_work.sh 8/18 8/24 | grep 'Total Hours'
echo "8/18 to 8/24, Total Hours (cached): 53.25"
this_week=53
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 8/25 8/31 | grep 'Total Hours'
echo "8/25 to 8/31, Total Hours (cached): 52.3333333333"
this_week=52
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 9/1 9/7
echo "9/01 to 9/07, Total Hours (cached): 43.75"
this_week=44
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 9/8 9/14
echo "9/08 to 9/14, Total Hours (cached): 53.5833333333"
this_week=54
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 9/15 9/21
echo "9/15 to 9/21, Total Hours (cached): 56.0"
this_week=56
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 9/22 9/28
echo "9/22 to 9/28, Total Hours (cached): 50.5"
this_week=51
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 9/29 10/5
echo "9/29 to 10/05, Total Hours (cached): 58.0833333333"
this_week=58
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 10/6 10/12
echo "10/06 to 10/12, Total Hours (cached): 76.25"
this_week=76
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 10/13 10/19
echo "10/30 to 10/19, Total Hours (cached): 51.0"
this_week=51
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# how_much_did_i_work.sh 10/20 10/26
echo "10/20 to 10/26, Total Hours (cached): 47.5"
this_week=48
n_weeks=$((n_weeks+1))
total=$((total+this_week))

# how_much_did_i_work.sh 10/27 11/2
echo "10/27 to 11/2, Total Hours (cached): 57.3333333333"
this_week=57
n_weeks=$((n_weeks+1))
total=$((total+this_week))

#how_much_did_i_work.sh 11/3 11/9 
echo "11/3 to 11/9, Total Hours (cached): 61.75"
this_week=62
n_weeks=$((n_weeks+1))
total=$((total+this_week))

# how_much_did_i_work.sh 11/10 11/16
echo "11/10 to 11/16, Total Hours (cached): 64.25"
this_week=64
n_weeks=$((n_weeks+1))
total=$((total+this_week))

echo "need to fill in here"

# how_much_did_i_work.sh 12/8 12/14
echo "12/8 to 12/14, Total Hours (cached): 73.0333333333"
this_week=73
n_weeks=$((n_weeks+1))
total=$((total+this_week))

# how_much_did_i_work.sh 12/15 12/21
echo "12/15 to 12/21, Total Hours (cached): 53.0"
this_week=53
n_weeks=$((n_weeks+1))
total=$((total+this_week))


# PF: need to fill in teh gap from 



echo "Average hours per week"
echo $((total/n_weeks))
