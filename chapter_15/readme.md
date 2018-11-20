## chapter 15 上下文管理器和else块

**主要内容**

- [x] with语句

- [x] for、while和try语句的else字句

1、with语句

with语句会设置一个临时的上下文，交给上下文管理器对象控制，并且负责清理上下文。

这么做能避免错误并减少样板代码，因此API更安全，而且更容易使用。

2、先做这个，再做那个：if 之外的else块

* `for...else...` 仅当for循环运行完毕时（即for循环没有被break语句终止）才运行else块。

* `while...else...` 仅当while循环因为条件为假值而退出时（即while循环没有被break语句终止）才运行else块。

* `try...else...` 仅当try块中没有异常抛出时才运行else块。

* 在所有情况下，如果异常或者return、break、continue语句导致控制权跳到了复合语句的主块之外，else子句也会被跳过。