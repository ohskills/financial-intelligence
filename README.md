# Financial Intelligence Agent

**综合金融智能分析助手** - 新闻 + 研究 + 分析 + 监控

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## ⚡ 快速开始

```bash
# 一键安装
bash install.sh

# 测试
python3 modules/news/fetch_financial_express.py 10
python3 modules/research/stock_analyzer.py 688110
```

---

## 🎯 核心功能

- ✅ 实时财经新闻 (财经慢报 + CoinDesk)
- ✅ 股票深度研究 (基本面 + 技术面)
- ✅ 10项技术指标 (MA/MACD/KDJ/BOLL/RSI/ATR/OBV等)
- ✅ 资金流向监控
- ✅ 龙虎榜追踪
- ✅ 智能评分
- ✅ 多市场支持 (A股/美股/港股/加密)

---

## 📦 安装

### 必需依赖
```bash
pip install akshare pandas requests beautifulsoup4 lxml
```

### 可选依赖
```bash
pip install tushare yfinance matplotlib  # 可选
```

---

## ⚙️ 配置

### 最小配置 (无需 API Key)

```json
{
  "data_sources": {
    "primary": "akshare"
  },
  "news_sources": {
    "财经慢报": {
      "enabled": true
    }
  }
}
```

### 完整配置 (可选 LLM)

```json
{
  "llm": {
    "provider": "openrouter",
    "api_key": "sk-xxx",
    "model": "anthropic/claude-sonnet-4"
  },
  "data_sources": {
    "primary": "akshare",
    "tushare": {
      "token": "your_token"
    }
  }
}
```

**支持的 LLM**:
- OpenRouter (推荐)
- SiliconFlow (国内)
- Google Gemini
- OpenAI
- DashScope (阿里云)

**注意**: 不配置 LLM 仍可使用所有核心功能!

---

## 📖 使用

### 命令行

```bash
# 新闻
python3 modules/news/fetch_financial_express.py 20

# 股票分析
python3 modules/research/stock_analyzer.py 688110

# 龙虎榜
python3 modules/research/dragon_tiger.py 688110
```

### 飞书

```
@小丽 抓取财经慢报
@小丽 分析东芯股份
@小丽 龙虎榜 688110
```

---

## 📊 输出示例

```
======================================================================
📊 东芯股份 (688110) - 完整技术分析报告
======================================================================

## 实时行情
最新价: ¥142.50 (+2.30%)
成交量: 12,500,000股
换手率: 15.63%

## 技术指标
MA5:  ¥138.20 (+3.11%) 🟢
MACD: 金叉 (DIF 2.35, DEA 1.82) 🟢
KDJ:  超买区 (K 85.6, D 78.3) 🔴
BOLL: 接近上轨 (85.4%) ⚠️
RSI:  76.3 (中性) 🟡

## 资金流向
主力合计: +1830万 🟢
超大单: +1250万
大单:   +580万

## 龙虎榜
上榜日期: 2026-03-12
净买入: +1756万
机构净买入: +600万
信号: 🟢 游资+机构联手买入

## 综合评分
技术面评分: 6.0/10 ⭐⭐⭐⭐⭐⭐

操作建议: ⏸️ 观望 - 技术面中性,等待明确信号
======================================================================
```

---

## 🏗️ 项目结构

```
financial-intelligence/
├── install.sh              # 一键安装
├── SKILL.md               # 完整文档
├── config.example.json    # 配置模板
│
├── modules/
│   ├── news/              # 新闻模块
│   ├── research/          # 研究模块
│   └── data/              # 数据适配器
│
└── docs/                  # 详细文档
```

---

## 📚 文档

- [完整文档](SKILL.md) - 详细使用说明
- [配置指南](docs/CONFIG.md) - 所有配置选项
- [API 文档](docs/API.md) - 开发接口
- [示例集合](docs/EXAMPLES.md) - 使用案例

---

## 🔌 数据源

| 来源 | 类型 | 费用 | 状态 |
|------|------|------|------|
| AKShare | API | 免费 | ✅ 默认 |
| 财经慢报 | Telegram | 免费 | ✅ 已启用 |
| CoinDesk | RSS | 免费 | ✅ 已启用 |
| Tushare | API | 积分 | 🔜 可选 |
| yFinance | API | 免费 | 🔜 可选 |

---

## ❓ 常见问题

**Q: 必须配置 LLM 吗?**  
A: 不需要。不配置LLM仍可使用新闻、技术分析、龙虎榜等核心功能。

**Q: 数据准确吗?**  
A: 使用 AKShare 抓取东方财富官方数据,准确性有保障。

**Q: 支持哪些市场?**  
A: A股、美股、港股、加密货币。

**Q: 如何定时推送?**  
A: 使用 `openclaw cron` 配置定时任务。

---

## 🤝 贡献

欢迎提交 Issue 和 PR!

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [AKShare](https://github.com/akfamily/akshare)
- [ValueCell](https://github.com/ValueCell-ai/valuecell)
- OpenClaw Community

---

**Version**: 1.0.0  
**Updated**: 2026-03-12
