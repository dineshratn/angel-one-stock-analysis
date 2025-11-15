#!/usr/bin/env python3
"""
Gold ETF Detailed Analysis
Compare and analyze all Indian Gold ETFs
"""

import sys
import os
from datetime import datetime, timedelta

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    import yfinance as yf
    import pandas as pd
    import numpy as np
except ImportError:
    print("Error: Required libraries not installed")
    print("Run: pip install yfinance pandas numpy")
    sys.exit(1)


# Gold ETFs
GOLD_ETFS = {
    "GOLDSHARE.NS": {
        "name": "Nippon India ETF Gold BeES",
        "amc": "Nippon India",
        "launch_year": 2014,
        "aum": "₹6,500+ Cr",
        "expense_ratio": "1.00%",
        "tracking": "Domestic Gold Price"
    },
    "GOLDBEES.NS": {
        "name": "Nippon India ETF Gold BeES (Old)",
        "amc": "Nippon India",
        "launch_year": 2007,
        "aum": "₹2,000+ Cr",
        "expense_ratio": "1.00%",
        "tracking": "Domestic Gold Price"
    },
    "HDFCGOLD.NS": {
        "name": "HDFC Gold ETF",
        "amc": "HDFC Mutual Fund",
        "launch_year": 2010,
        "aum": "₹500+ Cr",
        "expense_ratio": "1.00%",
        "tracking": "Domestic Gold Price"
    },
}


def get_gold_etf_data():
    """Fetch detailed data for all gold ETFs"""
    print("=" * 100)
    print("GOLD ETF COMPREHENSIVE ANALYSIS")
    print("=" * 100)
    print(f"\nFetching data for {len(GOLD_ETFS)} Gold ETFs...\n")

    etf_data = []

    for symbol, info in GOLD_ETFS.items():
        try:
            print(f"Analyzing {symbol}...")
            ticker = yf.Ticker(symbol)

            # Get current data
            hist_1d = ticker.history(period="1d")
            if hist_1d.empty:
                print(f"  ⚠️  No recent data")
                continue

            latest = hist_1d.iloc[-1]

            # Get historical data for analysis
            hist_1w = ticker.history(period="5d")
            hist_1m = ticker.history(period="1mo")
            hist_3m = ticker.history(period="3mo")
            hist_6m = ticker.history(period="6mo")
            hist_1y = ticker.history(period="1y")
            hist_3y = ticker.history(period="3y")

            # Calculate returns
            returns = {}
            if len(hist_1w) >= 5:
                returns['1w'] = ((latest['Close'] - hist_1w.iloc[0]['Close']) / hist_1w.iloc[0]['Close'] * 100)
            if len(hist_1m) >= 20:
                returns['1m'] = ((latest['Close'] - hist_1m.iloc[0]['Close']) / hist_1m.iloc[0]['Close'] * 100)
            if len(hist_3m) >= 60:
                returns['3m'] = ((latest['Close'] - hist_3m.iloc[0]['Close']) / hist_3m.iloc[0]['Close'] * 100)
            if len(hist_6m) >= 120:
                returns['6m'] = ((latest['Close'] - hist_6m.iloc[0]['Close']) / hist_6m.iloc[0]['Close'] * 100)
            if len(hist_1y) >= 200:
                returns['1y'] = ((latest['Close'] - hist_1y.iloc[0]['Close']) / hist_1y.iloc[0]['Close'] * 100)
            if len(hist_3y) >= 600:
                returns['3y'] = ((latest['Close'] - hist_3y.iloc[0]['Close']) / hist_3y.iloc[0]['Close'] * 100)

            # Volatility (annualized standard deviation)
            if len(hist_1y) > 1:
                daily_returns = hist_1y['Close'].pct_change().dropna()
                volatility = daily_returns.std() * np.sqrt(252) * 100  # Annualized
            else:
                volatility = 0

            # 52-week stats
            week_52_high = hist_1y['High'].max() if not hist_1y.empty else 0
            week_52_low = hist_1y['Low'].min() if not hist_1y.empty else 0

            # Average volumes
            avg_volume_1m = hist_1m['Volume'].mean() if not hist_1m.empty else 0
            avg_volume_3m = hist_3m['Volume'].mean() if not hist_3m.empty else 0

            etf_data.append({
                'symbol': symbol,
                'name': info['name'],
                'amc': info['amc'],
                'launch_year': info['launch_year'],
                'aum': info['aum'],
                'expense_ratio': info['expense_ratio'],
                'current_price': float(latest['Close']),
                'volume': int(latest['Volume']),
                'avg_volume_1m': int(avg_volume_1m),
                'avg_volume_3m': int(avg_volume_3m),
                'week_52_high': week_52_high,
                'week_52_low': week_52_low,
                'returns': returns,
                'volatility': volatility
            })

            print(f"  ✅ Current Price: ₹{float(latest['Close']):.2f}")

        except Exception as e:
            print(f"  ❌ Error: {e}")
            continue

    return etf_data


