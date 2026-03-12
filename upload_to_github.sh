#!/bin/bash
# Financial Intelligence Agent - 上传到 GitHub
# 仓库: https://github.com/ohskills/financial-intelligence

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  开始上传到 GitHub                                         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence

# 清理可能存在的 git
if [ -d ".git" ]; then
    rm -rf .git
fi

echo "1️⃣  初始化 Git..."
git init
git branch -M main

echo ""
echo "2️⃣  添加文件..."
git add .

echo ""
echo "3️⃣  创建提交..."
git commit -m "feat: Financial Intelligence Agent v1.0.0

📰 财经新闻聚合
- 20+ 新闻源支持 (财经慢报、CoinDesk、Bloomberg、Reuters 等)
- 自动分类与重要性评分
- 用户可自定义配置新闻源

📊 股票深度研究
- 实时行情获取 (AKShare)
- 10项技术指标分析 (MA, MACD, KDJ, BOLL, RSI, ATR, OBV)
- 资金流向监控
- 龙虎榜追踪
- 智能综合评分

🌍 多市场支持
- A股、美股、港股、加密货币

🎯 核心特性
- 完全免费 (无需 API Key)
- 开箱即用
- 用户可配置
- 完整中英文档 (15000+ 字)
- Mac/Linux 支持"

echo ""
echo "4️⃣  关联远程仓库..."
git remote add origin https://github.com/ohskills/financial-intelligence.git

echo ""
echo "5️⃣  推送到 GitHub..."
git push -u origin main

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  ✅ 成功推送到 GitHub!                                     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "🎉 仓库地址: https://github.com/ohskills/financial-intelligence"
echo ""
echo "下一步:"
echo "  1. 访问 https://github.com/ohskills/financial-intelligence 检查"
echo "  2. 准备截图和图标 (可选)"
echo "  3. 提交到 ClawHub.ai"
echo ""
