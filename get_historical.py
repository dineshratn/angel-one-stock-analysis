#!/usr/bin/env python3
"""
Get historical data for Reliance Industries
"""
import yfinance as yf
import pandas as pd

def main():
    symbol = "RELIANCE.NS"

    print(f"Fetching historical data for {symbol}...")
    print()

    try:
        ticker = yf.Ticker(symbol)

        # Get different timeframes
        hist_1m = ticker.history(period="1mo", interval="1d")
        hist_3m = ticker.history(period="3mo", interval="1d")
        hist_1y = ticker.history(period="1y", interval="1wk")

        print("=" * 80)
        print("RELIANCE INDUSTRIES - HISTORICAL PRICE ANALYSIS")
        print("=" * 80)
        print()

        # 1 Month Analysis
        print("📅 LAST 1 MONTH (Daily)")
        print("-" * 80)
        if not hist_1m.empty:
            first_price = hist_1m.iloc[0]['Close']
            last_price = hist_1m.iloc[-1]['Close']
            change = last_price - first_price
            change_pct = (change / first_price) * 100

            print(f"Starting Price:      ₹{first_price:.2f}")
            print(f"Current Price:       ₹{last_price:.2f}")
            print(f"1-Month Change:      ₹{change:.2f} ({change_pct:+.2f}%)")
            print(f"1-Month High:        ₹{hist_1m['High'].max():.2f}")
            print(f"1-Month Low:         ₹{hist_1m['Low'].min():.2f}")
            print(f"Avg Volume (1M):     {hist_1m['Volume'].mean():,.0f} shares")

            # Moving averages
            hist_1m['SMA_5'] = hist_1m['Close'].rolling(window=5).mean()
            hist_1m['SMA_20'] = hist_1m['Close'].rolling(window=20).mean()

            if not hist_1m['SMA_5'].isna().all() and not hist_1m['SMA_20'].isna().all():
                sma_5 = hist_1m['SMA_5'].iloc[-1]
                sma_20 = hist_1m['SMA_20'].iloc[-1]
                print(f"5-Day MA:            ₹{sma_5:.2f}")
                print(f"20-Day MA:           ₹{sma_20:.2f}")

                if last_price > sma_5 > sma_20:
                    print(f"Trend:               STRONG UPTREND ↑↑")
                elif last_price > sma_20:
                    print(f"Trend:               UPTREND ↑")
                elif last_price < sma_5 < sma_20:
                    print(f"Trend:               STRONG DOWNTREND ↓↓")
                elif last_price < sma_20:
                    print(f"Trend:               DOWNTREND ↓")
                else:
                    print(f"Trend:               SIDEWAYS →")
        print()

        # 3 Month Analysis
        print("📅 LAST 3 MONTHS")
        print("-" * 80)
        if not hist_3m.empty:
            first_price = hist_3m.iloc[0]['Close']
            last_price = hist_3m.iloc[-1]['Close']
            change = last_price - first_price
            change_pct = (change / first_price) * 100

            print(f"3-Month Change:      ₹{change:.2f} ({change_pct:+.2f}%)")
            print(f"3-Month High:        ₹{hist_3m['High'].max():.2f}")
            print(f"3-Month Low:         ₹{hist_3m['Low'].min():.2f}")
            print(f"Avg Volume (3M):     {hist_3m['Volume'].mean():,.0f} shares")
        print()

        # 1 Year Analysis
        print("📅 LAST 1 YEAR (Weekly)")
        print("-" * 80)
        if not hist_1y.empty:
            first_price = hist_1y.iloc[0]['Close']
            last_price = hist_1y.iloc[-1]['Close']
            change = last_price - first_price
            change_pct = (change / first_price) * 100

            print(f"1-Year Change:       ₹{change:.2f} ({change_pct:+.2f}%)")
            print(f"1-Year High:         ₹{hist_1y['High'].max():.2f}")
            print(f"1-Year Low:          ₹{hist_1y['Low'].min():.2f}")

            # Volatility (standard deviation)
            volatility = hist_1y['Close'].pct_change().std() * 100
            print(f"Volatility (1Y):     {volatility:.2f}%")
        print()

        # Recent 5-day trend
        print("📊 LAST 5 TRADING DAYS")
        print("-" * 80)
        recent = hist_1m.tail(5)[['Open', 'High', 'Low', 'Close', 'Volume']]
        recent['Change %'] = recent['Close'].pct_change() * 100

        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.float_format', lambda x: f'₹{x:,.2f}' if x > 100 else f'{x:.2f}%')

        print(recent.to_string())
        print()

        # Support and Resistance levels
        print("🎯 KEY LEVELS (Based on Recent History)")
        print("-" * 80)

        # Calculate pivot points from last day
        last_day = hist_1m.iloc[-1]
        pivot = (last_day['High'] + last_day['Low'] + last_day['Close']) / 3
        r1 = 2 * pivot - last_day['Low']
        s1 = 2 * pivot - last_day['High']
        r2 = pivot + (last_day['High'] - last_day['Low'])
        s2 = pivot - (last_day['High'] - last_day['Low'])

        print(f"Resistance 2 (R2):   ₹{r2:.2f}")
        print(f"Resistance 1 (R1):   ₹{r1:.2f}")
        print(f"Pivot Point:         ₹{pivot:.2f}")
        print(f"Support 1 (S1):      ₹{s1:.2f}")
        print(f"Support 2 (S2):      ₹{s2:.2f}")
        print()

        # Performance summary
        print("📈 PERFORMANCE SUMMARY")
        print("-" * 80)

        # Count up/down days
        hist_1m['Daily_Change'] = hist_1m['Close'].pct_change()
        up_days = (hist_1m['Daily_Change'] > 0).sum()
        down_days = (hist_1m['Daily_Change'] < 0).sum()

        print(f"Up Days (1M):        {up_days} days")
        print(f"Down Days (1M):      {down_days} days")
        print(f"Win Rate:            {(up_days/(up_days+down_days)*100):.1f}%")

        # Largest gain/loss
        max_gain = hist_1m['Daily_Change'].max() * 100
        max_loss = hist_1m['Daily_Change'].min() * 100
        print(f"Largest Gain:        {max_gain:.2f}%")
        print(f"Largest Loss:        {max_loss:.2f}%")

        print()
        print("=" * 80)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
