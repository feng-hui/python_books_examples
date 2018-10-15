# 流畅的Python中的例子

基于python3,不兼容python2

## 第三章 字典和集合[全部总结](https://github.com/feng-hui/fluent_python_examples/blob/master/summary/chapter03_summary.md)

#### 1、魔术方__missing__

__missing__ 主要使用在字典查询键值找不到键值的时候

[ch03_the_magic_method_of_missing](https://github.com/feng-hui/fluent_python_examples/blob/master/ch03_the_magic_method_of_missing.py)

## 第五章 一等函数

#### 1、用户定义的可调用类型

只要用户在类中实现了魔术方法__call__即可让对应的类可以像函数一样被调用,可以通过内置函数callable()来检测是否可以被调用。

[ch05_bingo](https://github.com/feng-hui/fluent_python_examples/blob/master/ch05_bingocall.py)

#### 2、仅限关键字参数的用法(keyword-only)

通过一个生成含有一个标签或多个标签的html来说明关键词参数是如何使用的。同时通过function(a, *, b)函数强制传入形参b，实际参数类似b=2。

[ch05_keyword_only-argument](https://github.com/feng-hui/fluent_python_examples/blob/master/ch05_keyword_only.py)

#### 3、[函数内省](https://segmentfault.com/q/1010000012595419)的用法

通过dir()函数可以获得一个函数所有的方法、属性、参数值等，这些方法或属性或值表示函数有什么功能。

[ch05_introspection_function](https://github.com/feng-hui/fluent_python_examples/blob/master/ch05_introspection_function.py)


