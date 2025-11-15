# Indian ETF Price Tracker

Track prices and analyze popular Exchange Traded Funds (ETFs) listed on NSE India.

## 🎯 What are ETFs?

**Exchange Traded Funds (ETFs)** are investment funds traded on stock exchanges, similar to stocks. They hold assets like stocks, commodities, or bonds and generally operate with an arbitrage mechanism designed to keep trading close to its net asset value.

### Benefits of ETFs:
- ✅ **Low Cost** - Much lower expense ratios than mutual funds (0.05% - 1%)
- ✅ **Instant Diversification** - Own multiple stocks with one purchase
- ✅ **Liquidity** - Trade anytime during market hours
- ✅ **Transparency** - Holdings disclosed daily
- ✅ **Tax Efficient** - Lower capital gains distributions

---

## 📊 Tracked ETFs (17 ETFs)

### **Equity ETFs - Large Cap**

| Symbol | Name | Index | AUM | Expense Ratio |
|--------|------|-------|-----|---------------|
| **NIFTYBEES.NS** | Nippon India ETF Nifty BeES | Nifty 50 | ₹10,000+ Cr | 0.05% ⭐ |
| **SETFNIF50.NS** | SBI ETF Nifty 50 | Nifty 50 | ₹12,000+ Cr | 0.07% ⭐ |
| **HDFCNIF100.NS** | HDFC Nifty 100 ETF | Nifty 100 | ₹800+ Cr | 0.35% |
| **HDFCSENSEX.NS** | HDFC Sensex ETF | BSE Sensex | ₹1,000+ Cr | 0.35% |

**Best for:** Long-term wealth creation, core portfolio holding

---

### **Equity ETFs - Mid Cap**

| Symbol | Name | Index | AUM | Expense Ratio |
|--------|------|-------|-----|---------------|
| **JUNIORBEES.NS** | Nippon India ETF Nifty Junior BeES | Nifty Next 50 | ₹2,500+ Cr | 0.36% |
| **SETFNN50.NS** | SBI ETF Nifty Next 50 | Nifty Next 50 | ₹2,000+ Cr | 0.30% |
| **ICICINXT50.NS** | ICICI Prudential Nifty Next 50 ETF | Nifty Next 50 | ₹1,500+ Cr | 0.31% |

**Best for:** Higher growth potential, satellite portfolio holding

---

### **Sectoral ETFs**

| Symbol | Name | Index | AUM | Expense Ratio |
|--------|------|-------|-----|---------------|
| **BANKBEES.NS** | Nippon India ETF Bank BeES | Nifty Bank | ₹5,500+ Cr | 0.43% |
| **PSUBNKBEES.NS** | Nippon India ETF PSU Bank BeES | Nifty PSU Bank | ₹1,200+ Cr | 0.52% |
| **ITBEES.NS** | Nippon India ETF Nifty IT BeES | Nifty IT | ₹800+ Cr | 0.62% |

**Best for:** Tactical allocation, sector-specific bets

---

### **Gold ETFs**

| Symbol | Name | Index | AUM | Expense Ratio |
|--------|------|-------|-----|---------------|
| **GOLDSHARE.NS** | Nippon India ETF Gold BeES | Domestic Gold | ₹6,500+ Cr | 1.00% |
| **GOLDBEES.NS** | Nippon India ETF Gold BeES (Old) | Domestic Gold | ₹2,000+ Cr | 1.00% |
| **HDFCGOLD.NS** | HDFC Gold ETF | Domestic Gold | ₹500+ Cr | 1.00% |

**Best for:** Portfolio diversification, inflation hedge

---

### **Liquid/Debt ETFs**

| Symbol | Name | Index | AUM | Expense Ratio |
|--------|------|-------|-----|---------------|
| **LIQUIDBEES.NS** | Nippon India ETF Liquid BeES | CRISIL Liquid Fund | ₹17,000+ Cr | 0.06% ⭐ |

**Best for:** Emergency fund, short-term parking, cash management

---

### **International ETFs**

| Symbol | Name | Index | AUM | Expense Ratio |
|--------|------|-------|-----|---------------|
| **HNGSNGBEES.NS** | Nippon India ETF Hang Seng BeES | Hang Seng | ₹400+ Cr | 0.70% |

**Best for:** International diversification, Hong Kong market exposure

