## chapter 15 上下文管理器和else块

**主要内容**

- [x] with语句

- [x] for、while和try语句的else子句

1、with语句

with语句会设置一个临时的上下文，交给上下文管理器对象控制，并且负责清理上下文。

这么做能避免错误并减少样板代码，因此API更安全，而且更容易使用。

2、先做这个，再做那个：if 之外的else块

* `for...else...` 仅当for循环运行完毕时（即for循环没有被break语句终止）才运行else块。
* `while...else...` 仅当while循环因为条件为假值而退出时（即while循环没有被break语句终止）才运行else块。
* `try...else...` 仅当try块中没有异常抛出时才运行else块。
* 在所有情况下，如果异常或者return、break、continue语句导致控制权跳到了复合语句的主块之外，else子句也会被跳过。

3、上下文管理器和with块

上下文管理器对象存在的目的是管理with语句，就像迭代器的存在是为了管理for语句。

* 上下文管理器协议包含`__enter__`和`__exit__`方法；
* with语句开始时，会在上下文管理器对象（with后的语句）调用`__enter__`方法，with语句运行结束后，会在上下文管理器对象上调用`__exit__`方法；
* `__exit__`方法扮演`finally`的角色，作用为释放资源或者还原临时变更的状态；
* with语句的目的是为了简化`try/finally`模式。
* as后的语句表示的为`__enter__`方法的返回值。

4、深入了解上下文管理器

`__exit__`方法的参数解析

主要包含三个参数，`exc_type`、`exc_val`、`exc_tb`

* `exc_type` 异常类（例如：`ZeroDivisionError`）
* `exc_val` 异常实例，如果有参数传给异常构造方法，这些参数可以使用`exc_val.args`获得；
* `exc_tb` traceback对象

5、contextlib模块中的实用工具

* `closing` 如果对象提供了`close()`方法，但没有实现`__enter__`/`__exit__`协议，那么可以使用这个函数构建上下文管理器；
* `suppress` 构建临时忽略指定异常的上下文管理器；
* `@contextmanager` 可以把简单的生成器函数变成上下文管理器；
* `ContextDecorator` 这是个基类，用于定义基于类的上下文管理器。这种上下文管理器也能用于装饰函数，在受管理的上下文中运行整个函数；
* `ExitStack` 这个上下文管理器能进入多个上下文管理器，with块结束时，`ExitStack`按照后进先出的顺序调用栈中的上下文管理器的`__exit__`方法。如果事先不知道with块要进入多少个上下文管理器，可以使用这个类。

6、使用@contextmanager

主要功能：通过使用这个装饰器可以把简单的生成器函数编程上下文管理器。[可以参见代码[ch15_mirror_gen_exc.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_15/ch15_mirror_gen.py)]

