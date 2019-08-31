#### 9、vim程序编辑器

##### 9.1、vi与vim

（1）为什么要学习vim?

* 所有的Unix Like系统都会内建vi文本编辑器，其他的文本编辑器不一定存在；
* 有很多软件的编辑接口都会主动调用vi（例如：crontab、visudo、edquota等）；
* vim具有程序编辑的能力，可以主动地以字体颜色辨别语法地正确性，方便程序设计；
* 程序简单，编辑相当快速。

**可以将vim视为vi的进阶版本。**

##### 9.2、vi的使用

（1）vi的三种模式

* 一般指令模式（command mode）：以vi打开一个文件称为一般指令模式（默认模式），可以使用[上下左右]按键来移动光标、可以删除字符或删除整列、或者使用复制粘贴来处理文件。
* 编辑模式（insert mode）：可以使用[i，I，o，O，a，A，r，R]进入编辑模式。
* 指令列命令模式（command-line mode）：在一般模式下，输入[:|/|?]三个中任何一个按钮，可以搜索、保存、替换、退出、显示或取消行号等相关操作。

（2）vi使用快捷键说明（只统计常用的，其他请自行google或参考鸟哥Linux私房菜第9章内容）

A、一般指令模式下

快捷键 | 说明
-- | --
/ | 1、快捷移动光标的方法
h / (向左箭头) | 光标向左移动一个字符
j / (向下箭头) | 光标向下移动一个字符
k / (向上箭头) | 光标向上移动一个字符
l / (向右箭头) | 光标向右移动一个字符
crtl + f | 屏幕【向下】移动一页，相当于【Page Down】按键
crtl + b | 屏幕【向上】移动一页，相当于【Page Up】按键
0或功能键【Home】 | 移动到光标所在行的最前面字符处
$或功能键【End】 | 移动到光标所在行的最后面字符处
G | 移动到这个文件的最后一列
gg或1G | 移动到这个文件的第一列
n + 回车 | n表示数字，例如：按下3再回车，表示向下移动3行
/ | 2、搜索与替换
/word | 向下搜索名称为word的字符串
?word | 向上搜索名称为word的字符串
n | 重复前一个搜索动作，常用于搜索完跳到下一个或上一个搜索到的字符串位置
N | 同n相反，例如：向下搜索，使用N之后则为向上进行搜索
:n1,n2s/word1/word2/g | n1、n2均为数字，表示在n1和n2之间进行搜索word1这个字符串并替换为word2字符串
:1,$s/word1/word2/g | 全文搜索并替换
:1,$s/word1/word2/gc | 全文搜索并替换，替换之前需要确认（确认根据提示输入y即可）
/ | 3、删除、复制与粘贴
x / X | x（相当于[del]功能键）向后删除，X向前删除
dd | 删除整行
ndd | n表示数字，删除光标所在行下的n行
yy | 复制光标所在行
nyy | n表示数字，复制光标所在行后的n行
p/P | p将复制的数据粘贴在光标下一行上，P则为从当前行插入，当前行向下顺延，例如从第10行开始粘贴20行数据，则原来的第10行经过粘贴后到第30行。
u | 撤销上一个动作

B、从一般指令模式切换为编辑模式

快捷键 | 说明
-- | --
i,I | 进入插入模式（Insert mode）：<br>i为【从光标所在处插入】，I为【从光标所在行的第一个非空字符处开始插入】
a,A | 进入插入模式（Insert mode）：<br> a为【从光标所在的下一个字符处开始插入】,A为【从光标所在行的最后一个字符处开始插入】
o,O | 进入插入模式（Insert mode）：<br> o为【从光标所在行的下一行进行插入】,O为【从光标所在行的上一行进行插入】
r,R | 进入取代模式Replace mode）：<br> r只会取代光标处的字符1次，R会一直取代光标所在的文字直到按下ESC为止。
ESC | 退出编辑模式，回到一般指令模式

C、一般指令模式切换到指令列模式

快捷键 | 说明
-- | --
:w | 写入到文件
:w! | 当文件为只读属性，强制写入，是否能够写入，与文件的权限有关
:q | 退出vi
:q! | 修改过文件但不想保存，强制离开vi
:wq | 保存
:w [filename] | 将编辑的文件另存为一个新文件