---

### **Shariah-Compliant ETFs**

| Symbol | Name | Index | AUM | Expense Ratio |
|--------|------|-------|-----|---------------|
| **SHARIABEES.NS** | Nippon India ETF Nifty Shariah BeES | Nifty50 Shariah | ₹300+ Cr | 0.65% |

**Best for:** Shariah-compliant investing

---

## 🚀 How to Use the ETF Tracker

### **Run the Tracker**

```bash
# Basic usage
python indian_etfs.py

# Output: Live prices, analysis, and CSV export
```

### **What You Get**

1. **Live Prices** - Current NAV of all ETFs
2. **Category Analysis** - ETFs grouped by type
3. **Top Performers** - ETFs near 52-week highs
4. **Value Opportunities** - ETFs near 52-week lows
5. **Detailed Stats** - Volume, AUM, expense ratios
6. **CSV Export** - Data exported for further analysis

---

## 📈 Sample Output

```
====================================================================================================
INDIAN ETF PRICE TRACKER
====================================================================================================

📊 SUMMARY
Total ETFs Tracked:     16
Average Price:          ₹334.57
Highest Priced ETF:     Nippon India ETF Liquid BeES (₹1,000.00)
Lowest Priced ETF:      HDFC Nifty 100 ETF (₹27.15)

🏆 TOP PERFORMERS (Near 52-Week High)
BANKBEES.NS          Nippon India ETF Bank BeES               ₹603.29    0.28% below
NIFTYBEES.NS         Nippon India ETF Nifty BeES              ₹292.83    0.86% below

💎 VALUE OPPORTUNITIES (Near 52-Week Low)
LIQUIDBEES.NS        Nippon India ETF Liquid BeES             ₹1,000.00  4.61% above
SHARIABEES.NS        Nippon India ETF Nifty Shariah BeES      ₹506.40   15.11% above
```

---

## 💡 Investment Strategies Using ETFs

### **1. Core-Satellite Strategy**
**Core (70%):**
- NIFTYBEES.NS or SETFNIF50.NS (Nifty 50 exposure)

**Satellite (30%):**
- JUNIORBEES.NS (Mid-cap growth)
- BANKBEES.NS (Sector bet)
- GOLDSHARE.NS (Hedge)

### **2. Balanced Portfolio**
- **50%** - NIFTYBEES.NS (Large cap)
- **25%** - JUNIORBEES.NS (Mid cap)
- **15%** - GOLDSHARE.NS (Gold)
- **10%** - LIQUIDBEES.NS (Liquid)

### **3. Aggressive Growth**
- **40%** - JUNIORBEES.NS (Mid cap)
- **30%** - ITBEES.NS (IT sector)
- **30%** - BANKBEES.NS (Banking)

### **4. Conservative**
- **60%** - NIFTYBEES.NS (Stable large cap)
- **30%** - LIQUIDBEES.NS (Liquid/Safety)
- **10%** - GOLDSHARE.NS (Hedge)

---

## 🎯 Best ETFs by Use Case

### **For Beginners**
✅ **NIFTYBEES.NS** - Lowest expense ratio (0.05%), tracks Nifty 50
✅ **SETFNIF50.NS** - SBI's Nifty 50 ETF, very low cost (0.07%)

### **For Emergency Fund**
✅ **LIQUIDBEES.NS** - Trade at ₹1,000, highly liquid, low expense (0.06%)

### **For Gold Investment**
✅ **GOLDSHARE.NS** - Largest gold ETF, highest liquidity

### **For Tax Saving (ELSS Alternative)**
⚠️ Note: ETFs don't offer tax deduction like ELSS, but have lower expense ratios

### **For International Exposure**
✅ **HNGSNGBEES.NS** - Hong Kong market exposure

### **For Banking Sector Bet**
✅ **BANKBEES.NS** - Large AUM, good liquidity
✅ **PSUBNKBEES.NS** - PSU banks exposure (higher risk/reward)

### **For IT Sector Exposure**
✅ **ITBEES.NS** - Pure IT sector play

---

## 📊 Current Market Snapshot (Live Data)

Based on latest run (Nov 15, 2025):

### **Top 5 by Price:**
1. LIQUIDBEES.NS - ₹1,000.00 (by design)
2. JUNIORBEES.NS - ₹750.88
3. SETFNN50.NS - ₹744.14
4. BANKBEES.NS - ₹603.29
5. HNGSNGBEES.NS - ₹533.00

