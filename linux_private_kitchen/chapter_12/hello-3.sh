#!bin/bash
# Program:
#	Show "Hello" from $1...... by using case ...... esac
# History:
# 2019/07/16	 F 	First Release

path=/bin:/sbin:/usr/bin:~/bin
export path

case $1 in
  "hello")
	echo "Hello, how are you?"
	;;
  "")
	echo "You Must input parameters, ex> {${0} some word}"
	;;
  *)
	echo "Usage ${0} {hello}"
	;;
esac
