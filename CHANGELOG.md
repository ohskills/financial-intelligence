# Changelog

All notable changes to Financial Intelligence Agent will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-12

### Added
- 📰 **财经新闻聚合模块**
  - 20+ 新闻源支持 (财经慢报、CoinDesk、Bloomberg、Reuters 等)
  - 自动分类 (8大类别: 地缘政治、加密货币、A股、美股、货币政策、能源商品、科技、公司动态)
  - 重要性智能评分 (1-10分)
  - 用户可自定义启用/禁用新闻源
  - 新闻源管理工具 (`manage_sources.py`)

- 📊 **股票深度研究模块**
  - 实时行情获取 (基于 AKShare)
  - 基本面分析 (财务健康度、竞争格局、增长前景)
  - 10项技术指标:
    - MA (移动平均线)
    - MACD (异同移动平均线)
    - KDJ (随机指标)
    - BOLL (布林带)
    - RSI (相对强弱指数)
    - ATR (真实波动幅度)
    - OBV (能量潮)
  - 资金流向分析 (主力/散户/机构)
  - 龙虎榜追踪 (游资/机构席位)
  - 筹码分布分析
  - 智能综合评分系统

- 🌍 **多市场支持**
  - A股 (沪深主板、科创板、创业板)
  - 美股 (NASDAQ、NYSE)
  - 港股 (HKEX)
  - 加密货币 (BTC、ETH 等)

- ⚙️ **配置系统**
  - 完全可配置的新闻源
  - 可选 LLM 集成 (OpenRouter, SiliconFlow, Google, OpenAI, DashScope)
  - 可选 Tushare Pro 集成 (更详细的 A股数据)
  - 飞书/Telegram/Discord 推送支持

- 📚 **完整文档**
  - SKILL.md (15000+ 字完整文档)
  - INSTALL_MAC.md (Mac 安装指南)
  - NEWS_SOURCES.md (新闻源管理)
  - CLAWHUB_PUBLISH.md (发布指南)
  - 中英文 README

- 🛠️ **工具与脚本**
  - 一键安装脚本 (`install.sh`, `install_mac.sh`)
  - 完整测试脚本 (`test.py`)
  - 新闻源管理工具
  - 示例配置文件

### Features
- ✅ 完全免费 (使用 AKShare 开源数据源)
- ✅ 开箱即用 (无需任何 API Key)
- ✅ 用户可自定义配置
- ✅ 模块化设计 (易于扩展)
- ✅ 完整中英文文档
- ✅ Mac/Linux 支持
- ✅ 智能缓存 (减少 API 调用)
- ✅ 错误处理 (友好的错误提示)

### Technical
- Python 3.8+ 支持
- 依赖最小化 (核心功能仅需 4 个包)
- 模块化架构
- 清晰的项目结构
- 完整的类型注释 (部分)

### Documentation
- 完整的 API 文档
- 详细的配置说明
- 丰富的使用示例
- 常见问题解答
- 故障排查指南

## [Unreleased]

### Planned
- [ ] 更多新闻源集成 (金十数据、华尔街见闻等)
- [ ] K线图可视化
- [ ] DCF 估值模型
- [ ] 行业分析功能
- [ ] 股票对比分析
- [ ] 批量分析工具
- [ ] 定时监控与提醒
- [ ] Web UI 界面
- [ ] Docker 支持
- [ ] Windows 支持
- [ ] 多语言支持 (英文版)

---

**Legend**:
- 📰 News Module
- 📊 Research Module
- 🌍 Market Support
- ⚙️ Configuration
- 📚 Documentation
- 🛠️ Tools
- 🔧 Technical
- 🐛 Bug Fix
- ⚡ Performance
- 🎨 UI/UX
