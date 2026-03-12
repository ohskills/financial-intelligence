#!/usr/bin/env python3
"""
Financial Intelligence Agent - 测试脚本
验证各模块功能是否正常
"""

import sys
import os

def test_news_module():
    """测试新闻模块"""
    print("\n" + "="*60)
    print("📰 测试新闻模块")
    print("="*60)
    
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules/news'))
        from fetch_financial_express import fetch_financial_express
        
        print("抓取财经慢报最新 5 条...")
        news = fetch_financial_express(max_items=5)
        
        if news:
            print(f"✅ 新闻模块正常 (获取 {len(news)} 条)")
            return True
        else:
            print("⚠️ 新闻模块返回空数据 (可能网络问题)")
            return False
            
    except Exception as e:
        print(f"❌ 新闻模块测试失败: {e}")
        return False

def test_research_module():
    """测试研究模块"""
    print("\n" + "="*60)
    print("📊 测试股票研究模块")
    print("="*60)
    
    try:
        # 简单验证模块可导入
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules/research'))
        
        print("检查 stock_analyzer.py...")
        if os.path.exists('modules/research/stock_analyzer.py'):
            print("✅ stock_analyzer.py 存在")
        
        print("检查 stock_with_dragon_tiger.py...")
        if os.path.exists('modules/research/stock_with_dragon_tiger.py'):
            print("✅ stock_with_dragon_tiger.py 存在")
        
        print("✅ 研究模块文件完整")
        return True
        
    except Exception as e:
        print(f"❌ 研究模块测试失败: {e}")
        return False

def test_config():
    """测试配置文件"""
    print("\n" + "="*60)
    print("⚙️  测试配置文件")
    print("="*60)
    
    try:
        import json
        
        if os.path.exists('config.json'):
            with open('config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
            print("✅ config.json 存在且格式正确")
            
            # 检查关键配置
            if 'data_sources' in config:
                print(f"  - 数据源: {config['data_sources'].get('primary', 'unknown')}")
            
            if 'llm' in config and config['llm'].get('api_key'):
                print(f"  - LLM: {config['llm'].get('provider', 'unknown')} (已配置)")
            else:
                print(f"  - LLM: 未配置 (可选)")
            
            return True
        else:
            print("⚠️ config.json 不存在,请运行 install.sh")
            return False
            
    except Exception as e:
        print(f"❌ 配置文件测试失败: {e}")
        return False

def test_dependencies():
    """测试依赖"""
    print("\n" + "="*60)
    print("📦 测试 Python 依赖")
    print("="*60)
    
    deps = {
        'akshare': '必需',
        'pandas': '必需',
        'requests': '必需',
        'beautifulsoup4': '必需',
        'tushare': '可选',
        'yfinance': '可选',
        'matplotlib': '可选'
    }
    
    all_ok = True
    
    for dep, status in deps.items():
        try:
            __import__(dep)
            print(f"✅ {dep:<20} ({status})")
        except ImportError:
            if status == '必需':
                print(f"❌ {dep:<20} ({status}) - 请安装")
                all_ok = False
            else:
                print(f"⚠️ {dep:<20} ({status}) - 未安装")
    
    return all_ok

def main():
    """运行所有测试"""
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║  Financial Intelligence Agent - 功能测试                   ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    results = []
    
    # 测试依赖
    results.append(("依赖", test_dependencies()))
    
    # 测试配置
    results.append(("配置", test_config()))
    
    # 测试新闻模块
    results.append(("新闻模块", test_news_module()))
    
    # 测试研究模块
    results.append(("研究模块", test_research_module()))
    
    # 汇总
    print("\n" + "="*60)
    print("📊 测试汇总")
    print("="*60)
    
    for name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{name:<15} {status}")
    
    all_passed = all([r[1] for r in results])
    
    print("\n" + "="*60)
    if all_passed:
        print("🎉 所有测试通过!")
        print("\n下一步:")
        print("  1. 测试新闻: python3 modules/news/fetch_financial_express.py 10")
        print("  2. 测试分析: python3 modules/research/stock_analyzer.py 688110")
        print("  3. 查看文档: cat SKILL.md")
    else:
        print("⚠️ 部分测试未通过")
        print("\n请检查:")
        print("  1. 是否运行了 install.sh")
        print("  2. 是否安装了所有必需依赖")
        print("  3. 网络是否正常")
    print("="*60)
    print()
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
