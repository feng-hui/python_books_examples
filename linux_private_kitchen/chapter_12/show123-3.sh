#!/bin/bash
# Program:
#	This script only accepts the following parameter: one, two, three.
# History:
# 2019/07/16	 Fenghui 	First release
path=/bin:/sbin:/usr/bin:~/bin
export path

function printit() {
	echo "Your choice is ${1}"
}

echo "This program willl print your selection !"

#read -p "Input your choice: " choice
#case ${choice} in
case ${1} in
  "one")
	printit 1
	;;
  "two")
	printit 2
	;;
  "three")
	printit 3
	;;
  *)
	echo "Usage ${0} {one|two|three}"
	;;
esac 
