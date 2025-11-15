# Stock Analysis MCP Server

A Model Context Protocol (MCP) server for real-time stock market analysis with Claude Desktop. Supports **10+ free stock market APIs** including Yahoo Finance, Alpha Vantage, Twelve Data, Finnhub, and more. Perfect for analyzing Indian stocks (NSE/BSE) and global markets.

## 🌟 Features

- **Multiple Free APIs**: Choose from 10+ free stock market data providers
- **No API Key Required**: Works out-of-the-box with Yahoo Finance (default)
- **Live Market Data**: Real-time stock prices, quotes, and market data
- **Historical Data**: Access historical candle data for technical analysis
- **PostgreSQL Storage**: Persistent database storage via Supabase
- **Portfolio Analysis**: AI-powered portfolio allocation based on P/E and dividend yields
- **MCP Integration**: Seamless integration with Claude Desktop
- **Docker Support**: Containerized deployment for consistency
- **API Fallback**: Automatic fallback to alternative APIs if primary fails

## 📊 Supported APIs

| API | Free Tier | API Key | Best For |
|-----|-----------|---------|----------|
| **Yahoo Finance** ⭐ | Unlimited | ❌ No | General use (DEFAULT) |
| Alpha Vantage | 25/day | ✅ Yes | Technical indicators |
| Twelve Data | 800/day | ✅ Yes | Real-time data |
| Finnhub | 60/min | ✅ Yes | News & sentiment |
| NSE India | Varies | ❌ No | Indian stocks (NSE) |
| IEX Cloud | 50k/month | ✅ Yes | US fundamentals |
| Polygon.io | 5/min | ✅ Yes | High-quality US data |
| Marketstack | 100/month | ✅ Yes | Global coverage |

**See [FREE_STOCK_APIS.md](FREE_STOCK_APIS.md) for complete list and details**

## 📋 Prerequisites

1. **Database**: Supabase account (free tier available) or PostgreSQL
2. **Docker** (optional): For containerized deployment
3. **Claude Desktop**: Latest version installed
4. **API Keys** (optional): Only if you want to use APIs other than Yahoo Finance

## 🚀 Quick Start (No API Key Needed!)

### Step 1: Get Database (Supabase)

1. **Sign up for Supabase** (free): https://supabase.com/
2. **Create a new project**
3. **Get your DATABASE_URL**:
   - Go to Project Settings > Database
   - Copy the "Connection String" (URI format)

### Step 2: Configure Environment

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your database URL:
```env
# Required: Database
DATABASE_URL=postgresql://postgres:yourpassword@db.xxx.supabase.co:5432/postgres

# Optional: Choose API provider (default: yfinance - no key needed)
STOCK_API_PROVIDER=yfinance
```

**That's it! No API keys needed with Yahoo Finance (default provider)**

### Step 3: Install Dependencies (if running locally)

```bash
pip install -r requirements.txt
```

### Step 4: Test the Setup

```bash
# Test API providers
python test_api_providers.py

# Analyze stocks
python analyze_all_stocks.py
```

## 🔑 Using Other APIs (Optional)

Want to use a different API? Here's how:

### Option 1: Alpha Vantage (25 calls/day)
```bash
# 1. Get free API key: https://www.alphavantage.co/support/#api-key
# 2. Add to .env:
ALPHAVANTAGE_API_KEY=your_key_here
STOCK_API_PROVIDER=alphavantage
```

### Option 2: Twelve Data (800 calls/day)
```bash
# 1. Get free API key: https://twelvedata.com/pricing
# 2. Add to .env:
TWELVEDATA_API_KEY=your_key_here
STOCK_API_PROVIDER=twelvedata
```

### Option 3: Finnhub (60 calls/min)
```bash
# 1. Get free API key: https://finnhub.io/register
# 2. Add to .env:
FINNHUB_API_KEY=your_key_here
STOCK_API_PROVIDER=finnhub
```

**See [FREE_STOCK_APIS.md](FREE_STOCK_APIS.md) for all 10+ API options!**

---

## 🐳 Docker Setup

### Step 3: Build Docker Image

```bash
# Build the image
docker build -t angel-one-stock-analysis .

# Verify the build
docker images | grep angel-one
```

### Step 4: Configure Claude Desktop

1. **Find your Claude Desktop config file**:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. **Add the MCP server configuration**:
```json
{
  "mcpServers": {
    "angel-one-stocks": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "/absolute/path/to/project/src/database:/app/src/database",
        "--env-file",
        "/absolute/path/to/project/.env",
        "angel-one-stock-analysis"
      ]
    }
  }
}
```

**Important**: Replace `/absolute/path/to/project` with the actual path to this project directory!

### Step 5: Test the Setup

1. **Restart Claude Desktop**

2. **Check MCP Tools**: You should see the Angel One tools in Claude's tools menu:
   - `get_table_overview`
   - `query_database`
   - `refresh_market_data`
   - `get_historical_data`

## 🎮 Usage Examples

Once configured, you can ask Claude questions like:

