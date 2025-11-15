#!/usr/bin/env python3
"""
Simple script to get table overview from stock database
"""
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from stock_analysis.main import get_table_overview
    print(get_table_overview())
except Exception as e:
    print(f"Error: {e}")
    print(f"\nMake sure dependencies are installed:")
    print("pip install pandas psycopg2-binary yfinance mcp")
    sys.exit(1)
