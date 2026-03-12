#!/bin/bash

# Financial Intelligence Agent - 安装脚本
# 自动安装依赖并初始化配置

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Financial Intelligence Agent - 安装向导                   ║"
echo "║  综合金融智能分析助手                                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 未安装,请先安装 Python 3.8+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1-2)
echo "✅ Python 版本: $PYTHON_VERSION"
echo ""

# 创建目录结构
echo "📁 创建目录结构..."
mkdir -p modules/news
mkdir -p modules/research
mkdir -p modules/data
mkdir -p utils
mkdir -p scripts
mkdir -p docs
mkdir -p logs
echo "✅ 目录创建完成"
echo ""

# 安装依赖
echo "📦 安装 Python 依赖..."
echo ""
echo "必需依赖:"
pip3 install akshare pandas requests beautifulsoup4 lxml --break-system-packages -q
echo "✅ akshare, pandas, requests, beautifulsoup4, lxml"
echo ""

echo "可选依赖 (按需安装):"
read -p "安装 Tushare Pro? (y/n): " install_tushare
if [[ $install_tushare == "y" ]]; then
    pip3 install tushare --break-system-packages -q
    echo "✅ tushare"
fi

read -p "安装 yFinance (美股)? (y/n): " install_yfinance
if [[ $install_yfinance == "y" ]]; then
    pip3 install yfinance --break-system-packages -q
    echo "✅ yfinance"
fi

read -p "安装 Matplotlib (图表)? (y/n): " install_matplotlib
if [[ $install_matplotlib == "y" ]]; then
    pip3 install matplotlib --break-system-packages -q
    echo "✅ matplotlib"
fi

echo ""
echo "✅ 依赖安装完成"
echo ""

# 初始化配置
echo "⚙️  初始化配置..."
if [ ! -f config.json ]; then
    cp config.example.json config.json
    echo "✅ 创建 config.json (从 config.example.json 复制)"
else
    echo "⚠️  config.json 已存在,跳过"
fi
echo ""

# 配置向导
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  配置向导                                                  ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

echo "1️⃣  LLM 配置 (可选,用于 AI 摘要)"
echo "   如果不需要 AI 功能,可以跳过"
echo ""
read -p "配置 LLM API Key? (y/n): " config_llm

if [[ $config_llm == "y" ]]; then
    echo ""
    echo "支持的 LLM 提供商:"
    echo "  1. OpenRouter (推荐, openrouter.ai)"
    echo "  2. SiliconFlow (国内, siliconflow.cn)"
    echo "  3. Google Gemini (ai.google.dev)"
    echo "  4. OpenAI (platform.openai.com)"
    echo "  5. DashScope (阿里云, dashscope.aliyun.com)"
    echo ""
    read -p "选择提供商 (1-5): " llm_provider
    
    case $llm_provider in
        1) provider="openrouter" ;;
        2) provider="siliconflow" ;;
        3) provider="google" ;;
        4) provider="openai" ;;
        5) provider="dashscope" ;;
        *) provider="openrouter" ;;
    esac
    
    read -p "输入 API Key: " api_key
    
    # 更新 config.json
    if command -v jq &> /dev/null; then
        jq ".llm.provider = \"$provider\" | .llm.api_key = \"$api_key\"" config.json > config.tmp
        mv config.tmp config.json
        echo "✅ LLM 配置已保存"
    else
        echo "⚠️  jq 未安装,请手动编辑 config.json"
        echo "   设置 llm.provider = \"$provider\""
        echo "   设置 llm.api_key = \"$api_key\""
    fi
else
    echo "⏭️  跳过 LLM 配置 (仍可使用新闻和技术分析功能)"
fi

echo ""
echo "2️⃣  数据源配置"
echo "   AKShare (免费) 已默认启用"
echo ""

if [[ $install_tushare == "y" ]]; then
    read -p "配置 Tushare Pro Token? (y/n): " config_tushare
    if [[ $config_tushare == "y" ]]; then
        echo "注册: https://tushare.pro"
        read -p "输入 Token: " tushare_token
        if command -v jq &> /dev/null; then
            jq ".data_sources.tushare.enabled = true | .data_sources.tushare.token = \"$tushare_token\"" config.json > config.tmp
            mv config.tmp config.json
            echo "✅ Tushare 配置已保存"
        else
            echo "⚠️  请手动编辑 config.json 设置 Tushare token"
        fi
    fi
fi

echo ""
echo "3️⃣  推送配置"
echo "   飞书推送已默认启用"
read -p "修改飞书群 ID? (y/n): " config_feishu

if [[ $config_feishu == "y" ]]; then
    read -p "输入飞书群 ID: " feishu_group
    if command -v jq &> /dev/null; then
        jq ".delivery.feishu.targets = [\"$feishu_group\"]" config.json > config.tmp
        mv config.tmp config.json
        echo "✅ 飞书配置已保存"
    else
        echo "⚠️  请手动编辑 config.json 设置飞书群 ID"
    fi
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  安装完成!                                                 ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 下一步:"
echo ""
echo "1. 测试新闻抓取:"
echo "   python3 modules/news/fetch_financial_express.py 10"
echo ""
echo "2. 测试股票分析:"
echo "   python3 modules/research/stock_analyzer.py 688110"
echo ""
echo "3. 查看完整文档:"
echo "   cat SKILL.md"
echo ""
echo "4. 配置定时任务 (可选):"
echo "   openclaw cron add --schedule \"0 9 * * *\" --task \"财经晨报推送\""
echo ""
echo "🎉 开始使用 Financial Intelligence Agent!"
echo ""
