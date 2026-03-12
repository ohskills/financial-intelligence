#!/bin/bash

# Financial Intelligence Agent - Mac 自动安装脚本
# 使用方法: bash install_mac.sh

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Financial Intelligence Agent - Mac 安装                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查 Python
echo "🔍 检查 Python..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 未安装${NC}"
    echo ""
    echo "请先安装 Python 3.8+:"
    echo "  brew install python@3.11"
    echo ""
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✅ ${PYTHON_VERSION}${NC}"
echo ""

# 询问安装位置
echo "📁 选择安装位置:"
echo "  1. ~/financial-intelligence (推荐)"
echo "  2. 自定义路径"
echo ""
read -p "选择 (1/2): " install_choice

if [ "$install_choice" = "2" ]; then
    read -p "输入安装路径: " INSTALL_DIR
else
    INSTALL_DIR="$HOME/financial-intelligence"
fi

echo ""
echo "安装到: $INSTALL_DIR"
echo ""

# 询问安装方式
echo "📥 选择安装方式:"
echo "  1. 从服务器下载 (需要 SSH 访问)"
echo "  2. 手动安装 (最小化)"
echo ""
read -p "选择 (1/2): " download_choice

if [ "$download_choice" = "1" ]; then
    # 从服务器下载
    echo ""
    read -p "服务器地址 (默认: ubuntu@ip-10-0-1-120): " SERVER
    SERVER=${SERVER:-ubuntu@ip-10-0-1-120}
    
    SERVER_PATH="/home/ubuntu/.openclaw/workspace/skills/financial-intelligence"
    
    echo ""
    echo "📥 从服务器下载..."
    
    # 测试连接
    if ssh -o BatchMode=yes -o ConnectTimeout=5 $SERVER "test -d $SERVER_PATH" 2>/dev/null; then
        echo -e "${GREEN}✅ 服务器连接成功${NC}"
        
        # 下载文件
        mkdir -p "$INSTALL_DIR"
        scp -r "$SERVER:$SERVER_PATH/"* "$INSTALL_DIR/"
        
        echo -e "${GREEN}✅ 文件下载完成${NC}"
    else
        echo -e "${YELLOW}⚠️  无法连接服务器,切换到手动安装${NC}"
        download_choice="2"
    fi
fi

if [ "$download_choice" = "2" ]; then
    # 手动安装
    echo ""
    echo "📦 手动安装模式..."
    
    # 创建目录
    mkdir -p "$INSTALL_DIR/modules/news"
    mkdir -p "$INSTALL_DIR/modules/research"
    mkdir -p "$INSTALL_DIR/modules/data"
    mkdir -p "$INSTALL_DIR/utils"
    mkdir -p "$INSTALL_DIR/logs"
    
    cd "$INSTALL_DIR"
    
    # 创建最小配置
    cat > config.json << 'EOF'
{
  "version": "1.0.0",
  "data_sources": {
    "primary": "akshare",
    "akshare": {
      "enabled": true
    }
  },
  "news_sources": {
    "财经慢报": {
      "enabled": true
    },
    "coindesk": {
      "enabled": true
    }
  }
}
EOF
    
    echo -e "${GREEN}✅ 目录结构创建完成${NC}"
    echo -e "${YELLOW}⚠️  核心模块文件需要手动下载${NC}"
    echo ""
    echo "请从服务器下载以下文件:"
    echo "  - modules/news/fetch_financial_express.py"
    echo "  - modules/research/stock_analyzer.py"
    echo ""
fi

# 安装依赖
echo ""
echo "📦 安装 Python 依赖..."
echo ""

pip3 install --quiet akshare pandas requests beautifulsoup4 lxml 2>&1 | grep -v "already satisfied" || true

echo -e "${GREEN}✅ 必需依赖已安装${NC}"

# 询问安装可选依赖
echo ""
read -p "安装可选依赖 (Tushare, yFinance, Matplotlib)? (y/n): " install_optional

if [ "$install_optional" = "y" ]; then
    pip3 install --quiet tushare yfinance matplotlib 2>&1 | grep -v "already satisfied" || true
    echo -e "${GREEN}✅ 可选依赖已安装${NC}"
fi

# 测试
echo ""
echo "🧪 测试安装..."
cd "$INSTALL_DIR"

if [ -f "test.py" ]; then
    python3 test.py
else
    echo -e "${YELLOW}⚠️  test.py 不存在,跳过测试${NC}"
fi

# 完成
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  ✅ 安装完成!                                              ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "安装路径: $INSTALL_DIR"
echo ""
echo "快速开始:"
echo "  cd $INSTALL_DIR"
echo ""

if [ -f "modules/news/fetch_financial_express.py" ]; then
    echo "  # 测试新闻抓取"
    echo "  python3 modules/news/fetch_financial_express.py 10"
    echo ""
fi

if [ -f "modules/research/stock_analyzer.py" ]; then
    echo "  # 测试股票分析"
    echo "  python3 modules/research/stock_analyzer.py 688110"
    echo ""
fi

echo "  # 查看文档"
echo "  cat README.md"
echo ""

if [ "$download_choice" = "2" ]; then
    echo -e "${YELLOW}注意: 手动安装模式,核心文件需要额外下载!${NC}"
    echo ""
    echo "从服务器下载核心文件:"
    echo "  scp ubuntu@ip-10-0-1-120:$SERVER_PATH/modules/news/*.py $INSTALL_DIR/modules/news/"
    echo "  scp ubuntu@ip-10-0-1-120:$SERVER_PATH/modules/research/*.py $INSTALL_DIR/modules/research/"
    echo ""
fi

echo "🎉 开始使用 Financial Intelligence Agent!"
echo ""
