#!/usr/bin/env python3
"""
Analyze Reliance Industries stock
"""
import os
import psycopg2
import pandas as pd
import json

def main():
    database_url = os.getenv('DATABASE_URL')

    if not database_url:
        print("Error: DATABASE_URL not set")
        return

    try:
        conn = psycopg2.connect(database_url)

        # Get detailed Reliance data
        query = """
            SELECT *
            FROM stock_data
            WHERE trading_symbol = 'RELIANCE'
        """
        df = pd.read_sql_query(query, conn)

        if df.empty:
            print("No data found for RELIANCE")
            conn.close()
            return

        # Convert to dict for easier access
        stock = df.iloc[0].to_dict()

        # Print detailed analysis
        print("=" * 80)
        print("RELIANCE INDUSTRIES LIMITED - DETAILED STOCK ANALYSIS")
        print("=" * 80)
        print()

        # Basic Information
        print("📊 BASIC INFORMATION")
        print("-" * 80)
        print(f"Company Name:        {stock['name']}")
        print(f"Trading Symbol:      {stock['trading_symbol']}")
        print(f"Exchange:            {stock['exchange']}")
        print(f"Instrument Type:     {stock['instrument_type']}")
        print(f"Last Updated:        {stock['last_updated']}")
        print()

        # Price Information
        print("💰 PRICE INFORMATION")
        print("-" * 80)
        print(f"Last Price:          ₹{stock['last_price']:,.2f}")
        print(f"Open Price:          ₹{stock['open_price']:,.2f}")
        print(f"High Price:          ₹{stock['high_price']:,.2f}")
        print(f"Low Price:           ₹{stock['low_price']:,.2f}")
        print(f"Close Price:         ₹{stock['close_price']:,.2f}")

        # Calculate day change
        if stock['open_price'] and stock['last_price']:
            day_change = stock['last_price'] - stock['open_price']
            day_change_pct = (day_change / stock['open_price']) * 100
            print(f"Day Change:          ₹{day_change:,.2f} ({day_change_pct:+.2f}%)")
        print()

        # 52-Week Range
        print("📈 52-WEEK PERFORMANCE")
        print("-" * 80)
        print(f"52-Week High:        ₹{stock['week_high_52']:,.2f}")
        print(f"52-Week Low:         ₹{stock['week_low_52']:,.2f}")
        print(f"52-Week Range:       ₹{stock['week_low_52']:,.2f} - ₹{stock['week_high_52']:,.2f}")

        # Calculate position in 52-week range
        if stock['week_high_52'] and stock['week_low_52']:
            range_52w = stock['week_high_52'] - stock['week_low_52']
            position = ((stock['last_price'] - stock['week_low_52']) / range_52w) * 100
            print(f"Position in Range:   {position:.1f}% from 52-week low")

            # Distance from high/low
            dist_from_high = ((stock['week_high_52'] - stock['last_price']) / stock['week_high_52']) * 100
            dist_from_low = ((stock['last_price'] - stock['week_low_52']) / stock['week_low_52']) * 100
            print(f"Distance from High:  {dist_from_high:.2f}% below")
            print(f"Distance from Low:   {dist_from_low:.2f}% above")
        print()

        # Volume Information
        print("📊 VOLUME & LIQUIDITY")
        print("-" * 80)
        print(f"Volume:              {stock['volume']:,} shares")
        if stock['volume'] and stock['last_price']:
            turnover = stock['volume'] * stock['last_price']
            print(f"Turnover:            ₹{turnover:,.2f}")
        print()

        # Valuation Metrics
        print("💼 VALUATION METRICS")
        print("-" * 80)
        if stock['market_cap']:
            market_cap_cr = stock['market_cap'] / 10000000
            print(f"Market Cap:          ₹{market_cap_cr:,.2f} Crores")
        else:
            print(f"Market Cap:          N/A")

        if stock['pe_ratio']:
            print(f"P/E Ratio:           {stock['pe_ratio']:.2f}x")
        else:
            print(f"P/E Ratio:           N/A")

        if stock['dividend_yield']:
            print(f"Dividend Yield:      {stock['dividend_yield']:.2f}%")
        else:
            print(f"Dividend Yield:      N/A")
        print()

        # Technical Indicators
        print("🔍 TECHNICAL ANALYSIS")
        print("-" * 80)

        # Price momentum
        if stock['close_price'] and stock['open_price']:
            if stock['close_price'] > stock['open_price']:
                print(f"Price Action:        BULLISH (Green Candle)")
            elif stock['close_price'] < stock['open_price']:
                print(f"Price Action:        BEARISH (Red Candle)")
            else:
                print(f"Price Action:        NEUTRAL (Doji)")

        # Volatility (High-Low range)
        if stock['high_price'] and stock['low_price'] and stock['open_price']:
            day_range = stock['high_price'] - stock['low_price']
            volatility_pct = (day_range / stock['open_price']) * 100
            print(f"Day Range:           ₹{day_range:.2f} ({volatility_pct:.2f}%)")
            print(f"Volatility:          {'High' if volatility_pct > 2 else 'Moderate' if volatility_pct > 1 else 'Low'}")
        print()

        # Investment Analysis
        print("🎯 QUICK ASSESSMENT")
        print("-" * 80)

        signals = []

        # P/E Analysis
        if stock['pe_ratio']:
            if stock['pe_ratio'] < 15:
                signals.append("✓ Undervalued P/E ratio")
            elif stock['pe_ratio'] > 30:
                signals.append("⚠ High P/E ratio (growth premium)")
            else:
                signals.append("• Moderate P/E ratio")

        # 52-week position
        if position > 80:
            signals.append("⚠ Near 52-week high (resistance zone)")
        elif position < 20:
            signals.append("✓ Near 52-week low (potential support)")
        else:
            signals.append("• Trading in mid-range")

        # Dividend yield
        if stock['dividend_yield'] and stock['dividend_yield'] > 2:
            signals.append("✓ Good dividend yield")

        # Volume
        if stock['volume'] > 5000000:
            signals.append("✓ High liquidity")

        for signal in signals:
            print(signal)

        print()
        print("=" * 80)
        print("⚠️  DISCLAIMER: This analysis is for informational purposes only.")
        print("    Always conduct your own research and consult a financial advisor.")
        print("=" * 80)

        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
