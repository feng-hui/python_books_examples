#!/bin/bash
# Program:
#	Calculate 1+2+3+...
# History:
# 2019/07/16     Fenghui        First release
path=/bin:/sbin:/usr/bin:~/bin
export path

s=0
i=0

while [ ${i} != "100" ]
do
	i=$(($i+1))
	s=$(($s+$i))
done
echo "1+2+3+...+100 ==> ${s}."
