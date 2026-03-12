#!/usr/bin/env python3
"""
Real Stock Analysis with AKShare - 真实股票分析
完整技术分析 + 真实数据
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
import numpy as np

class RealStockAnalyzer:
    
    def __init__(self, symbol="688110"):
        self.symbol = symbol
        self.name = None
        self.current_data = None
        self.history_data = None
    
    def fetch_realtime_data(self):
        """获取实时行情"""
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
    
    def fetch_history_data(self, days=60):
        """获取历史K线数据"""
        print(f"📈 获取 {days} 天历史K线...")
        
        try:
            # 日线行情
            end_date = datetime.now().strftime('%Y%m%d')
            start_date = (datetime.now() - timedelta(days=days+30)).strftime('%Y%m%d')
            
            df = ak.stock_zh_a_hist(
                symbol=self.symbol,
                period="daily",
                start_date=start_date,
                end_date=end_date,
                adjust="qfq"  # 前复权
            )
            
            if df.empty:
                print("❌ 无历史数据")
                return False
            
            # 重命名列
            df.rename(columns={
                '日期': 'date',
                '开盘': 'open',
                '收盘': 'close',
                '最高': 'high',
                '最低': 'low',
                '成交量': 'volume',
                '成交额': 'amount',
                '振幅': 'amplitude',
                '涨跌幅': 'change_pct',
                '涨跌额': 'change',
                '换手率': 'turnover'
            }, inplace=True)
            
            self.history_data = df
            print(f"✅ 获取 {len(df)} 条历史数据\n")
            return True
            
        except Exception as e:
            print(f"❌ 历史数据获取失败: {e}")
            return False
    
    def calculate_ma(self, period=5):
        """计算移动平均线"""
        if self.history_data is None or len(self.history_data) < period:
            return None
        return self.history_data['close'].tail(period).mean()
    
    def calculate_macd(self):
        """计算MACD"""
        if self.history_data is None or len(self.history_data) < 26:
            return None
        
        closes = self.history_data['close']
        
        # EMA
        ema12 = closes.ewm(span=12, adjust=False).mean()
        ema26 = closes.ewm(span=26, adjust=False).mean()
        
        dif = ema12 - ema26
        dea = dif.ewm(span=9, adjust=False).mean()
        macd = (dif - dea) * 2
        
        return {
            'dif': round(dif.iloc[-1], 2),
            'dea': round(dea.iloc[-1], 2),
            'macd': round(macd.iloc[-1], 2)
        }
    
    def calculate_kdj(self, period=9):
        """计算KDJ"""
        if self.history_data is None or len(self.history_data) < period:
            return None
        
        df = self.history_data.tail(period).copy()
        
        low_min = df['low'].min()
        high_max = df['high'].max()
        
        close = df['close'].iloc[-1]
        
        if high_max == low_min:
            rsv = 50
        else:
            rsv = ((close - low_min) / (high_max - low_min)) * 100
        
        # 简化KDJ (实际应该递推)
        k = rsv * 2/3 + 50 * 1/3
        d = k * 2/3 + 50 * 1/3
        j = 3 * k - 2 * d
        
        return {
            'K': round(k, 2),
            'D': round(d, 2),
            'J': round(j, 2)
        }
    
    def calculate_boll(self, period=20):
        """计算布林带"""
        if self.history_data is None or len(self.history_data) < period:
            return None
        
        closes = self.history_data['close'].tail(period)
        
        middle = closes.mean()
        std = closes.std()
        
        upper = middle + 2 * std
        lower = middle - 2 * std
        
        current = self.current_data['price']
        width = (upper - lower) / middle * 100
        
        if upper != lower:
            position = (current - lower) / (upper - lower) * 100
        else:
            position = 50
        
        return {
            'upper': round(upper, 2),
            'middle': round(middle, 2),
            'lower': round(lower, 2),
            'width': round(width, 2),
            'position': round(position, 1)
        }
    
    def calculate_rsi(self, period=6):
        """计算RSI"""
        if self.history_data is None or len(self.history_data) < period + 1:
            return None
        
        closes = self.history_data['close'].tail(period + 1)
        deltas = closes.diff()[1:]
        
        gains = deltas.where(deltas > 0, 0).mean()
        losses = -deltas.where(deltas < 0, 0).mean()
        
        if losses == 0:
            return 100
        
        rs = gains / losses
        rsi = 100 - (100 / (1 + rs))
        
        return round(rsi, 1)
    
    def fetch_fund_flow(self):
        """获取资金流向"""
        print(f"💰 获取资金流向数据...")
        
        try:
            # 个股资金流
            market = "sh" if self.symbol.startswith("6") or self.symbol.startswith("68") else "sz"
            
            df = ak.stock_individual_fund_flow(stock=self.symbol, market=market)
            
            if df.empty:
                print("❌ 无资金流向数据")
                return None
            
            latest = df.iloc[-1]
            
            result = {
                '超大单': float(latest.get('超大单净流入-净额', 0)) * 10000 if '超大单净流入-净额' in latest else 0,
                '大单': float(latest.get('大单净流入-净额', 0)) * 10000 if '大单净流入-净额' in latest else 0,
                '中单': float(latest.get('中单净流入-净额', 0)) * 10000 if '中单净流入-净额' in latest else 0,
                '小单': float(latest.get('小单净流入-净额', 0)) * 10000 if '小单净流入-净额' in latest else 0,
            }
            
            result['主力合计'] = result['超大单'] + result['大单']
            
            print(f"✅ 资金流向获取成功\n")
            return result
            
        except Exception as e:
            print(f"⚠️ 资金流向获取失败: {e}")
            return None
    
    def generate_report(self):
        """生成完整分析报告"""
        
        if not self.current_data:
            print("❌ 无实时数据,无法生成报告")
            return
        
        print("\n" + "="*70)
        print(f"📊 {self.name} ({self.symbol}) - 完整技术分析报告")
        print("="*70)
        print(f"数据来源: AKShare (东方财富)")
        print(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
        
        # 实时行情
        print(f"\n## 一、实时行情\n")
        print(f"最新价: ¥{self.current_data['price']:.2f}")
        print(f"涨跌额: {self.current_data['change']:+.2f}")
        print(f"涨跌幅: {self.current_data['change_pct']:+.2f}%")
        print(f"今开: ¥{self.current_data['open']:.2f}")
        print(f"最高: ¥{self.current_data['high']:.2f}")
        print(f"最低: ¥{self.current_data['low']:.2f}")
        print(f"昨收: ¥{self.current_data['pre_close']:.2f}")
        print(f"成交量: {self.current_data['volume']:,}股")
        print(f"成交额: ¥{self.current_data['amount']/100000000:.2f}亿")
        print(f"换手率: {self.current_data['turnover']:.2f}%")
        
        if not self.history_data is None:
            # 均线
            print(f"\n## 二、均线系统\n")
            ma5 = self.calculate_ma(5)
            ma10 = self.calculate_ma(10)
            ma20 = self.calculate_ma(20)
            ma30 = self.calculate_ma(30)
            ma60 = self.calculate_ma(60)
            
            current = self.current_data['price']
            
            if ma5: print(f"MA5:  ¥{ma5:.2f} ({(current-ma5)/ma5*100:+.2f}%)")
            if ma10: print(f"MA10: ¥{ma10:.2f} ({(current-ma10)/ma10*100:+.2f}%)")
            if ma20: print(f"MA20: ¥{ma20:.2f} ({(current-ma20)/ma20*100:+.2f}%)")
            if ma30: print(f"MA30: ¥{ma30:.2f} ({(current-ma30)/ma30*100:+.2f}%)")
            if ma60: print(f"MA60: ¥{ma60:.2f} ({(current-ma60)/ma60*100:+.2f}%)")
            
            # 趋势
            if ma5 and ma10 and ma20:
                if ma5 > ma10 > ma20:
                    trend = "🟢 多头排列 (强势)"
                elif ma5 < ma10 < ma20:
                    trend = "🔴 空头排列 (弱势)"
                else:
                    trend = "🟡 震荡整理"
                print(f"\n趋势: {trend}")
            
            # MACD
            macd = self.calculate_macd()
            if macd:
                print(f"\n## 三、MACD指标\n")
                print(f"DIF: {macd['dif']}")
                print(f"DEA: {macd['dea']}")
                print(f"MACD: {macd['macd']}")
                
                if macd['dif'] > macd['dea']:
                    signal = "🟢 金叉 (看多)"
                else:
                    signal = "🔴 死叉 (看空)"
                print(f"信号: {signal}")
            
            # KDJ
            kdj = self.calculate_kdj()
            if kdj:
                print(f"\n## 四、KDJ指标\n")
                print(f"K值: {kdj['K']}")
                print(f"D值: {kdj['D']}")
                print(f"J值: {kdj['J']}")
                
                if kdj['K'] > 80 and kdj['D'] > 80:
                    signal = f"🔴 超买区 (K={kdj['K']:.1f}, D={kdj['D']:.1f}) - 警惕回调"
                elif kdj['K'] < 20 and kdj['D'] < 20:
                    signal = f"🟢 超卖区 (K={kdj['K']:.1f}, D={kdj['D']:.1f}) - 关注反弹"
                else:
                    signal = "🟡 中性区"
                print(f"信号: {signal}")
            
            # BOLL
            boll = self.calculate_boll()
            if boll:
                print(f"\n## 五、布林带 (BOLL)\n")
                print(f"上轨: ¥{boll['upper']}")
                print(f"中轨: ¥{boll['middle']}")
                print(f"下轨: ¥{boll['lower']}")
                print(f"带宽: {boll['width']:.2f}%")
                print(f"位置: {boll['position']:.1f}% (0%=下轨, 100%=上轨)")
                
                if boll['position'] > 80:
                    signal = "⚠️ 接近上轨 - 压力大"
                elif boll['position'] < 20:
                    signal = "⚠️ 接近下轨 - 支撑强"
                else:
                    signal = "🟡 中部震荡"
                print(f"信号: {signal}")
            
            # RSI
            rsi6 = self.calculate_rsi(6)
            rsi12 = self.calculate_rsi(12)
            
            if rsi6:
                print(f"\n## 六、RSI指标\n")
                print(f"RSI(6):  {rsi6}")
                print(f"RSI(12): {rsi12}")
                
                if rsi6 > 80:
                    signal = "🔴 超买 (警惕回调)"
                elif rsi6 < 20:
                    signal = "🟢 超卖 (可能反弹)"
                else:
                    signal = "🟡 中性"
                print(f"信号: {signal}")
        
        # 资金流向
        fund_flow = self.fetch_fund_flow()
        if fund_flow:
            print(f"\n## 七、资金流向 (今日)\n")
            print(f"超大单: {fund_flow['超大单']/10000:.0f}万")
            print(f"大单:   {fund_flow['大单']/10000:.0f}万")
            print(f"中单:   {fund_flow['中单']/10000:.0f}万")
            print(f"小单:   {fund_flow['小单']/10000:.0f}万")
            print(f"{'─'*40}")
            print(f"主力合计: {fund_flow['主力合计']/10000:.0f}万")
            
            if fund_flow['主力合计'] > 0:
                signal = "🟢 主力流入 (买盘强)"
            else:
                signal = "🔴 主力流出 (卖压大)"
            print(f"信号: {signal}")
        
        # 综合评分
        print(f"\n## 八、综合评分\n")
        
        score = 5.0
        reasons = []
        
        if self.history_data is not None:
            # 趋势
            ma5 = self.calculate_ma(5)
            ma10 = self.calculate_ma(10)
            if ma5 and ma10:
                if ma5 > ma10:
                    score += 1.5
                    reasons.append("✅ 短期均线向上")
                else:
                    score -= 1.5
                    reasons.append("❌ 短期均线向下")
            
            # MACD
            macd = self.calculate_macd()
            if macd:
                if macd['dif'] > macd['dea']:
                    score += 1.0
                    reasons.append("✅ MACD金叉")
                else:
                    score -= 1.0
                    reasons.append("❌ MACD死叉")
            
            # KDJ
            kdj = self.calculate_kdj()
            if kdj:
                if kdj['K'] > 80:
                    score -= 1.5
                    reasons.append("⚠️ KDJ超买")
                elif kdj['K'] < 30:
                    score += 1.5
                    reasons.append("✅ KDJ超卖反弹机会")
            
            # RSI
            rsi6 = self.calculate_rsi(6)
            if rsi6:
                if rsi6 < 30:
                    score += 1.0
                    reasons.append("✅ RSI超卖")
                elif rsi6 > 70:
                    score -= 1.0
                    reasons.append("⚠️ RSI超买")
        
        # 资金
        if fund_flow:
            if fund_flow['主力合计'] > 0:
                score += 2.0
                reasons.append("✅ 主力资金流入")
            else:
                score -= 2.0
                reasons.append("❌ 主力资金流出")
        
        score = max(0, min(10, score))
        
        stars = "⭐" * int(score)
        print(f"技术面评分: {score:.1f}/10 {stars}\n")
        
        print("评分依据:")
        for reason in reasons:
            print(f"  {reason}")
        
        # 操作建议
        print(f"\n## 九、操作建议\n")
        
        if score >= 7:
            suggestion = "✅ **买入** - 技术面强势,可逢低布局"
        elif score >= 5:
            suggestion = "⏸️ **观望** - 技术面中性,等待明确信号"
        else:
            suggestion = "❌ **回避** - 技术面弱势,建议空仓或减仓"
        
        print(suggestion)
        
        # 计算支撑压力
        if self.history_data is not None and len(self.history_data) >= 20:
            recent_high = self.history_data['high'].tail(20).max()
            recent_low = self.history_data['low'].tail(20).min()
            
            print(f"\n支撑位: ¥{recent_low:.2f}")
            print(f"压力位: ¥{recent_high:.2f}")
        
        print(f"\n{'='*70}")
        print(f"⚠️  风险提示: 技术分析仅供参考,需结合基本面和市场环境综合判断。")
        print(f"{'='*70}\n")

def main():
    symbol = sys.argv[1] if len(sys.argv) > 1 else "688110"
    
    analyzer = RealStockAnalyzer(symbol)
    
    # 获取实时数据
    if not analyzer.fetch_realtime_data():
        print("❌ 无法获取实时数据,退出")
        return
    
    # 获取历史数据
    analyzer.fetch_history_data(days=60)
    
    # 生成报告
    analyzer.generate_report()

if __name__ == "__main__":
    main()