### **Most Liquid (by Volume):**
1. GOLDBEES.NS - 28.5M units
2. ITBEES.NS - 13.4M units
3. HDFCGOLD.NS - 5.1M units
4. NIFTYBEES.NS - 4.7M units
5. PSUBNKBEES.NS - 3.9M units

### **Near 52-Week Highs (Best Performers):**
1. ICICINXT50.NS - 0.00% below high
2. BANKBEES.NS - 0.28% below high
3. PSUBNKBEES.NS - 0.40% below high

### **Near 52-Week Lows (Value Picks):**
1. LIQUIDBEES.NS - 4.61% above low
2. ICICINXT50.NS - 11.64% above low
3. SHARIABEES.NS - 15.11% above low

---

## 💰 Cost Comparison

### **ETF vs Mutual Fund:**

| Feature | ETF | Index Mutual Fund | Active Mutual Fund |
|---------|-----|-------------------|-------------------|
| Expense Ratio | 0.05% - 1% | 0.1% - 0.5% | 1% - 2.5% |
| Trading | Intraday | End of day | End of day |
| Minimum Investment | 1 unit (~₹30-1000) | ₹500-5000 | ₹500-5000 |
| Exit Load | None | Sometimes | Usually 1% |
| Liquidity | High | Medium | Medium |
| Transparency | Daily | Daily | Monthly |

**ETF Advantage:** Lower costs = Higher returns over time!

Example: ₹10 lakh invested over 10 years
- **ETF (0.05%):** ₹19.67 lakh
- **Index Fund (0.3%):** ₹19.19 lakh
- **Active Fund (1.5%):** ₹17.31 lakh

---

## 🔍 How to Buy ETFs

### **Method 1: Demat Account (Recommended)**
1. Open demat account with any broker (Zerodha, Groww, Upstox, etc.)
2. Search for ETF symbol (e.g., NIFTYBEES.NS)
3. Buy like a stock during market hours

### **Method 2: Mutual Fund Platform**
Some ETFs available on platforms like Coin, Groww, etc.

### **Method 3: Direct with AMC**
Create and redeem in large units (not practical for retail)

---

## 📝 Important Notes

### **Tax Treatment:**
- **Equity ETFs:** Taxed like equity shares
  - LTCG (>1 year): 12.5% above ₹1.25 lakh
  - STCG (<1 year): 20%
- **Gold ETFs:** Taxed like non-equity
  - LTCG (>3 years): 20% with indexation
  - STCG (<3 years): As per slab
- **Liquid ETFs:** Taxed like debt funds

### **Tracking Error:**
ETFs may not perfectly track their index. Lower is better.
- **Excellent:** < 0.25%
- **Good:** 0.25% - 0.5%
- **Average:** 0.5% - 1%

### **Expense Ratios (Lowest is Best):**
- **NIFTYBEES.NS:** 0.05% ⭐ **LOWEST**
- **LIQUIDBEES.NS:** 0.06% ⭐
- **SETFNIF50.NS:** 0.07% ⭐

---

## 🚀 Getting Started

### **For Complete Beginners:**
Start with **NIFTYBEES.NS** or **SETFNIF50.NS**
- Low cost
- Diversified (50 stocks)
- Easy to understand
- Highly liquid

### **Sample First Investment:**
```
Buy: 10 units of NIFTYBEES.NS @ ₹293
Investment: ₹2,930
Exposure: Entire Nifty 50 index
```

---

## 📞 Support & Resources

- **NSE ETF List:** https://www.nseindia.com/market-data/exchange-traded-funds-etf
- **SEBI ETF Guidelines:** https://www.sebi.gov.in/
- **AMC Websites:**
  - Nippon India: https://www.nipponindiaetf.com/
  - SBI MF: https://www.sbimf.com/
  - HDFC MF: https://www.hdfcfund.com/

---

## ⚠️ Disclaimer

This tool is for informational purposes only. ETF investments are subject to market risks. Past performance is not indicative of future returns. Please:
- Do your own research
- Understand the underlying index
- Consider your risk tolerance
- Consult a financial advisor
- Read the scheme documents

---

**Track Smart. Invest Smarter! 📈💰**