def display_gold_etf_analysis(etf_data):
    """Display comprehensive gold ETF analysis"""
    if not etf_data:
        print("\n⚠️  No ETF data available")
        return

    print("\n" + "=" * 100)
    print("CURRENT PRICES & KEY METRICS")
    print("=" * 100)
    print()

    # Sort by price
    etf_data_sorted = sorted(etf_data, key=lambda x: x['current_price'], reverse=True)

    print(f"{'Symbol':<20} {'Name':<40} {'Price':<12} {'Volume':<15}")
    print("-" * 100)
    for etf in etf_data_sorted:
        print(f"{etf['symbol']:<20} {etf['name'][:38]:<40} ₹{etf['current_price']:>9,.2f}  {etf['volume']:>12,}")

    print("\n" + "=" * 100)
    print("DETAILED COMPARISON")
    print("=" * 100)

    for i, etf in enumerate(etf_data_sorted, 1):
        print(f"\n{'=' * 100}")
        print(f"#{i}. {etf['name']}")
        print(f"{'=' * 100}")
        print(f"Symbol:              {etf['symbol']}")
        print(f"AMC:                 {etf['amc']}")
        print(f"Launch Year:         {etf['launch_year']}")
        print(f"AUM:                 {etf['aum']}")
        print(f"Expense Ratio:       {etf['expense_ratio']}")
        print()
        print(f"Current Price:       ₹{etf['current_price']:.2f}")
        print(f"52-Week High:        ₹{etf['week_52_high']:.2f}")
        print(f"52-Week Low:         ₹{etf['week_52_low']:.2f}")
        print(f"52W Range:           ₹{etf['week_52_low']:.2f} - ₹{etf['week_52_high']:.2f}")

        # Position in range
        if etf['week_52_high'] and etf['week_52_low']:
            range_52w = etf['week_52_high'] - etf['week_52_low']
            position = ((etf['current_price'] - etf['week_52_low']) / range_52w) * 100
            print(f"Position in Range:   {position:.1f}% from low")

        print()
        print("LIQUIDITY ANALYSIS:")
        print(f"Today's Volume:      {etf['volume']:,} units")
        print(f"Avg Volume (1M):     {etf['avg_volume_1m']:,.0f} units")
        print(f"Avg Volume (3M):     {etf['avg_volume_3m']:,.0f} units")

        # Liquidity rating
        if etf['avg_volume_1m'] > 10000000:
            liquidity = "EXCELLENT (Very High Liquidity)"
        elif etf['avg_volume_1m'] > 1000000:
            liquidity = "GOOD (High Liquidity)"
        elif etf['avg_volume_1m'] > 100000:
            liquidity = "MODERATE"
        else:
            liquidity = "LOW"

        print(f"Liquidity Rating:    {liquidity}")

        print()
        print("RETURNS ANALYSIS:")
        returns = etf['returns']
        if '1w' in returns:
            print(f"1-Week Return:       {returns['1w']:+.2f}%")
        if '1m' in returns:
            print(f"1-Month Return:      {returns['1m']:+.2f}%")
        if '3m' in returns:
            print(f"3-Month Return:      {returns['3m']:+.2f}%")
        if '6m' in returns:
            print(f"6-Month Return:      {returns['6m']:+.2f}%")
        if '1y' in returns:
            print(f"1-Year Return:       {returns['1y']:+.2f}%")
        if '3y' in returns:
            print(f"3-Year Return:       {returns['3y']:+.2f}%")
            cagr_3y = (((etf['current_price'] / (etf['current_price'] / (1 + returns['3y']/100))) ** (1/3)) - 1) * 100
            print(f"3-Year CAGR:         {cagr_3y:+.2f}%")

        print()
        print(f"Volatility (1Y):     {etf['volatility']:.2f}% (annualized)")

    # Comparative analysis
    print("\n" + "=" * 100)
    print("COMPARATIVE ANALYSIS")
    print("=" * 100)

    print("\n📊 PRICE COMPARISON:")
    print("-" * 100)
    highest_price = max(etf_data, key=lambda x: x['current_price'])
    lowest_price = min(etf_data, key=lambda x: x['current_price'])
    print(f"Highest Price:       {highest_price['name'][:50]} - ₹{highest_price['current_price']:.2f}")
    print(f"Lowest Price:        {lowest_price['name'][:50]} - ₹{lowest_price['current_price']:.2f}")
    print(f"Price Difference:    ₹{highest_price['current_price'] - lowest_price['current_price']:.2f} ({((highest_price['current_price'] - lowest_price['current_price'])/lowest_price['current_price']*100):.2f}%)")

    print("\n📈 LIQUIDITY COMPARISON:")
    print("-" * 100)
    by_volume = sorted(etf_data, key=lambda x: x['avg_volume_1m'], reverse=True)
    for i, etf in enumerate(by_volume, 1):
        print(f"{i}. {etf['name'][:50]:<52} {etf['avg_volume_1m']:>12,.0f} units/day")

    print("\n💰 RETURNS COMPARISON (1-Year):")
    print("-" * 100)
    etfs_with_1y = [etf for etf in etf_data if '1y' in etf['returns']]
    if etfs_with_1y:
        by_returns = sorted(etfs_with_1y, key=lambda x: x['returns']['1y'], reverse=True)
        for i, etf in enumerate(by_returns, 1):
            print(f"{i}. {etf['name'][:50]:<52} {etf['returns']['1y']:>8.2f}%")

    # Investment recommendations
    print("\n" + "=" * 100)
    print("💡 INVESTMENT RECOMMENDATIONS")
    print("=" * 100)

    print("\n🏆 BEST FOR LIQUIDITY:")
    best_liquidity = max(etf_data, key=lambda x: x['avg_volume_1m'])
    print(f"   {best_liquidity['name']}")
    print(f"   - Average Volume: {best_liquidity['avg_volume_1m']:,.0f} units/day")
    print(f"   - Easy entry/exit with minimal price impact")

    print("\n💎 BEST VALUE (Lowest Price):")
    print(f"   {lowest_price['name']}")
    print(f"   - Price: ₹{lowest_price['current_price']:.2f}")
    print(f"   - Lower entry barrier for small investors")

    print("\n📊 LARGEST AUM:")
    largest_aum = max(etf_data, key=lambda x: int(x['aum'].replace('₹', '').replace(',', '').replace('+ Cr', '').replace('+', '').strip()))
    print(f"   {largest_aum['name']}")
    print(f"   - AUM: {largest_aum['aum']}")
    print(f"   - Better stability and tracking")

    # Gold investment insights
    print("\n" + "=" * 100)
    print("🥇 GOLD INVESTMENT INSIGHTS")
    print("=" * 100)

    print("\n✅ ADVANTAGES OF GOLD ETFs:")
    print("   • No making charges (vs physical gold)")
    print("   • No storage/safety concerns")
    print("   • High liquidity - sell anytime")
    print("   • Can buy fractional units")
    print("   • Lower expense ratio than Gold MFs")
    print("   • Traded on NSE during market hours")

    print("\n⚠️  CONSIDERATIONS:")
    print("   • All have 1% expense ratio (industry standard)")
    print("   • No dividends - returns only from price appreciation")
    print("   • LTCG tax: 20% with indexation (hold >3 years)")
    print("   • STCG tax: As per income slab (hold <3 years)")

    print("\n📈 WHEN TO INVEST IN GOLD:")
    print("   • Portfolio diversification (5-10% allocation)")
    print("   • Inflation hedge")
    print("   • Market uncertainty/volatility")
    print("   • Rupee depreciation concerns")
    print("   • Festive season (cultural significance)")

    print("\n💰 INVESTMENT STRATEGIES:")
    print("   • SIP Approach: Invest fixed amount monthly")
    print("   • Lump Sum: 5-10% of portfolio as hedge")
    print("   • Tactical: Increase allocation during uncertainty")
    print("   • Rebalancing: Maintain 5-10% target allocation")

    # Final recommendation
    print("\n" + "=" * 100)
    print("🎯 FINAL RECOMMENDATION")
    print("=" * 100)

    print("\n🥇 TOP PICK: GOLDSHARE.NS (Nippon India ETF Gold BeES)")
    print("   Reasons:")
    print(f"   ✅ Highest liquidity ({best_liquidity['avg_volume_1m']:,.0f} units/day)")
    print("   ✅ Largest AUM (₹6,500+ Cr)")
    print("   ✅ Better tracking accuracy")
    print("   ✅ Easy entry/exit")
    print(f"   ✅ Current Price: ₹{[e for e in etf_data if e['symbol'] == 'GOLDSHARE.NS'][0]['current_price']:.2f}")

    print("\n📊 SAMPLE INVESTMENT:")
    goldshare = [e for e in etf_data if e['symbol'] == 'GOLDSHARE.NS'][0]
    investments = [10000, 25000, 50000, 100000]
    print(f"   {'Amount':<15} {'Units':<10} {'Gold (approx)'}")
    print("   " + "-" * 50)
    for amt in investments:
        units = amt / goldshare['current_price']
        # Assuming 1 unit ≈ 1 gram gold equivalent
        print(f"   ₹{amt:>12,}   {units:>6.1f}     ~{units:.1f}g gold equivalent")

    print("\n" + "=" * 100)
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 100)


def main():
    """Main function"""
    print("\n🥇 Starting Gold ETF Analysis...\n")

    # Fetch data
    etf_data = get_gold_etf_data()

    if etf_data:
        # Display analysis
        display_gold_etf_analysis(etf_data)
    else:
        print("\n❌ Failed to fetch Gold ETF data")

    print("\n✅ Gold ETF analysis complete!")


if __name__ == "__main__":
    main()
