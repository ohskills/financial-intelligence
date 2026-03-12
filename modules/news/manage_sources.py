#!/usr/bin/env python3
"""
News Sources Manager - 新闻源管理
允许用户启用/禁用新闻源,查看可用源列表
"""

import json
import os
import sys

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'sources_config.json')

def load_config():
    """加载配置"""
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_config(config):
    """保存配置"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def list_sources(show_all=False):
    """列出新闻源"""
    config = load_config()
    
    print("\n" + "="*80)
    print("📰 可用新闻源列表")
    print("="*80)
    print()
    
    # 按市场分组
    markets = {}
    for source in config['sources']:
        market = source.get('market', 'other')
        if market not in markets:
            markets[market] = []
        markets[market].append(source)
    
    market_names = {
        'global': '🌍 全球',
        'china': '🇨🇳 中国',
        'us': '🇺🇸 美国',
        'hk': '🇭🇰 香港',
        'crypto': '₿ 加密货币',
        'other': '📰 其他'
    }
    
    total_enabled = 0
    total_free = 0
    
    for market, sources in sorted(markets.items()):
        print(f"\n## {market_names.get(market, market)}\n")
        print(f"{'ID':<20} {'名称':<20} {'状态':<8} {'费用':<8} {'描述'}")
        print("-" * 80)
        
        for source in sources:
            if not show_all and not source.get('enabled', False):
                continue
            
            status = "✅ 已启用" if source.get('enabled', False) else "⚪ 未启用"
            free = "免费" if source.get('free', True) else "付费"
            
            name = source.get('name', source['id'])
            desc = source.get('description', '')[:30]
            
            print(f"{source['id']:<20} {name:<20} {status:<8} {free:<8} {desc}")
            
            if source.get('enabled', False):
                total_enabled += 1
            if source.get('free', True):
                total_free += 1
    
    print("\n" + "="*80)
    print(f"📊 统计: 总计 {len(config['sources'])} 个新闻源")
    print(f"  - ✅ 已启用: {total_enabled}")
    print(f"  - 💰 免费: {total_free}")
    print(f"  - 💳 付费: {len(config['sources']) - total_free}")
    print("="*80)
    print()

def enable_source(source_id):
    """启用新闻源"""
    config = load_config()
    
    for source in config['sources']:
        if source['id'] == source_id:
            source['enabled'] = True
            
            # 更新用户偏好
            if source_id not in config['user_preferences']['enabled_sources']:
                config['user_preferences']['enabled_sources'].append(source_id)
            
            save_config(config)
            print(f"✅ 已启用: {source.get('name', source_id)}")
            
            # 提示依赖
            if source.get('requires_subscription'):
                print(f"⚠️  需要订阅: {source.get('description', '')}")
            if source.get('requires_scraping'):
                print(f"⚠️  需要爬虫,可能不稳定")
            if source.get('requires_vip'):
                print(f"⚠️  需要 VIP 会员")
            
            return True
    
    print(f"❌ 未找到新闻源: {source_id}")
    return False

def disable_source(source_id):
    """禁用新闻源"""
    config = load_config()
    
    for source in config['sources']:
        if source['id'] == source_id:
            source['enabled'] = False
            
            # 更新用户偏好
            if source_id in config['user_preferences']['enabled_sources']:
                config['user_preferences']['enabled_sources'].remove(source_id)
            
            save_config(config)
            print(f"⚪ 已禁用: {source.get('name', source_id)}")
            return True
    
    print(f"❌ 未找到新闻源: {source_id}")
    return False

def show_source_details(source_id):
    """显示新闻源详情"""
    config = load_config()
    
    for source in config['sources']:
        if source['id'] == source_id:
            print("\n" + "="*60)
            print(f"📰 {source.get('name', source_id)}")
            print("="*60)
            print(f"ID: {source['id']}")
            print(f"类型: {source.get('type', 'unknown')}")
            print(f"市场: {source.get('market', 'unknown')}")
            print(f"语言: {source.get('language', 'unknown')}")
            print(f"更新频率: {source.get('update_frequency', 'unknown')}")
            print(f"状态: {'✅ 已启用' if source.get('enabled') else '⚪ 未启用'}")
            print(f"费用: {'免费' if source.get('free', True) else '付费'}")
            print(f"\n描述: {source.get('description', '无')}")
            print(f"\nURL: {source.get('url', '无')}")
            
            if source.get('rss_url'):
                print(f"RSS: {source['rss_url']}")
            if source.get('api_url'):
                print(f"API: {source['api_url']}")
            
            if source.get('categories'):
                print(f"\n分类: {', '.join(source['categories'])}")
            
            if source.get('requires_subscription'):
                print(f"\n⚠️  需要订阅")
            if source.get('requires_scraping'):
                print(f"⚠️  需要爬虫")
            if source.get('requires_vip'):
                print(f"⚠️  需要 VIP")
            
            print("="*60)
            print()
            return True
    
    print(f"❌ 未找到新闻源: {source_id}")
    return False

def setup_wizard():
    """配置向导"""
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║  新闻源配置向导                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    config = load_config()
    
    print("推荐配置 (免费 + 实时):\n")
    
    recommended = [
        ('financial_express', '财经慢报', 'Telegram实时快讯,中文'),
        ('coindesk', 'CoinDesk', '加密货币权威,英文'),
        ('cointelegraph', 'Cointelegraph', '加密货币社区,英文'),
        ('eastmoney', '东方财富', 'A股门户,中文'),
        ('reuters', 'Reuters', '路透社全球新闻,英文')
    ]
    
    for i, (source_id, name, desc) in enumerate(recommended, 1):
        print(f"{i}. {name:<20} - {desc}")
    
    print()
    choice = input("选择要启用的源 (例如: 1,2,3 或 all 全选): ").strip()
    
    if choice.lower() == 'all':
        for source_id, _, _ in recommended:
            enable_source(source_id)
    else:
        try:
            indices = [int(x.strip()) for x in choice.split(',')]
            for idx in indices:
                if 1 <= idx <= len(recommended):
                    source_id = recommended[idx-1][0]
                    enable_source(source_id)
        except:
            print("❌ 输入无效")
    
    print("\n✅ 配置完成!")
    print("\n查看已启用的源:")
    list_sources(show_all=False)

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='新闻源管理工具')
    parser.add_argument('action', nargs='?', default='list',
                       choices=['list', 'enable', 'disable', 'info', 'setup'],
                       help='操作: list/enable/disable/info/setup')
    parser.add_argument('source_id', nargs='?', help='新闻源 ID')
    parser.add_argument('--all', action='store_true', help='显示所有源 (包括未启用)')
    
    args = parser.parse_args()
    
    if args.action == 'list':
        list_sources(show_all=args.all)
    
    elif args.action == 'enable':
        if not args.source_id:
            print("❌ 请指定新闻源 ID")
            sys.exit(1)
        enable_source(args.source_id)
    
    elif args.action == 'disable':
        if not args.source_id:
            print("❌ 请指定新闻源 ID")
            sys.exit(1)
        disable_source(args.source_id)
    
    elif args.action == 'info':
        if not args.source_id:
            print("❌ 请指定新闻源 ID")
            sys.exit(1)
        show_source_details(args.source_id)
    
    elif args.action == 'setup':
        setup_wizard()

if __name__ == "__main__":
    main()
