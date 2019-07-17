#!/bin/bash
# Program:
#	Use input dir name, I find the permission of files.
# History:
# 2019/07/17     Fenghui        First release
path=/bin:/sbin:/usr/bin:~/bin
export path

read -p "Please input the name of any directory:" dirname

# 判断文件夹是否存在或是否为文件夹
if [ "${dirname}" == "" -o ! -d "${dirname}" ]; then
	echo "${dirname} is not exist."
	exit 1
fi

# 获取目录里的所有文档的权限
filelist=$(ls ${dirname})
for doc in ${filelist}
do 
	perm=""
	test -r "${dirname}/${doc}" && perm="${perm} readable;"
	test -w "${dirname}/${doc}" && perm="${perm} writable;"
	test -x "${dirname}/${doc}" && perm="${perm} executable."
        echo "The permissions of ${dirname}/${doc} are: ${perm}"
done

