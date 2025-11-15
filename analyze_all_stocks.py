#!/usr/bin/env python3
"""
Analyze all Nifty 50 stocks based on P/E ratio and dividend yield
Generate investment recommendations with buy percentages
"""
import os
import psycopg2
import pandas as pd
import numpy as np

def main():
    database_url = os.getenv('DATABASE_URL')

    if not database_url:
        print("Error: DATABASE_URL not set")
        return

    try:
        conn = psycopg2.connect(database_url)

        # Get all stocks
        query = """
            SELECT
                trading_symbol,
                name,
                last_price,
                market_cap,
                pe_ratio,
                dividend_yield,
                volume,
                week_high_52,
                week_low_52,
                close_price,
                open_price
            FROM stock_data
            WHERE pe_ratio IS NOT NULL AND dividend_yield IS NOT NULL
            ORDER BY trading_symbol
        """
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty:
            print("No data found")
            return

        print("=" * 100)
        print("NIFTY 50 STOCKS - COMPREHENSIVE INVESTMENT ANALYSIS")
        print("Based on P/E Ratio and Dividend Yield")
        print("=" * 100)
        print()

        # Calculate additional metrics
        df['52w_position'] = ((df['last_price'] - df['week_low_52']) /
                              (df['week_high_52'] - df['week_low_52']) * 100)

        df['day_change_pct'] = ((df['close_price'] - df['open_price']) /
                                df['open_price'] * 100)

        # Market cap in crores
        df['market_cap_cr'] = df['market_cap'] / 10000000

        # Scoring system
        # P/E Score (lower is better, ideal range: 10-20)
        def pe_score(pe):
            if pd.isna(pe) or pe <= 0:
                return 0
            elif pe < 10:
                return 5  # Very undervalued
            elif pe < 15:
                return 10  # Undervalued
            elif pe < 20:
                return 8   # Fair value
            elif pe < 25:
                return 6   # Moderate
            elif pe < 30:
                return 4   # Expensive
            else:
                return 2   # Very expensive

        # Dividend Score (higher is better)
        def dividend_score(div_yield):
            if pd.isna(div_yield) or div_yield <= 0:
                return 0
            elif div_yield >= 4:
                return 10  # Excellent
            elif div_yield >= 3:
                return 8   # Very good
            elif div_yield >= 2:
                return 6   # Good
            elif div_yield >= 1:
                return 4   # Moderate
            else:
                return 2   # Low

        # Position score (prefer stocks not at 52-week high)
        def position_score(pos):
            if pd.isna(pos):
                return 5
            elif pos < 30:
                return 10  # Near low (opportunity)
            elif pos < 50:
                return 8   # Below mid-range
            elif pos < 70:
                return 6   # Mid-range
            elif pos < 85:
                return 4   # Upper range
            else:
                return 2   # Near high

        df['pe_score'] = df['pe_ratio'].apply(pe_score)
        df['div_score'] = df['dividend_yield'].apply(dividend_score)
        df['pos_score'] = df['52w_position'].apply(position_score)

        # Total score (weighted)
        df['total_score'] = (df['pe_score'] * 0.4 +  # 40% weight on P/E
                            df['div_score'] * 0.4 +   # 40% weight on dividend
                            df['pos_score'] * 0.2)    # 20% weight on position

        # Normalize to 100
        max_score = df['total_score'].max()
        df['normalized_score'] = (df['total_score'] / max_score * 100)

        # Investment rating
        def rating(score):
            if score >= 80:
                return "STRONG BUY"
            elif score >= 65:
                return "BUY"
            elif score >= 50:
                return "MODERATE BUY"
            elif score >= 35:
                return "HOLD"
            else:
                return "AVOID"

        df['rating'] = df['normalized_score'].apply(rating)

        # Calculate buy percentages (only for BUY and STRONG BUY)
        buy_stocks = df[df['normalized_score'] >= 50].copy()

        if not buy_stocks.empty:
            # Allocate based on normalized scores
            total_buy_score = buy_stocks['normalized_score'].sum()
            buy_stocks['buy_percentage'] = (buy_stocks['normalized_score'] / total_buy_score * 100)
        else:
            buy_stocks['buy_percentage'] = 0

        # Sort by score
        df_sorted = df.sort_values('normalized_score', ascending=False)

        # Display results
        print("📊 TOP INVESTMENT OPPORTUNITIES (Sorted by Score)")
        print("-" * 100)
        print()

        # Top picks
        top_picks = df_sorted.head(15)

        for idx, row in top_picks.iterrows():
            print(f"{'=' * 100}")
            print(f"#{top_picks.index.get_loc(idx) + 1}. {row['trading_symbol']} - {row['name'][:40]}")
            print(f"{'=' * 100}")
            print(f"  Price:              ₹{row['last_price']:,.2f}")
            print(f"  Market Cap:         ₹{row['market_cap_cr']:,.0f} Cr")
            print(f"  P/E Ratio:          {row['pe_ratio']:.2f}x")
            print(f"  Dividend Yield:     {row['dividend_yield']:.2f}%")
            print(f"  52W Position:       {row['52w_position']:.1f}%")
            print(f"  Day Change:         {row['day_change_pct']:+.2f}%")
            print(f"  Volume:             {row['volume']:,.0f}")
            print(f"  ")
            print(f"  Investment Score:   {row['normalized_score']:.1f}/100")
            print(f"  Rating:             {row['rating']}")

            if row['normalized_score'] >= 50 and not buy_stocks.empty:
                buy_pct = buy_stocks[buy_stocks['trading_symbol'] == row['trading_symbol']]['buy_percentage'].values
                if len(buy_pct) > 0:
                    print(f"  📈 BUY ALLOCATION:   {buy_pct[0]:.2f}% of portfolio")
            print()

        # Summary statistics
        print("\n" + "=" * 100)
        print("📈 INVESTMENT SUMMARY & ALLOCATION")
        print("=" * 100)
        print()

        # Category breakdown
        strong_buy = df[df['rating'] == 'STRONG BUY']
        buy = df[df['rating'] == 'BUY']
        moderate_buy = df[df['rating'] == 'MODERATE BUY']
        hold = df[df['rating'] == 'HOLD']
        avoid = df[df['rating'] == 'AVOID']

        print(f"STRONG BUY:         {len(strong_buy)} stocks")
        print(f"BUY:                {len(buy)} stocks")
        print(f"MODERATE BUY:       {len(moderate_buy)} stocks")
        print(f"HOLD:               {len(hold)} stocks")
        print(f"AVOID:              {len(avoid)} stocks")
        print()

        # Recommended portfolio allocation
        print("-" * 100)
        print("💰 RECOMMENDED PORTFOLIO ALLOCATION (Buy-worthy stocks only)")
        print("-" * 100)
        print()

        if not buy_stocks.empty:
            buy_allocation = buy_stocks.sort_values('buy_percentage', ascending=False)

            print(f"{'Rank':<6}{'Symbol':<12}{'Company':<35}{'Score':<10}{'Allocation':<12}{'Price':<12}")
            print("-" * 100)

            for i, (idx, row) in enumerate(buy_allocation.iterrows(), 1):
                print(f"{i:<6}{row['trading_symbol']:<12}{row['name'][:33]:<35}"
                      f"{row['normalized_score']:>6.1f}/100  "
                      f"{row['buy_percentage']:>6.2f}%      "
                      f"₹{row['last_price']:>9,.2f}")

            print("-" * 100)
            print(f"{'TOTAL':<53}{'':<10}{buy_allocation['buy_percentage'].sum():>6.2f}%")
            print()
        else:
            print("⚠️  No stocks meet the BUY criteria at current valuations.")
            print()

        # Best in category
        print("=" * 100)
        print("🏆 CATEGORY WINNERS")
        print("=" * 100)
        print()

        best_pe = df[df['pe_ratio'] > 0].nsmallest(5, 'pe_ratio')[['trading_symbol', 'name', 'pe_ratio', 'last_price']]
        best_div = df.nlargest(5, 'dividend_yield')[['trading_symbol', 'name', 'dividend_yield', 'last_price']]

        print("📉 LOWEST P/E RATIOS (Value Stocks):")
        print("-" * 100)
        for idx, row in best_pe.iterrows():
            print(f"  {row['trading_symbol']:<12} {row['name'][:40]:<42} P/E: {row['pe_ratio']:>6.2f}x  ₹{row['last_price']:,.2f}")
        print()

        print("💰 HIGHEST DIVIDEND YIELDS (Income Stocks):")
        print("-" * 100)
        for idx, row in best_div.iterrows():
            print(f"  {row['trading_symbol']:<12} {row['name'][:40]:<42} Yield: {row['dividend_yield']:>5.2f}%  ₹{row['last_price']:,.2f}")
        print()

        # Market statistics
        print("=" * 100)
        print("📊 MARKET STATISTICS")
        print("=" * 100)
        print()

        print(f"Average P/E Ratio:        {df['pe_ratio'].mean():.2f}x")
        print(f"Median P/E Ratio:         {df['pe_ratio'].median():.2f}x")
        print(f"Average Dividend Yield:   {df['dividend_yield'].mean():.2f}%")
        print(f"Median Dividend Yield:    {df['dividend_yield'].median():.2f}%")
        print()

        # Risk disclaimer
        print("=" * 100)
        print("⚠️  IMPORTANT DISCLAIMERS")
        print("=" * 100)
        print()
        print("1. This analysis is based ONLY on P/E ratio and dividend yield metrics")
        print("2. Does NOT consider: debt levels, growth rates, industry trends, management quality")
        print("3. Allocation percentages are algorithmic suggestions - not personalized advice")
        print("4. Past performance does not guarantee future results")
        print("5. Always conduct thorough research and consult a financial advisor")
        print("6. Consider your risk tolerance, investment horizon, and financial goals")
        print("7. Diversification across sectors is recommended")
        print()
        print("=" * 100)
        print("Analysis Date: November 14, 2025")
        print("=" * 100)

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
