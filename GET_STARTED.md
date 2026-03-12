# 🎉 Financial Intelligence Agent - 安装完成指南

恭喜!Skill 已经准备就绪。

---

## ✅ 当前状态

- ✅ 配置文件已创建 (`config.json`)
- ✅ 模块文件已就位
  - `modules/news/fetch_financial_express.py` (财经新闻)
  - `modules/research/stock_analyzer.py` (股票分析)
  - `modules/research/stock_with_dragon_tiger.py` (龙虎榜)
- ✅ 核心依赖已安装 (akshare, pandas, requests, beautifulsoup4)

---

## 🚀 立即开始

### 1. 测试新闻抓取

```bash
cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence

python3 modules/news/fetch_financial_express.py 15
```

**预期输出**: 15条分类新闻,带重要性评分

---

### 2. 测试股票分析

```bash
python3 modules/research/stock_analyzer.py 688110
```

**预期输出**: 东芯股份完整技术分析报告

---

### 3. 测试龙虎榜

```bash
python3 modules/research/stock_with_dragon_tiger.py 688110
```

**预期输出**: 实时行情 + 龙虎榜数据

---

## ⚙️ 配置 (可选)

### LLM 配置 (用于 AI 摘要)

编辑 `config.json`:

```json
{
  "llm": {
    "provider": "openrouter",  // 或 siliconflow, google
    "api_key": "sk-xxx",       // 你的 API Key
    "model": "anthropic/claude-sonnet-4"
  }
}
```

**注意**: 不配置 LLM 仍可使用所有核心功能!

---

### Tushare Pro (可选,更详细数据)

1. 注册: https://tushare.pro
2. 获取 token
3. 编辑 `config.json`:

```json
{
  "data_sources": {
    "tushare": {
      "enabled": true,
      "token": "your_token_here"
    }
  }
}
```

---

### 飞书推送配置

编辑 `config.json`:

```json
{
  "delivery": {
    "feishu": {
      "enabled": true,
      "targets": ["oc_2a435bb947763c62f5168fb27ee509dd"]
    }
  }
}
```

---

## 📚 使用文档

### 完整文档

```bash
cat SKILL.md  # 15000+ 字完整指南
```

### 快速参考

```bash
cat README.md  # 快速开始
```

---

## 🔧 定时推送 (可选)

使用 OpenClaw cron 配置定时任务:

```bash
# 每天早上9点推送财经新闻
openclaw cron add \
  --schedule "0 1 * * *" \
  --timezone "UTC" \
  --task "cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence && python3 modules/news/fetch_financial_express.py 20"

# 查看cron任务
openclaw cron list
```

---

## 🎯 下一步建议

### 新用户

1. ✅ 运行测试脚本: `python3 test.py`
2. ✅ 抓取一次新闻验证
3. ✅ 分析一只股票验证
4. ✅ 阅读完整文档 `SKILL.md`

### 进阶用户

1. 配置 LLM (可选)
2. 配置 Tushare Pro (可选)
3. 设置定时推送
4. 创建股票观察列表

---

## ❓ 需要帮助?

### 在飞书 @ 我

```
@小丽 抓取财经慢报

@小丽 分析东芯股份

@小丽 帮我配置 Financial Intelligence Agent
```

---

## 📊 功能对比

| 功能 | ValueCell | Financial Intelligence |
|------|-----------|------------------------|
| 财经新闻 | ❓ 未知 | ✅ 财经慢报+CoinDesk |
| 股票分析 | ✅ 有 | ✅ 10项技术指标 |
| 龙虎榜 | ❌ 无 | ✅ **新增** |
| 资金流向 | ❌ 无 | ✅ **新增** |
| 完全免费 | ❓ | ✅ **无需API Key** |
| 多市场 | ✅ | ✅ A股/美股/港股/加密 |

---

## 🎉 开始使用!

```bash
# 立即测试
python3 modules/news/fetch_financial_express.py 10

# 开始你的金融分析之旅! 🚀
```
