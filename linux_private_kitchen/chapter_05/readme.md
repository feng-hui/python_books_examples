#### 第五章 Linux的文件权限与目录配置

1、使用者与群组

* 使用者(user): 文件或目录的拥有着；
* 群组(group) 文件或目录的所属群组，一个群组可以有多个使用者加入。

2、Linux文件属性

档案类型 | 连结数 | 档案拥有者 | 档案所属群组 | 档案容量 | 档案最后被修改的时间| 档名
---|---|---|---|---|---|---
-rw-r--r-- | 1 | airflow | airflow | 2605 | Dec 14 14:29 | circus.ini

* 第一栏代表这个文件的类型与权限(permission)

3、如何改变文件属性与权限

* chgrp 改变文件所属群组
    * 使用方法： `chgrp [-R] dirname/filename ...`
    * 范例：`chgrp users initial-setup-ks.cfg`,`users`表示群组
    * 注意：在改变文件的所属群组的时候，必须保证该群组在`/etc/group`里存在，否则会报错如下：`chgrp： invalid group： 'group_name'`
* chown 改变文件拥有者
    * 使用方法： `chgro [-R] dirname/filename ...`
    * 范例：`chgrp users initial-setup-ks.cfg`,`users`表示群组
    * 注意：在改变文件的所属群组的时候，必须保证该群组在`/etc/group`里存在，否则会报错如下：`chgrp： invalid group： 'group_name'`
* chmod 改变文件的权限，SUID,SGID,SBIT等等的特性

**注释：-R 进行递归（recursive）的持续变更。常常用在变更某一目录内所有的文件之情况。**