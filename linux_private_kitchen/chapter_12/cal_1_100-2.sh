#!/bin/bash
# Program:
#	Calculate 1+2+3+...
# History:
# 2019/07/16     Fenghui        First release
path=/bin:/sbin:/usr/bin:~/bin
export path

read -p "Please input a number, I will count 1+2+3...+your input: "  nu

s=0

for ((i=1;i<=nu;i=i+1))
do
	s=$(($s+$i))
done
echo "1+2+3+...+100 ==> ${s}."
