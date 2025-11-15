"""
Stock Analysis MCP Server using Yahoo Finance (yfinance) with PostgreSQL
Free alternative - no API key required for Yahoo Finance
Uses Supabase PostgreSQL for persistent storage
"""

import os
import logging
from datetime import datetime
from typing import Any, Dict, List
from collections.abc import Hashable

import pandas as pd
import yfinance as yf
import psycopg2
from psycopg2.extras import execute_values
from mcp.server.fastmcp import FastMCP

from .constant_parameters import (
    COLUMNS_MAPPING,
    TABLE_SCHEMA,
    NIFTY_50_SYMBOLS,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("stock_analysis")


class StockDataError(Exception):
    """Custom exception for stock data errors"""
    pass


def get_database_connection():
    """
    Get PostgreSQL database connection from environment variables

    Returns:
        psycopg2 connection object
    """
    try:
        # Try DATABASE_URL first (standard for Supabase)
        database_url = os.getenv('DATABASE_URL')

        if database_url:
            conn = psycopg2.connect(database_url)
        else:
            # Fall back to individual components
            conn = psycopg2.connect(
                host=os.getenv('POSTGRES_HOST'),
                port=os.getenv('POSTGRES_PORT', '5432'),
                database=os.getenv('POSTGRES_DB', 'postgres'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD')
            )

        logger.info("Successfully connected to PostgreSQL database")
        return conn
    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")
        raise StockDataError(f"Database connection failed: {e}")


def initialize_database() -> None:
    """
    Initialize database with schema
    """
    try:
        conn = get_database_connection()
        cursor = conn.cursor()

        # Execute schema creation
        cursor.execute(TABLE_SCHEMA)
        conn.commit()

        cursor.close()
        conn.close()

        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise StockDataError(f"Database initialization failed: {e}")


def fetch_stock_data(symbols: List[str]) -> pd.DataFrame:
    """
    Fetch live market data for given symbols using yfinance

    Args:
        symbols: List of stock symbols (e.g., ['RELIANCE.NS', 'TCS.NS'])

    Returns:
        DataFrame with stock data
    """
    try:
        logger.info(f"Fetching market data for {len(symbols)} symbols")

        all_data = []

        # Fetch data for each symbol
        for symbol in symbols:
            try:
                ticker = yf.Ticker(symbol)

                # Get current info
                info = ticker.info

                # Get historical data (last 1 year to get 52-week high/low)
                hist = ticker.history(period="1y")

                if hist.empty:
                    logger.warning(f"No data available for {symbol}")
                    continue

                # Get latest data
                latest = hist.iloc[-1]

                # Prepare data record
                data_record = {
                    'symbol_token': symbol,
                    'trading_symbol': symbol.replace('.NS', '').replace('.BO', ''),
                    'name': info.get('longName', symbol),
                    'exchange': 'NSE' if '.NS' in symbol else 'BSE',
                    'instrument_type': 'EQ',
                    'last_price': info.get('currentPrice', float(latest['Close'])),
                    'open_price': float(latest['Open']),
                    'high_price': float(latest['High']),
                    'low_price': float(latest['Low']),
                    'close_price': float(latest['Close']),
                    'volume': int(latest['Volume']),
                    'week_high_52': info.get('fiftyTwoWeekHigh', float(hist['High'].max())),
                    'week_low_52': info.get('fiftyTwoWeekLow', float(hist['Low'].min())),
                    'market_cap': info.get('marketCap', None),
                    'pe_ratio': info.get('trailingPE', None),
                    'dividend_yield': info.get('dividendYield', None),
                    'last_updated': datetime.now()
                }

                all_data.append(data_record)
                logger.info(f"Fetched data for {symbol}: ₹{data_record['last_price']}")

            except Exception as e:
                logger.warning(f"Failed to fetch data for {symbol}: {e}")
                continue

        if not all_data:
            raise StockDataError("No stock data could be fetched")

        logger.info(f"Successfully fetched data for {len(all_data)} symbols")
        return pd.DataFrame(all_data)

    except Exception as e:
        logger.error(f"Failed to fetch market data: {e}")
        raise StockDataError(f"Market data fetch failed: {e}")


def scrape_data() -> None:
    """
    Fetch data from Yahoo Finance and store in PostgreSQL database
    """
    try:
        logger.info("Starting data scraping process")

        # Initialize database
        initialize_database()

        # Use Nifty 50 symbols
        symbols = NIFTY_50_SYMBOLS

        # Fetch market data
        market_df = fetch_stock_data(symbols)

        if market_df.empty:
            logger.warning("No market data fetched")
            return

        # Store in database
        conn = get_database_connection()
        cursor = conn.cursor()

        # Clear existing data
        cursor.execute("DELETE FROM stock_data")

        # Insert new data
        columns = list(market_df.columns)
        values = [tuple(row) for row in market_df.values]

        insert_query = f"""
            INSERT INTO stock_data ({', '.join(columns)})
            VALUES %s
            ON CONFLICT (symbol_token)
            DO UPDATE SET
                last_price = EXCLUDED.last_price,
                open_price = EXCLUDED.open_price,
                high_price = EXCLUDED.high_price,
                low_price = EXCLUDED.low_price,
                close_price = EXCLUDED.close_price,
                volume = EXCLUDED.volume,
                week_high_52 = EXCLUDED.week_high_52,
                week_low_52 = EXCLUDED.week_low_52,
                market_cap = EXCLUDED.market_cap,
                pe_ratio = EXCLUDED.pe_ratio,
                dividend_yield = EXCLUDED.dividend_yield,
                last_updated = EXCLUDED.last_updated
        """

        execute_values(cursor, insert_query, values)
        conn.commit()

        cursor.close()
        conn.close()

        logger.info(f"Stored {len(market_df)} records in database")
        logger.info("Data scraping completed successfully")

    except Exception as e:
        logger.error(f"Data scraping failed: {e}")
        raise StockDataError(f"Data scraping failed: {e}")


@mcp.tool()
def get_table_overview() -> str:
    """
    Get database table schema and preview with proper error handling.

    Returns:
        A formatted string containing table schema and sample data
    """
    logger.info("Getting table overview")

    try:
        conn = get_database_connection()

        # Get schema
        schema_query = """
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'stock_data'
            ORDER BY ordinal_position;
        """
        schema = pd.read_sql_query(schema_query, conn)

        # Get row count
        count_query = "SELECT COUNT(*) as count FROM stock_data;"
        count = pd.read_sql_query(count_query, conn)

        # Get sample data
        sample_query = "SELECT * FROM stock_data LIMIT 5;"
        sample = pd.read_sql_query(sample_query, conn)

        conn.close()

        # Format overview
        overview = f"""
DATABASE OVERVIEW
=================

Total Records: {count['count'].iloc[0]}

TABLE SCHEMA:
{schema.to_string(index=False)}

SAMPLE DATA (First 5 rows):
{sample.to_string(index=False)}
"""

        logger.info("Table overview generated successfully")
        return overview

    except Exception as e:
        logger.error(f"Failed to get table overview: {e}")
        raise StockDataError(f"Unable to get table overview: {e}")


@mcp.tool()
def query_database(sql_query: str) -> List[Dict[Hashable, Any]]:
    """
    Execute SQL query on the stock database and return results.

    Args:
        sql_query: SQL query to execute (SELECT statements only)

    Returns:
        List of dictionaries containing query results
    """
    logger.info(f"Executing database query: {sql_query[:100]}...")

    try:
        # Security: Only allow SELECT queries
        if not sql_query.strip().upper().startswith('SELECT'):
            raise StockDataError("Only SELECT queries are allowed")

        conn = get_database_connection()
        sql_output = pd.read_sql_query(sql_query, conn)
        conn.close()

        logger.info(f"Query returned {len(sql_output)} rows")
        return sql_output.to_dict(orient="records")

    except Exception as e:
        logger.error(f"Failed to execute database query: {e}")
        raise StockDataError(f"Database query execution failed: {e}")


@mcp.tool()
def refresh_market_data() -> str:
    """
    Force refresh of market data from Yahoo Finance.

    Returns:
        Status message indicating success or failure
    """
    logger.info("Manual refresh of market data requested")

    try:
        scrape_data()
        return "Market data refreshed successfully from Yahoo Finance"
    except Exception as e:
        logger.error(f"Failed to refresh market data: {e}")
        return f"Failed to refresh market data: {str(e)}"


@mcp.tool()
def get_historical_data(
    symbol: str,
    period: str = "1mo",
    interval: str = "1d"
) -> List[Dict[str, Any]]:
    """
    Fetch historical candle data for a specific symbol using Yahoo Finance.

    Args:
        symbol: Stock symbol (e.g., 'RELIANCE.NS' for NSE, 'RELIANCE.BO' for BSE)
        period: Data period - valid values: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        interval: Candle interval - valid values: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

    Returns:
        List of candle data dictionaries
    """
    logger.info(f"Fetching historical data for {symbol}")

    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period, interval=interval)

        if hist.empty:
            raise StockDataError(f"No historical data available for {symbol}")

        # Convert to list of dictionaries
        formatted_data = []
        for timestamp, row in hist.iterrows():
            formatted_data.append({
                'timestamp': timestamp.isoformat(),
                'open': float(row['Open']),
                'high': float(row['High']),
                'low': float(row['Low']),
                'close': float(row['Close']),
                'volume': int(row['Volume'])
            })

        logger.info(f"Fetched {len(formatted_data)} candles for {symbol}")
        return formatted_data

    except Exception as e:
        logger.error(f"Failed to fetch historical data: {e}")
        raise StockDataError(f"Historical data fetch failed: {e}")


@mcp.tool()
def search_stocks(query: str) -> List[Dict[str, Any]]:
    """
    Search for stocks by name or symbol.

    Args:
        query: Search term (company name or symbol)

    Returns:
        List of matching stocks with their details
    """
    logger.info(f"Searching for stocks matching: {query}")

    try:
        conn = get_database_connection()

        search_query = f"""
            SELECT trading_symbol, name, last_price, volume, exchange
            FROM stock_data
            WHERE trading_symbol ILIKE %s OR name ILIKE %s
            ORDER BY volume DESC
            LIMIT 10
        """

        results = pd.read_sql_query(search_query, conn, params=(f'%{query}%', f'%{query}%'))
        conn.close()

        return results.to_dict(orient="records")

    except Exception as e:
        logger.error(f"Stock search failed: {e}")
        raise StockDataError(f"Stock search failed: {e}")


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
