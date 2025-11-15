#!/usr/bin/env python3
"""
Indian ETF Price Tracker
Track prices of popular ETFs listed on NSE and BSE
"""

import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    import yfinance as yf
    import pandas as pd
except ImportError:
    print("Error: Required libraries not installed")
    print("Run: pip install yfinance pandas")
    sys.exit(1)


# Popular Indian ETFs
INDIAN_ETFS = {
    # Equity ETFs - Nifty Based
    "NIFTYBEES.NS": {
        "name": "Nippon India ETF Nifty BeES",
        "type": "Equity - Large Cap",
        "index": "Nifty 50",
        "aum": "₹10,000+ Cr",
        "expense_ratio": "0.05%"
    },
    "JUNIORBEES.NS": {
        "name": "Nippon India ETF Nifty Junior BeES",
        "type": "Equity - Mid Cap",
        "index": "Nifty Next 50",
        "aum": "₹2,500+ Cr",
        "expense_ratio": "0.36%"
    },
    "LIQUIDBEES.NS": {
        "name": "Nippon India ETF Liquid BeES",
        "type": "Liquid/Debt",
        "index": "CRISIL Liquid Fund Index",
        "aum": "₹17,000+ Cr",
        "expense_ratio": "0.06%"
    },
    "BANKBEES.NS": {
        "name": "Nippon India ETF Bank BeES",
        "type": "Equity - Sectoral",
        "index": "Nifty Bank",
        "aum": "₹5,500+ Cr",
        "expense_ratio": "0.43%"
    },

    # HDFC ETFs
    "HDFCNIF100.NS": {
        "name": "HDFC Nifty 100 ETF",
        "type": "Equity - Large Cap",
        "index": "Nifty 100",
        "aum": "₹800+ Cr",
        "expense_ratio": "0.35%"
    },
    "HDFCSENSEX.NS": {
        "name": "HDFC Sensex ETF",
        "type": "Equity - Large Cap",
        "index": "BSE Sensex",
        "aum": "₹1,000+ Cr",
        "expense_ratio": "0.35%"
    },

    # SBI ETFs
    "SETFNIF50.NS": {
        "name": "SBI ETF Nifty 50",
        "type": "Equity - Large Cap",
        "index": "Nifty 50",
        "aum": "₹12,000+ Cr",
        "expense_ratio": "0.07%"
    },
    "SETFNN50.NS": {
        "name": "SBI ETF Nifty Next 50",
        "type": "Equity - Mid Cap",
        "index": "Nifty Next 50",
        "aum": "₹2,000+ Cr",
        "expense_ratio": "0.30%"
    },

    # ICICI Prudential ETFs
    "ICICINXT50.NS": {
        "name": "ICICI Prudential Nifty Next 50 ETF",
        "type": "Equity - Mid Cap",
        "index": "Nifty Next 50",
        "aum": "₹1,500+ Cr",
        "expense_ratio": "0.31%"
    },

    # Kotak ETFs
    "KOTAKBKETF.NS": {
        "name": "Kotak Nifty Bank ETF",
        "type": "Equity - Sectoral",
        "index": "Nifty Bank",
        "aum": "₹800+ Cr",
        "expense_ratio": "0.50%"
    },

    # Gold ETFs
    "GOLDSHARE.NS": {
        "name": "Nippon India ETF Gold BeES",
        "type": "Commodity - Gold",
        "index": "Domestic Gold Price",
        "aum": "₹6,500+ Cr",
        "expense_ratio": "1.00%"
    },
    "GOLDBEES.NS": {
        "name": "Nippon India ETF Gold BeES (Old)",
        "type": "Commodity - Gold",
        "index": "Domestic Gold Price",
        "aum": "₹2,000+ Cr",
        "expense_ratio": "1.00%"
    },
    "HDFCGOLD.NS": {
        "name": "HDFC Gold ETF",
        "type": "Commodity - Gold",
        "index": "Domestic Gold Price",
        "aum": "₹500+ Cr",
        "expense_ratio": "1.00%"
    },

    # International ETFs
    "HNGSNGBEES.NS": {
        "name": "Nippon India ETF Hang Seng BeES",
        "type": "International - Hong Kong",
        "index": "Hang Seng",
        "aum": "₹400+ Cr",
        "expense_ratio": "0.70%"
    },

    # PSU Bank ETF
    "PSUBNKBEES.NS": {
        "name": "Nippon India ETF PSU Bank BeES",
        "type": "Equity - Sectoral",
        "index": "Nifty PSU Bank",
        "aum": "₹1,200+ Cr",
        "expense_ratio": "0.52%"
    },

    # IT ETF
    "ITBEES.NS": {
        "name": "Nippon India ETF Nifty IT BeES",
        "type": "Equity - Sectoral",
        "index": "Nifty IT",
        "aum": "₹800+ Cr",
        "expense_ratio": "0.62%"
    },

    # Shariah ETF
    "SHARIABEES.NS": {
        "name": "Nippon India ETF Nifty Shariah BeES",
        "type": "Equity - Shariah Compliant",
        "index": "Nifty50 Shariah",
        "aum": "₹300+ Cr",
        "expense_ratio": "0.65%"
    },
}


