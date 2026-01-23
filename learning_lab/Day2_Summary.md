# 学习日志：2026-01-20 (星期二)

## 本日核心收获
今天学习了Python基础语法，主要内容包括：
- 基础数据类型：数值类型、字符串操作
- 数据结构：列表、元组、字典、集合

## 学习内容总结
### 1. 基础数据类型
Python的六个标准数据类型中：  
- 不可变数据类型：Number（数字）、String（字符串）、Tuple（元组）、Bool（布尔类型）  
- 可变数据类型：List（列表）、Dictionary（字典）、Set（集合）    

不可变指的是对象创建后，其内部状态（值）无法被修改。   
变量是引用，不是盒子：Python变量更像是便利贴（标签），贴在对象上。   
赋值是改变引用，不是改变对象。  
运算返回新对象：数字运算总是创建新的数字对象。
```python
# 看似"修改"的操作，实际上是创建新对象
x = 10
x += 1  # 这等价于 x = x + 1

# 实际上发生的事情：
# 1. 计算 x + 1 得到新值 11
# 2. 创建新的整数对象 11
# 3. 让 x 指向这个新对象
# 4. 原对象 10 不变（如果没有其他引用，会被垃圾回收）
```

Python的常见的数据类型：
- Number（数字） （不可变）
    - 数值类型：int, float, complex, bool  
    **例如**：
        ```python
        a = 10
        b = 3.14
        c = 1 + 2j
        d = True
        # 输出类型
        print(type(a), type(b), type(c), type(d))
        ```
    - 数值运算：`+ - * / // % **`
        ```python
        >>> 5 + 4   # 加法
        9
        >>> 10 - 3  # 减法
        7
        >>> 2 * 3   # 乘法
        6
        >>> 10 / 2  # 除法，得到一个浮点数
        5.0
        >>> 10 // 3 # 整除，得到一个整数
        3
        >>> 10 % 3  # 取余
        1
        >>> 2 ** 3  # 乘方
        8
        ```
    - 数值比较：`== != < > <= >=`
    - 数值逻辑运算：`and or not`
    - 数值位运算：`& | ^ ~ << >>`
    - 数值类型转换：`int(), float(), complex(), bool()`
