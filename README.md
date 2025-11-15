# Angel One Stock Analysis MCP Server

A Model Context Protocol (MCP) server that integrates Angel One's SmartAPI with Claude Desktop for real-time stock market analysis. This project is adapted from the TradingView-based MCP server to work with Indian stock markets via Angel One.

## 🌟 Features

- **Live Market Data**: Fetch real-time stock prices, quotes, and market data from Angel One
- **Historical Data**: Access historical candle data for technical analysis
- **SQLite Storage**: Daily databases for historical tracking
- **MCP Integration**: Seamless integration with Claude Desktop
- **Docker Support**: Containerized deployment for consistency

## 📋 Prerequisites

1. **Angel One Account**: You need an active Angel One trading account
2. **SmartAPI Access**: Register and get API credentials
3. **Docker**: For containerized deployment
4. **Claude Desktop**: Latest version installed

## 🚀 Setup Guide

### Step 1: Get Angel One API Credentials

1. **Sign up for SmartAPI**:
   - Visit: https://smartapi.angelbroking.com/
   - Click "Sign Up" and create an account

2. **Create an App**:
   - Go to dashboard and click "Create an App"
   - Select API Type: "Market Feed API" and "Historical Data API"
   - Enter app name and details
   - You'll receive an **API Key** and **Secret Key**

3. **Enable TOTP** (Time-based One-Time Password):
   - Visit: https://smartapi.angelbroking.com/enable-totp
   - Enter your Angel One client ID and password
   - Enter OTP sent to your email/mobile
   - You'll see a QR code and a **TOTP token string** - save this!

### Step 2: Configure Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and fill in your credentials:
```env
ANGEL_API_KEY=your_api_key_from_smartapi
ANGEL_CLIENT_ID=your_angel_one_client_id
ANGEL_PASSWORD=your_angel_one_password
ANGEL_TOTP_TOKEN=your_totp_token_from_step3
```

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
