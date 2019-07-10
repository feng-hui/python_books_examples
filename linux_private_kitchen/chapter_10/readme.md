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

获取变量的值：echo $variable 或 echo ${variable}
变量赋值规则：
* 变量与变量内容以一个等号=来连接；
* 等号两边不能直接接空格符；
* 变量名称只能是英文字母或数字，第一个字符不能位数字；
* 变量内若有空格符可以使用双引号或单引号将变量内容包裹起来；
    * 双引号内的特殊字符如$等，可以保有原本的特性；
    * 单引号内的特殊字符则仅为一般字符（纯文本）。
* 可用跳脱符(\)将特殊符号（如[enter]、$、\、空格符、`等）变成一般字符；
* 在一串指令的执行中，可以使用反单引号(`)或$获取其他指令所提供的信息；
* 如果扩展变量内容，则可使用"$变量名称"或$变量累加内容，例如:PATH="$PATH:/home/bin"或PATH=${PATH}:/home/bin;
* 若变量需要在其他子程序执行，则需要以export来使得变量变成环境变量；例如：export PATH;
* 通常大写字符为系统默认变量，自行设定变量可以使用小写字符，方便判断（纯粹依照使用者新区与嗜好）；
* 取消变量的方法使用`unset`：`unset 变量名称`。

3、什么是【子程序】？

在当前shell的情况下，去启用另外一个新的shell，新的shell就是子程序。例如：在当前shell中直接执行`bash`命令就可以到一个子程序中。

4、环境变量的功能

查阅环境变量可以使用`env`或`export`这两个指令。

(1)、env查看环境环境变量以及结果说明

环境变量名称 | 含义
| -- | --
HOME | 用户的家目录
SHELL | 当前环境使用的SHELL程序
HISTSIZE | 历史命令的记录数
MAIL | 使用`mail`指令收信时，系统会读取的邮件信箱文件
PATH | 执行文件搜索的路径(目录与目录之间以:进行分割)
LANG | 系统语言
RANDOM | 随机数(0-32767)

（2）使用`set`查看所有变量（包含环境变量与自定义变量）

`set`除了可以显示环境变量，还可以显示一些与bash操作接口有关的变量以及用户定义的变量。

重要的介绍如下：

环境变量名称 | 含义
| -- | --
PS1 | 提示字符的设定（按下enter键后，光标前的一串文字）
$ | 当前shell的PID
? | 上个指令的回传值（如果成功为0，错误为非0）
OSTYPE/HOSTTYPE/MACHTYPE | 主机硬件与核心的等级

（3）、`export`：将自定义变量转成环境变量

`export 变量名称`，转换成环境变量之后，变量可以被子程序继承。

5、影响显示结果的语系变量(`locale`)

```
# 01 locale
# 查看所有已经设置的语系变量
>>> locale

# 02 locale -a
# 查看所有系统支持的语系
```

如果设定了`LANG`或者`LC_ALL`，则其他语系的变量都会被取代。

6、变量键盘读取、数组与宣告：`read`,`array`,`declare`

（1）`read`

> 读取来自键盘输入的变量。语法如下：

```
# read -pt variable
# -p 提示符
# -t 等待的时间（单位：秒）

>>> read 变量名称
>>> 输入内容
>>> echo $变量名称

>>> read -p '请输入变量内容:' -t 5 变量名称
>>> 输入内容
>>> echo $变量名称
```

（2）`array`

> 定义变量为数组类型。语法如下：

```
# var[index]=content
# var     变量名称
# index   索引值
# content 内容

>>> var[1]='the first value'
>>> var[2]='the second value'
>>> var[3]='the third value'

>>> echo "${var[1]},${var[2]},${var[3]}"
```

（3）`declare`/`typeset`

> 定义变量的类型。

* 如果设置为只读，则不能更改该变量的值；
* 如果想将变量变成环境变量采用`declare -x`，如果想将环境变量变成普通变量采用`declare +x`。

语法如下：

