# ClawHub.ai 发布指南

将 Financial Intelligence Agent 发布到 ClawHub.ai 的完整步骤

---

## 📋 发布前准备

### 1. 必需文件检查

确保以下文件存在且完整:

```
financial-intelligence/
├── skill.json              ✅ Skill 元数据
├── SKILL.md               ✅ 完整文档
├── README.md              ✅ 快速开始
├── LICENSE                ❓ 需要添加
├── CHANGELOG.md           ❓ 需要添加
├── .gitignore             ❓ 需要添加
├── icon.png               ❓ 需要添加 (256x256)
└── screenshots/           ❓ 需要添加
    ├── news.png
    ├── analysis.png
    └── dragon-tiger.png
```

---

## ⚙️ 准备工作

### 步骤 1: 添加 LICENSE

创建 `LICENSE` 文件 (MIT License):

```text
MIT License

Copyright (c) 2026 OpenClaw Skills

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### 步骤 2: 添加 CHANGELOG

创建 `CHANGELOG.md`:

```markdown
# Changelog

## [1.0.0] - 2026-03-12

### Added
- 📰 财经新闻聚合 (20+ 新闻源)
- 📊 股票深度研究 (基本面 + 技术面)
- 📈 10项技术指标分析
- 💰 资金流向监控
- 🐉 龙虎榜追踪
- 🎯 智能评分系统
- 🌍 多市场支持 (A股/美股/港股/加密)
- ⚙️ 可配置新闻源管理
- 🤖 可选 LLM 集成
- 📱 飞书推送支持

### Features
- 完全免费 (使用 AKShare)
- 开箱即用 (无需 API Key)
- 用户可自定义配置
- 完整中英文文档
- Mac/Linux 支持
```

---

### 步骤 3: 添加 .gitignore

创建 `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/
dist/
build/

# Config
config.json
*.local.json

# Logs
logs/
*.log

# Data
data/
cache/
*.db
*.sqlite

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Secrets
.env
*.key
*.pem
api_keys.txt
```

---

### 步骤 4: 准备图标

**要求**:
- 尺寸: 256x256 像素
- 格式: PNG (透明背景)
- 命名: `icon.png`

**建议主题**:
- 📊 + 📰 组合图标
- 或者金融图表 + 新闻符号
- 配色: 蓝色/绿色系 (专业感)

---

### 步骤 5: 准备截图

创建 `screenshots/` 目录,添加:

1. **news.png** - 新闻抓取截图
2. **analysis.png** - 股票分析截图
3. **dragon-tiger.png** - 龙虎榜截图

**要求**:
- 尺寸: 1280x720 或更高
- 格式: PNG/JPG
- 清晰度: 高清
- 内容: 实际运行效果

---

### 步骤 6: 完善 skill.json

确保 `skill.json` 包含所有必需字段:

```json
{
  "name": "Financial Intelligence Agent",
  "id": "financial-intelligence",
  "version": "1.0.0",
  "description": "综合金融智能分析助手 - 新闻聚合 + 股票研究 + 技术分析 + 龙虎榜监控",
  "author": {
    "name": "OpenClaw Skills",
    "email": "skills@openclaw.ai",
    "url": "https://github.com/openclaw/skills"
  },
  "license": "MIT",
  "tags": [
    "finance",
    "news",
    "stocks",
    "analysis",
    "trading",
    "chinese",
    "crypto"
  ],
  "categories": [
    "finance",
    "research",
    "automation"
  ],
  "icon": "icon.png",
  "screenshots": [
    "screenshots/news.png",
    "screenshots/analysis.png",
    "screenshots/dragon-tiger.png"
  ],
  "homepage": "https://github.com/openclaw/financial-intelligence",
  "repository": {
    "type": "git",
    "url": "https://github.com/openclaw/financial-intelligence"
  },
  "bugs": {
    "url": "https://github.com/openclaw/financial-intelligence/issues"
  },
  "capabilities": [
    "实时财经新闻聚合 (20+ 源)",
    "股票深度研究 (基本面 + 技术面)",
    "10项技术指标分析",
    "资金流向监控",
    "龙虎榜追踪",
    "智能评分系统",
    "多市场支持 (A股/美股/港股/加密)"
  ],
  "dependencies": {
    "python": ">=3.8",
    "required": {
      "akshare": ">=1.13.0",
      "pandas": ">=2.0.0",
      "requests": ">=2.31.0",
      "beautifulsoup4": ">=4.12.0"
    },
    "optional": {
      "tushare": ">=1.4.0",
      "yfinance": ">=0.2.0"
    }
  },
  "supported_platforms": [
    "linux",
    "macos"
  ],
  "installation": {
    "script": "install.sh",
    "manual": "INSTALL.md"
  },
  "configuration": {
    "required": [],
    "optional": [
      "llm.api_key",
      "tushare.token",
      "delivery.targets"
    ]
  },
  "keywords": [
    "financial",
    "news",
    "stock",
    "analysis",
    "akshare",
    "chinese",
    "龙虎榜",
    "资金流向",
    "技术分析"
  ]
}
```

---

## 🚀 发布到 ClawHub.ai

### 方法 1: 通过 GitHub (推荐)

#### 步骤 1: 创建 GitHub 仓库

```bash
cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence

# 初始化 Git
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial release: Financial Intelligence Agent v1.0.0"

