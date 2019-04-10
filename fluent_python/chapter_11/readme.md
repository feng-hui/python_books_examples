## chapter 11 接口：从协议到抽象基类

**主要内容**

- [x] 本章讨论的话题是接口：从鸭子类型的代表特征动态协议，到使接口更明确、能验证实现是否符合规定的抽象基类(Abstract Class, ABC)

1、Python文化中的接口和协议

接口：Python语言没有interface关键字，而且除了抽象基类，每个类都有接口：类实现或继承的公开属性(方法或数据属性)，包括特殊方法，如`__getitem__`或`__add__`。

2、猴子补丁

在运行时修改类或者模块，而不改动源码，被称为**猴子补丁**。

3、进一步了解鸭子类型(duck typing)

“鸭子类型”：忽略对象的真正类型，转而关注对象有没有实现所需要的方法、签名和语义。

4、白鹅类型（goose typing）

白鹅类型是指，只要cls是抽象基类，即cls的元类是abc.ABCMeta，就可以使用`isinstance(obj, cls)`。

5、标准库中的抽象基类

* collections.abc模块中的抽象基类

* 抽象基类的数字塔：numbers包定义的是数字塔（即各个抽象基类的层次结构是线性的），其中Number是位于最顶端的超类，随后是Complex子类，依次往下，最底端是Integer类。依次为`Number->Complex->Real->Rational->Integer`。
