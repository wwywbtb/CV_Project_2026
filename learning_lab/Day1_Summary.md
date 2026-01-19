# 学习日志：2026-01-19 (星期一)

## 🧠 本日核心收获
> 成功从零搭建了专业的 Python 数据科学开发环境，并掌握了代码版本管理的基本功。

## 📖 学了什么？
### 新概念/技能
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
### 解决的问题
（请从上面的 `problem_log.md` 中挑选1-2个印象最深的填写进来）
- **问题描述**：`git add.` 报错 `'add.' is not a git command`
- **解决步骤**：命令应为 `git add .`，`add` 和点之间必须有空格。
- **根本原因**：命令格式记忆/输入错误。
- **如何避免**：记住空格是命令的一部分。`git add .` 是一个固定短语。

## 💻 编写的代码
- `CV_Project_2026/main.py`：测试 OpenCV 安装。
- `CV_Project_2026/image_operations.py`：图像创建与灰度转换。
- `CV_Project_2026/.gitignore`：配置文件忽略规则。
- `learning_lab/notebooks/Day1_Learning_Log.ipynb`：Jupyter 学习日志。

## 📝 关键代码片段
```python
# 在 .gitignore 中，`!` 表示“例外”
output/*          # 忽略 output 文件夹下所有文件
!output/README.md # 但不忽略 output 下的 README.md 文件