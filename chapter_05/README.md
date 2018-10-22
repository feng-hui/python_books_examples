## 一等函数

1、什么是一等函数？

编程语言理论家把“一等对象”定义为满足下述条件的程序实体：

    * 在运行时创建；

    * 能赋值给变量或数据结构中的元素；

    * 能作为参数传给函数；

    * 能作为函数的返回结果。

2、一等函数例子[返回一个给定的数字n的阶乘]

```
def factorial(n):
    """return n!"""
    return 1 if n < 2 else factorial(n - 1) * n
```

+ 函数在调用的时候创建，满足1中的条件1；

+ fact = factorial，可以赋值给变量，满足1中的条件2；

+ map(factorial, range(10)),可以作为参数传给函数，满足1中的条件3；

+ 函数可以在闭包中使用，满足条件4。[参见《流畅的python》第7章装饰器]

3、什么是高阶函数(high-order function)？

高阶函数：接受函数为参数或者把函数作为结果返回的函数。

常见的高阶函数：map、reduce、filter、sorted等。

例如：

`fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']`

`sorted(fruits, key=len)`

4、map、filter、listcomps

map、filter返回的为生成器，listcomps返回的为列表。

代码参见[ch05_map_filter_listcomps.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_05/ch05_map_filter_listcomps.py)

5、计算0～99之和?

（1）方法1：直接使用sum函数,`sum(range(100))`

（2）方法2,使用reduce和add函数

```
from functools import reduce
from operator import add
reduce(add, range(100))
```

代码参见[ch05_summation.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_05/ch05_summation.py)

6、匿名函数(lambda)

匿名函数： 通过lambda关键字在Python表达式内创建匿名函数。

** 除了作为参数传递给高阶函数之外，Python很少使用匿名函数。 **

** 由于句法上的限制，非平凡的lambda表达式要么难以阅读，要么无法写出。 **

7、可调用对象

(1)什么是可调用对象？ 如果判断对象是否能调用，可以使用内置的`callable()`函数,例如`callable(sum)`,如果可调用,返回True,否则,返回False。

(2)Python数据模型文档列出7种可调用对象

    * 用户定义的函数：使用def语句或lambda表示创建；

    * 内置函数：使用C语言(CPython)实现的函数,如len或time.strftime

    * 内置方法：使用C语言实现的方,如：dict.get；

    * 方法：在类的定义体中定义的函数；

    * 类：调用类时会运行类的__new__方法创建一个实例,然后运行__init__方法初始化实例,最后把实例返回给调用方。

    * 类的实例：如果类定义了__call__方法，那么它的实例可以作为函数调用[详情参见代码](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_05/ch05_bingocall.py)；

    * 生成器函数：使用yield关键字的函数或方法。调用生成器函数返回的是生成器对象。

8、函数内省(function introspection)





