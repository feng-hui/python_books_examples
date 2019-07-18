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

#### 12.3、善用判断式

（1）利用test指令的测试功能

> 执行结果：不会显示任何我信息，可以通过$?或&&及||来展示整个结果。

例如：

```
test -e /dmtsai && echo "exist" || echo "Not exist"
```

test语法如下：

测试的标志 | 代表意义
-- | --
/ | 1、关于某个文档的【类型判断】
-e | 该【文档】是否存在?(常用)
-f | 该【文档】是否存在且为文件(file)?(常用)
-d | 该【文档】是否存在且为目录(directory)?(常用)
/ | 2、关于文档的权限检测
-r | 检测该文档是否存在且具有【可读】的权限?
-w | 检测该文档是否存在且具有【可写】的权限?
-x | 检测该文档是否存在且具有【可执行】的权限?
/ | 3、两个文件之间的比较
-nt | （newer than）判断file1是否比file2新
-ot | （older than）判断file1是否比file2旧
-ef | 判断file1与file2是否为同一个文件，主要用于判断两个文件是否指向统一inode
/ | 4、两个整数之间的比较
-eq | 相等（equal）
-ne | 不等（not equal）
-gt | n1 > n2（greater than）
-lt | n1 < n2（less than）
-ge | n1 >= n2（greater than or equal）
-le | n1 <= n2（less than or equal）
/ | 5、判断字符串的数据
test -z string | 判断字符串是否为0？若string为空字符串，则为true
test -n string | 判断字符串是否不为0？若string为空字符串，则为false。（-n可省略）
test str1==str2 | 判str1是否等于str2，若相等，则为true（bash中=和\==是相同的，推荐使用==）
test str1!=str2 | 判str1是否不等于str2，若相等，则为false
/ | 6、多重条件判断
-a | and
-o | or
!  | 取反

参考例子：`file_perm.sh`

（2）利用判断符号[]

例如：`[ -z "$HOME" ];echo $?` 判断$HOME是否为空然后输出返回值

**使用[]注意：*

* 在中括号[]内的每个组件都需要右空格键来分隔；
* 在中括号内的变量，最好都以双引号括起来；
* 在中括号内的常量，最好都以单引号或双引号括起来。

（3）Shell Script的默认变量（$0,$1...）

* $#：表示script后接的参数【个数】；
* $@：表示【"$1" "$2" "$3" "$4" 】，每个变量是独立的（用双引号括起来）；
* $*：表示【 "$1<u>c</u>$2<u>c</u>$3<u>c</u>$4" 】，其中<u>c</u>默认空格键。

$@和$*有所区别，但是一般使用$@即可。

参考例子:`how_paras.sh`

脚本后的参数可以通过`shift`指令产生偏移，例如:`shift 1`表示移除第一个参数。

##### 12.4、条件判断式

（1）if...then

语法如下：

```
# 语法1
if [ 条件判断式 ]; then
    条件成立，执行
fi

# 语法2
if [ 条件判断式 ]; then
    条件成立，执行
else
    条件不成立，执行
fi

# 语法3：
if [ 条件判断式1 ]; then
    条件1成立，执行
elif [ 条件判断式2 ]; then
    条件2成立，执行
else
    条件1和2不成立，执行
fi
```

（2）利用case...esac判断

语法如下：
```
case $变量名称 in
    "第一个变量内容")
        待执行的代码块1
        ;;
    "第二个变量内容")
        待执行代码块2
        ;;
    *）
        变量内容不包含在第一个和第二个变量内容中，待执行代码块3
        ;;
esac
```

(3)利用function功能

语法如下：

```
funciton fname() {
    代码块
}

# fname自定义执行指令名称
# shell script执行自上而下、由左到右
# function拥有内建变量，与shell script类似，$0表示函数名称，$1、$2...表示实参1、实参2...
```

##### 12.5、循环（loop）

（1）、while do done, util do done（不定循环）

```
# 语法1
# while do done
# 条件不成立、结束循环
while [condition]
do
    代码块
done

# 语法2
# 条件成立、结束循环
# util do done
util [condition]
do
    代码块
done
```

参考例子：`yes_to_stop.sh`

（2）、for do done（固定循环）

语法如下：

```
for var in con1 con2 con3
do
    代码块
done
```

（3）、for do done的数值处理
```
for ((start;stop;step))
do
    代码块
done
```

##### 12.6 Shell Script如何进行debug

```
# sh -n
# 不执行script，仅查询语法问题


# sh -v
# 在执行scripts之前，先将script的内容输出到屏幕上

# sh -x
# 将使用到的script内容显示到屏幕上，相当于debug功能。
```