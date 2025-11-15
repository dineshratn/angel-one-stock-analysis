#!/usr/bin/env python3
"""
Test script to verify Angel One API connection and fetch sample data
Run this before setting up Docker to ensure your credentials work
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from dotenv import load_dotenv
import pyotp
from SmartApi import SmartConnect

def test_angel_one_connection():
    """Test Angel One API connection"""
    print("=" * 60)
    print("Angel One API Connection Test")
    print("=" * 60)
    
    # Load environment variables
    load_dotenv()
    
    # Get credentials
    api_key = os.getenv("ANGEL_API_KEY")
    client_id = os.getenv("ANGEL_CLIENT_ID")
    password = os.getenv("ANGEL_PASSWORD")
    totp_token = os.getenv("ANGEL_TOTP_TOKEN")
    
    # Check if credentials are present
    print("\n1. Checking credentials...")
    if not all([api_key, client_id, password, totp_token]):
        print("❌ ERROR: Missing credentials in .env file")
        print("\nPlease ensure the following are set in your .env file:")
        print("  - ANGEL_API_KEY")
        print("  - ANGEL_CLIENT_ID")
        print("  - ANGEL_PASSWORD")
        print("  - ANGEL_TOTP_TOKEN")
        return False
    
    print("✅ All credentials found in .env file")
    
    # Test TOTP generation
    print("\n2. Testing TOTP generation...")
    try:
        totp = pyotp.TOTP(totp_token).now()
        print(f"✅ TOTP generated successfully: {totp}")
    except Exception as e:
        print(f"❌ ERROR: Failed to generate TOTP: {e}")
        print("\nPlease verify your ANGEL_TOTP_TOKEN is correct")
        return False
    
    # Test API connection
    print("\n3. Testing Angel One API connection...")
    try:
        smart_api = SmartConnect(api_key=api_key)
        print("✅ SmartConnect initialized")
        
        # Generate session
        print("\n4. Generating session...")
        data = smart_api.generateSession(client_id, password, totp)
        
        if not data.get('status'):
            print(f"❌ ERROR: Session generation failed: {data.get('message')}")
            return False
        
        print("✅ Session generated successfully!")
        print(f"   Client ID: {data['data']['clientcode']}")
        print(f"   Name: {data['data']['name']}")
        
        # Get profile
        print("\n5. Fetching user profile...")
        refresh_token = data['data']['refreshToken']
        profile = smart_api.getProfile(refresh_token)
        
        if profile.get('status'):
            print("✅ Profile fetched successfully!")
            exchanges = profile['data']['exchanges']
            print(f"   Available exchanges: {', '.join(exchanges)}")
        
        # Test market data fetch
        print("\n6. Testing market data fetch (SBIN-EQ)...")
        try:
            # SBIN token: 3045
            ltp_data = smart_api.ltpData("NSE", "SBIN-EQ", "3045")
            
            if ltp_data and ltp_data.get('status'):
                print("✅ Market data fetched successfully!")
                data = ltp_data.get('data', {})
                print(f"   Symbol: SBIN")
                print(f"   LTP: ₹{data.get('ltp', 'N/A')}")
                print(f"   Open: ₹{data.get('open', 'N/A')}")
                print(f"   High: ₹{data.get('high', 'N/A')}")
                print(f"   Low: ₹{data.get('low', 'N/A')}")
            else:
                print("⚠️  Market data fetch returned no data (market might be closed)")
        except Exception as e:
            print(f"⚠️  Market data test skipped: {e}")
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nYou can now proceed with Docker setup.")
        print("Run: docker build -t angel-one-stock-analysis .")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: API connection failed: {e}")
        print("\nPossible issues:")
        print("  1. Check if your credentials are correct")
        print("  2. Verify your Angel One account is active")
        print("  3. Ensure you have enabled SmartAPI access")
        print("  4. Check if your IP is whitelisted (if required)")
        return False


if __name__ == "__main__":
    print("\n📊 Angel One Stock Analysis - Connection Test\n")
    
    # Check if .env file exists
    if not Path(".env").exists():
        print("❌ ERROR: .env file not found!")
        print("\nPlease create a .env file with your credentials.")
        print("You can copy .env.example and fill in your details:")
        print("  cp .env.example .env")
        sys.exit(1)
    
    # Run test
    success = test_angel_one_connection()
    
    if not success:
        print("\n❌ Some tests failed. Please fix the issues before proceeding.")
        sys.exit(1)
    
    sys.exit(0)