### Basic Queries
```
"Show me the schema of the stock database"
"Refresh the market data"
"Show me all available stocks"
```

### Market Analysis
```
"Which stocks have volume greater than 1 million today?"
"Show me the top 10 stocks by price"
"Find stocks with price between 100 and 500"
```

### Historical Data
```
"Get me 5-minute candle data for SBIN-EQ for today"
"Fetch historical data for Reliance from last week"
```

### Advanced Analysis
```
"Analyze the market trends and show me high-volume stocks"
"Compare the performance of banking stocks"
"Find stocks that hit upper circuit today"
```

## 📁 Project Structure

```
angel-one-stock-analysis/
├── Dockerfile                          # Docker configuration
├── pyproject.toml                      # Python dependencies
├── .env.example                        # Example environment variables
├── README.md                           # This file
└── src/
    ├── stock_analysis/
    │   ├── __init__.py
    │   ├── main.py                     # MCP server implementation
    │   └── constant_parameters.py      # Configuration constants
    └── database/
        └── YYYY-MM-DD.db              # Daily SQLite databases
```

## 🔧 Available MCP Tools

### 1. `get_table_overview()`
Returns database schema and sample data.

### 2. `query_database(sql_query: str)`
Execute SELECT queries on the stock database.

**Example**:
```sql
SELECT trading_symbol, last_price, volume 
FROM stock_data 
WHERE volume > 1000000 
ORDER BY volume DESC 
LIMIT 10;
```

### 3. `refresh_market_data()`
Force refresh of market data from Angel One API.

### 4. `get_historical_data(symbol_token, exchange, interval, from_date, to_date)`
Fetch historical candle data.

**Parameters**:
- `symbol_token`: Token ID from scrip master
- `exchange`: "NSE", "BSE", "NFO", etc.
- `interval`: "ONE_MINUTE", "FIVE_MINUTE", "ONE_DAY", etc.
- `from_date`: "2024-01-01 09:15"
- `to_date`: "2024-01-01 15:30"

## 🔒 Security Notes

1. **Never commit your `.env` file** to version control
2. **Keep your API keys secure** - don't share them
3. **Use volume mounts** to persist database outside container
4. **Regular key rotation** is recommended for production use

## 🐛 Troubleshooting

### Common Issues

**1. Authentication Failed**
- Verify your credentials in `.env`
- Check if TOTP token is correct
- Ensure your Angel One account is active

**2. Database Not Found**
- The database is created on first data fetch
- Use `refresh_market_data()` to force data fetch
- Check volume mount path in Docker config

**3. Rate Limit Errors**
- Angel One has rate limits on API calls
- The code includes delays to handle this
- Try reducing batch size in the code

**4. Docker Volume Issues**
- Ensure the database path exists
- Check Docker has permission to write to the directory
- Use absolute paths in Docker config

### Debug Mode

Enable debug logging by modifying `main.py`:
```python
logging.basicConfig(level=logging.DEBUG)
```

## 📊 Database Schema

```sql
CREATE TABLE stock_data (
    symbol_token TEXT PRIMARY KEY,
    trading_symbol TEXT,
    name TEXT,
    exchange TEXT,
    instrument_type TEXT,
    last_price REAL,
    open_price REAL,
    high_price REAL,
    low_price REAL,
    close_price REAL,
    volume INTEGER,
    week_high_52 REAL,
    week_low_52 REAL,
    upper_circuit REAL,
    lower_circuit REAL,
    expiry DATE,
    strike_price REAL,
    lot_size INTEGER,
    tick_size REAL,
    last_updated TIMESTAMP
)
```

## 🔄 Customization

### Filter Different Stocks

Edit `constant_parameters.py`:
```python
# Change STOCK_FILTER to:
STOCK_FILTER = "NIFTY 100"  # For Nifty 100 stocks
STOCK_FILTER = "NIFTY 500"  # For Nifty 500 stocks
STOCK_FILTER = None          # For all NSE stocks
```

### Add Technical Indicators

You can extend the `scrape_data()` function to calculate and store technical indicators using libraries like `ta-lib` or `pandas-ta`.

### Modify Intervals

Change the default candle intervals in `constant_parameters.py`.

## 📚 References

- [Angel One SmartAPI Documentation](https://smartapi.angelbroking.com/docs)
- [SmartAPI Python SDK](https://github.com/angel-one/smartapi-python)
- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [Original TradingView Article](https://medium.com/@varungangu1/building-a-stock-analysis-mcp-server-with-docker-and-claude-desktop-eae4963dc3a7)

## 📝 License

This project is for educational purposes. Please check Angel One's terms of service for commercial use of their API.

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements!

## ⚠️ Disclaimer

This tool is for informational purposes only. Trading in stocks involves risk. Please do your own research and consult with financial advisors before making investment decisions. The developers are not responsible for any trading losses.

## 📧 Support

For Angel One API issues: [SmartAPI Support Forum](https://smartapi.angelone.in/smartapi/forum)

For MCP issues: Check the MCP documentation or Claude Desktop support

---

**Happy Trading! 📈💚**
