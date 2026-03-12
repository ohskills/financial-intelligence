# Financial Intelligence Agent

**综合金融智能分析助手** - 新闻聚合 + 股票研究 + 技术分析 + 龙虎榜监控

---

## 📋 目录

- [功能特性](#功能特性)
- [快速开始](#快速开始)
- [配置说明](#配置说明)
- [使用方法](#使用方法)
- [模块架构](#模块架构)
- [数据源](#数据源)
- [常见问题](#常见问题)

---

## 🎯 功能特性

### 1. 📰 财经新闻聚合

- **实时新闻**: 财经慢报 (Telegram)、CoinDesk (RSS)
- **自动分类**: 地缘政治、加密货币、A股、美股、能源商品等
- **重要性评分**: 1-10分智能评分
- **定时推送**: 早晚报 + 实时提醒

### 2. 📊 股票深度研究

- **基本面分析**: 财务健康度、竞争格局、增长前景
- **技术分析**: 10项指标 (MA, MACD, KDJ, BOLL, RSI, ATR, OBV等)
- **资金流向**: 主力/散户/机构资金动向
- **龙虎榜**: 游资/机构席位追踪
- **综合评分**: 多维度打分 + 操作建议

### 3. 🌍 多市场支持

- **A股**: 沪深主板、科创板、创业板
- **美股**: NASDAQ、NYSE
- **港股**: HKEX
- **加密货币**: BTC、ETH等

---

## 🚀 快速开始

### 一键安装

```bash
# 克隆或下载 skill
cd ~/.openclaw/workspace/skills/financial-intelligence

# 运行安装脚本
bash install.sh

# 启动配置向导
python3 main.py --config
```

### 手动安装

```bash
# 1. 安装 Python 依赖
pip install akshare pandas requests beautifulsoup4 lxml --break-system-packages

# 2. 可选: 安装额外依赖
pip install tushare yfinance matplotlib --break-system-packages

# 3. 复制配置文件
cp config.example.json config.json

# 4. 编辑配置
nano config.json
```

---

## ⚙️ 配置说明

### 1. LLM 配置 (可选)

如果需要 AI 摘要/分析功能,配置 LLM:

```json
{
  "llm": {
    "provider": "openrouter",  // 或 siliconflow, google, openai, dashscope
    "api_key": "sk-xxx",       // 你的 API Key
    "model": "anthropic/claude-sonnet-4-20250514",
    "temperature": 0.7,
    "max_tokens": 4096
  }
}
```

**支持的 LLM 提供商**:

| 提供商 | 注册地址 | 费用 | 推荐 |
|--------|---------|------|------|
| OpenRouter | [openrouter.ai](https://openrouter.ai) | 按量付费 | ⭐⭐⭐⭐⭐ |
| SiliconFlow | [siliconflow.cn](https://siliconflow.cn) | 按量付费 | ⭐⭐⭐⭐⭐ |
| Google | [ai.google.dev](https://ai.google.dev) | 免费配额 | ⭐⭐⭐⭐ |
| DashScope | [dashscope.aliyun.com](https://dashscope.aliyun.com) | 按量付费 | ⭐⭐⭐⭐ |

**注意**: 如果不配置 LLM,新闻抓取和技术分析功能仍然可用,只是没有 AI 摘要。

---

### 2. 数据源配置

#### AKShare (免费,推荐)

**无需配置!** 开箱即用。

```json
{
  "data_sources": {
    "primary": "akshare",
    "akshare": {
      "enabled": true
    }
  }
}
```

#### Tushare Pro (可选)

如果需要更详细的数据:

1. 注册: https://tushare.pro
2. 获取 token
3. 配置:

```json
{
  "data_sources": {
    "tushare": {
      "enabled": true,
      "token": "your_token_here",
      "points": 2000
    }
  }
}
```

#### yFinance (美股,可选)

```json
{
  "data_sources": {
    "yfinance": {
      "enabled": true
    }
  }
}
```

---

### 3. 新闻源配置

默认已启用:
- ✅ 财经慢报 (Telegram)
- ✅ CoinDesk (RSS)

可选新闻源 (需要配置):

```json
{
  "news_sources": [
    {
      "id": "bloomberg",
      "enabled": false,
      "api_key": ""
    },
    {
      "id": "华尔街见闻",
      "enabled": false,
      "vip_account": ""
    }
  ]
}
```

---

### 4. 推送配置

#### 飞书推送

```json
{
  "delivery": {
    "feishu": {
      "enabled": true,
      "targets": ["oc_2a435bb947763c62f5168fb27ee509dd"],
      "schedule": {
        "morning": "0 9 * * *",
        "evening": "0 18 * * *"
      }
    }
  }
}
```

#### Telegram推送

```json
{
  "delivery": {
    "telegram": {
      "enabled": true,
      "bot_token": "your_bot_token",
      "chat_id": "your_chat_id"
    }
  }
}
```

---

## 📖 使用方法

### 命令行使用

#### 1. 抓取财经新闻

```bash
# 抓取财经慢报最新 20 条
python3 main.py news --source 财经慢报 --limit 20

# 抓取 CoinDesk
python3 main.py news --source coindesk --limit 10

# 抓取所有源
python3 main.py news --all --limit 30
```

#### 2. 股票分析

```bash
# 完整分析 (基本面 + 技术面 + 龙虎榜)
python3 main.py stock --symbol 688110 --full

# 只看技术分析
python3 main.py stock --symbol 688110 --technical

# 只看龙虎榜
python3 main.py stock --symbol 688110 --dragon-tiger

# 批量分析
python3 main.py stock --watchlist stocks.txt
```

#### 3. 定时监控

```bash
# 启动监控服务
python3 main.py monitor --watchlist stocks.txt --interval 1h

# 后台运行
nohup python3 main.py monitor --watchlist stocks.txt &
```

---

### 飞书使用

在飞书群 @ 机器人:

```
@小丽 抓取财经慢报

@小丽 分析东芯股份

@小丽 分析 688110

@小丽 龙虎榜 688110

@小丽 监控 688110,600519,300750
```

---

## 🏗️ 模块架构

```
financial-intelligence/
├── skill.json              # Skill 元数据
├── SKILL.md               # 本文档
├── README.md              # 简化版说明
├── install.sh             # 安装脚本
├── main.py                # 主入口
├── config.example.json    # 配置模板
├── config.json            # 用户配置 (gitignore)
│
├── modules/               # 功能模块
│   ├── news/             # 新闻聚合模块
│   │   ├── config.json
│   │   ├── fetch_financial_express.py
│   │   ├── fetch_coindesk.py
│   │   └── news_aggregator.py
│   │
│   ├── research/         # 股票研究模块
│   │   ├── config.json
│   │   ├── stock_analyzer.py
│   │   ├── technical_analysis.py
│   │   └── dragon_tiger.py
│   │
│   └── data/             # 数据源适配器
│       ├── akshare_adapter.py
│       ├── tushare_adapter.py
│       └── yfinance_adapter.py
│
├── utils/                # 工具函数
│   ├── logger.py
│   ├── cache.py
│   └── formatter.py
│
├── scripts/              # 辅助脚本
│   ├── setup_cron.sh
│   └── test.py
│
└── docs/                 # 文档
    ├── API.md
    ├── CONFIG.md
    └── EXAMPLES.md
```

---

## 🔌 数据源

### 已集成

| 数据源 | 类型 | 市场 | 费用 | 状态 |
|--------|------|------|------|------|
| **AKShare** | Python库 | A股/美股/港股/加密 | 免费 | ✅ 主力 |
| **财经慢报** | Telegram | 全球 | 免费 | ✅ 已启用 |
| **CoinDesk** | RSS | 加密货币 | 免费 | ✅ 已启用 |

### 可选集成

| 数据源 | 类型 | 市场 | 费用 | 状态 |
|--------|------|------|------|------|
| Tushare Pro | API | A股/美股 | 积分制 | 🔜 可选 |
| yFinance | Python库 | 美股 | 免费 | 🔜 可选 |
| Bloomberg | API | 全球 | 付费 | ⏸️ 待实现 |
| 华尔街见闻 | API | 全球 | VIP | ⏸️ 待实现 |

---

## 🎯 完整配置示例

### config.json

```json
{
  "version": "1.0.0",
  
  "llm": {
    "provider": "openrouter",
    "api_key": "sk-or-v1-xxx",
    "model": "anthropic/claude-sonnet-4-20250514",
    "temperature": 0.7,
    "max_tokens": 4096,
    "enable_summary": true,
    "enable_translation": false
  },
  
  "data_sources": {
    "primary": "akshare",
    
    "akshare": {
      "enabled": true,
      "cache_ttl": 300
    },
    
    "tushare": {
      "enabled": false,
      "token": "",
      "points": 0
    },
    
    "yfinance": {
      "enabled": false
    }
  },
  
  "news_sources": {
    "财经慢报": {
      "enabled": true,
      "priority": "high",
      "url": "https://t.me/s/Financial_Express",
      "fetch_interval": 300
    },
    
    "coindesk": {
      "enabled": true,
      "priority": "medium",
      "url": "https://www.coindesk.com/arc/outboundfeeds/rss/"
    }
  },
  
  "analysis": {
    "technical_indicators": [
      "MA", "MACD", "KDJ", "BOLL", "RSI", "ATR", "OBV"
    ],
    "scoring": {
      "enabled": true,
      "min_score": 0,
      "max_score": 10
    }
  },
  
  "delivery": {
    "feishu": {
      "enabled": true,
      "targets": ["oc_2a435bb947763c62f5168fb27ee509dd"]
    },
    
    "telegram": {
      "enabled": false,
      "bot_token": "",
      "chat_id": ""
    },
    
    "schedule": {
      "morning_digest": {
        "cron": "0 9 * * *",
        "timezone": "Asia/Shanghai",
        "sources": ["财经慢报", "coindesk"],
        "limit": 20
      },
      
      "evening_digest": {
        "cron": "0 18 * * *",
        "timezone": "Asia/Shanghai",
        "sources": ["财经慢报"],
        "limit": 15
      }
    }
  },
  
  "filters": {
    "keywords": {
      "include": ["AI", "芯片", "新能源", "比特币"],
      "exclude": ["广告", "推广"]
    },
    "min_importance": 6
  },
  
  "performance": {
    "cache_enabled": true,
    "cache_ttl": 3600,
    "max_concurrent": 5,
    "timeout": 30
  }
}
```

---

## 💡 使用场景

### 场景 1: 日常投资决策

```bash
# 早上: 看新闻
python3 main.py news --source 财经慢报 --limit 20

# 发现热点股票,深度分析
python3 main.py stock --symbol 688110 --full

# 查看龙虎榜,看游资动向
python3 main.py stock --symbol 688110 --dragon-tiger
```

### 场景 2: 自动化监控

```bash
# 创建观察列表
echo "688110
600519
300750
002594" > watchlist.txt

# 启动监控 (每小时检查一次)
python3 main.py monitor --watchlist watchlist.txt --interval 1h

# 配置定时推送
openclaw cron add --schedule "0 9,18 * * *" \
  --task "python3 main.py news --all | 飞书推送"
```

### 场景 3: 快速调研

```bash
# 对比分析两只股票
python3 main.py compare --symbols 688110,688008

# 行业分析
python3 main.py sector --name "半导体" --top 10
```

---

## ❓ 常见问题

### Q1: 必须配置 LLM 吗?

**A**: 不是必须的。
- **不配置**: 新闻抓取、技术分析、龙虎榜等功能都可以用
- **配置后**: 额外获得 AI 摘要、智能分析、自然语言问答

### Q2: AKShare 稳定吗?

**A**: 
- **优点**: 免费、无需注册、覆盖全
- **缺点**: 依赖网络爬虫,偶尔会失败
- **建议**: 配置 Tushare 作为备用

### Q3: 数据有延迟吗?

**A**: 
- **实时行情**: 15分钟延迟 (免费版限制)
- **新闻**: 实时 (Telegram 推送即更新)
- **龙虎榜**: T+1 (交易所第二天公布)

### Q4: 如何添加新的新闻源?

**A**: 
1. 编辑 `modules/news/config.json`
2. 添加新源配置
3. 创建对应的 `fetch_xxx.py` 脚本
4. 在 `news_aggregator.py` 中注册

### Q5: 支持哪些 LLM?

**A**: 
- ✅ OpenRouter (推荐,支持所有主流模型)
- ✅ SiliconFlow (国内快,便宜)
- ✅ Google Gemini (免费配额)
- ✅ OpenAI
- ✅ DashScope (阿里云通义千问)
- ✅ Azure OpenAI
- ✅ 任何 OpenAI 兼容接口

### Q6: 如何导出分析报告?

**A**:
```bash
# 导出为 Markdown
python3 main.py stock --symbol 688110 --full --output report.md

# 导出为 JSON
python3 main.py stock --symbol 688110 --full --format json --output report.json

# 推送到飞书
python3 main.py stock --symbol 688110 --full --send-to feishu
```

---

## 🔧 高级配置

### 代理设置

```json
{
  "proxy": {
    "http": "http://proxy:port",
    "https": "http://proxy:port"
  }
}
```

### 日志配置

```json
{
  "logging": {
    "level": "INFO",
    "file": "logs/financial-intelligence.log",
    "max_size_mb": 100,
    "backup_count": 5
  }
}
```

### 性能优化

```json
{
  "performance": {
    "cache_enabled": true,
    "cache_backend": "memory",
    "max_workers": 5,
    "timeout": 30,
    "retry": {
      "max_attempts": 3,
      "backoff_factor": 2
    }
  }
}
```

---

## 📚 相关文档

- [API 文档](docs/API.md)
- [配置详解](docs/CONFIG.md)
- [使用示例](docs/EXAMPLES.md)
- [开发指南](docs/DEVELOPMENT.md)

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request!

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [AKShare](https://github.com/akfamily/akshare) - 免费开源的金融数据接口
- [ValueCell](https://github.com/ValueCell-ai/valuecell) - 项目灵感来源
- OpenClaw Community

---

**更新时间**: 2026-03-12  
**版本**: v1.0.0
