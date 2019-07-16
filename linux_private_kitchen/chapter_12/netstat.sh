#!bin/bash
# Program:
#	Using netstat and grep to detect WWW,SSH,FTP and MAIL services.
# History:
# 2019/07/16 F First Release
path=/bin:/sbin:/usr/bin:~/bin
export path

echo "Now, I will detect you linux server's services."
echo -e "The www, ftp, ssh, and mail(smtp) will be detected. \n"

testfile=/dev/shm/netstat_checking.txt
netstat -tuln > ${testfile}

testing=$(grep ":80 " ${testfile})
if [ "${testing}" != "" ]; then
	echo "WWW is running in you system."
fi

testing=$(grep ":22 " ${testfile})
if [ "${testing}" != "" ]; then
        echo "SSH is running in you system."
fi


