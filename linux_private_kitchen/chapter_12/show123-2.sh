#!/bin/bash
# Program:
#	This script only accepts the following parameter: one, two, three.
# History:
# 2019/07/16	 Fenghui 	First release
path=/bin:/sbin:/usr/bin:~/bin
export path

function printit() {
	echo -n "Your choice is "
}

echo "This program willl print your selection !"

#read -p "Input your choice: " choice
#case ${choice} in
case ${1} in
  "one")
	printit;echo ${1} | tr 'a-z' 'A-Z'
	;;
  "two")
	printit;echo ${1} | tr 'a-z' 'A-Z'
	;;
  "three")
	printit;echo ${1} | tr 'a-z' 'A-Z'
	;;
  *)
	echo "Usage ${0} {one|two|three}"
	;;
esac 
