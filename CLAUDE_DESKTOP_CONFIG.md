# Claude Desktop Configuration Guide

## Step 1: Locate Your Claude Desktop Config File

Since you're on Windows, the configuration file is located at:
```
%APPDATA%\Claude\claude_desktop_config.json
```

Or in full path:
```
C:\Users\dines\AppData\Roaming\Claude\claude_desktop_config.json
```

## Step 2: Edit the Configuration File

1. Open the file in a text editor (Notepad, VS Code, etc.)
2. If the file doesn't exist, create it with the following content
3. If it exists, add the MCP server configuration to the `mcpServers` section

## Configuration to Add

```json
{
  "mcpServers": {
    "stock-analysis": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "C:\\Users\\dines\\Downloads\\claud_stock_files\\angel-one-stock-analysis\\angel-one-stock-analysis\\src\\database:/app/src/database",
        "stock-analysis-yfinance"
      ]
    }
  }
}
```

**Note:** If you already have other MCP servers configured, just add the `"stock-analysis"` section inside the existing `"mcpServers"` object.

### Example with Multiple MCP Servers:
```json
{
  "mcpServers": {
    "existing-server": {
      "command": "...",
      "args": ["..."]
    },
    "stock-analysis": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "C:\\Users\\dines\\Downloads\\claud_stock_files\\angel-one-stock-analysis\\angel-one-stock-analysis\\src\\database:/app/src/database",
        "stock-analysis-yfinance"
      ]
    }
  }
}
```

## Step 3: Restart Claude Desktop

1. Completely quit Claude Desktop (right-click system tray icon → Quit)
2. Start Claude Desktop again
3. You should see the stock analysis tools available

## Step 4: Verify the Connection

In Claude Desktop, try asking:
```
"Show me the available stock market tools"
```

or

```
"Refresh the market data for Nifty 50 stocks"
```

## Available MCP Tools

Once connected, you'll have access to these tools:

1. **get_table_overview()** - View database schema and sample stock data
2. **query_database(sql_query)** - Run SQL queries on stock data
3. **refresh_market_data()** - Fetch latest data from Yahoo Finance
4. **get_historical_data(symbol, period, interval)** - Get historical candle data
5. **search_stocks(query)** - Search stocks by name or symbol

## Example Queries to Try

### Basic Queries
```
"Show me the database overview"
"Refresh the stock market data"
"Search for stocks containing 'HDFC'"
```

### SQL Queries
```
"Show me the top 10 stocks by volume"
"Find all banking stocks with price above 1000"
"What stocks hit their 52-week high?"
```

### Historical Data
```
"Get me 1 month of daily data for RELIANCE.NS"
"Fetch 5-minute candles for TCS.NS from the last 5 days"
```

### Analysis
```
"Which stocks have the highest volume today?"
"Compare RELIANCE.NS and TCS.NS performance"
"Show me all stocks with P/E ratio below 20"
```

## Troubleshooting

### Issue: MCP Server Not Showing Up
- Make sure Docker Desktop is running
- Check that the config file path is correct
- Verify the JSON syntax is valid (use jsonlint.com)
- Make sure you completely restarted Claude Desktop

### Issue: Database Error
- The database will be created automatically on first use
- Try running "refresh market data" first
- Check that the volume mount path exists

### Issue: Docker Permission Errors
- Make sure Docker Desktop has permission to access the folder
- Try running Docker Desktop as administrator

### Issue: No Stock Data
- Yahoo Finance may be slow - wait a minute and try again
- Markets may be closed (data is from last trading session)
- Some symbols may not be available on Yahoo Finance

## WSL Users (Like You!)

Since you're using WSL, you have two options:

### Option 1: Use Windows Path (Recommended)
Use the config shown above with Windows paths (C:\Users\...).

### Option 2: Use WSL Docker
If you want to run everything from WSL:
```json
{
  "mcpServers": {
    "stock-analysis": {
      "command": "wsl",
      "args": [
        "docker",
        "run",
        "-i",
        "--rm",
        "-v",
        "/mnt/c/Users/dines/Downloads/claud_stock_files/angel-one-stock-analysis/angel-one-stock-analysis/src/database:/app/src/database",
        "stock-analysis-yfinance"
      ]
    }
  }
}
```

## Need Help?

If you encounter any issues:
1. Check Docker Desktop is running: `docker ps`
2. Test the image manually: `docker run -it --rm stock-analysis-yfinance python -m src.stock_analysis.main`
3. Check Docker logs for errors
4. Verify the volume mount path exists

---

**You're all set!** 🚀 The stock analysis MCP server is now ready to use with Claude Desktop.
