#### 8、文件与文件系统的压缩、打包与备份

##### 8.1、Linux系统常见的压缩指令

扩展名 | 释义
-- | --
*.Z | compress程序压缩的文件
*.zip | zip程序压缩的文件
*.gz | gzip程序压缩的文件
*.bz2 | bzip2程序压缩的文件
*.xz | xz程序压缩的文件
*.tar | tar程序打包的文件，并没有压缩过
*.tar.gz | tar程序打包的文件，并且经过gzip压缩
*.tar.bz2 | tar程序打包的文件，并且经过bzip2压缩
*.tar.xz | tar程序打包的文件，并且经过xz压缩

**Linux上常见的压缩指令是gzip、bzip2以及xz，而compress渐渐被取代了。**
##### 8.2、gzip、bizp2、xz使用介绍

（1）语法介绍

语法如下：

```
1、gzip [-cdtv#] 文档名称

# 选项与参数：
-c: 标准输出，保持源文件不变，可以进行输出重导(>)
-d: 解压缩的参数
-t: 测试压缩文件完整性
-v: 详细模式（显示压缩比、压缩率、压缩前后的字节数等详细信息）
-1..-0: #为数字的意思，代表压缩等级，-1最快，但是压缩比最差，-9最慢，但是压缩比是最好的，默认值为-6

# 例如：

# 压缩与解压缩
gzip -v services(services为文档名称)
gzip -d services.gz
gzip -9 -c services > services2.gz


2、bizp2 [-cdkzv#] 文档名称
-k: 保留源文件
-z: 强制压缩的参数（可省略）
其他参数同gzip

3、xz [-dtlkv#] 文档名称
同bzip2和gzip
```

（2）相关指令介绍

```
# 相关指令主要是用于查看和查询压缩文件
# 1、zcat、zmore、zless、zgrep
# 例如：
zcat/zmore/zless service.gz
zgrep -n 'http' service.gz

# 2、bzcat、bzmore、bzless、bzgrep

# 3、xzcat、xzmore、xzless、xzgrep
```

###### 8.3、打包指令tar

（1）语法如下：

```
# 打包与压缩
tar [-z|-j|-J][cv] [-f 压缩文件的名称] 待压缩的文档名称

# 查看压缩文件
tar [-z|-j|-J][tv] [-f 已压缩的tar文档名称]

# 解压缩
tar [-z|-j|-J][xv] [-f 已压缩的tar文档名称] [-C 解压到指定的目录]

# 参数解释
-c: 新建打包文件，可搭配-v来查看过程中被打包的文档名称
-t: 查看打包文件中包含哪些文档
-x: 解打包或解压缩的功能，可以搭配-C在指定目录解开

-z/-j/-J: 分别表示同通过gzip、bzip2、xz来进行压缩或解压缩，压缩的文档名称最好为*.tar.gz(.bz2/.xz)

-v: 在压缩/解压缩的过程中，打印正在处理的文件名称
-f: 压缩后的文件名称或解压缩的文件名称，建议-f单独写
-C: 解压缩到指定的目录

-p: 保留备份数据的原本权限与属性，常用于备份重要的配置文件
-P: 保留绝对路径，允许备份数据中含有根目录
--exclude=FILE: 在压缩的过程中，不包含FILE
```

例如：
```
tar -zpcv -f /root/etc.tar.gz /etc
tar -jpcv -f /root/etc.tar.bz2 /etc
tar -Jpcv -f /root/etc.tar.xz /etc
或
time tar -zpcv -f /root/etc.tar.gz /etc（显示压缩花费的具体时间）
```

例如：打包某个目录，但不包含某些文件
```
tar -jcv -f /root/system.tar.bz2 --exclude=/root/etc* --exclude=/root/system.tar.bz2 /etc /root
```

（2）使用介绍

* 基本名称：tarfile、tarball，通过tar只打包的文件称为tarfile(`tar -cv file.tar`)；如果同时进行了压缩，那么称为tarball(`tar -zcv -f file.tar.gz`)。
* 特殊应用：通过标准输入与输出的数据留重导向以及管线命令的方式，将待处理的文件一边打包一边解压缩到指定目录中。(`cd /tmp;tar -cvf - /etc | tar -xvf -`)(第一个-表示标准输出，第二个-表示标准输入，可以将 - 理解为内存中的一个缓冲区之类的概念。)

