# Financial Intelligence Agent - Mac 本地安装指南

完整的安装步骤,适用于 macOS (Intel / Apple Silicon)

---

## 📋 前提条件

- ✅ macOS 10.15+ (Catalina 或更新)
- ✅ Python 3.8+ (系统自带或自行安装)
- ✅ 互联网连接

---

## 🚀 快速安装 (推荐)

### 方法 1: 从服务器下载

如果你的服务器 (ubuntu@ip-10-0-1-120) 上已经有 skill:

```bash
# 在你的 Mac 上执行

# 1. 下载整个 skill 目录
scp -r ubuntu@ip-10-0-1-120:/home/ubuntu/.openclaw/workspace/skills/financial-intelligence ~/financial-intelligence

# 2. 进入目录
cd ~/financial-intelligence

# 3. 运行安装脚本
bash install.sh
```

---

### 方法 2: 手动下载单个文件

如果你只想要某些模块:

```bash
# 创建目录
mkdir -p ~/financial-intelligence/modules/{news,research}

# 下载核心文件
scp ubuntu@ip-10-0-1-120:/home/ubuntu/.openclaw/workspace/skills/financial-intelligence/modules/news/fetch_financial_express.py \
  ~/financial-intelligence/modules/news/

scp ubuntu@ip-10-0-1-120:/home/ubuntu/.openclaw/workspace/skills/financial-intelligence/modules/research/stock_analyzer.py \
  ~/financial-intelligence/modules/research/

scp ubuntu@ip-10-0-1-120:/home/ubuntu/.openclaw/workspace/skills/financial-intelligence/config.example.json \
  ~/financial-intelligence/

# 复制配置
cd ~/financial-intelligence
cp config.example.json config.json
```

---

## 🔧 手动安装 (完整步骤)

### 步骤 1: 检查 Python

```bash
# 检查 Python 版本
python3 --version

# 应该显示 Python 3.8 或更高
# 如果没有,安装 Python:
# brew install python@3.11
```

---

### 步骤 2: 创建目录

```bash
# 创建 skill 目录
mkdir -p ~/financial-intelligence
cd ~/financial-intelligence

# 创建子目录
mkdir -p modules/news
mkdir -p modules/research
mkdir -p modules/data
mkdir -p utils
mkdir -p scripts
mkdir -p docs
mkdir -p logs
```

---

### 步骤 3: 下载文件

#### 选项 A: 从服务器完整下载

```bash
# 在 Mac 上执行
cd ~
scp -r ubuntu@ip-10-0-1-120:/home/ubuntu/.openclaw/workspace/skills/financial-intelligence ./
cd financial-intelligence
```

#### 选项 B: 手动创建核心文件

如果服务器无法访问,我会给你提供所有文件内容,你可以手动创建。

---

### 步骤 4: 安装依赖

```bash
cd ~/financial-intelligence

# 安装必需依赖
pip3 install akshare pandas requests beautifulsoup4 lxml

# 可选: 安装额外依赖
pip3 install tushare yfinance matplotlib
```

**注意**: Mac 上不需要 `--break-system-packages`,直接安装即可。

---

### 步骤 5: 配置

```bash
# 复制配置模板
cp config.example.json config.json

# (可选) 编辑配置
nano config.json  # 或用其他编辑器
```

**最小配置** (无需修改,开箱即用):
```json
{
  "data_sources": {
    "primary": "akshare"
  }
}
```

**进阶配置** (可选):
```json
{
  "llm": {
    "provider": "openrouter",
    "api_key": "sk-your-api-key"
  },
  "data_sources": {
    "primary": "akshare",
    "tushare": {
      "enabled": true,
      "token": "your-tushare-token"
    }
  }
}
```

---

### 步骤 6: 测试

```bash
# 测试新闻模块
python3 modules/news/fetch_financial_express.py 10

# 测试股票分析 (如果网络OK)
python3 modules/research/stock_analyzer.py 688110

# 运行完整测试
python3 test.py
```

---

## 📁 目录结构

安装完成后,你的目录应该是这样:

```
~/financial-intelligence/
├── config.json                     # 你的配置
├── install.sh                      # 安装脚本
├── test.py                         # 测试脚本
├── SKILL.md                        # 完整文档
├── README.md                       # 快速开始
│
└── modules/
    ├── news/
    │   ├── fetch_financial_express.py  # 财经慢报
    │   ├── sources_config.json         # 新闻源配置
    │   └── manage_sources.py           # 新闻源管理
    │
    └── research/
        ├── stock_analyzer.py           # 股票分析
        └── stock_with_dragon_tiger.py  # 龙虎榜
```

---

## 🎯 快速使用

### 1. 抓取新闻

```bash
cd ~/financial-intelligence

# 抓取财经慢报
python3 modules/news/fetch_financial_express.py 15
```

---

### 2. 分析股票

```bash
# 分析东芯股份
python3 modules/research/stock_analyzer.py 688110

# 查看龙虎榜
python3 modules/research/stock_with_dragon_tiger.py 688110
```

---

### 3. 管理新闻源

```bash
cd modules/news

# 查看所有可用新闻源
python3 manage_sources.py list --all

# 启用新闻源
python3 manage_sources.py enable eastmoney
python3 manage_sources.py enable reuters

# 运行配置向导
python3 manage_sources.py setup
```

---

## ⚙️ 高级配置

### 配置代理 (如果需要)

编辑 `config.json`:

```json
{
  "proxy": {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890"
  }
}
```

---

### 配置 LLM (可选)

