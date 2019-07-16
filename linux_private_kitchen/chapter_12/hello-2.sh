#!bin/bash
# Program:
#	Check $1 is equal to "hello".
# History:
# 2019/07/16	 F 	First Release

path=/bin:/sbin:/usr/bin:~/bin
export path

if [ "${1}" == "hello" ]; then
	echo "Hello, how are you?"
	exit 0
elif [ "${1}" == "" ]; then
	echo "You Must input parameters, ex> {${0} some word}"
else
	echo "The only parameter is 'hello', ex> {${0} hello}"
fi
