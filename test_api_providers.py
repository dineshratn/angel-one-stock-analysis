#!/usr/bin/env python3
"""
Test script for multiple stock API providers
Demonstrates how to use different APIs
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from stock_analysis.api_providers import APIProviderFactory


def test_provider(provider_name: str, symbol: str = "RELIANCE.NS"):
    """Test a specific API provider"""
    print(f"\n{'=' * 80}")
    print(f"Testing: {provider_name.upper()}")
    print(f"{'=' * 80}")

    try:
        # Get provider
        provider = APIProviderFactory.get_provider(provider_name)

        if not provider.is_available():
            print(f"❌ {provider.name} is not available (missing API key or configuration)")
            return False

        print(f"✅ {provider.name} is available")

        # Test quote
        print(f"\n📊 Testing quote for {symbol}...")
        quote = provider.get_quote(symbol)

        if quote:
            print(f"✅ Quote retrieved successfully:")
            print(f"   Last Price: ₹{quote.get('last_price', 'N/A')}")
            print(f"   Open: ₹{quote.get('open', 'N/A')}")
            print(f"   High: ₹{quote.get('high', 'N/A')}")
            print(f"   Low: ₹{quote.get('low', 'N/A')}")
            print(f"   Volume: {quote.get('volume', 'N/A'):,}")
        else:
            print(f"❌ Failed to retrieve quote")
            return False

        # Test historical data
        print(f"\n📈 Testing historical data...")
        hist = provider.get_historical_data(symbol, period="5d")

        if not hist.empty:
            print(f"✅ Historical data retrieved: {len(hist)} records")
            print(f"   Date Range: {hist.index[0]} to {hist.index[-1]}")
        else:
            print(f"⚠️  No historical data available")

        # Test company info
        print(f"\n🏢 Testing company info...")
        info = provider.get_company_info(symbol)

        if info:
            print(f"✅ Company info retrieved")
            # Print first few keys
            keys = list(info.keys())[:5]
            print(f"   Available fields: {', '.join(keys)}...")
        else:
            print(f"⚠️  No company info available")

        print(f"\n✅ {provider.name} - ALL TESTS PASSED")
        return True

    except Exception as e:
        print(f"\n❌ ERROR testing {provider_name}: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_fallback():
    """Test API fallback mechanism"""
    print(f"\n{'=' * 80}")
    print(f"Testing API Fallback Mechanism")
    print(f"{'=' * 80}")

    try:
        # Set fallback order
        fallback_order = ['yfinance', 'twelvedata', 'alphavantage', 'finnhub']

        provider = APIProviderFactory.get_provider_with_fallback(fallback_order)

        print(f"✅ Fallback selected: {provider.name}")

        # Test a quick quote
        quote = provider.get_quote("TCS.NS")
        if quote:
            print(f"✅ Fallback working - Retrieved TCS quote: ₹{quote.get('last_price', 'N/A')}")
        else:
            print(f"⚠️  Fallback provider could not retrieve data")

    except Exception as e:
        print(f"❌ Fallback test failed: {e}")


def main():
    """Main test function"""
    print("=" * 80)
    print("STOCK API PROVIDERS TEST SUITE")
    print("=" * 80)

    # List available providers
    available = APIProviderFactory.get_available_providers()
    print(f"\n📋 Available Providers: {', '.join(available)}")

    # Test each provider
    test_symbol = "RELIANCE.NS"
    print(f"\n🎯 Test Symbol: {test_symbol}")

    results = {}

    # Test Yahoo Finance (should always work)
    results['yfinance'] = test_provider('yfinance', test_symbol)

    # Test other providers (may need API keys)
    for provider in ['alphavantage', 'twelvedata', 'finnhub', 'nse']:
        results[provider] = test_provider(provider, test_symbol)

    # Test fallback
    test_fallback()

    # Summary
    print(f"\n{'=' * 80}")
    print(f"TEST SUMMARY")
    print(f"{'=' * 80}")

    for provider, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{provider:15} {status}")

    passed_count = sum(results.values())
    total_count = len(results)

    print(f"\n{passed_count}/{total_count} providers working")

    if passed_count == 0:
        print("\n⚠️  WARNING: No providers are working!")
        print("   Make sure to configure at least one API key in .env file")
        print("   Or use yfinance which requires no API key")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
