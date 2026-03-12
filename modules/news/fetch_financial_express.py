#!/usr/bin/env python3
"""
财经慢报 Telegram 新闻抓取
支持 https://t.me/Financial_Express
"""

import sys
import re
from datetime import datetime

def fetch_financial_express(url="https://t.me/s/Financial_Express", max_items=20):
    """
    抓取财经慢报 Telegram 频道
    """
    print(f"📰 抓取财经慢报: {url}\n")
    
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("📦 安装依赖...")
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4", "lxml", "--break-system-packages", "-q"])
        import requests
        from bs4 import BeautifulSoup
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"❌ 请求失败: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        # 查找所有消息
        messages = soup.find_all('div', class_='tgme_widget_message')
        
        news_items = []
        
        for msg in messages[:max_items]:
            try:
                # 提取文本
                text_div = msg.find('div', class_='tgme_widget_message_text')
                if not text_div:
                    continue
                
                text = text_div.get_text(strip=True, separator='\n')
                
                # 提取时间
                time_tag = msg.find('time')
                time_str = time_tag.get('datetime') if time_tag else None
                
                # 提取链接
                link_tag = msg.find('a', class_='tgme_widget_message_date')
                link = link_tag.get('href') if link_tag else None
                
                news_items.append({
                    'text': text,
                    'time': time_str,
                    'link': link
                })
                
            except Exception as e:
                continue
        
        print(f"✅ 成功抓取 {len(news_items)} 条新闻\n")
        return news_items
        
    except Exception as e:
        print(f"❌ 抓取失败: {e}")
        return []

def categorize_news(text):
    """新闻分类"""
    categories = []
    
    # 地缘政治
    if any(keyword in text for keyword in ['伊朗', '以色列', '俄罗斯', '乌克兰', '台湾', '朝鲜', '战争', '冲突', '制裁']):
        categories.append('🌍 地缘政治')
    
    # 加密货币
    if any(keyword in text for keyword in ['比特币', 'BTC', '以太坊', 'ETH', '加密货币', 'Crypto', 'DeFi', 'NFT']):
        categories.append('₿ 加密货币')
    
    # 美股
    if any(keyword in text for keyword in ['美股', '纳指', '道指', '标普', 'Tesla', 'Apple', 'NVIDIA', '特斯拉']):
        categories.append('🇺🇸 美股')
    
    # A股
    if any(keyword in text for keyword in ['A股', '沪指', '深指', '创业板', '科创板', '北向资金']):
        categories.append('🇨🇳 A股')
    
    # 央行货币政策
    if any(keyword in text for keyword in ['央行', '美联储', 'Fed', '加息', '降息', 'CPI', 'GDP', '通胀']):
        categories.append('💰 货币政策')
    
    # 能源商品
    if any(keyword in text for keyword in ['原油', '黄金', '白银', '天然气', '铜', '大宗商品']):
        categories.append('🛢️ 能源商品')
    
    # 科技
    if any(keyword in text for keyword in ['AI', '人工智能', 'ChatGPT', '芯片', '半导体', '云计算']):
        categories.append('🤖 科技')
    
    # 公司动态
    if any(keyword in text for keyword in ['IPO', '财报', '业绩', '并购', '增持', '减持', '回购']):
        categories.append('🏢 公司动态')
    
    return categories if categories else ['📰 综合']

def assess_importance(text):
    """评估重要性 (1-10分)"""
    score = 5  # 基准分
    
    # 关键词加分
    high_priority = ['突发', '重大', '暴涨', '暴跌', '熔断', '紧急', 'Breaking', 'ALERT']
    if any(kw in text for kw in high_priority):
        score += 3
    
    # 央行/政策
    if any(kw in text for kw in ['央行', '美联储', '财政部', '证监会', '政策']):
        score += 2
    
    # 大公司/大事件
    if any(kw in text for kw in ['苹果', 'Apple', '特斯拉', 'Tesla', 'NVIDIA', '微软', '谷歌']):
        score += 1
    
    # 数字越大越重要
    if re.search(r'[+\-]\d{1,2}%', text):  # 涨跌幅
        score += 1
    
    if re.search(r'\d+亿|十亿|百亿|千亿', text):  # 大额资金
        score += 1
    
    return min(10, max(1, score))

def format_news_report(news_items):
    """生成新闻报告"""
    if not news_items:
        print("❌ 无新闻数据")
        return
    
    print("="*70)
    print("📰 财经慢报 - 实时快讯")
    print("="*70)
    print(f"数据来源: https://t.me/Financial_Express")
    print(f"抓取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"新闻数量: {len(news_items)}条")
    print("="*70)
    print()
    
    # 按分类整理
    categorized = {}
    
    for idx, item in enumerate(news_items, 1):
        text = item['text']
        categories = categorize_news(text)
        importance = assess_importance(text)
        
        for category in categories:
            if category not in categorized:
                categorized[category] = []
            
            categorized[category].append({
                'index': idx,
                'text': text,
                'importance': importance,
                'time': item['time'],
                'link': item['link']
            })
    
    # 按分类输出
    for category, items in sorted(categorized.items()):
        print(f"## {category}\n")
        
        # 按重要性排序
        items.sort(key=lambda x: x['importance'], reverse=True)
        
        for item in items:
            # 格式化时间
            if item['time']:
                try:
                    dt = datetime.fromisoformat(item['time'].replace('Z', '+00:00'))
                    time_str = dt.strftime('%m-%d %H:%M')
                except:
                    time_str = ""
            else:
                time_str = ""
            
            # 输出
            importance_stars = "⭐" * min(item['importance'], 5)
            print(f"**[{item['index']}] {importance_stars}** ({time_str})")
            
            # 分段显示文本
            lines = item['text'].split('\n')
            for line in lines[:5]:  # 最多显示5行
                if line.strip():
                    print(f"  {line.strip()}")
            
            if len(lines) > 5:
                print(f"  ... (共{len(lines)}行)")
            
            if item['link']:
                print(f"  🔗 {item['link']}")
            
            print()
        
        print()
    
    print("="*70)
    print("📊 分类统计:")
    for category, items in sorted(categorized.items()):
        print(f"  {category}: {len(items)}条")
    print("="*70)

def main():
    max_items = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    
    # 抓取新闻
    news_items = fetch_financial_express(max_items=max_items)
    
    # 生成报告
    format_news_report(news_items)

if __name__ == "__main__":
    main()
