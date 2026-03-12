# 新闻源管理指南

Financial Intelligence Agent 现已支持 **20+ 新闻源**,用户可以自定义启用/禁用!

---

## 📊 新闻源列表

### 🌍 全球 (5个)

| ID | 名称 | 类型 | 费用 | 默认状态 |
|----|----|------|------|---------|
| financial_express | 财经慢报 | Telegram | 免费 | ✅ 已启用 |
| jinshi | 金十数据 | Web | 免费 | ⚪ 未启用 |
| bloomberg | Bloomberg | API | 付费 | ⚪ 未启用 |
| reuters | Reuters | RSS | 免费 | ⚪ 未启用 |
| ft | Financial Times | RSS | 付费 | ⚪ 未启用 |

### 🇨🇳 中国 (4个)

| ID | 名称 | 类型 | 费用 | 默认状态 |
|----|----|------|------|---------|
| eastmoney | 东方财富 | RSS | 免费 | ⚪ 未启用 |
| cn_securities | 中国证券报 | RSS | 免费 | ⚪ 未启用 |
| securities_times | 证券时报 | Web | 免费 | ⚪ 未启用 |
| 36kr | 36氪 | RSS | 免费 | ⚪ 未启用 |

### 🇺🇸 美国 (7个)

| ID | 名称 | 类型 | 费用 | 默认状态 |
|----|----|------|------|---------|
| wallstreetcn | 华尔街见闻 | API | 付费 | ⚪ 未启用 |
| wsj | Wall Street Journal | RSS | 付费 | ⚪ 未启用 |
| cnbc | CNBC | RSS | 免费 | ⚪ 未启用 |
| seeking_alpha | Seeking Alpha | Web | 免费 | ⚪ 未启用 |
| benzinga | Benzinga | RSS | 免费 | ⚪ 未启用 |
| finviz | Finviz | Web | 免费 | ⚪ 未启用 |
| yahoo_finance | Yahoo Finance | RSS | 免费 | ⚪ 未启用 |

### ₿ 加密货币 (3个)

| ID | 名称 | 类型 | 费用 | 默认状态 |
|----|----|------|------|---------|
| coindesk | CoinDesk | RSS | 免费 | ✅ 已启用 |
| cointelegraph | Cointelegraph | RSS | 免费 | ✅ 已启用 |
| the_block | The Block | RSS | 免费 | ⚪ 未启用 |

### 🇭🇰 香港 (1个)

| ID | 名称 | 类型 | 费用 | 默认状态 |
|----|----|------|------|---------|
| hkex_news | 港交所披露易 | Web | 免费 | ⚪ 未启用 |

**总计**: 20个新闻源 (16个免费, 4个付费)

---

## 🛠️ 管理新闻源

### 查看所有可用源

```bash
cd modules/news

# 只看已启用的
python3 manage_sources.py list

# 看所有源 (包括未启用)
python3 manage_sources.py list --all
```

---

### 启用新闻源

```bash
# 启用单个源
python3 manage_sources.py enable eastmoney

# 启用多个源
python3 manage_sources.py enable reuters
python3 manage_sources.py enable cnbc
python3 manage_sources.py enable the_block
```

---

### 禁用新闻源

```bash
python3 manage_sources.py disable coindesk
```

---

### 查看源详情

```bash
python3 manage_sources.py info financial_express
```

输出:
```
============================================================
📰 财经慢报
============================================================
ID: financial_express
类型: telegram
市场: global
语言: zh-CN
更新频率: realtime
状态: ✅ 已启用
费用: 免费

描述: Telegram 实时财经快讯,覆盖全球市场

URL: https://t.me/s/Financial_Express

分类: 综合, 实时快讯
============================================================
```

---

### 配置向导 (推荐)

```bash
python3 manage_sources.py setup
```

会显示推荐配置,可以快速启用多个源。

---

## 📝 手动编辑配置

编辑 `modules/news/sources_config.json`:

```json
{
  "sources": [
    {
      "id": "eastmoney",
      "name": "东方财富",
      "enabled": true,  // 改为 true 启用
      ...
    }
  ],
  
  "user_preferences": {
    "enabled_sources": [
      "financial_express",
      "coindesk",
      "eastmoney"  // 添加到这里
    ]
  }
}
```

---

## 🎯 推荐配置

### 方案 1: 中文投资者

```bash
python3 manage_sources.py enable financial_express  # 实时快讯
python3 manage_sources.py enable jinshi             # 金十数据
python3 manage_sources.py enable eastmoney          # A股门户
python3 manage_sources.py enable wallstreetcn       # 美股 (需VIP)
```

### 方案 2: 美股投资者

```bash
python3 manage_sources.py enable financial_express  # 全球快讯
python3 manage_sources.py enable cnbc              # 美股实时
python3 manage_sources.py enable seeking_alpha     # 分析观点
python3 manage_sources.py enable benzinga          # 交易新闻
```

### 方案 3: 加密货币

```bash
python3 manage_sources.py enable coindesk          # 已默认启用
python3 manage_sources.py enable cointelegraph     # 已默认启用
python3 manage_sources.py enable the_block         # 机构级
```

### 方案 4: 全能配置

```bash
python3 manage_sources.py enable financial_express
python3 manage_sources.py enable eastmoney
python3 manage_sources.py enable reuters
python3 manage_sources.py enable coindesk
python3 manage_sources.py enable cnbc
```

---

## 🔧 开发者: 添加新的新闻源

编辑 `modules/news/sources_config.json`,添加新源:

```json
{
  "id": "my_custom_source",
  "name": "我的新闻源",
  "type": "rss",  // 或 telegram, web, api
  "url": "https://example.com/",
  "rss_url": "https://example.com/rss",
  "priority": "medium",
  "categories": ["综合"],
  "market": "global",
  "language": "zh-CN",
  "update_frequency": "hourly",
  "enabled": false,
  "free": true,
  "description": "我的自定义新闻源"
}
```

然后创建对应的抓取脚本:
- `fetch_my_custom_source.py`

---

## ❓ 常见问题

### Q1: 付费源怎么配置?

**A**: 编辑 `sources_config.json`,添加 API key:
```json
{
  "id": "bloomberg",
  "api_key": "your_api_key_here",
  "enabled": true
}
```

### Q2: 如何增加抓取频率?

**A**: 使用 OpenClaw cron 配置多个时间:
```bash
openclaw cron add --schedule "0 */2 * * *" --task "抓取新闻"
```

### Q3: 新闻重复怎么办?

**A**: 配置去重:
```json
{
  "filters": {
    "deduplication": {
      "enabled": true,
      "similarity_threshold": 0.85
    }
  }
}
```

### Q4: 如何只看中文新闻?

**A**: 编辑 `user_preferences`:
```json
{
  "user_preferences": {
    "language_preference": "zh-CN"
  }
}
```

---

## 📊 使用统计

```bash
python3 manage_sources.py list --all
```

会显示:
- ✅ 已启用源数量
- 💰 免费源数量
- 💳 付费源数量

---

## 🚀 快速开始

```bash
# 1. 查看所有可用源
python3 manage_sources.py list --all

# 2. 运行配置向导
python3 manage_sources.py setup

# 3. 测试抓取
python3 fetch_financial_express.py 10

# 4. 查看已启用的源
python3 manage_sources.py list
```

---

**现在你有 20+ 新闻源可以选择!** 🎉
