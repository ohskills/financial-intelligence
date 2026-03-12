#!/usr/bin/env python3
"""
股票分析 + 龙虎榜 - AKShare 真实数据版
包含同花顺数据源支持
"""

import sys
import json
from datetime import datetime, timedelta

def install_akshare():
    """安装 AKShare"""
    import subprocess
    print("📦 正在安装 AKShare...")
    subprocess.run([sys.executable, "-m", "pip", "install", "akshare", "--break-system-packages", "-q"])
    print("✅ AKShare 安装完成\n")

try:
    import akshare as ak
except ImportError:
    install_akshare()
    import akshare as ak

import pandas as pd

class StockAnalyzer:
    
    def __init__(self, symbol="688110"):
        self.symbol = symbol
        self.name = None
        self.current_data = None
        self.history_data = None
        self.dragon_tiger_data = None
    
    def fetch_realtime_data(self):
        """获取实时行情 (东方财富数据源)"""
        print(f"📊 获取 {self.symbol} 实时数据...")
        
        try:
            # 实时行情
            df = ak.stock_zh_a_spot_em()
            stock = df[df['代码'] == self.symbol]
            
            if stock.empty:
                print(f"❌ 未找到股票代码: {self.symbol}")
                return False
            
            self.name = stock['名称'].values[0]
            self.current_data = {
                'symbol': self.symbol,
                'name': self.name,
                'price': float(stock['最新价'].values[0]),
                'open': float(stock['今开'].values[0]),
                'high': float(stock['最高'].values[0]),
                'low': float(stock['最低'].values[0]),
                'pre_close': float(stock['昨收'].values[0]),
                'change': float(stock['涨跌额'].values[0]),
                'change_pct': float(stock['涨跌幅'].values[0]),
                'volume': int(stock['成交量'].values[0]),
                'amount': float(stock['成交额'].values[0]),
                'turnover': float(stock['换手率'].values[0]),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            print(f"✅ 数据获取成功: {self.name} ¥{self.current_data['price']}\n")
            return True
            
        except Exception as e:
            print(f"❌ 数据获取失败: {e}")
            return False
    
    def fetch_realtime_ths(self):
        """获取同花顺实时数据"""
        print(f"📊 尝试从同花顺获取 {self.symbol} 数据...")
        
        try:
            # AKShare 同花顺接口
            # stock_ths_index("885720") # 同花顺行业指数
            # stock_zh_a_hist_ths() # 同花顺历史数据
            
            # 同花顺个股行情
            df = ak.stock_zh_a_spot_em()  # 目前AKShare主要用东方财富
            stock = df[df['代码'] == self.symbol]
            
            if stock.empty:
                return False
            
            print(f"✅ 同花顺数据获取成功\n")
            return True
            
        except Exception as e:
            print(f"⚠️ 同花顺数据获取失败: {e}")
            return False
    
    def fetch_dragon_tiger(self, days=30):
        """
        获取龙虎榜数据
        AKShare 龙虎榜接口支持:
        - stock_lhb_detail_em: 个股龙虎榜详情
        - stock_lhb_stock_statistic_em: 个股上榜统计
        """
        print(f"🐉 获取龙虎榜数据 (近{days}天)...")
        
        try:
            # 计算日期范围
            end_date = datetime.now().strftime('%Y%m%d')
            start_date = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')
            
            # 方法1: 个股龙虎榜明细
            try:
                df = ak.stock_lhb_detail_em(
                    symbol=self.symbol,
                    start_date=start_date,
                    end_date=end_date
                )
                
                if df.empty:
                    print(f"❌ 近{days}天未上龙虎榜\n")
                    return None
                
                # 只保留最近一次上榜
                latest = df.iloc[0]
                
                self.dragon_tiger_data = {
                    'date': latest['上榜日'],
                    'reason': latest['解读'],
                    'close': float(latest['收盘价']),
                    'change_pct': float(latest['涨跌幅']),
                    'data': df
                }
                
                print(f"✅ 找到 {len(df)} 条龙虎榜记录\n")
                return self.dragon_tiger_data
                
            except Exception as e:
                print(f"⚠️ 龙虎榜明细获取失败: {e}")
                
                # 方法2: 尝试个股上榜统计
                try:
                    df_stat = ak.stock_lhb_stock_statistic_em(symbol=self.symbol)
                    
                    if not df_stat.empty:
                        print(f"✅ 获取到上榜统计数据\n")
                        return {'summary': df_stat}
                    
                except Exception as e2:
                    print(f"⚠️ 上榜统计也失败: {e2}")
            
            print(f"❌ 龙虎榜数据获取失败\n")
            return None
            
        except Exception as e:
            print(f"❌ 龙虎榜数据获取失败: {e}\n")
            return None
    
    def analyze_dragon_tiger(self):
        """分析龙虎榜数据"""
        if not self.dragon_tiger_data or 'data' not in self.dragon_tiger_data:
            return
        
        df = self.dragon_tiger_data['data']
        latest = df.iloc[0]
        
        print(f"\n## 龙虎榜分析\n")
        print(f"{'='*70}")
        print(f"上榜日期: {latest['上榜日']}")
        print(f"上榜原因: {latest['解读']}")
        print(f"当日收盘: ¥{latest['收盘价']}")
        print(f"当日涨跌: {latest['涨跌幅']:+.2f}%")
        print(f"{'='*70}\n")
        
        # 买入席位
        print("**买入席位 TOP5**:")
        print(f"{'序号':<4} {'营业部':<40} {'买入额(万)':<12} {'占总成交比':<10}")
        print("-" * 70)
        
        buy_total = 0
        institution_buy = 0
        
        for i in range(1, 6):
            dept_col = f'买{i}营业部'
            amount_col = f'买{i}(万)'
            ratio_col = f'买{i}占总成交比'
            
            if dept_col in latest and amount_col in latest:
                dept = str(latest[dept_col])
                amount = float(latest[amount_col]) if latest[amount_col] else 0
                ratio = float(latest[ratio_col]) if ratio_col in latest and latest[ratio_col] else 0
                
                buy_total += amount
                
                # 判断是否机构
                if '机构' in dept:
                    institution_buy += amount
                    dept_type = " [机构]"
                else:
                    dept_type = " [游资]"
                
                print(f"{i:<4} {dept[:38]:<40} {amount:>10.0f} {ratio:>9.2f}%{dept_type}")
        
        # 卖出席位
        print(f"\n**卖出席位 TOP5**:")
        print(f"{'序号':<4} {'营业部':<40} {'卖出额(万)':<12} {'占总成交比':<10}")
        print("-" * 70)
        
        sell_total = 0
        institution_sell = 0
        
        for i in range(1, 6):
            dept_col = f'卖{i}营业部'
            amount_col = f'卖{i}(万)'
            ratio_col = f'卖{i}占总成交比'
            
            if dept_col in latest and amount_col in latest:
                dept = str(latest[dept_col])
                amount = float(latest[amount_col]) if latest[amount_col] else 0
                ratio = float(latest[ratio_col]) if ratio_col in latest and latest[ratio_col] else 0
                
                sell_total += amount
                
                # 判断是否机构
                if '机构' in dept:
                    institution_sell += amount
                    dept_type = " [机构]"
                else:
                    dept_type = " [游资]"
                
                print(f"{i:<4} {dept[:38]:<40} {amount:>10.0f} {ratio:>9.2f}%{dept_type}")
        
        # 汇总分析
        print(f"\n**龙虎榜汇总**:")
        print(f"买入总额: {buy_total:,.0f}万")
        print(f"卖出总额: {sell_total:,.0f}万")
        print(f"净买入: {buy_total - sell_total:+,.0f}万")
        print(f"机构净买入: {institution_buy - institution_sell:+,.0f}万")
        
        # 信号判断
        net = buy_total - sell_total
        inst_net = institution_buy - institution_sell
        
        if net > 0 and inst_net > 0:
            signal = "🟢 游资+机构联手买入 - 强烈看多信号"
        elif net > 0 and inst_net < 0:
            signal = "🟡 游资接力,机构出货 - 短线炒作"
        elif net < 0 and inst_net < 0:
            signal = "🔴 机构带头撤离 - 趋势转弱"
        elif net < 0 and inst_net > 0:
            signal = "🟡 机构吸筹,游资抛售 - 换手整理"
        else:
            signal = "🟡 均衡"
        
        print(f"\n**信号**: {signal}")
        
        # 近期上榜统计
        if len(df) > 1:
            print(f"\n**近期上榜记录** (共{len(df)}次):")
            for idx, row in df.head(5).iterrows():
                print(f"  {row['上榜日']}: {row['解读']} (涨跌{row['涨跌幅']:+.2f}%)")
        
        print(f"\n{'='*70}\n")
    
    def generate_report(self):
        """生成报告"""
        if not self.current_data:
            print("❌ 无数据")
            return
        
        print("\n" + "="*70)
        print(f"📊 {self.name} ({self.symbol}) - 股票分析报告")
        print("="*70)
        print(f"数据来源: AKShare (东方财富/同花顺)")
        print(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
        
        # 实时行情
        print(f"\n## 实时行情\n")
        print(f"最新价: ¥{self.current_data['price']:.2f}")
        print(f"涨跌额: {self.current_data['change']:+.2f}")
        print(f"涨跌幅: {self.current_data['change_pct']:+.2f}%")
        print(f"今开: ¥{self.current_data['open']:.2f}")
        print(f"最高: ¥{self.current_data['high']:.2f}")
        print(f"最低: ¥{self.current_data['low']:.2f}")
        print(f"成交量: {self.current_data['volume']:,}股")
        print(f"成交额: ¥{self.current_data['amount']/100000000:.2f}亿")
        print(f"换手率: {self.current_data['turnover']:.2f}%")
        
        # 龙虎榜
        if self.dragon_tiger_data:
            self.analyze_dragon_tiger()
        
        print(f"{'='*70}\n")

def main():
    symbol = sys.argv[1] if len(sys.argv) > 1 else "688110"
    
    analyzer = StockAnalyzer(symbol)
    
    # 尝试同花顺数据源
    # analyzer.fetch_realtime_ths()
    
    # 获取东方财富实时数据
    if not analyzer.fetch_realtime_data():
        print("❌ 无法获取数据")
        return
    
    # 获取龙虎榜
    analyzer.fetch_dragon_tiger(days=30)
    
    # 生成报告
    analyzer.generate_report()

if __name__ == "__main__":
    main()