```
# declare [-aixr] variable
# -a 将变量定义为数组（array）类型
# -i 将变量定义为整数数字（integer）类型
# -x 将变量定义为环境变量（同export用法相同）
# -r 将变量定义为只读（readonly）类型

>>> declare
>>> 显示所有的变量名称与内容

# 如果没有-i，输出的为字符串(100+300+500)
# bash环境计算只能达到整数形态，所以1/3的结果为0
>>> declare -i sum=100+300+500
>>> echo $sum
>>> 900
```

7、与文件系统及程序的限制关系：`ulimit`

> 限制用户可以使用的系统资源大小，比如：可以开启的文件数量、可以使用的CPU时间、可以使用的内存大小等。

语法如下：
[只做了解，具体的参数含义可以在自行查看]

```
# ulimit [-SHacdfltu] [配额]

# 列出所有的限制额度
# 如果结果为0，则表示不限制
>>> ulimit -a
```

8、变量内容的删除、取代与替换

（1）变量内容的删除

* 从前到后进行删除
    * `#`  删除符合的最短的数据
    * `##` 删除符合的最长数据
* 从后到前进行删除
    * `%`  删除符合的最短的数据
    * `%%` 删除符合的最长数据

```
# 变量内容的删除

# 从前到后进行删除
# ${变量#/关键词}
# ${变量##/关键词}

# 从后向前进行删除
# ${变量%/关键词}
# ${变量%%/关键词}

>>> path=${PATH}
>>> echo ${path#/*local/bin:}
>>> echo ${path##/*local/bin:}

>>> echo ${path%:*bin}
>>> echo ${path%%:*bin}
```

（2）变量内容的替换

* `/`  替换符合要求的一个字符串
* `//` 替换符合要求的所有字符串

语法如下：
```
# echo ${变量/旧字符串/新字符串}
# echo ${变量//旧字符串/新字符串}

>>> echo ${path/sbin/SBIN}
>>> echo ${path//sbin/SBIN}
```

（3）变量的测试与内容替换

##### 10.3 命令别名设定：`alias`、`unalias`

1、命令别名设定与取消

语法如下：

```
# alias 别名='指令 选项...'
# 例如：
alias lm='ls -l | more'
alias rm='rm -i'

# 取消命名
# unalias 指令名称
unalias lm
```

2、历史命令:`history`

常用如下：

```
# 显示n条历史命令：
history [n]

# 将目前shell中的所有history内容删除
history -c

# 读、追加与写
# history [-raw] histfiles
```

历史命令是如何读取与写入的：

* 当登录系统后，系统会主动地由家目录地~/.bash_history读取曾经下过的指令；
* 系统在注销的时候，会根据HISTORYFILESIZ的大小将最近的符合这个大小的记录到系统里；例如：登录系统之后下达了100条指令，HISTORYFILESIZE=1000的情况下，会将101\~1100这1000条指令更新到~/.bash_history中；
* 可以通过`history -w`强制写入，因为记录的指令数永远都是HISTORYFILESIZE大小，所以旧的已记录的指令会被主动拿掉更新成最新的已下达的指令。

##### 10.4、BASH SHELL的操作环境

1、路径与指令搜寻顺序

* 以相对/绝对路径执行指令，例如【/bin/ls】或【./ls】；
* 由`alias`找到指令来执行；
* 由bash内建的(builtin)指令来执行；
* 透过$PATH这个变量的顺序搜寻到的第一个指令来执行。


例如：(由于系统可能设置别名，所以结果可能有所不同)

```
>>> type echo
>>> echo is a shell builtin

>>> type ls
>>> ls is aliased to `ls --color=auto'

>>> type rm
>>> rm is /bin/rm
```

2、bash的进站与欢迎讯息: /etc/issue./etc/mod

（1）进站信息：/etc/issue

常见的值为：
```
# /etc/issue中的内容
\S
Kernel \r on an \m

# 含义
\S 表示操作系统名称
\r表示操作系统的版本（相当于uname -r）
\m表示硬件的等级（i380/i486/i586/i686...）

