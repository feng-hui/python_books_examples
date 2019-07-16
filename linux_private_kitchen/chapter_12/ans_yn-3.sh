#!/bin/bash
# Program
#	This Program shows the user's choice.
# History
# 2019-07-16	FengHui		First Release

path=/bin:/sbin:/usr/bin:~/bin
export path

read -p "Please input (Y/N): " yn

#[ "${yn}" == "Y" -o "${yn}" == "y" ] && echo "OK, continue" && exit 0
#[ "${yn}" == "N" -o "${yn}" == "n" ] && echo "Oh, interrupt" && exit 0


if [ "${yn}" == "Y" ] || [ "${yn}" == "y" ]; then
  echo "OK, continue"
  exit 0
elif [ "${yn}" == "N" ] || [ "${yn}" == "n" ]; then
  echo "Oh, interrupt"
  exit 0
else
  echo "I dont't know what your choice is."
  exit 0
fi
