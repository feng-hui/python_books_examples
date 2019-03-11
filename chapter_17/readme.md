## chapter 17 使用期物处理并发

**主要内容**

- [x] 主要讨论Python3.2引入的concurrent.futures模块

#### 1、什么是期物？

期物是一种对象，表示异步执行的操作。

#### 2、期物在哪里？

* 期物是`concurrent.futures`模块和`asyncio`模块包含的重要组件，可是，作为这两个库的用户，我们有时却见不到期物。
* 通常情况下自己不应该创建期物，而只能由并发框架实例化。原因很简单：期物表示终将发生的事情，而确定某件事会发生的唯一方法是执行的时间已经排定。## chapter 17 使用期物处理并发

**主要内容**

- [x] 主要讨论Python3.2引入的concurrent.futures模块

#### 1、什么是期物？

期物是一种对象，表示异步执行的操作。

#### 2、期物在哪里？

* 期物是`concurrent.futures`模块和`asyncio`模块包含的重要组件，可是，作为这两个库的用户，我们有时却见不到期物。
* 期物封装待完成的操作，可以放入队列，完成的状态可以查询，得到的结果（或抛出异常）后可以获取结果（或异常）。
* 通常情况下自己不应该创建期物，而只能由并发框架实例化。原因很简单：期物表示终将发生的事情，而确定某件事会发生的唯一方法是执行的时间已经排定。

#### 3、`concurrent.futures`模块

* `concurrent.futures`模块的主要特色是ThredPoolExecutor和ProcessPoolExecutor类，这两个类实现的接口能分别在不同的线程或进程中执行可调用的对象。
* 这两个类在内部维护着一个工作线程或进程池，以及要执行的任务队列。

#### 4、阻塞型I/O和GIL

（1）GIL

CPython解释器本身就不是线程安全的，因此有全局解释锁(GIL)，一次只允许使用一个线程执行Python字节码。因此通常一个Python进程通常不能使用多个CPU核心。

这是Cpython解释器的局限，与Python语言本身无关。Jython和IronPython没有这种限制。

（2）为什么说Python对I/O密集型任务有作用？

* 因为标准库中所有执行阻塞型I/O操作的函数，在等待操作系统返回结果时都会释放GIL。
* 这意味着Python语言在这个层次上可以使用多线程，而I/O密集型Python程序能从中受益：一个Python线程等待网络响应时，阻塞型I/O会释放GIL，再运行一个线程。

(3)如何轻松绕开GIL?

在CPU密集型作业中使用`concurrent.futures.ProcessPoolExecutor`可以轻松避开GIL,详情如下。

#### 5、concurrent.futures启动线程和进程

* `concurrent.futures`模块实现的时真正的并行计算，因为它使用`ProcessPoolExecutor`类把工作分配给多个Python进程处理。
* 使用这个模块可以轻松绕开GIL，利用所有可用的CPU核心，进程池默认使用`os.cpu_count`作为默认的进程数。
* 由于机器不同，cpu核心有所不同，所以不能保证多进程一定比多线程快。
* 多进程适用于CPU密集型任务。