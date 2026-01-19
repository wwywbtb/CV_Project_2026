# 问题追踪日志

## 2026-01-19 (Day 1)
### 问题1：`git add.` 报错 `'add.' is not a git command`
- **状态**：✅ 已解决
- **环境**：Windows 命令提示符
- **错误信息**：`git: 'add.' is not a git command. See 'git --help'.`
- **解决方案**：命令应为 `git add .`，`add` 和点之间必须有空格。
- **根本原因**：命令格式记忆/输入错误。
- **如何避免**：记住空格是命令的一部分。`git add .` 是一个固定短语。

### 问题2：`git push` 失败，提示 `Failed to connect to github.com port 443`
- **状态**：✅ 已解决
- **环境**：家庭宽带网络
- **错误信息**：`fatal: unable to access 'https://github.com/...': Failed to connect to github.com port 443 after 21129 ms: Could not connect to server`
- **解决方案**：切换至手机移动热点网络后，重试 `git push` 成功。
- **根本原因**：本地网络服务商或防火墙对 GitHub 的 HTTPS 端口 (443) 访问有限制或不稳定。
- **如何避免**：
    1.  可配置 SSH 密钥替代 HTTPS 远程连接（长期方案）。
    2.  将手机热点作为备用网络。
    3.  如果使用代理，需为 Git 配置代理。

### 问题3：使用 `mkdir -p` 命令报错“命令语法不正确”
- **状态**：✅ 已解决
- **环境**：Windows 命令提示符 (CMD)
- **解决方案**：Windows CMD 不支持 `-p` 参数。改用逐级创建：
    ```cmd
    mkdir learning_lab
    cd learning_lab
    mkdir notebooks
    mkdir data
    ```
- **根本原因**：`-p` 是 Linux/Unix 和 PowerShell 的参数，原生 CMD 不支持。

### 问题4：中断 Jupyter 服务器后，习惯性输入了 `y`
- **状态**：✅ 已解决
- **环境**：Anaconda Prompt
- **现象**：按两次 `Ctrl+C` 成功关闭 Jupyter 服务器后，终端空行提示符下输入了 `y`，导致报错 `'y' 不是内部或外部命令`。
- **解决方案**：无需任何操作。`Ctrl+C` 中断后已不需要确认，直接在提示符下输入下一条命令即可。
- **根本原因**：对命令行交互流程的误解。