#!/bin/bash
# Program:
#	Use id, finger command to check system account's information.
# History:
# 2019/07/17     Fenghui        First release
path=/bin:/sbin:/usr/bin:~/bin
export path

users=$(last | cut -d' ' -f1 | grep '[^$]' | head -n 10)

for username in ${users}
do
	id $username
done

