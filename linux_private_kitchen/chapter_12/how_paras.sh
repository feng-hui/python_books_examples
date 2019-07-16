#!/bin/bash
# Program
#	This Program shows the script name,parameters...
# History
# 2019-07-16    FengHui         First Release

path=/bin:/sbin:/usr/bin:~/bin
export path

echo "The script name is      ==> ${0}"
echo "Total parameters is     ==> $#"
[ "$#" -lt 2 ] && echo "The number of parametes less than 2. Stop here." && exit 0

echo "Your whole parameter is ==> '$@'"
echo "The first parameter is  ==> $1"
echo "The second parameter is ==> $2"
