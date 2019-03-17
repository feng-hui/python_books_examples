## chapter 19 动态属性和特性

**主要内容**

- [x] 动态属性和特性

#### 1、什么是动态属性和特性？

* 在Python中，数据的属性和处理数据的方法成属性（attribute）。其实，方法只是可调用的属性。
* 除二者之外，我们还可以创建特性（property）。

#### 2、如何使用动态属性访问JSON类数据?

动态属性访问形式如下（feed为一个JSON对象）：

`feed['Schedule']['events'][40]['name'] -> feed.Schedule.events[40].name`

* （1）可以通过访问不存在的属性时，调用`__getattr__`来处理，可以在这个函数里报错找不到该属性，也可以构建`build`函数来获取当前属性的值，详情参见代码：[ch19_explore1.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_19/ch19_explore1.py)；
* （2）通过`__new__`方法直接处理，详情参见：[ch19_explore2.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_19/ch19_explore2.py)

**注意：**可以通过`from keyword import iskeyword`来判断字典中的键是否为Python关键字，然后在处理的时候，可以为关键字加上类似下划线(_)这样的符号，避免访问出错（报错类型为：`SyntaxError`）。

#### 3、使用`shelve`模块调整JSON数据源的结构

01、`shelve`库介绍

`shelve`库位于标准库，直接翻译为架子模块，`shelve`模块提供pickle存储方式，pickle(泡菜)时Python对象序列化格式名字，可以将对象序列化文件的形式。（可以理解为：泡菜放在架子上，所以`shelve`提供pickle存储方式。）

`shelve.open`高阶函数返回一个`shelve.Shelf`实例，这是简单的简直对象数据库，背后有`dbm`模块支持。

特点介绍：

* `shelve.Shelf`是`abc.MutableMapping`子类，因此提供了处理映射类型的重要方法；
* 此外，它还提供了几个管理I/O的方法，如`sync`和`closed`：它也是一个上下文管理器；
* 只要把新值赋予键，就会保存键和值；
* 键必须是字符串；
* 值必须是pickle模块能处理的对象。

