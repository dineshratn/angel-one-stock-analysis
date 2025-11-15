# Usage Examples - Angel One Stock Analysis MCP Server

Practical examples of how to use the MCP server with Claude Desktop.

## 🎯 Basic Examples

### 1. View Database Structure
```
You: "Show me the stock database schema"

Claude will use: get_table_overview()
```

### 2. Refresh Data
```
You: "Refresh the market data from Angel One"

Claude will use: refresh_market_data()
```

### 3. Check Available Stocks
```
You: "How many stocks are in the database?"

Claude will use: query_database("SELECT COUNT(*) FROM stock_data")
```

## 📊 Market Analysis Examples

### Top Performers by Volume
```
You: "Show me the top 10 stocks by trading volume today"

SQL Query Claude might use:
SELECT trading_symbol, name, last_price, volume
FROM stock_data
ORDER BY volume DESC
LIMIT 10;
```

### Price Range Filter
```
You: "Find stocks priced between 500 and 1000 rupees"

SQL Query:
SELECT trading_symbol, name, last_price, volume
FROM stock_data
WHERE last_price BETWEEN 500 AND 1000
ORDER BY volume DESC;
```

### High Volume, Low Price
```
You: "Show me stocks under 100 rupees with volume over 1 million"

SQL Query:
SELECT trading_symbol, name, last_price, volume
FROM stock_data
WHERE last_price < 100 AND volume > 1000000
ORDER BY volume DESC;
```

### Circuit Breakers
```
You: "Which stocks hit their upper circuit today?"

SQL Query:
SELECT trading_symbol, name, last_price, upper_circuit,
       ROUND((last_price / upper_circuit * 100), 2) as pct_of_circuit
FROM stock_data
WHERE last_price >= upper_circuit * 0.99
ORDER BY volume DESC;
```

### 52-Week Analysis
```
You: "Find stocks trading near their 52-week high"

SQL Query:
SELECT trading_symbol, name, last_price, week_high_52,
       ROUND((last_price / week_high_52 * 100), 2) as pct_of_52w_high
FROM stock_data
WHERE last_price >= week_high_52 * 0.95
ORDER BY volume DESC;
```

## 📈 Historical Data Examples

### Intraday Candles
```
You: "Get 5-minute candle data for Reliance (token: 2885) for today"

Claude will use: get_historical_data(
    symbol_token="2885",
    exchange="NSE",
    interval="FIVE_MINUTE",
    from_date="2024-11-14 09:15",
    to_date="2024-11-14 15:30"
)
```

### Daily Data for Analysis
```
You: "Fetch last 30 days of daily data for SBIN"

Claude will use: get_historical_data(
    symbol_token="3045",
    exchange="NSE",
    interval="ONE_DAY",
    from_date="2024-10-15 00:00",
    to_date="2024-11-14 23:59"
)
```

## 🔍 Advanced Queries

### Sector Leaders (Banking)
```
You: "Show me all banking stocks with their prices and volumes"

SQL Query:
SELECT trading_symbol, name, last_price, volume, 
       open_price, high_price, low_price
FROM stock_data
WHERE name LIKE '%BANK%'
   OR trading_symbol LIKE '%BANK%'
ORDER BY volume DESC;
```

### Gap Up/Down Analysis
```
You: "Find stocks with significant gap up from previous close"

SQL Query:
SELECT trading_symbol, name, 
       close_price as prev_close,
       open_price,
       last_price as current_price,
       ROUND(((open_price - close_price) / close_price * 100), 2) as gap_pct
FROM stock_data
WHERE ((open_price - close_price) / close_price * 100) > 2
ORDER BY gap_pct DESC;
```

### Volatility Check
```
You: "Show stocks with high intraday volatility"

SQL Query:
SELECT trading_symbol, name, last_price,
       high_price, low_price,
       ROUND(((high_price - low_price) / low_price * 100), 2) as intraday_range_pct
FROM stock_data
WHERE ((high_price - low_price) / low_price * 100) > 3
ORDER BY intraday_range_pct DESC
LIMIT 20;
```

## 🎨 Complex Analysis

### Multi-Criteria Screening
```
You: "Find liquid stocks (volume > 1M) trading below 500, 
      with intraday gains over 2%"

SQL Query:
SELECT trading_symbol, name, last_price, volume,
       ROUND(((last_price - open_price) / open_price * 100), 2) as gain_pct
FROM stock_data
WHERE volume > 1000000
  AND last_price < 500
  AND ((last_price - open_price) / open_price * 100) > 2
ORDER BY gain_pct DESC;
```