D、vim环境的变更

快捷键 | 说明
-- | --
:set nu | 显示行号
:set nonu | 取消显示行号

（3）vim的暂存、救援回复与开启时的警告讯息

> 当系统因为某些原因而导致类似宕机的情况，vim可以通过【暂存】机制来恢复编辑未保存的数据。

当编辑某个vim，例如:ss.sh，按下`crtl + z`，通过`ls -al`可以看到如`.ss.sh.swp`的暂存文档，这个文档主要记录修改的动作，如果这个时候系统宕机或者通过命令`kill -9 %1`模拟宕机，再打开该文件的时候可以看到提示信息，按照提示信息进行操作即可恢复编辑过未保存的文件。

暂存恢复按钮如下：

恢复操作 | 说明
-- | --
[O]pen Read-Only | 以只读方式打开该文件
(E)dit anyway | 正常编辑
(R)ecover | 恢复编辑但未保存的内容
(D)elete it | 删除暂存盘的内容
(Q)uit | 退出
(A)bort | 退出

##### 9.3 vim的额外功能

第一次打开一个vim文件的时候，在文件的最下方会显示如下信息：
* vim会进行语法检验，不同内容会显示不同的颜色，例如：注释显示为深蓝色
* 文件的最下方【左边】显示该文件的属性，包括行数、字符数，如果为只读，显示只读属性；
* 文件的最下方【右边】显示光标的位置以及光标处在文件的位置，例如：当光标在第一行显示为：1,1 Top，1,1为行列信息，Top为大概的位置信息，可能为Top，20%、Bot等类似信息。

（1）区块选择(Visual  Block)

> 上文提到的不管是复制粘贴或是其他操作，基本都是以列为单位进行的操作，下面介绍一下如何搞定一个区块范围？

快捷键 | 说明
-- | --
v | 字符选择，会选择光标经过的地方，被选择的地方呈现为白色
V | 列选择，，会选择光标经过的地方，被选择的地方呈现为白色
ctrl + v | 区块选择，会选择光标经过的地方，被选择的地方呈现为白色
y | 复制选择的内容
d | 删除选择的内容
p | 将复制的区块，粘贴在光标位于的位置

**按下v或V或ctrl + v在脚本底部会出现VISUAL BLOCK字样**

（2）多文件编辑

> 使用命令`vim a.sh b.sh`同时打开两个文件，然后通过如下命令可同时编辑两个文件

使用方法：通过上述命令同时打开两个文件之后，可以进行一个文件复制粘贴到另一个文件上或者进行其他可以进行的操作。

使用场景：快速复制想要复制的内容到另外一个文件里去

命令 | 说明
-- | --
:n | 编辑下一个文件
:N | 编辑上一个文件
:files | 列出目前这个vim开启的所有文件

（3）多窗口功能

> 场景: 比对一个大文件前后的数据，避免来回查看

使用方法：在指令列模式下输入`:sp {filename}`打开对应的文件，filename不填默认再次打开当前文件，切换窗口可参照如下命令：

命令 | 说明
-- | --
:sp [filename] | 开启一个新窗口，默认打开当前文件
ctrl+w + j<br>ctrl+w + 向下箭头 | 移动到下一个窗口，使用方法：先按下ctrl键不放，然后按下w后放开所有的键，然后再按下j（向下箭头），则光标可移动到下一个窗口
ctrl+w + k<br>ctrl+w + 向上箭头 | 移动到下一个窗口，使用方法：先按下ctrl键不放，然后按下w后放开所有的键，然后再按下j（向下箭头），则光标可移动到下一个窗口
ctrl+w + q | 关闭当前档口

（4）vim的补全功能

命令 | 使用说明
-- | --
ctrl + x -> ctrl + n | 以当前正在编辑的文件中的内容作为补全依据（常用）
ctrl + x -> ctrl + f | 以当前正在编辑的文件所处的目录中的文件名称作为补全依据
ctrl + x -> ctrl + o | 以当前文件的扩展名作为语法补充、以vim内建的关键词作为补全依据（常用）