- String（字符串）  （<span style="font-size: 14px;">不可变</span>）   

    Python 中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

    字符串是不可变的，因此不能修改字符串中的字符。  
    ```python
    str = 'WWenuyyubo'
    str.replace('e','E')
    print(str)
    结果：WWenuyyubo
    ```
    字符串的索引值以 0 为开始值，-1 为从末尾的开始位置。  
    [![字符串索引示意图](https://s41.ax1x.com/2026/01/23/pZg8G7D.png)](https://imgchr.com/i/pZg8G7D)  
    加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数。
    - 字符串创建：`str = "Hello, world!"`
    - 字符串索引：`str[0]`代表 `str` 的第一个字符，  
    `str[-1]`代表 `str` 的最后一个字符。
    - 字符串切片：  
        ```python
        str[头下标:尾下标]
        str[0:5]    #代表'str'的前 5 个字符,不包括第 5 个字符
        str[0:-1]   #代表'str'的除最后一个字符外的所有字符 
        str[2:]     #代表'str'的从第 2 个字符开始到结尾的所有字符
        str[::2]代表    #'str' 的所有偶数位置的字符  
        str[1::2]代表   #'str' 的所有奇数位置的字符  
        str[::-1]代表   #'str' 的所有字符倒序排列。
        ```
    - 字符串方法：`lower(), upper(), islower(), isupper(), isdigit(), isalpha(), isalnum(), startswith(), endswith(), find(), replace(), split(), join()`
    - 字符串格式化：`%s, %d, %f, %x, %o, %e, %g`
    - 字符串拼接：`+`
    - 字符串编码：`encode(), decode()`
    - 字符串格式化：`format()`
    - 字符串常用内置函数：`len(), max(), min(), sum(), sorted(), reversed()`   

    实例如下：  
    ```python
    # 字符串创建
    str = "Hello, world!"
    print(str)   # 输出结果：Hello, world!

    # 字符串索引
    print(str[0])   # 输出结果：H
    print(str[-1])  # 输出结果：!

    # 字符串切片
    print(str[0:5])   # 输出索引为0-4的字符，输出结果：Hello, 
    print(str[2:])    # 输出索引为2-7的字符，输出结果：llo, world!
    print(str[0:-1])  # 输出索引为0-7的字符，输出结果：Hello, world
    print(str[::2])   # 第三个参数为步长，输出所有偶数位置的字符，输出结果：Hlo,wrd!
    print(str[1::2])  # 输出所有奇数位置的字符，输出结果：el,o,wrd!
    print(str[::-1])    # 倒序输出结果：!dlrow ,olleH

    # 字符串方法
    print(str.lower())   # 将字符串全部转为小写，输出结果：hello, world!
    print(str.upper())   # 将字符串全部转为大写，输出结果：HELLO, WORLD!
    print(str.islower())  # 询问字符串是否全部为小写，输出结果：True
    print(str.isupper())  # 询问字符串是否全部为大写，输出结果：True
    print(str.isdigit())  # 询问字符串是否全部为数字，输出结果：False
    print(str.isalpha())  # 询问字符串是否全部为字母，输出结果：False
    print(str.isalnum())  # 询问字符串是否全部为字母或数字，输出结果：True
    print(str.startswith("H"))  # 询问字符串是否以 'H' 开头，输出结果：True
    print(str.endswith("!"))   # 询问字符串是否以 '!' 结尾，输出结果：True
    print(str.find("l"))      # 输出 'l' 在字符串中第一次出现的位置，输出结果：2
    print(str.replace("l", "L"))  # 将字符串中的 'l' 替换为 'L'，输出结果：HeLLo, worLd!
    print(str.split(","))  # 以 ',' 分割字符串，输出结果：['Hello', ' world!']
    print(",".join(str))   # 以 ',' 将字符串连接起来，输出结果：Hello, world!

    # 字符串格式化
    print("姓名:%s, 年龄:%d" % ("小明", 20))  # 将字符串和变量格式化输出，输出结果：姓名:小明, 年龄:20

    # 字符串拼接
    print("Hello, " + "world!")  # 将字符串和变量拼接，输出结果：Hello, world!  
    print("Hello, " * 3)  # 将字符串重复 3 次，输出结果：Hello, Hello, Hello,

    # 字符串编码
    print(str.encode("utf-8"))  # 编码字符串为 'utf-8' 格式，输出结果：b'Hello, world!'
    print(str.decode("utf-8"))  # 解码字符串为 'utf-8' 格式，输出结果：Hello, world!

    ```
    Python 使用反斜杠 \ 转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串。
    ```python
    \n  # 换行符    
    print("Hello, \nworld!")  # 输出结果：Hello, 
                                 #          world!
    r"Hello, \nworld!"  # 原始字符串，不发生转义
    print(r"Hello, \nworld!")  # 输出结果：Hello, \nworld!
    ```
    与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如 word[0] = 'm' 会导致错误。
    
- List（列表）  （可变）  
    列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

    列表是写在方括号 [] 之间、用逗号分隔开的元素列表。  

    和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

    列表截取的语法格式如下：  `变量[头下标:尾下标]`  
    
    索引值以 0 为开始值，-1 为从末尾的开始位置。  
    [![列表索引示意图](https://s41.ax1x.com/2026/01/23/pZg8wct.png)](https://imgchr.com/i/pZg8wct)  
    加号 + 是列表连接运算符，星号 * 是重复操作。

    - 列表操作：索引、切片、方法、格式化
    - 列表常用内置函数：`len(), max(), min(), sum(), sorted(), reversed()`
    - 列表方法：`append(), insert(), pop(), remove(), clear(), extend(), index(), count(), sort(), reverse()`
        ```python
        # 列表创建
        list1 = [1, 2, 3, 4, 5]
        list2 = ['a', 'b', 'c']
        list3 = [1, 'a', [1, 2, 3]]
        # 列表索引
        print(list1[0])   # 输出结果：1
        print(list2[-1])  # 输出结果：c
        # 列表切片
        print(list1[0:3])   # 输出索引为0-2的元素，输出结果：[1, 2, 3]
        print(list2[1:])    # 输出索引为1-3的元素，输出结果：['b', 'c']
        print(list3[2][1])  # 输出列表list3的第三个元素的第二个元素，输出结果：2
        print(list1[::3])   # 第三个参数3为步长，输出结果：[1, 4]
        # 列表删除
        del list1[1]
        # 列表修改
        list1[0] = 100
        list2[1] = 'B'
        list3[2][1] = 4
        # 列表方法
        list1.append(6)   # 在列表末尾添加元素6
        list1.insert(1, 0)   # 在列表索引1的位置插入元素0
        list1.pop()   # 删除列表末尾元素
        list1.remove(2)   # 删除列表中值为2的元素
        list1.clear()   # 清空列表
        list1.extend(list2)   # 将list2中的元素添加到list1中
        print(list1.index(3))   # 输出列表中值为3的元素的索引，输出结果：2
        print(list1.count(2))   # 输出列表中值为2的元素的个数，输出结果：1
        list1.sort()   # 排序
        list1.reverse()   # 反转
        # 列表格式化
        print("列表1：", list1)
        print("列表2：", list2)
        print("列表3：", list3)
        print("列表1：{0[0]} {0[1]} {0[2]} {0[3]} {0[4]}".format(list1))
        print("列表2：{0[0]} {0[1]} {0[2]}".format(list2))
        print("列表3：{0[2][1]}".format(list3))
        ```
    - 列表推导式：`[表达式 for 变量 in 可迭代对象 if 条件]`
        ```python
        # 列表推导式
        list4 = [x**2 for x in range(10) if x%2==0]
        print(list4)   # 输出结果：[0, 4, 16, 36, 64]
        ``` 
    注意：  
    <span style="margin-left: 20px;">如果list1里面使用了list2，则list2也会随着list1的修改而修改。但是在给list1整体直接赋值的时候，list2并不会被修改。</span>
    ```python
    list1.append(222)
    print(list1)
    print(list2)

    list1[0]=66
    print(list1)
    print(list2)

    list1=[2,4,6]
    print(list1)
    print(list2)
    #结果：
    [222]
    [2, 'a', [222]]

    [66]
    [2, 'a', [66]]

    [2, 4, 6]
    [2, 'a', [66]]
    ```
- Tuple（元组）  （不可变）  
    元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。  
    元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。  
    其实，可以把字符串看作一种特殊的元组。  
    虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。   
    ```python
    list1 = [1,2,3,3,'1a1',45445]
    tup1 = (1,2,3.14,'aaa',list1)   # 包含可变的列表
    print(tup1)
    list1.clear()
    print(tup1)
    结果输出：
    (1, 2, 3.14, 'aaa', [1, 2, 3, 3, '1a1', 45445])
    (1, 2, 3.14, 'aaa', [])
    ```
    ```python
    >>> tup[0] = 11  # 修改元组元素的操作是非法的
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    ``` 
    构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：  
    ```python
    tup1 = ()    # 空元组
    tup2 = (20,) # 一个元素，需要在元素后添加逗号
    tup3 = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
    ```
    如果你想创建只有一个元素的元组，需要注意在元素后面添加一个逗号，以区分它是一个元组而不是一个普通的值，这是因为在没有逗号的情况下，Python会将括号解释为数学运算中的括号，而不是元组的表示。  
    如果不添加逗号，它将被解释为一个普通的值而不是元组。  
    ```python
    tup1 = (1,)
    tup2 = (1)
    print(type(tup1))
    print(type(tup2))
    结果输出：
    <class 'tuple'>
    <class 'int'>
    ```

- Set（集合）  （可变）
    Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。  
    集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。  
    在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。  
    另外，也可以使用 set() 函数创建集合。  
    注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。  
    创建格式：  
    ```python
    parame = {value01,value02,...}
    或者
    parame = set(value)
    ```
    - 集合操作：创建、添加、删除、遍历、交集、并集、差集、对称差、子集、超集、真子集、幂集
    - 集合常用内置函数：`len(), max(), min(), sum(), sorted(), reversed()`
    - 集合方法：`add(), remove(), clear(), update(), union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset(), isdisjoint()`
    ```python
    # 集合创建
    set1 = {1, 2, 3, 3, '1a1', 45445}
    set2 = set('hello')
    set3 = set([1, 2, 3, 3, '1a1', 45445])
    # 集合操作    
    set1.add(4)   # 添加元素
    set1.remove(3)   # 删除元素
    set1.clear()   # 清空集合
    set1.update(set2)   # 更新集合意思是将set2中的元素添加到set1中
    set3 = set1.union(set2)   # 并集
    set3 = set1.intersection(set2)   # 交集 
    set3 = set1.difference(set2)   # 差集
    set3 = set1.symmetric_difference(set2)   # 对称差意思是将set1和set2中不同的元素合并
    set1.issubset(set2)   # 是否为子集
    set1.issuperset(set2)   # 是否为超集
    set1.isdisjoint(set2)   # 是否为不交集
    # 集合运算
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(a - b)     # a 和 b 的差集
    print(a | b)     # a 和 b 的并集
    print(a & b)     # a 和 b 的交集
    print(a ^ b)     # a 和 b 中不同时存在的元素相当于对称差
    print(a <= b)    # a 是否为 b 的子集
    print(a >= b)    # a 是否为 b 的超集
    print(a < b)     # a 是否为 b 的真子集
    print(a > b)     # a 是否为 b 的真超集
    # 集合遍历
    for elem in set1:
        print(elem)
    # 集合格式化
    print("集合1：", set1)
    print("集合2：", set2)
    print("集合3：", set3)
    ```
    - 集合推导式：`{表达式 for 变量 in 可迭代对象 if 条件}`
        ```python
        # 集合推导式
        set4 = {x**2 for x in range(10) if x%2==0}
        print(set4)   # 输出结果：{0, 4, 16, 36, 64}
        ``` 

- Dictionary（字典）  （可变）  
    字典（dictionary）是Python中另一个非常有用的内置数据类型。   
    列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。  
    字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。  
    键(key)必须使用不可变类型。  
    在同一个字典中，键(key)必须是唯一的。  
    ```python
    # 字典创建
    dict1 = {'name': 'Alice', 'age': 20, 'city': 'Beijing'}
    dict2 = dict(name='Bob', age=25, city='Shanghai')
    dict3 = dict([('name', 'Charlie'), ('age', 30), ('city', 'Guangzhou')])
    dict = {}
    dict['one'] = "1 - 菜鸟教程"
    dict[2]     = "2 - 菜鸟工具"
    # 字典索引
    print(dict1['name'])   # 输出结果：Alice
    print(dict2['age'])    # 输出结果：25
    # 字典修改
    dict1['name'] = 'Alicia'
    dict2['age'] = 30
    # 字典方法
    print(dict1.keys())   # 输出字典所有键
    print(dict1.values())   # 输出字典所有值
    print(dict1.items())   # 输出字典所有键值对
    print(dict1.get('name'))   # 输出键为 'name' 的值
    dict1.pop('age')   # 删除键为 'age' 的值
    dict1.popitem()   # 删除最后一对键值对
    dict1.clear()   # 清空字典
    # 字典遍历
    for key, value in dict1.items():
        print(key, value)
    # 字典格式化
    print("字典1：", dict1)
    print("字典2：", dict2)
    print("字典3：", dict3)
    # 字典推导式
    dict4 = {x: x**2 for x in range(10) if x%2==0}
    print(dict4)   # 输出结果：{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
    ```
    注意：  
    1、字典是一种映射类型，它的元素是键值对。  
    2、字典的关键字必须为不可变类型，且不能重复。  
    3、创建空字典使用 { }。  
- bytes
    在 Python3 中，bytes 类型表示的是不可变的二进制序列（byte sequence）。  
    与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。  
    bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用 bytes 类型来传输二进制数据。  
    创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：  
    此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：  
    ```python
    x = bytes("hello", encoding="utf-8")
    ```
    与字符串类型类似，bytes 类型也支持许多操作和方法，如切片、拼接、查找、替换等等。同时，由于 bytes 类型是不可变的，因此在进行修改操作时需要创建一个新的 bytes 对象。例如：  
    ```python
    x = b"hello"
    y = x[1:3]  # 切片操作，得到 b"el"
    z = x + b"world"  # 拼接操作，得到 b"helloworld"
    print(y)     # 输出 b"el"
    print(z)     # 输出 b"helloworld"
    ```
    需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值。例如：  
    ```python
    x = b"hello"
    if x[0] == ord("h"):
    print("The first element is 'h'")
    ```
    其中 ord() 函数用于将字符转换为相应的整数值。  
    另外，bytes 类型支持与整数值进行运算，但结果仍然是 bytes 类型。例如：  
    ```python
    x = b"hello"
    y = x * 2  # 重复拼接
    print(y)     # 输出 b"hellohello"
    ```
- 类型转换和数学运算  
    有时候，我们需要对数据内置的类型进行转换，数据类型的转换，一般情况下你只需要将数据类型作为函数名即可。  
    以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。  
    [![类型转换](https://s41.ax1x.com/2026/01/23/pZg8d1I.png)](https://imgchr.com/i/pZg8d1I)
- 注释  
    Python 中有多种注释方式，包括单行注释、多行注释。
    - 单行注释：以 # 开头，表示注释内容到行尾。
    - 多行注释：以 ''' 或 """ 开始，以对应的结束符号 ''' 或 """ 结束，表示注释内容到结束符号为止。
    ```python
    # 单行注释
    print("Hello, world!")  # 输出结果：Hello, world!

    '''
    多行注释
    这是一个多行注释，
    多行注释可以由 ''' 或 """ 开始，
    并由对应的结束符号 ''' 或 """ 结束。
    '''
    ```

### 2. 数据结构
- **列表(List)**：可变序列，支持增删改查
- **元组(Tuple)**：不可变序列，适合存储常量
- **字典(Dictionary)**：键值对映射，快速查找
- **集合(Set)**：无序不重复，支持集合运算

### 3. 常用函数
- 数学函数：
    [![数学函数](https://s41.ax1x.com/2026/01/23/pZg8a9A.png)](https://imgchr.com/i/pZg8a9A)  
- 随机数函数:  
    [![随机数函数](https://s41.ax1x.com/2026/01/23/pZg8ttH.png)](https://imgchr.com/i/pZg8ttH)
    ```python
    import random
    # 随机整数
    print(random.randint(1, 10))   # 输出结果：随机整数
    # 随机实数
    print(random.random())   # 输出结果：随机实数
    # 随机序列
    print(random.sample(range(10), 5))   # 输出结果：随机序列
    ```
    重点：randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
    ```python
    import random
    random.randrange ([start,] stop [,step])
    ```
    start -- 指定范围内的开始值，包含在范围内。  
    stop -- 指定范围内的结束值，不包含在范围内。  
    step -- 指定递增基数。  
    示例：
    ```python
    #!/usr/bin/python3
    import random
 
    # 从 1-100 中选取一个奇数
    print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
 
    # 从 0-99 选取一个随机数
    print ("randrange(100) : ", random.randrange(100))

    #输出结果：
    randrange(1,100, 2) :  97
    randrange(100) :  42
    ```
- 三角函数：  
    [![三角函数](https://s41.ax1x.com/2026/01/23/pZg8Nhd.png)](https://imgchr.com/i/pZg8Nhd)
- 数学常量 
    [![数学常量](https://s41.ax1x.com/2026/01/23/pZg8YAe.png)](https://imgchr.com/i/pZg8YAe)
### 3. 控制流
- 条件判断：if-elif-else，嵌套条件
    Python中if语句的一般形式如下所示：  
    ```python
    if condition_1:
        statement_block_1
    elif condition_2:
        statement_block_2
    else:
        statement_block_3
    ```
    注意：   
    1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。  
    2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。

- 循环：for循环（遍历序列），while循环（条件循环）  
    - Python 中 while 语句的一般形式：
        ```python
        while 判断条件(condition)：
            执行语句(statements)……
        ```
    - while 循环使用 else 语句
        如果 while 后面的条件语句为 false 时，则执行 else 的语句块。  
        语法格式如下：
        ```python
        while condition:
            # 循环体语句
        else:
            # 循环结束后的语句
        ```
    - for 语句  
        Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。  
        for循环的一般格式如下：
        ```python
        for variable in iterable:
            # 循环体语句
        else:
            <statements>
        ```
        其中，variable 是一个变量，用于迭代遍历的元素，iterable 是可迭代对象，如列表、字符串、元组等。  
    - range() 函数
        range() 函数用于生成一个整数序列，该序列包含指定的范围内的整数。  
        range() 函数的一般形式如下：
        ```python
        range(start, stop, step)
        ```
        start -- 序列的起始值，默认为 0。  
        stop -- 序列的终止值，该值不包含在序列中。  
        step -- 序列的步长，默认为 1。  
        示例：
        ```python
        for i in range(5):
            print(i)
        # 输出结果：0 1 2 3 4
        ```
- 循环控制：break, continue, else子句

### 4. 函数
- 函数定义与调用
- 参数：位置参数、默认参数、可变参数、关键字参数
- 返回值：单个或多个返回值
- lambda表达式：匿名函数
- 递归函数：函数调用自身

## 编写的主要代码
1. `python_foundation.ipynb`：语法学习笔记
2. `student_manager.py`：综合项目-学生成绩管理系统
3. 各种练习代码

## 关键知识点
- 列表推导式：`[x**2 for x in range(10) if x%2==0]`
- 字符串f-string格式化：`f"姓名:{name}, 年龄:{age}"`
- 字典遍历：`for key, value in dict.items():`
- 函数默认参数：`def func(name, age=20):`

## 明日计划
学习NumPy库，进行数值计算和数组操作，为计算机视觉打基础。