#### 12、学习Shell Scripts

##### 12.1、为什么学习Shell Scripts

（1）、学习Shell Scripts的好处

* 自动化管理的重要依据；
* 追踪与管理系统的重要工作；
* 简单入侵检测功能；
* 连续指令单一化；
* 简易的数据处理；
* 跨平台支持与学习历程较短。

（2）执行Shell Scripts的注意事项

* 指令的执行是从上而下、从左而右的分析与执行；
* 指令、选项与参数间的多个空格都会被忽略掉；
* 空行会被忽略，并且[tab]按键形成的空白同样被视为空格；
* 如果遇到Enter符号（CR），就会尝试开始执行该行（或该串）指令；
* 如果一行的内容太多，可以使用【\\[enter]】来延申至下一行；
* 【#】可作为注释，任何在#后面的文字都会被当作注释而被忽略掉。

（3）如何执行Shell Scripts

* 直接指令下达：shell.sh文件必须具备可读与可执行(rx)的权限，然后：
    *  绝对路径：使用`/home/dmtsai/shell.sh`来下达指令；
    *  相对路径：在当前目录下，使用`./shell.sh`来执行；
    *  变量[PATH]功能，将shell.sh放在PATH指令的目录内，例如：~/bin/。
* 以bash程序来执行：`bash shell.sh`或`sh shell.sh`来执行。

（4）撰写Shell Scripts的良好习惯简历

在每个script的文件开头记录如下内容：

* script的功能；
* script的版本信息；
* script的作者与联系方式；
* script的版权宣告方式；
* script的History（历史记录）；
* script内特殊的指令，使用【绝对路径】的方式来下达；
* script执行时需要的环境变量预先宣告与设定；
* 必要的地方最好要加上注释；
* 代码块最好能以[tab]键进行缩进保持美观同时更方便问题排查；
* 推荐工具vim而不是vi，因为vim会有语法检验机制。

##### 12.2、简单的shell script练习

（1）常用指令介绍

```
# 执行过程中输入相关内容进行交互
read -p "提示内容" variable_name

# date的用法

# 前N天
date --date='2 days ago' +%Y%m%d
date --date='1 days ago' +%Y%m%d

# 执行指令
$(command)

# 数学计算
$((数学计算表达式))
"数学计算表达式" | bc
# 例如
echo "$((10*20))"
echo "10*20" | bc

# 如何计算pi的值，通过bc指令
#待续
```

（2）执行shell script方式的差异

* 直接执行（sh script或./scirpt）：在子程序中执行（子程序中执行过后的变量如果直接在父程序中获取变量的内容获取不到）；
* `source script`在父程序中执行。

#### 10.3、善用判断式

（1）利用test指令的测试功能

> 执行结果：不会显示任何我信息，可以通过$?或&&及||来展示整个结果。

例如：

```
test -e /dmtsai && echo "exist" || echo "Not exist"
```