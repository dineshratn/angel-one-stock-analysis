# Free Stock Market APIs

This document lists all free stock market APIs integrated into this project and how to use them.

## Supported APIs

### 1. Yahoo Finance (yfinance) ⭐ **DEFAULT**
**Status:** ✅ Currently Implemented
**Rate Limit:** Unlimited (unofficial API)
**Coverage:** Global stocks, indices, cryptocurrencies
**Data:** Real-time quotes, historical data, company info

**Pros:**
- No API key required
- Excellent coverage
- Rich data including fundamentals
- Historical data up to decades

**Cons:**
- Unofficial API (may change without notice)
- No official support

**Usage:**
```python
import yfinance as yf
ticker = yf.Ticker("RELIANCE.NS")
data = ticker.history(period="1mo")
```

---

### 2. Alpha Vantage
**Status:** 🆕 New Addition
**Rate Limit:** 25 requests/day (free tier)
**API Key:** Required (free)
**Coverage:** Stocks, forex, crypto, technical indicators
**Sign up:** https://www.alphavantage.co/support/#api-key

**Pros:**
- Official API with good documentation
- Technical indicators built-in
- Fundamental data available
- Stable and reliable

**Cons:**
- Very limited free tier (25 calls/day)
- Requires API key

**Usage:**
```python
# Get API key from: https://www.alphavantage.co/support/#api-key
# Add to .env: ALPHAVANTAGE_API_KEY=your_key
```

---

### 3. Twelve Data
**Status:** 🆕 New Addition
**Rate Limit:** 800 requests/day (free tier)
**API Key:** Required (free)
**Coverage:** 10,000+ stocks, forex, crypto
**Sign up:** https://twelvedata.com/pricing

**Pros:**
- Higher free tier limit (800 calls/day)
- Real-time and historical data
- Good documentation
- WebSocket support

**Cons:**
- Requires API key
- Some features limited to paid tiers

**Usage:**
```python
# Get API key from: https://twelvedata.com/
# Add to .env: TWELVEDATA_API_KEY=your_key
```

---

### 4. Finnhub
**Status:** 🆕 New Addition
**Rate Limit:** 60 calls/minute (free tier)
**API Key:** Required (free)
**Coverage:** Stocks, forex, crypto, company news
**Sign up:** https://finnhub.io/register

**Pros:**
- Good rate limit for free tier
- Company news and sentiment
- Institutional ownership data
- IPO calendar

**Cons:**
- Requires API key
- Advanced features require premium

**Usage:**
```python
# Get API key from: https://finnhub.io/
# Add to .env: FINNHUB_API_KEY=your_key
```

---

### 5. Polygon.io
**Status:** 🆕 New Addition
**Rate Limit:** 5 calls/minute (free tier)
**API Key:** Required (free)
**Coverage:** US stocks, options, forex, crypto
**Sign up:** https://polygon.io/pricing

**Pros:**
- High-quality data
- Options data available
- Good documentation
- WebSocket support

**Cons:**
- Limited free tier (5 calls/min)
- Primarily US markets

**Usage:**
```python
# Get API key from: https://polygon.io/
# Add to .env: POLYGON_API_KEY=your_key
```

---

### 6. NSE India (Official)
**Status:** 🆕 New Addition
**Rate Limit:** Varies
**API Key:** Not required
**Coverage:** All NSE stocks
**Website:** https://www.nseindia.com/

**Pros:**
- Official NSE data
- No API key needed
- Real-time Indian market data
- Free and unlimited

**Cons:**
- Requires proper headers/cookies
- May need session management
- NSE-specific only

**Usage:**
```python
# Direct scraping from NSE website
# Requires headers and session handling
```

---

### 7. BSE India (Official)
**Status:** 🆕 New Addition
**Rate Limit:** Varies
**API Key:** Not required
**Coverage:** All BSE stocks
**Website:** https://www.bseindia.com/

**Pros:**
- Official BSE data
- No API key needed
- Free access

**Cons:**
- Requires web scraping
- BSE-specific only

---