# 创建 GitHub 仓库后,关联并推送
git remote add origin https://github.com/your-username/financial-intelligence.git
git branch -M main
git push -u origin main
```

#### 步骤 2: 在 ClawHub.ai 提交

1. 访问: https://clawhub.ai/submit
2. 填写表单:
   - **Skill Name**: Financial Intelligence Agent
   - **GitHub URL**: https://github.com/your-username/financial-intelligence
   - **Version**: 1.0.0
   - **Category**: Finance & Research
   - **Description**: 综合金融智能分析助手 - 20+ 新闻源聚合、股票深度研究、技术分析、龙虎榜监控
3. 上传截图
4. 提交审核

---

### 方法 2: 直接上传

#### 步骤 1: 打包

```bash
cd /home/ubuntu/.openclaw/workspace/skills

# 创建压缩包
tar -czf financial-intelligence-v1.0.0.tar.gz financial-intelligence/

# 或者 zip
zip -r financial-intelligence-v1.0.0.zip financial-intelligence/
```

#### 步骤 2: 上传到 ClawHub.ai

1. 访问: https://clawhub.ai/submit
2. 选择 "Upload Archive"
3. 上传 `financial-intelligence-v1.0.0.tar.gz`
4. 填写元数据
5. 提交审核

---

## 📝 提交信息模板

### 标题
```
Financial Intelligence Agent - 综合金融智能分析助手
```

### 简短描述 (150字以内)
```
20+ 新闻源聚合、股票深度研究、10项技术指标分析、资金流向监控、龙虎榜追踪。支持 A股/美股/港股/加密货币。完全免费,开箱即用,无需 API Key。用户可自定义配置新闻源和分析参数。
```

### 详细描述
```markdown
## 功能特性

### 📰 财经新闻聚合
- 20+ 新闻源 (财经慢报、CoinDesk、Bloomberg、Reuters 等)
- 自动分类 (8大类别)
- 重要性评分 (1-10分)
- 用户可自定义启用/禁用新闻源

### 📊 股票深度研究
- 基本面分析 (财务健康度、竞争格局、增长前景)
- 10项技术指标 (MA, MACD, KDJ, BOLL, RSI, ATR, OBV 等)
- 资金流向分析 (主力/散户/机构)
- 龙虎榜追踪 (游资/机构席位)
- 智能综合评分 + 操作建议

### 🌍 多市场支持
- A股 (沪深主板、科创板、创业板)
- 美股 (NASDAQ、NYSE)
- 港股 (HKEX)
- 加密货币 (BTC、ETH 等)

### 🎯 核心优势
- ✅ 完全免费 (使用 AKShare 开源数据)
- ✅ 开箱即用 (无需任何 API Key)
- ✅ 用户可配置 (20+ 新闻源自由选择)
- ✅ 可选 LLM 集成 (支持 OpenRouter, SiliconFlow 等)
- ✅ 完整中英文档 (15000+ 字)
- ✅ Mac/Linux 支持

## 快速开始

```bash
# 安装
bash install.sh

# 抓取新闻
python3 modules/news/fetch_financial_express.py 20

# 分析股票
python3 modules/research/stock_analyzer.py 688110
```

## 配置

最小配置 (无需修改):
```json
{
  "data_sources": {
    "primary": "akshare"
  }
}
```

可选配置:
- LLM API Key (AI 摘要)
- Tushare Pro Token (更详细数据)
- 飞书推送配置

## 文档

- SKILL.md - 完整文档 (15000+ 字)
- INSTALL_MAC.md - Mac 安装指南
- NEWS_SOURCES.md - 新闻源管理
```

### 标签 (Tags)
```
finance, news, stocks, analysis, trading, chinese, crypto, akshare, technical-analysis, dragon-tiger, 龙虎榜, 资金流向
```

---

## ✅ 发布前检查清单

- [ ] 所有代码文件完整
- [ ] README.md 清晰易读
- [ ] SKILL.md 文档完整
- [ ] LICENSE 文件存在
- [ ] CHANGELOG.md 存在
- [ ] .gitignore 配置正确
- [ ] icon.png (256x256)
- [ ] 至少 3 张截图
- [ ] skill.json 元数据完整
- [ ] install.sh 可执行
- [ ] test.py 运行正常
- [ ] 所有示例代码可运行
- [ ] 无敏感信息 (API keys, tokens)
- [ ] 依赖版本明确
- [ ] 支持平台标注清楚

---

## 🎯 审核要点

ClawHub.ai 审核会检查:

1. **功能完整性**
   - Skill 是否可以运行
   - 功能是否与描述一致

2. **文档质量**
   - 是否有清晰的安装指南
   - 是否有使用示例
   - 是否标注依赖和配置

3. **代码质量**
   - 代码是否规范
   - 是否有错误处理
   - 是否有注释

4. **用户体验**
   - 是否易于安装
   - 是否易于配置
   - 是否有友好的错误提示

5. **安全性**
   - 是否有明显安全漏洞
   - 是否处理敏感信息
   - 是否有恶意代码

---

## 📧 联系

如果有问题:
- GitHub Issues: https://github.com/your-username/financial-intelligence/issues
- ClawHub.ai 支持: support@clawhub.ai
- Discord: https://discord.com/invite/clawd

---

## 🎉 发布后

发布成功后:

1. **推广**
   - 在 Discord 社区分享
   - 在 Twitter 宣传
   - 写一篇博客介绍

2. **维护**
   - 关注 Issues
   - 及时更新文档
   - 收集用户反馈

3. **迭代**
   - 根据反馈改进
   - 添加新功能
   - 发布新版本

---

**准备好后,就可以发布到 ClawHub.ai 了!** 🚀