如果想要 AI 摘要功能:

```json
{
  "llm": {
    "provider": "openrouter",
    "api_key": "sk-or-v1-xxx",
    "model": "anthropic/claude-sonnet-4"
  }
}
```

支持的提供商:
- OpenRouter (推荐)
- SiliconFlow (国内)
- Google Gemini
- OpenAI
- DashScope (阿里云)

---

### 配置 Tushare Pro (可选)

如果需要更详细的 A股数据:

1. 注册: https://tushare.pro
2. 获取 token
3. 编辑 `config.json`:

```json
{
  "data_sources": {
    "tushare": {
      "enabled": true,
      "token": "your-token-here"
    }
  }
}
```

---

## 🔧 常见问题

### Q1: pip3 安装失败

**问题**: `pip3: command not found`

**解决**:
```bash
# 安装 pip
python3 -m ensurepip --upgrade

# 或者用 Homebrew 安装 Python
brew install python@3.11
```

---

### Q2: AKShare 安装失败

**问题**: 网络错误或依赖冲突

**解决**:
```bash
# 使用国内镜像
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple akshare

# 或者阿里云镜像
pip3 install -i https://mirrors.aliyun.com/pypi/simple/ akshare
```

---

### Q3: 网络连接失败

**问题**: `Connection aborted` 或 `RemoteDisconnected`

**原因**: 
- 防火墙拦截
- 需要代理访问某些网站

**解决**:
```bash
# 1. 配置代理 (如果你用 ClashX/Surge)
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890

# 2. 或在 config.json 中配置代理
# 3. 或使用 VPN
```

---

### Q4: 数据不准确

**问题**: 股价显示不对

**原因**: 使用了模拟数据

**解决**: 
- 确保网络正常
- 确保 AKShare 已正确安装
- 运行 `python3 test.py` 检查

---

### Q5: Mac 权限问题

**问题**: `Permission denied`

**解决**:
```bash
# 给脚本添加执行权限
chmod +x install.sh
chmod +x modules/news/*.py
chmod +x modules/research/*.py
```

---

## 📖 文档

### 完整文档

```bash
# 查看完整使用指南
cat SKILL.md

# 查看快速开始
cat README.md

# 查看新闻源管理
cat modules/news/NEWS_SOURCES.md
```

---

## 🚀 下一步

### 基础使用

1. ✅ 测试新闻抓取
2. ✅ 测试股票分析
3. ✅ 查看文档

### 进阶配置

1. 配置新闻源 (启用更多源)
2. 配置 LLM (AI 摘要)
3. 配置 Tushare (更详细数据)

### 自动化

1. 使用 cron 定时抓取
2. 配置飞书推送
3. 创建观察列表

---

## 💡 推荐工作流

### 每天早上

```bash
cd ~/financial-intelligence

# 1. 看新闻
python3 modules/news/fetch_financial_express.py 20

# 2. 分析关注的股票
python3 modules/research/stock_analyzer.py 688110
python3 modules/research/stock_analyzer.py 600519
```

### 定时任务 (可选)

使用 macOS cron:

```bash
# 编辑 crontab
crontab -e

# 添加定时任务 (每天早上 9 点)
0 9 * * * cd ~/financial-intelligence && python3 modules/news/fetch_financial_express.py 20 > ~/news.txt
```

---

## 🆘 需要帮助?

### 方法 1: 查看文档

```bash
cat SKILL.md  # 完整文档
cat README.md  # 快速指南
```

### 方法 2: 运行测试

```bash
python3 test.py
```

会显示哪个模块有问题。

### 方法 3: 联系我

在飞书群 @ 我:
```
@小丽 Mac 安装 Financial Intelligence Agent 遇到问题
```

---

## ✅ 验证安装

运行以下命令验证安装成功:

```bash
cd ~/financial-intelligence

# 1. 检查目录结构
ls -la

# 2. 检查依赖
python3 -c "import akshare; print('AKShare:', akshare.__version__)"
python3 -c "import pandas; print('Pandas:', pandas.__version__)"

# 3. 运行测试
python3 test.py

# 4. 测试新闻
python3 modules/news/fetch_financial_express.py 5

# 如果以上都成功, 安装完成! 🎉
```

---

## 📦 打包好的安装脚本

保存为 `install_mac.sh`:

```bash
#!/bin/bash

echo "🚀 Financial Intelligence Agent - Mac 安装脚本"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 未安装"
    echo "请运行: brew install python@3.11"
    exit 1
fi

echo "✅ Python $(python3 --version)"

# 创建目录
echo "📁 创建目录..."
mkdir -p ~/financial-intelligence
cd ~/financial-intelligence
mkdir -p modules/{news,research,data} utils scripts docs logs

# 从服务器下载
echo "📥 从服务器下载文件..."
scp -r ubuntu@ip-10-0-1-120:/home/ubuntu/.openclaw/workspace/skills/financial-intelligence/* .

# 安装依赖
echo "📦 安装依赖..."
pip3 install akshare pandas requests beautifulsoup4 lxml

# 配置
if [ ! -f config.json ]; then
    cp config.example.json config.json
    echo "✅ 配置文件已创建"
fi

# 测试
echo "🧪 运行测试..."
python3 test.py

echo ""
echo "✅ 安装完成!"
echo ""
echo "快速开始:"
echo "  cd ~/financial-intelligence"
echo "  python3 modules/news/fetch_financial_express.py 10"
```

使用:
```bash
chmod +x install_mac.sh
./install_mac.sh
```

---

**安装完成后,开始使用! 🎉**