### 8. Marketstack
**Status:** 🆕 New Addition
**Rate Limit:** 100 requests/month (free tier)
**API Key:** Required (free)
**Coverage:** 70+ exchanges worldwide
**Sign up:** https://marketstack.com/signup/free

**Pros:**
- Simple REST API
- Easy to use
- Good documentation

**Cons:**
- Very limited free tier
- Real-time data only in paid tiers

**Usage:**
```python
# Get API key from: https://marketstack.com/
# Add to .env: MARKETSTACK_API_KEY=your_key
```

---

### 9. IEX Cloud
**Status:** 🆕 New Addition
**Rate Limit:** 50,000 messages/month (free tier)
**API Key:** Required (free)
**Coverage:** US stocks, news, company data
**Sign up:** https://iexcloud.io/pricing

**Pros:**
- Generous free tier
- High-quality data
- Company fundamentals
- News and social sentiment

**Cons:**
- Primarily US markets
- Requires API key

**Usage:**
```python
# Get API key from: https://iexcloud.io/
# Add to .env: IEX_CLOUD_API_KEY=your_key
```

---

### 10. World Trading Data
**Status:** 🆕 New Addition
**Rate Limit:** 250 requests/day (free tier)
**API Key:** Required (free)
**Coverage:** Global stocks
**Sign up:** https://www.worldtradingdata.com/pricing

**Pros:**
- Global coverage
- Intraday data
- Mutual funds support

**Cons:**
- Limited free tier
- API may have delays

---

## Configuration

Add your API keys to `.env` file:

```env
# Yahoo Finance (no key needed - default)
USE_YFINANCE=true

# Alpha Vantage
ALPHAVANTAGE_API_KEY=your_key_here

# Twelve Data
TWELVEDATA_API_KEY=your_key_here

# Finnhub
FINNHUB_API_KEY=your_key_here

# Polygon.io
POLYGON_API_KEY=your_key_here

# Marketstack
MARKETSTACK_API_KEY=your_key_here

# IEX Cloud
IEX_CLOUD_API_KEY=your_key_here

# API Provider Selection (choose one)
# Options: yfinance, alphavantage, twelvedata, finnhub, polygon, nse, bse, marketstack, iexcloud
STOCK_API_PROVIDER=yfinance
```

## Rate Limit Comparison

| API | Free Tier Limit | API Key | Best For |
|-----|-----------------|---------|----------|
| Yahoo Finance | Unlimited | ❌ No | General use, historical data |
| Alpha Vantage | 25/day | ✅ Yes | Technical indicators |
| Twelve Data | 800/day | ✅ Yes | Moderate usage, real-time |
| Finnhub | 60/min | ✅ Yes | News, sentiment |
| Polygon.io | 5/min | ✅ Yes | High-quality US data |
| NSE India | Varies | ❌ No | Indian stocks (NSE) |
| BSE India | Varies | ❌ No | Indian stocks (BSE) |
| Marketstack | 100/month | ✅ Yes | Simple queries |
| IEX Cloud | 50k msg/month | ✅ Yes | US stocks, fundamentals |
| World Trading Data | 250/day | ✅ Yes | Global coverage |

## Recommendation

**For most users:** Start with **Yahoo Finance** (no setup required)

**For Indian markets specifically:** Use **NSE/BSE** official sources

**For reliable paid-tier features:** **Twelve Data** or **IEX Cloud** (generous free tiers)

**For news/sentiment:** **Finnhub**

**For technical analysis:** **Alpha Vantage**

## Getting Started

1. Choose your preferred API from the list above
2. Sign up and get API key (if required)
3. Add API key to `.env` file
4. Set `STOCK_API_PROVIDER` in `.env`
5. Run the application

## API Fallback Strategy

The application can be configured to automatically fallback to alternative APIs if one fails:

```env
# Enable fallback
API_FALLBACK_ENABLED=true

# Fallback order (comma-separated)
API_FALLBACK_ORDER=yfinance,twelvedata,alphavantage,finnhub
```

This ensures high availability even if one API is down or rate-limited.
