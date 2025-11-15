#!/usr/bin/env python3
"""
Test script to call MCP tools directly
"""
import sys
import os
import asyncio

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

async def main():
    from stock_analysis.main import get_table_overview

    print("Fetching table overview...")
    result = get_table_overview()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