### Statistical Summary
```
You: "Give me statistics on the market - average price, total volume, etc."

SQL Query:
SELECT 
    COUNT(*) as total_stocks,
    ROUND(AVG(last_price), 2) as avg_price,
    ROUND(MIN(last_price), 2) as min_price,
    ROUND(MAX(last_price), 2) as max_price,
    SUM(volume) as total_volume,
    ROUND(AVG(volume), 0) as avg_volume
FROM stock_data;
```

## 🤖 Smart Assistant Queries

### Natural Language to SQL
Claude can understand natural language and convert it to SQL:

```
You: "What are the most expensive stocks in the database?"

Claude interprets as:
SELECT trading_symbol, name, last_price
FROM stock_data
ORDER BY last_price DESC
LIMIT 10;
```

### Comparative Analysis
```
You: "Compare the performance of RELIANCE and TCS today"

Claude might query:
SELECT trading_symbol, name, last_price, 
       open_price, volume,
       ROUND(((last_price - open_price) / open_price * 100), 2) as change_pct
FROM stock_data
WHERE trading_symbol IN ('RELIANCE-EQ', 'TCS-EQ');
```

### Portfolio Tracking
```
You: "I own INFY, WIPRO, and HCL. How are they performing?"

Claude will fetch current prices and calculate changes for your portfolio.
```

## 🔧 Troubleshooting Queries

### Check Data Freshness
```
SQL Query:
SELECT MAX(last_updated) as last_data_update
FROM stock_data;
```

### Count by Exchange
```
SQL Query:
SELECT exchange, COUNT(*) as count
FROM stock_data
GROUP BY exchange
ORDER BY count DESC;
```

### Identify Missing Data
```
SQL Query:
SELECT trading_symbol, name
FROM stock_data
WHERE last_price IS NULL
   OR volume IS NULL;
```

## 💡 Tips for Best Results

1. **Be Specific**: "Show me banking stocks" is better than "Show me stocks"

2. **Use Time Context**: Mention "today", "now", "current" for live data

3. **Combine Criteria**: "High volume, low price stocks under 100"

4. **Ask for Explanations**: "Explain why these stocks are good picks"

5. **Request Visualizations**: "Create a chart of top 10 stocks by volume" (Claude can create React artifacts)

## 🔄 Workflow Examples

### Daily Market Screening
```
1. "Refresh market data"
2. "Show me top 10 gainers by percentage"
3. "Which of these have volume over 5 million?"
4. "Get me historical data for the top 3"
5. "Create a summary report with key insights"
```

### Stock Research
```
1. "Get current price and volume for RELIANCE"
2. "Fetch last 7 days of daily data for RELIANCE"
3. "Compare RELIANCE with other oil & gas stocks"
4. "Show me 52-week high/low for RELIANCE"
```

### Options Trading Setup
```
1. "Find high volatility stocks today"
2. "Show me their historical volatility over 30 days"
3. "Which ones have upcoming earnings?"
4. "Get current options chain data" (requires extension)
```

## 📚 Learning Resources

To get symbol tokens:
```python
import pandas as pd
import requests

url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
df = pd.DataFrame(requests.get(url).json())

# Search for a stock
df[df['symbol'].str.contains('RELIANCE')]
```

Common Exchange Codes:
- `NSE` - National Stock Exchange (Equity)
- `BSE` - Bombay Stock Exchange
- `NFO` - NSE Futures & Options
- `MCX` - Multi Commodity Exchange

Interval Options for Historical Data:
- `ONE_MINUTE`, `THREE_MINUTE`, `FIVE_MINUTE`
- `TEN_MINUTE`, `FIFTEEN_MINUTE`, `THIRTY_MINUTE`
- `ONE_HOUR`, `ONE_DAY`

---

**Pro Tip**: Claude can remember context within a conversation, so you can build complex analyses step by step!

Example conversation:
```
You: "Show me high volume stocks"
Claude: [shows list]
You: "Now filter these to only show stocks under 200"
Claude: [refines the query]
You: "Great! Get me historical data for the top 3"
Claude: [fetches historical data]
```

Happy analyzing! 📊
