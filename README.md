# 流畅的Python中的例子

基于python3,不兼容python2

## 第三章 字典和集合

#### 1、魔术方__missing__

__missing__ 主要使用在字典查询键值找不到键值的时候

[ch03_the_magic_method_of_missing](https://github.com/feng-hui/fluent_python_examples/blob/master/ch03_the_magic_method_of_missing.py)

## 第五章 一等函数

#### 1、用户定义的可调用类型

只要用户在类中实现了魔术方法__call__即可让对应的类可以像函数一样被调用,可以通过内置函数callable()来检测是否可以被调用。

[ch05_bingo](https://github.com/feng-hui/fluent_python_examples/blob/master/ch05_bingocall.py)
