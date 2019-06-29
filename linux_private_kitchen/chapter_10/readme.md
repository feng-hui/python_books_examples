#### 第十章 认识与学习BASH

##### 10.1、认识BASH与Shell

1、什么是shell？

shell的功能是提供用户操作的一个接口，用户可以通过shell（指令列模式）来操作应用程序。

2、Bash shell功能？

* 命令编修功能（history，默认记录1000条，当前执行的所有指定暂存在内存中，成功注销之后会记录到.bash_history中）
* 命令和文件补全功能（[tab]键）
    * [Tab] 在一串指令的第一个字的后面，则未命令补全
    * [Tab] 在一串指令的第二个字以后时，则为文件补全
    * 若安装`bash-completion`软件，则在某些指令后面使用[tab]键时，可以进行选项/参数的补全。
* 设置命令别名（alias）
* 工作控制、前景背景控制
* 程序化脚本
* 通配符

3、查询指令是否为内建命令？(type)

```
# 系统不同，查到的结果可能有所不同
# type根据不同的参数可以显示不同的结果，具体可以使用man type来查看

# 1、直接查询
>>> type ll
>>> ll is aliased to `ls -l --color=auto'

>>> type export
>>> export is a shell builtin

>>> type rm
>>> rm is hashed (/bin/rm)

# 2、打印指令的类型(builtin 内建、alias 别名、file 外部指令)

>>> type -t export
>>> builtin

>>> type -t ls
>>> alias

>>> type -t rm
>>> file
```

4、指令的下达与快速编辑按钮

* 指令串过长：`\[Enter]]`(\+回车，中间没有空格，执行完成之后跳到下一行继续输入)
* 快速删除输入的指令：[ctrl]+u/[ctrl]+k（删除光标之前的所有指令串/删除光标之后的所有指令串）
* 快速移动指令串中的光标：[ctrl]+a/[ctrl]+e（光标快速移动到整个指令串的最前面/最后面）

##### 10.2、Shell的变量功能

1、什么是变量?

变量就是以一组文字或符号等，来取代一些设定或是一串保留的数据。

2、变量的取用与设定

变量的取用：echo