#!/bin/bash
# Program:
#	Use ping command to check the network's PC state.
# History:
# 2019/07/17     Fenghui        First release
path=/bin:/sbin:/usr/bin:~/bin
export path

network='192.168.1'

for sitenu in $(seq 1 10)
do
	ping -c 1 -w 1 ${network}.$sitenu &> /dev/null && result=0 || result=1
	if [ "${result}" == 0 ]; then
		echo "Server ${network}.${sitenu} is UP."
	else
		echo "Server ${network}.${sitenu} is DOWN."
	fi
done
