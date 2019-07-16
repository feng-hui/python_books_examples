#!/bin/bash
# Program
#	User input a scale number to calculate pi number.
# History
# 2019-07-16	FengHui		First Release
path=/bin:/sbin:/usr/bin:~/bin
export path

echo -e "This program will calculate pi value. \n"
echo -e "You should input a float number to calculate pi value. \n"
read -p "The scale number (10-1000) ?" checking
num=${checking:-"10"}
echo -e "Starting calculate pi value.Be patient."
time echo "scale=${num}; 4*a(1)" | bc -lq

