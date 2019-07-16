#!/bin/bash
# Program:
#	User inputs his first name and last name.Then Program shows his full name.
# History:
# 2019/07/17 Fenghui First release
path=/bin:/sbin:/usr/bin:~/bin
export path

read -p "Please input your first name: " firstname
read -p "Please input your lat name: " lastname

echo -e "Your full name is: ${firstname} ${lastname}."
