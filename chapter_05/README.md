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

* 函数在调用的时候创建，满足1中的条件1；

* fact = factorial，可以赋值给变量，满足1中的条件2；

* map(factorial, range(10)),可以作为参数传给函数，满足1中的条件3；

* 函数可以在闭包中使用，满足条件4。[参见《流畅的python》第7章装饰器]

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

** 除了作为参数传递给高阶函数之外，Python很少使用匿名函数。**

** 由于句法上的限制，非平凡的lambda表达式要么难以阅读，要么无法写出。**

7、可调用对象

(1)什么是可调用对象？ 如果判断对象是否能调用，可以使用内置的`callable()`函数,例如`callable(sum)`,如果可调用,返回True,否则,返回False。

(2)Python数据模型文档列出7种可调用对象

* 用户定义的函数：使用def语句或lambda表示创建；

* 内置函数：使用C语言(CPython)实现的函数,如len或time.strftime

* 内置方法：使用C语言实现的方,如：dict.get；

* 方法：在类的定义体中定义的函数；

* 类：调用类时会运行类的__new__方法创建一个实例,然后运行__init__方法初始化实例,最后把实例返回给调用方。

* 类的实例：如果类定义了__call__方法，那么它的实例可以作为函数调用([详情参见代码](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_05/ch05_bingocall.py))；

* 生成器函数：使用yield关键字的函数或方法。调用生成器函数返回的是生成器对象。

8、函数内省(function introspection)

(1)什么是内省？内省是对属性、事件的一种缺省处理方法。（通俗地来讲，当你拿到一个函数对象，可以通过函数内省知道它的属性、参数等信息。）

(2)使用dir(object)可以获得所有函数对象的属性。

(3)函数特有的属性([参见代码](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_05/ch05_attribute_of_function.py))

|名称|类型|说明
| __annotations__| dict| 参数和返回值的注解
| __call__| method-wrapper| 实现()运算符；即可调用对象协议
| __closure__| tuple| 函数闭包,即自由变量的绑定
| __code__| code| 编译成字节码
| __defaults__| tuple| 形式参数的默认值
| __get__| method-wrapper| 实现只读描述协议（参见第20章）
| __globals__| dict| 函数所在模块的全局变量
| __kwdefaults__| dict| 仅限关键字形式参数的默认值
| __name__| str| 函数名称
| __qualname__| str| 函数的限定名称,如Random.choice（参阅PEP3155）

9、仅限关键字参数(keyword-only argument)

\* 位置参数或定位参数,支持list和set

** 关键字参数,支持dict

类似cls=None, 关键字参数的一种,如果在参数强制必须传入值,则可以写成(a, *, b), 实参为类似(1, b=2)。

10、函数注解

`def clip(text: str, max_len: 'int > 0'=80) -> str: pass`

类似上述写法即为函数注解。

parameter: type

parameter: 'expression'=value

function -> type

函数声明的各个参数可以在:后增加注解表达式。如果参数有默认值,注解放在参数名和等号之间。

注解返回值，在)和函数声明末尾：之间添加一个->和一个表达式。

11、函数参数的种类

可以通过`inspect.Signature.parameters`获取所有参数的种类和默认值,直接`from inspect import signature`即可

参数的种类包括：

名称|解释
POSITIONAL_OR_KEYWORD| 可以通过定位参数或关键字参数传入的形参（多数Python函数的参数属于此类）
VAR_POSITIONAL| 定位参数元组
VAR_KEYWORD| 关键字参数字典
KEYWORD_ONLY| 仅限关键字参数(Python3新增)
POSITIONAL_ONLY| 仅限定位参数

12、支持函数式编程的模块

operator模块,常用的数学相关的模块add、mul等

Name | Academy | score
- | :-: | -:
Harry Potter | Gryffindor| 90
Hermione Granger | Gryffindor | 100
Draco Malfoy | Slytherin | 90
---------------------
作者：tuxingchen6
来源：CSDN
原文：https://blog.csdn.net/tuxingchen6/article/details/55222951
版权声明：本文为博主原创文章，转载请附上博文链接！




