## 字典

1、跟字典有关的内置函数都在__builtins__.__dict__中可以查看。

2、散列表是字典类型性能出众的根本原因。

字典在Python中被广泛使用，它是Python的基石，例如：变量的命名空间、实例的属性和函数的关键字参数都可以看到字典的身影。

3、什么是可散列的数据类型

    * (1)如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个散列对象需要实现__hash__()方法。

    * (2)另外这个可散列对象还要有__qe__()方法，这样才能跟其他键做比较。

    * (3)如果两个散列对象是相等的，那么它们的散列值一定是一样的。如果一个对象是可散列的，散列值就是它们的id()函数的返回值。

4、字典推导(dictcomp)：可以从任何键值对作为元素的可迭代对象构建出字典。

`DIAL_CODES = [(86, 'China'), (91, 'India')]` 形如列表里面以元组形式存在的多个键值对的表达式称之为字典推导。

`num_list = [i for i in range(10)]`  列表推导(listcomp),通过一个迭代器或列表生成一个新的列表的表达式称为列表推导。

5、创建字典的常见方式：

    * (1) a = dict(one=1, two=2, three=3)
    * (2) b = {'one': 1, 'two': 2, 'three': 3}
    * (3) c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))  通过zip生成的即为字典推导与(4)的意思是一样的。
    * (4) d = dict([('two', 2), ('one', 1), ('three', 3)])
    * (5) e = dict({'one': 1, 'two': 2, 'three': 3})
    *     a == b == c == d == e

6、用setdefault处理找不到的键

介绍：当d[k]不能找到正确的键的时候，Python会抛出异常，这个行为符合Python所信奉的"快速失败"的哲学。

例如：为任意一个变量word设置一个默认值[]，只要找不到这个键就会默认设置它的值为[]。

(1)、通过setdefault设置默认键的值为[]

```
index={}
index.setdefault(word, [])
```

(2)、通过collections.defaultdict实现默认值的设置

首先新建一个字典`dd = defaultdict(list)`,对于dd这个字典在任意键找不到的时候会默认返回一个[]作为结果。[参见详情](https://github.com/feng-hui/fluent_python_examples/blob/master/ch03_default_dict.py)

defaultdict(default_factory)设置的默认值只对__getitem__有作用，其他时候不生效。

7、特殊方法`__missing__`

所有的映射处理找不到的键的时候，都会牵扯到`__missing__`方法。

`__missing__`方法只会被`__getitem__`调用。

8、字典的变种

(1)`collections.OrderDict`,这个类型在添加键的时候会保持顺序,因此键的迭代次序总是一致的。

    * `popitem`方法默认删除并返回字典最后一个元素,如果添加参数`last=False`则会删除并返回第一个添加进去的元素。

(2)`collections.ChainMap`[使用方法](https://github.com/feng-hui/fluent_python_examples/blob/master/ch03_chainmap.py),该类型可以容纳数个不同的对象,在进行键查找操作的时候,这些对象会被当成一个整体逐个查找,知道键被找到为止。

(3)`collections.Counter`,这个映射类型会给每个键准备一个计数器,每次更新一个键的时候都会增加这个计数器。这个类型可以用来给散列表计数。

其中`most_common(n)`会按照次序依次返回映射里最常见的n个键和他们的计数,结果为列表推导。例如：

返回的结果为一个字典推导式。

```
ct = collections.Counter('afdafsdfweadfa')
ct.update('adaf')
ct.common(n)
```

9、子类化UserDict

就创造自定义dict类型来说，以UserDict为基类，总比以普通的dict来得方便。

更倾向于从UserDict而不是从dict的主要原因是，后者有时会在某些方法实现上走一些捷径，导致我们不得不在它的子类中重写这些方法，但UserDict就不会带来这些问题。

10、不可变映射类型

从Python3.3开始，types模块引入了一个封装类名叫做MappingProxyType，如果给这个类一个映射,它会返回一个只读的映射视图。

虽然是个只读视图，但是它是动态的。

[需要补使用方法]

11、集合

set和frozenset，set类本身是不可散列的，frozenset是可散列的，set里的元素必须是可散列的。

例如：统计集合needles的元素在集合haystack中出现的次数。

[后续补使用方法]

12、如何构建集合

除空集外，集合的字面量--{1}、{1, 2}等等跟它的数学形式一模一样。如果是空集，必须写成set()形式，如果写成{}这样表示是一个空字典。

如何构建集合？

{1, 2, 3}这种字面量句法相比于构造方法set([1, 2, 3])更快且更容易读，后者的速度要慢一些。

可以通过dis.dis(反汇编函数)来看看两个方法的字节码有什么不同？使用方法为dis.dis({1, 2, 3})。

13、集合推导（setcomps）

例如：`{chr(i) for i in range(32, 256)}`