（5）vim环境设定与记录：~/.vimrc,~/.viminfo

A、操作行为记录

> 当我们打开一个脚本文件，经常可以看到有些文字被高亮显示或者当我们搜索之后再次打开发现上次的搜索结果记录依然存在，下面介绍一下这个原理。

原理：

因为vim会主动将我们对于文件的操作行文记录下来，让我们可以下次再次打开的时候更方便操作，记录操作行为的文件为：~/.viminfo。

B、环境设定

设定参数 | 说明
-- | --
:set nu<br>:set nonu | 设置与取消行号
:set hlsearch<br>:set nohlsearch | 设置与取消高亮搜索，默认：hlsearch
:set hlsearch<br>:set nohlsearch | 设置与取消高亮搜索，默认：hlsearch
:set autoindent<br>:set noautoindent | 设置与取消自动缩进
:set backup<br>:set nobackup | 是否自动备份，一般是nobackup，设置之后会在文件所在目录下自动生成filename~文件，记录原始的filename内容
:set ruler<br>:set noruler | 是否显示文档底部的说明信息）（控制右下角状态栏）
:set showmode<br>:set showmode | 是否类似--INSERT--的字样（控制左下角状态栏）\
:set backspace=(012) | 进入编辑模式是否可以通过退格键(backspace)删除任意字符，设置为2，删除任意值，设置为0或1，可以删除刚刚输入的字符，而无法删除原来的文字
:set all | 查看所有的vim环境参数设定值
:set | 查看与系统默认值不同的设定参数，一般为用户自己设置的参数
:syntax on<br>:syntax off | 是否根据程序语法显示不同颜色，例如：纯文本文档，如果开头以#开始，那么这一列为蓝色
:set bg=dark<br>:set bg=light | 设置北京色，默认：light

C、vim的默认值一般放在在/etc/vimrc这个文件里，可以通过新建或修改~/.vimrc（当前用户下）文件来自行设置想要设置的参数

例如：

```
vi ~/.vimrc

# 内容如下
set hlsearch
set backspace=2
set autoindent
set ruler
set showmode
set nu
set bg=dark
syntax on
```

##### 9.4、其他注意事项

（1）中文编码问题

常用中文编码有big5和utf8两种，如果文件是使用big5编码生成的，而vim所处的终端接口是使用的utf8编码，则由于编码不同，打开的文件是一对乱码。

（2）DOS与linux的换行符

* DOS(Windows系统)的换行符为^M$，为CR和LF两个符号
* Linux下只有LF($)一个符号

Linux下如果执行shell脚本，判断两条指令的依据是Enter，Linux的Enter为LF符号，而DOS下生成的文件的换行符为CRLF（多个^M），这样脚本就无法执行。

（2）编码转换（dos2unix、unix2dos）

```
# 语法介绍如下
dos2unix/unix2dos [-kn] file [newfile]

-k 表示保留该文件原本的mtime时间格式（不更新文件上次内容经过修订的时间）
-n 保留原本的文档内，将转换后的内容输出到新文件

# 例子

mkdir /home/**

cp -a /etc/man.config .

# unix2dos

unix2dos -k man.config
dos2unix -k -n man.config man.config.linux
```

（3）语系编码转换

A、语法介绍

```
iconv -f 原本编码 -t 新编码 filename [-o newfile]

--list/-l   列出iconv支持的所有语系
-f          from，表示原本的编码
-t          to，表示要更改为什么编码
-o          输出到一个新的文件
```

B、语系编码转换例子

```
# 下载文件到当前目录
wget http://linux.vbird.org/linux_basic/0310vi/vi.big5

# 转换编码格式为utf8并存储为新的文件
iconv -f big5 vi.big5 -t utf8 -o vi.utf8

# 通过file命令查看文件为什么格式
file vi*

# 查看的结果如下
>>> vi.big5: ISO-8859 text, with CRLF line terminators
>>> vi.utf8: UTF-8 Unicode text, with CRLF line terminators

# 将繁体转换为简体
iconv -f utf8 -t big5 vi.utf8 | iconv -f big5 -t gb2312 | iconv -f gb2312 -t utf8 -o vi.gb.utf8
```