#!/bin/bash
# Program:
#	This script only accepts the following parameter: one, two, three.
# History:
# 2019/07/16	 Fenghui 	First release
path=/bin:/sbin:/usr/bin:~/bin
export path

echo "This program willl print your selection !"

read -p "Input your choice: " choice
case ${choice} in
#case ${1} in
  "one")
	echo "Your choice is ONE"
	;;
  "two")
	echo "Your choice is TWO"
	;;
  "three")
	echo "Your choice is Three"
	;;
  *)
	echo "Usage ${0} {one|two|three}"
	;;
esac 
