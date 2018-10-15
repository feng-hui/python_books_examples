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

    * (1) `a = dict(one=1, two=2, three=3)`
    * (2) `b = {'one': 1, 'two': 2, 'three': 3}`
    * (3) `c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))`  通过zip生成的即为字典推导与(4)的意思是一样的。
    * (4) `d = dict([('two', 2), ('one', 1), ('three', 3)])`
    * (5) `e = dict({'one': 1, 'two': 2, 'three': 3})`
    a == b == c == d == e

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