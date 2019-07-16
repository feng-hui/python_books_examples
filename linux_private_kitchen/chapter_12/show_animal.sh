#!/bin/bash
# Program:
#	This script only accepts the following parameter: one, two, three.
# History:
# 2019/07/16     Fenghui        First release

path=/bin:/sbin:/usr/bin:~/bin
export path

for animal in dog cat elephant
do
	echo "There are ${animal}s..."
done