def get_etf_prices():
    """Fetch current prices for all Indian ETFs"""
    print("=" * 100)
    print("INDIAN ETF PRICE TRACKER")
    print("=" * 100)
    print(f"\nFetching prices for {len(INDIAN_ETFS)} ETFs...")
    print()

    etf_data = []

    for symbol, info in INDIAN_ETFS.items():
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")

            if hist.empty:
                print(f"⚠️  No data for {symbol}")
                continue

            latest = hist.iloc[-1]

            # Get 1-year data for 52-week high/low
            hist_1y = ticker.history(period="1y")

            etf_data.append({
                'symbol': symbol,
                'name': info['name'],
                'type': info['type'],
                'index': info['index'],
                'price': float(latest['Close']),
                'open': float(latest['Open']),
                'high': float(latest['High']),
                'low': float(latest['Low']),
                'volume': int(latest['Volume']),
                'week_52_high': float(hist_1y['High'].max()) if not hist_1y.empty else 0,
                'week_52_low': float(hist_1y['Low'].min()) if not hist_1y.empty else 0,
                'aum': info['aum'],
                'expense_ratio': info['expense_ratio']
            })

            print(f"✅ {symbol:<20} ₹{float(latest['Close']):>10,.2f}")

        except Exception as e:
            print(f"❌ Error fetching {symbol}: {e}")
            continue

    return pd.DataFrame(etf_data)


def display_etf_report(df):
    """Display comprehensive ETF report"""
    if df.empty:
        print("\n⚠️  No ETF data available")
        return

    print("\n" + "=" * 100)
    print("ETF ANALYSIS REPORT")
    print("=" * 100)

    # Overall summary
    print(f"\n📊 SUMMARY")
    print("-" * 100)
    print(f"Total ETFs Tracked:     {len(df)}")
    print(f"Average Price:          ₹{df['price'].mean():,.2f}")
    print(f"Highest Priced ETF:     {df.loc[df['price'].idxmax(), 'name']} (₹{df['price'].max():,.2f})")
    print(f"Lowest Priced ETF:      {df.loc[df['price'].idxmin(), 'name']} (₹{df['price'].min():,.2f})")

    # By category
    print(f"\n📁 ETFs BY CATEGORY")
    print("-" * 100)
    category_counts = df['type'].value_counts()
    for category, count in category_counts.items():
        print(f"{category:<30} {count:>3} ETFs")

    # Top performers (near 52-week high)
    df['pct_from_52w_high'] = ((df['week_52_high'] - df['price']) / df['week_52_high'] * 100)
    top_performers = df.nsmallest(5, 'pct_from_52w_high')

    print(f"\n🏆 TOP PERFORMERS (Near 52-Week High)")
    print("-" * 100)
    print(f"{'Symbol':<20} {'Name':<40} {'Price':<12} {'From High':<12}")
    print("-" * 100)
    for _, row in top_performers.iterrows():
        print(f"{row['symbol']:<20} {row['name'][:38]:<40} ₹{row['price']:>9,.2f}  "
              f"{row['pct_from_52w_high']:>6.2f}% below")

    # Value opportunities (near 52-week low)
    df['pct_from_52w_low'] = ((df['price'] - df['week_52_low']) / df['week_52_low'] * 100)
    value_picks = df.nsmallest(5, 'pct_from_52w_low')

    print(f"\n💎 VALUE OPPORTUNITIES (Near 52-Week Low)")
    print("-" * 100)
    print(f"{'Symbol':<20} {'Name':<40} {'Price':<12} {'From Low':<12}")
    print("-" * 100)
    for _, row in value_picks.iterrows():
        print(f"{row['symbol']:<20} {row['name'][:38]:<40} ₹{row['price']:>9,.2f}  "
              f"{row['pct_from_52w_low']:>6.2f}% above")

    # Detailed table
    print(f"\n📋 COMPLETE ETF LIST")
    print("-" * 100)
    print(f"{'Symbol':<20} {'Name':<35} {'Type':<25} {'Price':<12} {'Volume':<15}")
    print("-" * 100)

    for _, row in df.sort_values('type').iterrows():
        print(f"{row['symbol']:<20} {row['name'][:33]:<35} {row['type']:<25} "
              f"₹{row['price']:>9,.2f}  {row['volume']:>12,}")

    # Category-wise breakdown
    print(f"\n" + "=" * 100)
    print("CATEGORY-WISE ANALYSIS")
    print("=" * 100)

    for category in df['type'].unique():
        category_df = df[df['type'] == category]
        print(f"\n📦 {category}")
        print("-" * 100)
        print(f"{'Symbol':<20} {'Name':<40} {'Price':<12} {'AUM':<12} {'Expense':<10}")
        print("-" * 100)

        for _, row in category_df.iterrows():
            print(f"{row['symbol']:<20} {row['name'][:38]:<40} ₹{row['price']:>9,.2f}  "
                  f"{row['aum']:<12} {row['expense_ratio']:<10}")

    print("\n" + "=" * 100)
    print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 100)


def get_etf_by_category(category_filter=None):
    """Get ETFs filtered by category"""
    if category_filter:
        filtered = {k: v for k, v in INDIAN_ETFS.items() if category_filter.lower() in v['type'].lower()}
        return filtered
    return INDIAN_ETFS


def main():
    """Main function"""
    print("\n🔍 Starting ETF price tracking...\n")

    # Fetch ETF data
    df = get_etf_prices()

    if not df.empty:
        # Display report
        display_etf_report(df)

        # Export to CSV (optional)
        output_file = f"indian_etf_prices_{datetime.now().strftime('%Y%m%d')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\n💾 Data exported to: {output_file}")
    else:
        print("\n❌ Failed to fetch ETF data")

    print("\n✅ ETF tracking complete!")


if __name__ == "__main__":
    main()
