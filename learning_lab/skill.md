1.  **Anaconda 虚拟环境**：
    - **是什么**：一个独立的 Python 项目沙箱。
    - **为什么重要**：为计算机视觉项目创建纯净、可复现的依赖环境，是专业开发的起点。
    - **代码示例**：
        ```bash
        # 这是我今天创建的环境
        conda create -n cv_2026 python=3.9 -y   # 创建名为 `cv_2026` 的独立环境
        conda activate cv_2026  # 激活新环境
        ```

2.  **Git & GitHub 工作流**：
    - **是什么**：代码的“时间机器”和“云端备份”。
    - **为什么重要**：管理代码所有修改历史，实现团队协作和跨设备同步。今天我把本地项目推送到 GitHub 了。
    - **将本地项目上传到Git完整流程**:
        ```bash
        #在当前目录下创建一个新的空的库
        git init
        #添加文件到暂存区
        git add .
        #提交
        git commit -m "描述"
        # 将默认分支重命名为 main
        git branch -M main
        #添加远程仓库连接
        git remote add origin https://github.com/你的用户名/仓库名.git
        #如果在Git中建好了，就克隆仓库到本地，使用下面一个命令
        git clone https://github.com/你的用户名/仓库名.git
        #推送代码
        git push -u origin main
        ```
    - **后续Git操作流程**：
        ```bash
        # 这是我今天成功执行的流程
        #修改代码
        git add .  #添加文件到暂存区
        git commit -m "描述"   #提交更改
        git push origin main  #推送到远程
        ```
    - **其他Git操作命令**:
        ```bash
        git status  #查看仓库当前的状态，显示有变更的文件
        git diff [<文件名>]     #查看尚未暂存的更改。如果已经 git add 了，就看不到了
        git log --oneline   #--oneline 参数让输出简洁，是查看历史最常用的方式。

3. **Windows的一些cmd命令**:
    - **📁 文件与目录管理**
        ```bash
        #切换工作目录
        cd 目录    #切换相应目录
        cd..    #返回上一级目录
        cd\     #直接回到系统根目录
        cd /d D:\路径   #跨盘符切换
        #列出目录下的所有文件和文件夹
        dir     #列出当前目录下的所有文件和文件夹
        dir /a  #显示包括隐藏文件在内的所有文件
        #创建新目录
        mkdir 新目录名    #必须分步创建：先mkdir parent，再cd parent，再mkdir child
        #创建文件
        echo 内容 > 文件名      # 创建/覆盖文件，> 是“重定向”，会覆盖原文件
        echo 内容 >> 文件名     # 追加内容，>> 是“追加”，内容加到文件末尾
        #查看文本文件内容
        type "文件名"   #快速查看文本文件内容
        #删除文件
        del "文件名"    #删除文件
        del *.tmp   #可删除所有 .tmp 结尾的临时文件
    - **🐍 程序运行与环境**:
        ```bash
        python 脚本名.py     #最基础的运行方式
        conda activate 环境名   #激活环境,今天成功激活了 cv_2026
        jupyter notebook    #先 cd 到目标目录再启动。今天在 learning_lab/notebooks 目录下启动
4. **Python基础语法**:
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
        ![字符串索引示意图](./images/string_index.png)
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
        ![列表索引示意图](./images/list_index.png)
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
    - Set（集合）  （可变）
    - Dictionary（字典）  （可变）
    
    - 字符串操作：索引、切片、方法、格式化
    - 类型转换和数学运算
    