#!/bin/bash
# Program:
#	User inputs 2 integer numbers;program will cross these two numbers.
# History:
# 2019/07/07	FengHui	First release
path=/bin:/sbin:/usr/bin:~/bine
export path

echo -e "You should input two integer numbers,I will multiply them! \n"
read -p "Fist number: " firstnu
read -p "Second number: " secondnu
total=$((${firstnu}*${secondnu}))
echo -e "\nThe result of ${firstnu} * ${secondnu} is ==> ${total}."
