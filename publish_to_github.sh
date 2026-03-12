#!/bin/bash

# GitHub 发布脚本
# 使用前请先在 GitHub 创建仓库: https://github.com/new

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Financial Intelligence Agent - GitHub 发布准备            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# 进入项目目录
cd /home/ubuntu/.openclaw/workspace/skills/financial-intelligence

# 清理可能存在的 git 目录
if [ -d ".git" ]; then
    echo "⚠️  检测到已有 .git 目录,是否重新初始化?"
    read -p "继续? (y/n): " confirm
    if [ "$confirm" != "y" ]; then
        echo "已取消"
        exit 0
    fi
    rm -rf .git
fi

echo "1️⃣  初始化 Git 仓库..."
git init
git branch -M main

echo ""
echo "2️⃣  添加所有文件..."
git add .

echo ""
echo "3️⃣  创建初始提交..."
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
echo "✅ Git 初始化完成!"
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  下一步: 创建 GitHub 仓库并推送                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "请按照以下步骤操作:"
echo ""
echo "1️⃣  在浏览器打开: https://github.com/new"
echo ""
echo "2️⃣  填写仓库信息:"
echo "   - Repository name: financial-intelligence"
echo "   - Description: 综合金融智能分析助手 - 新闻聚合 + 股票研究 + 技术分析"
echo "   - Public (公开) ✅"
echo "   - 不要勾选 Initialize with README (已有文件)"
echo ""
echo "3️⃣  创建仓库后,复制仓库 URL (例如: https://github.com/你的用户名/financial-intelligence.git)"
echo ""
read -p "输入你的 GitHub 仓库 URL: " REPO_URL

echo ""
echo "4️⃣  关联远程仓库..."
git remote add origin "$REPO_URL"

echo ""
echo "5️⃣  推送到 GitHub..."
echo ""
read -p "准备好推送了吗? (y/n): " confirm

if [ "$confirm" = "y" ]; then
    echo ""
    echo "正在推送..."
    git push -u origin main
    
    echo ""
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║  ✅ 成功推送到 GitHub!                                     ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo ""
    echo "🎉 仓库地址: $REPO_URL"
    echo ""
    echo "下一步:"
    echo "  1. 访问你的 GitHub 仓库检查文件"
    echo "  2. 准备截图和图标"
    echo "  3. 提交到 ClawHub.ai"
    echo ""
else
    echo ""
    echo "手动推送命令:"
    echo "  git push -u origin main"
    echo ""
fi

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  推送完成后的清单                                          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "✅ 代码已推送到 GitHub"
echo "❓ 准备图标 (icon.png, 256x256)"
echo "❓ 准备截图 (3张)"
echo ""
echo "准备截图:"
echo "  python3 modules/news/fetch_financial_express.py 15 > /tmp/news.txt"
echo "  python3 modules/research/stock_analyzer.py 688110 > /tmp/analysis.txt"
echo ""
echo "然后截图保存为:"
echo "  - screenshots/news.png"
echo "  - screenshots/analysis.png"
echo "  - screenshots/dragon-tiger.png"
echo ""
