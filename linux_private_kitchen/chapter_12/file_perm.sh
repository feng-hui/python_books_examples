#!/bin/bash
# Program
#	User input a filename,program will check the flowing:
#	1) exists? 2) file/directory 3) file permissions
# History
# 2019-07-16	FengHui		First Release
path=/bin:/sbin:/usr/bin:~/bin
export path

# 1、输入文档名称，并且判断是否真的输入字符串
echo -e "Please input a filename,I will check the filename's type and permission. \n\n"
read -p "File name: " filename
test -z ${filename} && echo -e "You must input a filename" && exit 0

# 2、判断文件是否存在
test ! -e ${filename} && echo "Filename ${filename} does not exist." && exit 0
# 3、判断文档类型
test -f ${filename} && filetype="Filename is regular file"
test -d ${filename} && filetype="Filename is directory"
# 4、判断文档的执行权限
test -r ${filename} && perm="readable"
test -w ${filename} && perm="${perm} writeable"
test -x ${filename} && perm="${perm} executable"
# 5、输出结果
echo ${filetype}
echo "The permisson of the filename(${filename}) is ${perm}"