# 更多含义可参考man issue
```

（2）登录后获取到的信息：/etc/motd

所有用户都可以看到

3、bash的环境配置文件

（1）login与non-login shell

* login shell：取得bash时需要完整的登入流程的，就称为loginshell。
* non-login shell：取得bash接口的方法不需要重复登入的举动。像常用的在bash环境下输入`bash`指令产生的bash（子程序）就是non-login shell。

（2）login和non-login shell的区别

* 01、login-shell
    * /etc/profile：系统整体的配置文件，建议最好不要随意修改。
    * ~/.bash_profile或\~/.bash_login或\~/.profile：属于用户配置文件，可修改。

* /etc/profile：可以利用使用的UID来决定狠毒重要的变量数据。设定的变量主要由：

    * PATH：会依据UID决定PATH变量要不要含有sbin的系统指令目录；
    * MAIL
    * USER
    * HOSTNAME
    * HISTSIZE
    * umask：root默认为022而一般用户为002。

* /etc/profile.d/*.sh，/etc/profile.d/目录下由多个扩展名为.sh的文件，如果使用者具有r的泉下你，就会自动呼叫该叫版本。在CentOS7.x中，这个目录规范了bash操作接口的颜色、语系、ll与ls的别名、vi的别名、which的别名等。
* /etc/locale.conf：这个文件时被/etc/profile.d/lang.sh呼叫进来的，决定bash预设使用何种语系。文件里最重要的就是LANG/LC_ALL等变量的设定。
* /usr/share/bash-completion/completions/*：命令补全、文档名补全、指令的选项/参数补全等。

* ~/.bash_profile（login shell才会进行读取），系统会首先读取整体环境设定的配置文件，然后读取用户配置文件。文件主要使用的为下述三个中的一个，依序是：~/.bash_profile、~/.bash_login、~/.profile，读取的顺序按照这个顺序，读取到第一个之后，其他就不再进行读取。


```
graph LR
/etc/profile-->/.bash_profile
/etc/profile-.->/etc/profile.d/*.sh
/etc/profile.d/*.sh-.->/etc/locale.conf
/.bash_profile-->开始操作bash
/.bash_profile-.->/.bashrc
/.bashrc-.->/etc/bashrc
```
**[实线为主流程，虚线为被呼叫的配置文件]**

（3）source：读入环境配置文件的指令

由于/etc/profile与~/.bash_profile都是在login shell的时候才会读取，所以如果在登录之后修改了文件，则使用`source`指令即可不注销而直接让配置文件生效。

（4）~/.bashrc（non-login shell会读）

非登录获取bash操作接口的环境配置文件为~/.bashrc，注意/etc/bashrc为CentOS特有。

（5）其他配置文件

* /etc/man_db.conf：使用`man`指令的时候，man page的路径位置到那里去寻找
* ~/.bash_history：历史命令，每次登录bash后，bash会先读取这个文件，将所有的历史指令读入内存
* ~/.bash_logout：注销bash后读取的配置文件

4、终端机的环境设定：stty、set

当登录系统之后，可以利用退格键删除命令行上的字符、ctrl+c强制终止一个指令的运行；输入错误会有声音警告，这些都是登录终端机的时候自动获取的输入环境的设定。

（1）stty(setting tty)：`stty -a`获取目前环境中所有的按键列表，常用的如下：

* intr(ctrl+c)：强制终止指令运行；
* quit(ctr+\\)：发送一个quit的讯号给目前正在run的程序；
* erase(ctrc+?)：向后删除字符；
* kill(ctrl+U)：删除在目前指令列上的所有文字；
* eof(ctrl+D)：End of file，表示结束输入；
* start(ctrl+Q)：在某个程序停止后，重新启动它的output；
* stop(ctrl+S)：停止当前屏幕的输出；
* susp(ctrl+Z)：发送一个terminal stop的讯号给正在run的程序（可以通过fg直接回到stop的程序）。

**场景1**：

比如在`vim 某个文件`之后，误操作导致屏幕不动了(使用了ctrl+s)，可以通过ctrl+Q来恢复正常。

（2）set

* echo $-：查看目前所有的set设定值

