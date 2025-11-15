"""
Stock Market API Providers
Abstraction layer for multiple free stock market APIs
"""

import os
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import pandas as pd

# API Libraries
import yfinance as yf
import requests
from time import sleep

logger = logging.getLogger(__name__)


class StockAPIProvider(ABC):
    """Abstract base class for stock API providers"""

    @abstractmethod
    def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current quote for a symbol"""
        pass

    @abstractmethod
    def get_historical_data(self, symbol: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
        """Get historical data for a symbol"""
        pass

    @abstractmethod
    def get_company_info(self, symbol: str) -> Dict[str, Any]:
        """Get company information"""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if API is available and properly configured"""
        pass


class YahooFinanceProvider(StockAPIProvider):
    """Yahoo Finance API Provider (yfinance)"""

    def __init__(self):
        self.name = "Yahoo Finance"

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current quote"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            hist = ticker.history(period="1d")

            if hist.empty:
                return {}

            latest = hist.iloc[-1]

            return {
                'symbol': symbol,
                'last_price': info.get('currentPrice', float(latest['Close'])),
                'open': float(latest['Open']),
                'high': float(latest['High']),
                'low': float(latest['Low']),
                'close': float(latest['Close']),
                'volume': int(latest['Volume']),
                'timestamp': datetime.now()
            }
        except Exception as e:
            logger.error(f"Yahoo Finance error for {symbol}: {e}")
            return {}

    def get_historical_data(self, symbol: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
        """Get historical data"""
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period, interval=interval)
            return hist
        except Exception as e:
            logger.error(f"Yahoo Finance historical data error for {symbol}: {e}")
            return pd.DataFrame()

    def get_company_info(self, symbol: str) -> Dict[str, Any]:
        """Get company information"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            return info
        except Exception as e:
            logger.error(f"Yahoo Finance company info error for {symbol}: {e}")
            return {}

    def is_available(self) -> bool:
        """Check if Yahoo Finance is available"""
        return True  # No API key needed


class AlphaVantageProvider(StockAPIProvider):
    """Alpha Vantage API Provider"""

    def __init__(self):
        self.name = "Alpha Vantage"
        self.api_key = os.getenv('ALPHAVANTAGE_API_KEY')
        self.base_url = "https://www.alphavantage.co/query"

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current quote"""
        try:
            # Remove exchange suffix for Alpha Vantage
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            params = {
                'function': 'GLOBAL_QUOTE',
                'symbol': clean_symbol,
                'apikey': self.api_key
            }

            response = requests.get(self.base_url, params=params)
            data = response.json()

            if 'Global Quote' not in data:
                return {}

            quote = data['Global Quote']

            return {
                'symbol': symbol,
                'last_price': float(quote.get('05. price', 0)),
                'open': float(quote.get('02. open', 0)),
                'high': float(quote.get('03. high', 0)),
                'low': float(quote.get('04. low', 0)),
                'close': float(quote.get('08. previous close', 0)),
                'volume': int(quote.get('06. volume', 0)),
                'timestamp': datetime.now()
            }
        except Exception as e:
            logger.error(f"Alpha Vantage error for {symbol}: {e}")
            return {}

    def get_historical_data(self, symbol: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
        """Get historical data"""
        try:
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            params = {
                'function': 'TIME_SERIES_DAILY',
                'symbol': clean_symbol,
                'apikey': self.api_key,
                'outputsize': 'full'
            }

            response = requests.get(self.base_url, params=params)
            data = response.json()

            if 'Time Series (Daily)' not in data:
                return pd.DataFrame()

            df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
            df.index = pd.to_datetime(df.index)
            df = df.rename(columns={
                '1. open': 'Open',
                '2. high': 'High',
                '3. low': 'Low',
                '4. close': 'Close',
                '5. volume': 'Volume'
            })
            df = df.astype(float)

            return df.sort_index()
        except Exception as e:
            logger.error(f"Alpha Vantage historical error for {symbol}: {e}")
            return pd.DataFrame()

    def get_company_info(self, symbol: str) -> Dict[str, Any]:
        """Get company information"""
        try:
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            params = {
                'function': 'OVERVIEW',
                'symbol': clean_symbol,
                'apikey': self.api_key
            }

            response = requests.get(self.base_url, params=params)
            data = response.json()

            return data
        except Exception as e:
            logger.error(f"Alpha Vantage company info error for {symbol}: {e}")
            return {}

    def is_available(self) -> bool:
        """Check if API key is configured"""
        return bool(self.api_key)


class TwelveDataProvider(StockAPIProvider):
    """Twelve Data API Provider"""

    def __init__(self):
        self.name = "Twelve Data"
        self.api_key = os.getenv('TWELVEDATA_API_KEY')
        self.base_url = "https://api.twelvedata.com"

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current quote"""
        try:
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            params = {
                'symbol': clean_symbol,
                'apikey': self.api_key
            }

            response = requests.get(f"{self.base_url}/quote", params=params)
            data = response.json()

            if 'code' in data and data['code'] >= 400:
                return {}

            return {
                'symbol': symbol,
                'last_price': float(data.get('close', 0)),
                'open': float(data.get('open', 0)),
                'high': float(data.get('high', 0)),
                'low': float(data.get('low', 0)),
                'close': float(data.get('previous_close', 0)),
                'volume': int(data.get('volume', 0)),
                'timestamp': datetime.now()
            }
        except Exception as e:
            logger.error(f"Twelve Data error for {symbol}: {e}")
            return {}

    def get_historical_data(self, symbol: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
        """Get historical data"""
        try:
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            params = {
                'symbol': clean_symbol,
                'interval': interval,
                'apikey': self.api_key,
                'outputsize': 5000
            }

            response = requests.get(f"{self.base_url}/time_series", params=params)
            data = response.json()

            if 'values' not in data:
                return pd.DataFrame()

            df = pd.DataFrame(data['values'])
            df['datetime'] = pd.to_datetime(df['datetime'])
            df = df.set_index('datetime')
            df = df.rename(columns={
                'open': 'Open',
                'high': 'High',
                'low': 'Low',
                'close': 'Close',
                'volume': 'Volume'
            })
            df = df.astype(float)

            return df.sort_index()
        except Exception as e:
            logger.error(f"Twelve Data historical error for {symbol}: {e}")
            return pd.DataFrame()

    def get_company_info(self, symbol: str) -> Dict[str, Any]:
        """Get company information"""
        try:
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            params = {
                'symbol': clean_symbol,
                'apikey': self.api_key
            }

            response = requests.get(f"{self.base_url}/profile", params=params)
            data = response.json()

            return data
        except Exception as e:
            logger.error(f"Twelve Data company info error for {symbol}: {e}")
            return {}

    def is_available(self) -> bool:
        """Check if API key is configured"""
        return bool(self.api_key)


class FinnhubProvider(StockAPIProvider):
    """Finnhub API Provider"""

    def __init__(self):
        self.name = "Finnhub"
        self.api_key = os.getenv('FINNHUB_API_KEY')
        self.base_url = "https://finnhub.io/api/v1"

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current quote"""
        try:
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            headers = {'X-Finnhub-Token': self.api_key}
            response = requests.get(f"{self.base_url}/quote?symbol={clean_symbol}", headers=headers)
            data = response.json()

            if not data or 'c' not in data:
                return {}

            return {
                'symbol': symbol,
                'last_price': float(data.get('c', 0)),  # current price
                'open': float(data.get('o', 0)),
                'high': float(data.get('h', 0)),
                'low': float(data.get('l', 0)),
                'close': float(data.get('pc', 0)),  # previous close
                'volume': 0,  # Not provided in quote
                'timestamp': datetime.now()
            }
        except Exception as e:
            logger.error(f"Finnhub error for {symbol}: {e}")
            return {}

    def get_historical_data(self, symbol: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
        """Get historical data"""
        try:
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            # Convert period to timestamps
            end_time = int(datetime.now().timestamp())
            if period == "1mo":
                start_time = int((datetime.now() - timedelta(days=30)).timestamp())
            elif period == "3mo":
                start_time = int((datetime.now() - timedelta(days=90)).timestamp())
            elif period == "1y":
                start_time = int((datetime.now() - timedelta(days=365)).timestamp())
            else:
                start_time = int((datetime.now() - timedelta(days=30)).timestamp())

            # Map interval
            resolution = 'D' if interval == '1d' else interval

            headers = {'X-Finnhub-Token': self.api_key}
            url = f"{self.base_url}/stock/candle?symbol={clean_symbol}&resolution={resolution}&from={start_time}&to={end_time}"
            response = requests.get(url, headers=headers)
            data = response.json()

            if data.get('s') != 'ok':
                return pd.DataFrame()

            df = pd.DataFrame({
                'Open': data['o'],
                'High': data['h'],
                'Low': data['l'],
                'Close': data['c'],
                'Volume': data['v']
            })
            df.index = pd.to_datetime(data['t'], unit='s')

            return df.sort_index()
        except Exception as e:
            logger.error(f"Finnhub historical error for {symbol}: {e}")
            return pd.DataFrame()

    def get_company_info(self, symbol: str) -> Dict[str, Any]:
        """Get company information"""
        try:
            clean_symbol = symbol.replace('.NS', '').replace('.BO', '')

            headers = {'X-Finnhub-Token': self.api_key}
            response = requests.get(f"{self.base_url}/stock/profile2?symbol={clean_symbol}", headers=headers)
            data = response.json()

            return data
        except Exception as e:
            logger.error(f"Finnhub company info error for {symbol}: {e}")
            return {}

    def is_available(self) -> bool:
        """Check if API key is configured"""
        return bool(self.api_key)


class NSEIndiaProvider(StockAPIProvider):
    """NSE India Official API Provider"""

    def __init__(self):
        self.name = "NSE India"
        self.base_url = "https://www.nseindia.com/api"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
        })
        self._init_session()

    def _init_session(self):
        """Initialize session with NSE"""
        try:
            self.session.get("https://www.nseindia.com", timeout=10)
        except:
            pass

    def get_quote(self, symbol: str) -> Dict[str, Any]:
        """Get current quote"""
        try:
            clean_symbol = symbol.replace('.NS', '')

            url = f"{self.base_url}/quote-equity?symbol={clean_symbol}"
            response = self.session.get(url, timeout=10)
            data = response.json()

            if 'priceInfo' not in data:
                return {}

            price_info = data['priceInfo']

            return {
                'symbol': symbol,
                'last_price': float(price_info.get('lastPrice', 0)),
                'open': float(price_info.get('open', 0)),
                'high': float(price_info.get('intraDayHighLow', {}).get('max', 0)),
                'low': float(price_info.get('intraDayHighLow', {}).get('min', 0)),
                'close': float(price_info.get('close', 0)),
                'volume': int(data.get('preOpenMarket', {}).get('totalTradedVolume', 0)),
                'timestamp': datetime.now()
            }
        except Exception as e:
            logger.error(f"NSE India error for {symbol}: {e}")
            return {}

    def get_historical_data(self, symbol: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
        """Get historical data (limited support)"""
        logger.warning("NSE India historical data requires advanced scraping")
        return pd.DataFrame()

    def get_company_info(self, symbol: str) -> Dict[str, Any]:
        """Get company information"""
        try:
            clean_symbol = symbol.replace('.NS', '')

            url = f"{self.base_url}/quote-equity?symbol={clean_symbol}"
            response = self.session.get(url, timeout=10)
            data = response.json()

            return data.get('info', {})
        except Exception as e:
            logger.error(f"NSE India company info error for {symbol}: {e}")
            return {}

    def is_available(self) -> bool:
        """Check if NSE API is available"""
        return True


class APIProviderFactory:
    """Factory to create and manage API providers"""

    _providers = {
        'yfinance': YahooFinanceProvider,
        'alphavantage': AlphaVantageProvider,
        'twelvedata': TwelveDataProvider,
        'finnhub': FinnhubProvider,
        'nse': NSEIndiaProvider,
    }

    @classmethod
    def get_provider(cls, provider_name: str = None) -> StockAPIProvider:
        """Get API provider instance"""
        if provider_name is None:
            provider_name = os.getenv('STOCK_API_PROVIDER', 'yfinance')

        provider_name = provider_name.lower()

        if provider_name not in cls._providers:
            logger.warning(f"Unknown provider: {provider_name}, falling back to yfinance")
            provider_name = 'yfinance'

        provider_class = cls._providers[provider_name]
        provider = provider_class()

        if not provider.is_available():
            logger.warning(f"{provider.name} is not available, falling back to yfinance")
            return YahooFinanceProvider()

        logger.info(f"Using API provider: {provider.name}")
        return provider

    @classmethod
    def get_available_providers(cls) -> List[str]:
        """Get list of available provider names"""
        return list(cls._providers.keys())

    @classmethod
    def get_provider_with_fallback(cls, fallback_order: List[str] = None) -> StockAPIProvider:
        """Get provider with automatic fallback"""
        if fallback_order is None:
            fallback_order_str = os.getenv('API_FALLBACK_ORDER', 'yfinance,twelvedata,alphavantage')
            fallback_order = [p.strip() for p in fallback_order_str.split(',')]

        for provider_name in fallback_order:
            try:
                provider = cls.get_provider(provider_name)
                if provider.is_available():
                    return provider
            except Exception as e:
                logger.error(f"Failed to initialize {provider_name}: {e}")
                continue

        # Final fallback to yfinance
        return YahooFinanceProvider()
