#!/bin/bash
# Program:
#	Repeat question util user input correct answer.
# History:
# 2019/07/16     Fenghui        First release

path=/bin:/sbin:/usr/bin:~/bin
export path

while [ "${yn}" != "yes" -a "${yn}" != "YES" ]
do
	read -p "Please input yes/YES to stop this program: " yn
done

echo "Ok, you input the correct answer."
