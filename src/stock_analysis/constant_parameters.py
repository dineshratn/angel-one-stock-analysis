"""
Configuration parameters for Yahoo Finance integration
"""

# Database columns mapping (from Yahoo Finance to our DB schema)
COLUMNS_MAPPING = {
    "symbol": "trading_symbol",
    "longName": "name",
    "currentPrice": "last_price",
    "open": "open_price",
    "dayHigh": "high_price",
    "dayLow": "low_price",
    "previousClose": "close_price",
    "volume": "volume",
    "fiftyTwoWeekHigh": "week_high_52",
    "fiftyTwoWeekLow": "week_low_52",
}

# Nifty 50 stock symbols (with .NS suffix for NSE)
NIFTY_50_SYMBOLS = [
    "RELIANCE.NS",
    "TCS.NS",
    "HDFCBANK.NS",
    "INFY.NS",
    "ICICIBANK.NS",
    "HINDUNILVR.NS",
    "ITC.NS",
    "SBIN.NS",
    "BHARTIARTL.NS",
    "BAJFINANCE.NS",
    "KOTAKBANK.NS",
    "LT.NS",
    "HCLTECH.NS",
    "AXISBANK.NS",
    "ASIANPAINT.NS",
    "MARUTI.NS",
    "SUNPHARMA.NS",
    "TITAN.NS",
    "ULTRACEMCO.NS",
    "NESTLEIND.NS",
    "WIPRO.NS",
    "BAJAJFINSV.NS",
    "ONGC.NS",
    "NTPC.NS",
    "TATAMOTORS.NS",
    "TECHM.NS",
    "M&M.NS",
    "POWERGRID.NS",
    "ADANIENT.NS",
    "TATASTEEL.NS",
    "COALINDIA.NS",
    "BAJAJ-AUTO.NS",
    "INDUSINDBK.NS",
    "JSWSTEEL.NS",
    "DRREDDY.NS",
    "SBILIFE.NS",
    "GRASIM.NS",
    "CIPLA.NS",
    "APOLLOHOSP.NS",
    "TATACONSUM.NS",
    "EICHERMOT.NS",
    "BPCL.NS",
    "HINDALCO.NS",
    "DIVISLAB.NS",
    "BRITANNIA.NS",
    "HEROMOTOCO.NS",
    "ADANIPORTS.NS",
    "HDFCLIFE.NS",
    "UPL.NS",
    "LTIM.NS",
]

# Additional popular stocks (optional, can be added)
BANK_NIFTY_SYMBOLS = [
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "KOTAKBANK.NS",
    "AXISBANK.NS",
    "SBIN.NS",
    "INDUSINDBK.NS",
    "BANDHANBNK.NS",
    "FEDERALBNK.NS",
    "IDFCFIRSTB.NS",
    "PNB.NS",
]

# Database table schema with additional useful columns (PostgreSQL)
TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS stock_data (
    symbol_token TEXT PRIMARY KEY,
    trading_symbol TEXT NOT NULL,
    name TEXT,
    exchange TEXT,
    instrument_type TEXT,
    last_price NUMERIC,
    open_price NUMERIC,
    high_price NUMERIC,
    low_price NUMERIC,
    close_price NUMERIC,
    volume BIGINT,
    week_high_52 NUMERIC,
    week_low_52 NUMERIC,
    market_cap BIGINT,
    pe_ratio NUMERIC,
    dividend_yield NUMERIC,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_trading_symbol ON stock_data(trading_symbol);
CREATE INDEX IF NOT EXISTS idx_exchange ON stock_data(exchange);
CREATE INDEX IF NOT EXISTS idx_last_price ON stock_data(last_price);
CREATE INDEX IF NOT EXISTS idx_volume ON stock_data(volume);
"""
