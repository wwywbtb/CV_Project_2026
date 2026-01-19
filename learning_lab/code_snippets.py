#代码片段库 - 常用、易忘的代码块集合
"""
代码片段库 - 常用、易忘的代码块集合
供未来项目快速复制粘贴，避免重复查资料。
"""

# ==================== Git 核心工作流 ====================
GIT_BASIC_WORKFLOW = '''
# Git 基础工作流
git add .                          # 添加所有更改（注意 add 和 . 之间有空格！）
git commit -m "描述性信息"         # 提交到本地仓库
git push origin main              # 推送到远程GitHub仓库
git status                        # 检查状态（最常用）
'''

GIT_INIT_AND_CONNECT = '''
# 将本地已有项目连接到新的GitHub仓库
git init
git add .
git commit -m "初始提交"
git branch -M main
git remote add origin https://github.com/你的用户名/仓库名.git
git push -u origin main
'''

# ==================== Conda 环境管理 ====================
CONDA_ENV_MANAGE = '''
# 1. 创建新环境（Day1 完成的 cv_2026）
conda create -n 环境名 python=3.9 -y

# 2. 激活/切换环境
conda activate 环境名

# 3. 安装包
conda install 包名
# 或
pip install 包名

# 4. 查看已安装包
conda list
'''

# ==================== Jupyter Notebook ====================
JUPYTER_BASIC = '''
# 在特定目录启动 Jupyter Notebook（今天刚做的）
cd 你的项目路径/notebooks
jupyter notebook

# 浏览器打开后：
# 1. 点击右上角 "New" -> 选择 Python 内核
# 2. 重命名笔记本文件
# 3. 在单元格中写代码，按 Shift+Enter 运行
# 4. 自动保存，或手动点击保存图标
'''

# 使用示例
if __name__ == "__main__":
    print("=== 代码片段库使用说明 ===")
    print("1. 这是一个Python文件，但内容主要是字符串常量。")
    print("2. 当你在新项目中需要某个功能时，来这里复制对应的代码块。")
    print("3. 例如：需要初始化Git，就复制 GIT_INIT_AND_CONNECT 的内容。")
    print("4. 随着学习深入，不断往这里添加你自己的高频代码块。")