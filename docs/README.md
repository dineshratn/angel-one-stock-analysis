# Stock Analysis Website

Live website for Indian stock market analysis, ETF tracking, and portfolio recommendations.

## 🌐 Live Website

Visit: **https://dineshratn.github.io/angel-one-stock-analysis/**

## 📊 Features

- **Real-time Stock Analysis** - Nifty 50 stocks with P/E ratios and dividend yields
- **ETF Tracker** - 17+ Indian ETFs with live prices
- **Portfolio Recommendations** - AI-powered allocation strategies
- **Gold ETF Analysis** - Detailed comparison of 3 gold ETFs
- **10+ Free APIs** - Multiple data source options

## 🛠️ Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Custom CSS with responsive design
- **Data:** Python scripts for live data fetching
- **Deployment:** GitHub Pages

## 📁 Structure

```
docs/
├── index.html          # Homepage
├── css/
│   └── style.css      # Stylesheets
├── js/
│   └── main.js        # JavaScript
├── data/              # Generated data files
└── images/            # Assets
```

## 🚀 Local Development

1. Clone the repository
2. Open `docs/index.html` in a browser
3. Or use a local server:
   ```bash
   cd docs
   python -m http.server 8000
   ```
4. Visit `http://localhost:8000`

## 📊 Data Updates

The website displays static analysis. For live data:

1. Run analysis scripts:
   ```bash
   python analyze_all_stocks.py
   python indian_etfs.py
   python analyze_gold_etf.py
   ```

2. Regenerate website:
   ```bash
   python generate_website.py
   ```

3. Commit and push changes

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

Open source project for educational purposes.

## ⚠️ Disclaimer

This tool is for informational purposes only. Not financial advice.
Always do your own research and consult with financial advisors.

---

**Made with ❤️ for Indian investors**
