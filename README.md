> 流畅的Python

- [x] 基于Python3,不兼容Python2

- [x] 目录结构如下

* 第一部分　序幕

    * chapter 01 Python 数据模型

* 第二部分　数据结构

    * chapter 02 序列构成的数组

    * chapter 03 字典和集合

    * chapter 04 文本和字节序列

* 第三部分　把函数视作对象

    * chapter 05 一等函数

    * chapter 06 使用一等函数实现设计模式

    * chapter 07 函数装饰器和闭包

* 第四部分　面向对象惯用法

    * chapter 08 对象引用、可变性和垃圾回收

    * chapter 09 符合 Python 风格的对象

    * chapter 10 序列的修改、散列和切片

    * chapter 11 接口：从协议到抽象基类

    * chapter 12 继承的优缺点

    * chapter 13 正确重载运算符

* 第五部分　控制流程

    * chapter 14 可迭代的对象、迭代器和生成器

    * chapter 15 上下文管理器和 else 块

    * chapter 16 协程

    * chapter 17 使用期物处理并发

    * chapter 18 使用 asyncio 包处理并发

* 第六部分　元编程

    * chapter 19 动态属性和特性

    * chapter 20 属性描述符

    * chapter 21 类元编程

#### chapter01 Python 数据模型

* (1) [ch01_nametuple.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_01/ch01_nametuple.py) 具名元组的使用

* (2) [ch01_vector.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_01/ch01_vector.py) 如何构建一个满足需求的向量类？

* (3) [ch01_vector_v2.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_01/ch01_vector_v2.py)

#### chapter02 序列构成的数组

#### chapter03 字典和集合

1、魔术方法__missing__

__missing__ 主要使用在字典查询键值找不到键值的时候

[ch03_the_magic_method_of_missing](https://github.com/feng-hui/fluent_python_examples/blob/master/ch03_the_magic_method_of_missing.py)

#### chpater04 文本和字节序列

#### chapter05 一等函数

1、用户定义的可调用类型

只要用户在类中实现了魔术方法__call__即可让对应的类可以像函数一样被调用,可以通过内置函数callable()来检测是否可以被调用。

[ch05_bingo](https://github.com/feng-hui/fluent_python_examples/blob/master/ch05_bingocall.py)

2、仅限关键字参数的用法(keyword-only)

通过一个生成含有一个标签或多个标签的html来说明关键词参数是如何使用的。同时通过function(a, *, b)函数强制传入形参b，实际参数类似b=2。

[ch05_keyword_only-argument](https://github.com/feng-hui/fluent_python_examples/blob/master/ch05_keyword_only.py)

3、[函数内省](https://segmentfault.com/q/1010000012595419)的用法

通过dir()函数可以获得一个函数所有的方法、属性、参数值等，这些方法或属性或值表示函数有什么功能。

[ch05_introspection_function](https://github.com/feng-hui/fluent_python_examples/blob/master/ch05_introspection_function.py)

#### chapter06 使用一等函数实现设计模式

1、order 购物订单模型(经典"策略模式")

经典的“策略”模式，使用[“策略”设计模式](https://baike.baidu.com/item/%E7%AD%96%E7%95%A5%E6%A8%A1%E5%BC%8F/646307?fr=aladdin)处理订单折扣

[ch06_order](https://github.com/feng-hui/fluent_python_examples/blob/master/ch06_order.py)

2、another_oder 使用一等函数实现"策略模式"

使用一等函数替代ch06_order中的类来简化“策略”模式

[ch06_another_order](https://github.com/feng-hui/fluent_python_examples/blob/master/ch06_another_order.py)

#### chapter07 使用一等函数实现设计模式

#### chapter07 使用一等函数实现设计模式

* (1) [ch07_deco.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_deco.py) 一个最简单的装饰器

* (2) [ch07_registration.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_registration.py) Python何时执行装饰器

* (3) [ch07_orderdeco.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_orderdeco.py) 使用装饰器改造“策略”模式

* (4) [ch07_average_oo.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_average_oo.py) 闭包，见代码里的类`Avg`

* (5) [ch07_simple_decor.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_simple_decor.py) 定义一个简单的`clock`装饰器，输出函数的运行时间

* (6) [ch07_clockdeco_demo.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_clockdeco_demo.py) 引入`clock`装饰器，装饰定义好的函数（函数分别为：factorial函数和fibonacci函数）

* (7) [ch07_clockdeco_param.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_clockdeco_param.py) 引入参数进一步丰富装饰器的功能，参数主要为输出的具体格式

* (8) [ch07_parameterized_deco.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_parameterized_deco.py) 参数化的装饰器，主要使用的为2中定义的一个`registration`函数

* (9)  [ch07_single_dispatch_deco.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_07/ch07_single_dispatch_deco.py) 标准库中的装饰器2-singledispatch的使用，该装饰器的一个显著特征是可以在系统中的任何地方和任何模块中注册专门函数，支持模块化扩展。

#### chapter08 对象引用、可变性和垃圾回收

#### chapter09  符合 Python 风格的对象

* (1) [ch09_vector2d.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_09/ch09_vector2d.py) 改造向量类

* (2) [ch09_vector2d_03.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_09/ch09_vector2d_03.py) 向量类的可散列、私有属性的使用以及`__slots__`的使用

* (3) [ch09_the_difference_of_staticmethod_and_classmethod.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_09/ch09_the_difference_of_staticmethod_and_classmethod.py) classmethod和staticmethod的使用

