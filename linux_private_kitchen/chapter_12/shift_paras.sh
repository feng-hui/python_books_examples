#!/bin/bash
# Program
#       This Program shows the script name,parameters...
# History
# 2019-07-16    FengHui         First Release
 
path=/bin:/sbin:/usr/bin:~/bin
export path

echo "Total parameter number is  ==> $#"
echo "Your whole parameter is    ==> '$@'"

shift 
echo "Total parameter number is  ==> $#"
echo "Your whole parameter is    ==> '$@'"

shift 3
echo "Total parameter number is  ==> $#"
echo "Your whole parameter is    ==> '$@'"