具体的代码参见：[ch19_osconfeed.py](https://github.com/feng-hui/fluent_python_examples/blob/master/chapter_19/ch19_osconfeed.py)

#### 4、特性


`property`构造方法如下：

`property(fget=None, fset=None, fdel=None, doc=None)`

一般的用法是通过装饰器`@property`，也可以通过普通的函数来使用。

伪代码如下：

```
class Ps:

    def get_v(self):
        return self.__v

    def set_v(self, v)：
        if v > 20:
            self.__v = v
        else:
            raise ValueError('v must > 0')

    v = property(get_v, set_v, 'check the value of the attribute')
```

4.1、特性会覆盖类属性

* 特性都是类属性，但是特性管理的其实是实例属性的存取。
* 如果实例和所属的类有同名数据属性，那么实例会覆盖（或称为遮盖）类属性。


例如：
```
class ExampleClass:

    data = 'the class data attr'

    @property
    def prop((self):
        return 'the prop value'

>>> obj = ExampleClass()
>>> vars(obj)  # 返回实例的属性
{}  # 表示没有实例属性
>>> obj.data  # 在没有实例的属性的时候，获取的是类的属性ExampleClass.data
'the class data attr'
>>> obj.data = 'bar'
>>> vars(obj)
{'data': 'bar'}
>>> obj.data
'bar'
>>> ExampleClass.data
'the class data attr'
```

* 实例属性不会遮盖类特性。

```
>>> Class.prop  # 获取特性对象本身
>>> obj.prop  # 输出的结果为：'the prop value'
>>> obj.prop = 'foo'  # 直接给特性赋值会报错，报错类型为AttributeError: can't set attribute
>>> obj.__dict__['prop'] = 'foo'  # 给实例属性直接存入一个名称为prop的属性
>>> vars(obj)  # 输出结果为{'data': 'the class data attr', 'prop': 'foo'}
>>> obj.prop  # 输出结果为'the prop value',不会更改特性的值
>>> ExampleClass.prop = 'bar'  # 重新为特性赋值，会销毁特性对象
>>> obj.prop  # 输出结果为'foo',获取之前存入的实例属性值
```

#### 5、处理属性的重要属性和函数

5.1、影响属性处理方式的特殊属性

* `__class__` 对象所属类的引用（即`obj.__class__`与`type(obj)`的作用相同）；
* `__dict__` 一个映射，存储对象或类的可写属性。有`__dict__`属性的对象，任何时候都能随意设置新属性。如果类有`__slots__`属性，它的实例可能没有`__dict__`属性。
* `__slots__` 类可以定义这个属性，限制实例有哪些属性。`__slots__`属性的值是一个字符串组成的元组，指明允许有的属性。如果`__slots__`中没有`__dict__`，那么该类没有`__dict__`属性，实例只允许有指定名称的属性。

5.2、处理属性的内置函数

* `dir([object])`
    * 列出对象的大多数属性。根据官方文档说明，dir函数的目的是交互式使用，因此没有提供完整的属性列表。只列出一组“重要的”属性名。
    * dir函数能审查有没有`__dict__`属性的对象。dir函数不会列出`__dict__`属性本身，但会列出其中的键。
    * dir函数也不会列出的几个特殊属性，例如`__mro__`、`__bases__`、`__name__`。
    * 如果没有指定可选的object参数，dir函数会列出当前作用域中的名称。
* `getattr(object, name[, default])`
    * 从object对象获取那么字符串对应的属性。获取的属性可能来自对象所属的类或超类。
    * 如果没有指定的属性，`getattr`函数会抛出`AttributeError`异常，或者返回default参数的值。
* `hasattr(object, name, value)`
    * 如果object对象中存在指定的属性，或者以某种方式（例如继承）通过object对象获取指定的属性，返回True；
    * 官方文档指出：这个函数的实现方法是通过调用`getattr`函数，看看是否抛出异常。
* `setattr(object, name, value)`
    * 把object对象指定属性的值设为value，前提是object对象能接受那个值。
    * 这个函数可能会创建一个新属性，或者覆盖现有的属性。
*  `vars([object])`
    * 返回object对象的`__dict__`属性，如果实例所属的类定义了`__Slots__`属性，实例没有 `__dict__`属性，那么vars函数不能处理那个实例。
    * 如果没有指定参数，那么vars()函数的作用与locals()函数一样，返回本地作用阈的字典。

5.3、处理属性的特殊方法

* 在用户自己的类中，下列特殊方法用于获取、设置、删除和列出属性;
* 使用点号或内置的getattr、setattr、delattr函数存取属性都会触发下述相应的这些特殊方法。但是直接通过`__dict__`属性读写不会触发这些方法；
* 特殊方法`__getattribute__`和`__setattr__`不管怎么用都会被调用，机会影响每一次属性存取。因此比`__getattr__`方法（只处理不存在的属性名）更难正确使用。
* 与定义这些特殊方法相比，使用特性(property)或描述符相对不容易出错。

假设：类名 Class，它的实例为：obj，obj的属性为attr

* `__delattr__(self, name)` del语句删除属性时调用。
* `__dir__(self)` 把对象传给dir函数时调用，列出属性。
* `__getattr__(self, name)` 仅当获取指定的属性失败，搜索过obj、Class、超类之后调用。
* `__getattribute__(self, name)`
    * 尝试获取指定的属性时调用，寻找的是特殊属性或特殊方法时除外。
    * 点号与getattr和hasattr内置函数会触发这个方法。调用这个方法失败，才会调用`__getattr__`方法；
    * 为了在获取obj实例的属性时不导致无限递归，`__getattribute__`方法的实现要使用超类的该方法`super().__getattribute__`。
* `__setattr__(self, name, value)`
    * 尝试设置指定的属性时调用。
    * 点号或setattr内置函数会触发这个方法。

```
—— 整理人Fenghui
—— 整理时间：2019-03-17 15:37
```