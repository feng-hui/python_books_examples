## chapter 16 协程

**主要内容**

- [x] 生成器作为协程使用时的行为和状态

- [x] 使用装饰器预激协程

- [x] 调用方法如何使用生成器对象的`.close()`和`.throw(...)`方法控制协程

- [x] 协程终止时如何返回值

- [x] yield from 新句法的用途和含义

- [x] 使用案例——使用协程管理仿真系统中的并发活动

#### 1、什么是协程？

协程是指一个过程，这个过程与调用方协作，产出由调用方提供的值。

**协程的使用和特性**

* 生成器的调用方可以使用`.send(...)`方法发送数据，`.throw()`方法让调用方抛出异常，`.close()`贩方法是终止生成器。
* Python3.3（2012年）对生成器的语法新增了两处改动：
    * 生成器可以返回一个值，Python3.3之前的版本是不可以的，如果给return提供值，会抛出SyntaxError异常；
    * 新引入了`yield from`句法，使用它可以把复杂的生成器重构成小型的嵌套生成器，省去了把之前的工作委托给子生成器所需的大量样板代码。

#### 2、协程状态

协程有四个状态，状态可以通过`inspect.getgeneartorstate(...)`函数确定[使用方法：`import inspect`]。

01、GEN_STARTED 协程等待开始

02、GEN_RUNNING 解释器正在执行

03、GEN_SUSPENDED 在yield表达式处暂停

04、GEN_CLOSED 执行结束。

#### 3、终止协程和异常处理

01、throw方法 异常处理

`generator.throw(exc_type[, exc_value[, traceback]])`

致使生成器在暂停的yield表达式处抛出指定的异常。

02、close方法 终止协程

`generator.close()`

致使生成器在暂停的yield表达式处抛出GeneratorExit异常。

#### 4、如何使用`yield from`?

01、Python 3.3 引入`yield from`的原理和意义?

* `yield from x` 表达式对x对象所做的第一件事是，调用`iter(x)`，从中获取迭代器。

* `yield from` 的主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来，这样二者可以直接发送和生产值，还可以直接传出，而不用在位于中间的协程中添加大量处理异常的样板代码。有了这个结构，协程可以通过以前不可能的方式委托职责。

02、相关名词解释

[参见对应的代码](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_16/ch16_coroaverager3.py)

委派生成器：包含yield from <iterable> 表达式的生成器函数。

子生成器：从yield from 表达式中<iterable> 部分获取的生成器。

调用方：PEP380 使用“调用方”这个术语指代委派生成器的客户端代码。

03、yield from的意义

* 子生成器产出的值都直接传给委派生成器的调用方；
* 使用send()方法发给委派生成器的值都直接传给子生成器；
* 生成器退出时，生成器（或子生成器）中的`return expr`表达式会触发StopIteration异常抛出；
* yield from表达式的值是生成器终止时传给StopIteration异常的第一个参数；
* 传入委派生成器的异常，除了GeneratorExit之外都传给子生成器的throw()方法,如果调用throw()方法时抛出StopIteration异常，委派生成器恢复运行。StopIteration之外的异常会向上冒泡，传给委派生成器。
* 如果把GeneratorExit异常传入委派生成器，或者在委派生成器上调用close()方法，那么在子生成器上调用close()方法。如果调用close()方法导致异常抛出，那么异常会向上冒泡，传给委派生成器；否则委派生成器抛出GeneratorExit异常。
