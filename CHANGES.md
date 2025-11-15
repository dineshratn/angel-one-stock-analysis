# Changes from Original TradingView Implementation

This document outlines the key modifications made to adapt the original TradingView-based MCP server to work with Angel One's SmartAPI for Indian stock markets.

## 🔄 Major Changes

### 1. Data Source Replacement

**Original (TradingView)**:
- Used TradingView's scanner API
- Scraped data via HTTP POST requests
- No authentication required
- Access to 70+ technical indicators directly

**New (Angel One)**:
- Uses Angel One's SmartAPI
- Official Python SDK (`smartapi-python`)
- Requires authentication (API key, TOTP)
- Market data via REST API calls

### 2. Authentication System

**Added**:
- TOTP (Time-based One-Time Password) authentication
- Session management with JWT tokens
- API key and client ID credentials
- Environment-based configuration

**Code Changes**:
```python
# New: Angel One authentication
from SmartApi import SmartConnect
import pyotp

smart_api = SmartConnect(api_key=api_key)
totp = pyotp.TOTP(totp_token).now()
data = smart_api.generateSession(client_id, password, totp)
```

### 3. Data Structure

**Original Database Schema**:
- 70+ columns with TradingView indicators
- RSI, MACD, candlestick patterns included
- Direct mapping from TradingView API

**New Database Schema**:
- Simplified to core fields
- Focus on price, volume, circuit limits
- Extensible for custom indicators
- Schema in `constant_parameters.py`:

```python
TABLE_SCHEMA = """
CREATE TABLE stock_data (
    symbol_token TEXT PRIMARY KEY,
    trading_symbol TEXT,
    name TEXT,
    exchange TEXT,
    last_price, open_price, high_price, low_price, close_price,
    volume, week_high_52, week_low_52,
    upper_circuit, lower_circuit,
    ...
)
"""
```

### 4. Market Coverage

**Original**:
- TradingView global markets
- NIFTY and NIFTY Junior indices
- International stocks

**New**:
- Indian markets (NSE, BSE, NFO, MCX)
- NSE equity stocks
- F&O instruments
- Commodities

### 5. New MCP Tools

Added tool not in original:

**`get_historical_data()`**:
```python
@mcp.tool()
def get_historical_data(
    symbol_token: str,
    exchange: str,
    interval: str,
    from_date: str,
    to_date: str
) -> List[Dict[str, Any]]:
    """Fetch historical candle data"""
```

Allows fetching OHLCV data for backtesting and analysis.

### 6. Dependencies

**Removed**:
- Direct HTTP scraping libraries
- TradingView-specific parsers

**Added**:
```toml
smartapi-python = "^1.3.0"  # Official Angel One SDK
pyotp = "^2.9.0"            # For TOTP generation
python-dotenv = "^1.0.0"    # Environment management
```

### 7. Configuration Files

**New Files**:
- `.env.example` - Template for credentials
- `test_connection.py` - Connection testing script
- `QUICK_START.md` - Simplified setup guide

**Modified Files**:
- `constant_parameters.py` - Angel One specific constants
- `main.py` - Complete rewrite for Angel One API

## 🔧 API Differences

### Data Fetching

**TradingView Approach**:
```python
response = requests.post(
    url=SCANNER_URL,
    headers=HEADERS,
    params=PARAMS,
    data=DATA
)
```

**Angel One Approach**:
```python
# Authenticate first
smart_api = get_smart_api()

# Fetch data
ltp_response = smart_api.ltpData(
    exchange,
    trading_symbol,
    symbol_token
)
```

### Rate Limits

**TradingView**:
- No explicit rate limits mentioned
- Single bulk API call

**Angel One**:
- Rate limits enforced
- Batched requests (50 symbols per batch)
- Built-in delays to avoid throttling

## 📊 Data Quality Differences

### TradingView
- ✅ 70+ technical indicators pre-calculated
- ✅ Real-time scanner data
- ✅ Global market coverage
- ❌ Unofficial API (scraping)
- ❌ No authentication

### Angel One
- ✅ Official, documented API
- ✅ Secure authentication
- ✅ Historical data access
- ✅ Order placement capability (can be added)
- ❌ Technical indicators need to be calculated
- ❌ Limited to Indian markets

## 🚀 Future Enhancements

Possible additions to match TradingView features:

1. **Technical Indicators**:
   - Integrate `ta-lib` or `pandas-ta`
   - Calculate RSI, MACD, moving averages
   - Store in database

2. **Real-time WebSocket**:
   - Use Angel One's WebSocket API
   - Stream live prices
   - Update database in real-time

3. **Options Chain**:
   - Fetch options data
   - Calculate Greeks
   - Store premium data

4. **Order Execution**:
   - Add MCP tools for placing orders
   - Portfolio management
   - Risk management

## 📝 Migration Notes

If you're migrating from the TradingView version:

1. **Database Schema**: Not directly compatible. You'll need to recreate databases.

2. **Queries**: Update SQL queries to use new column names:
   - `close` → `close_price`
   - `RSI` → (needs to be calculated)
   - `market_cap_basic` → (needs to be fetched separately)

3. **Configuration**: Replace TradingView constants with Angel One credentials.

4. **Tools**: Same tool names, but different data returned.

## 🔗 References

- [Original Article](https://medium.com/@varungangu1/building-a-stock-analysis-mcp-server-with-docker-and-claude-desktop-eae4963dc3a7)
- [Angel One SmartAPI Docs](https://smartapi.angelbroking.com/docs)
- [SmartAPI Python SDK](https://github.com/angel-one/smartapi-python)

---

**Summary**: This implementation maintains the MCP server architecture and Docker deployment from the original but completely replaces the data source from TradingView to Angel One, adding authentication and focusing on Indian stock markets.
