# GitHub Pages Setup Guide

## 🌐 Enable Your Website

Your website is ready! Follow these steps to make it live.

---

## 📝 Step-by-Step Instructions

### Step 1: Go to Repository Settings

1. Visit your GitHub repository: https://github.com/dineshratn/angel-one-stock-analysis
2. Click on **"Settings"** tab (top right)

### Step 2: Navigate to Pages Section

1. In the left sidebar, scroll down and click **"Pages"**
2. Or directly visit: https://github.com/dineshratn/angel-one-stock-analysis/settings/pages

### Step 3: Configure Source

1. Under **"Build and deployment"** section
2. Under **"Source"**, select **"Deploy from a branch"**
3. Under **"Branch"**:
   - Select **"main"** from the dropdown
   - Select **"/docs"** from the folder dropdown
   - Click **"Save"**

### Step 4: Wait for Deployment

1. GitHub will start building your site (takes 1-2 minutes)
2. Refresh the page after a minute
3. You'll see a message: **"Your site is live at..."**

### Step 5: Visit Your Website

Your website will be available at:

**https://dineshratn.github.io/angel-one-stock-analysis/**

---

## ✅ Verification

Once deployed, you should see:

- ✅ Professional homepage with stock analysis
- ✅ Nifty 50 top picks
- ✅ ETF tracker showcase
- ✅ Portfolio strategies
- ✅ API comparison
- ✅ Responsive mobile design

---

## 🔄 Updating the Website

To update your website with latest data:

### Method 1: Manual Update

1. Edit files in `docs/` folder
2. Commit changes:
   ```bash
   git add docs/
   git commit -m "Update website data"
   git push
   ```
3. GitHub Pages will auto-rebuild (1-2 minutes)

### Method 2: Regenerate from Analysis

1. Run latest analysis:
   ```bash
   python analyze_all_stocks.py
   python indian_etfs.py
   python analyze_gold_etf.py
   ```

2. Update website (if needed):
   ```bash
   python generate_website.py
   ```

3. Commit and push:
   ```bash
   git add -A
   git commit -m "Update with latest market data"
   git push
   ```

---

## 🎨 Customization

### Change Colors

Edit `docs/css/style.css`:

```css
:root {
    --primary-color: #2563eb;    /* Change main blue color */
    --secondary-color: #10b981;  /* Change green accent */
}
```

### Update Content

Edit `docs/index.html`:
- Stock picks in `<section id="stocks">`
- ETF data in `<section id="etfs">`
- Portfolio strategies in `<section id="portfolio">`

### Add New Pages

1. Create new HTML file in `docs/` (e.g., `docs/about.html`)
2. Link it in navigation or footer
3. Commit and push

---

## 🔧 Troubleshooting

### Website Not Loading?

1. Check GitHub Pages status in Settings > Pages
2. Ensure source is set to **main branch** and **/docs folder**
3. Wait 2-3 minutes after pushing changes
4. Clear browser cache (Ctrl+F5)

### 404 Error?

1. Verify `docs/index.html` exists
2. Check file permissions
3. Ensure all files are committed and pushed

### Styling Not Working?

1. Check browser console for errors (F12)
2. Verify `docs/css/style.css` exists
3. Check CSS file paths in HTML

### Changes Not Appearing?

1. Check Actions tab for build status
2. GitHub Pages caches - wait 2-5 minutes
3. Do hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

---

## 📊 Adding Live Data

To fetch and display real-time data:

### Option 1: GitHub Actions (Automated)

Create `.github/workflows/update-data.yml`:

```yaml
name: Update Stock Data
on:
  schedule:
    - cron: '0 10 * * 1-5'  # 10 AM on weekdays
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: python analyze_all_stocks.py
      - run: python generate_website.py
      - name: Commit changes
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add docs/
          git commit -m "Auto-update stock data" || true
          git push
```

### Option 2: Manual Updates

Run scripts locally and commit:

```bash
# Fetch latest data
python analyze_all_stocks.py
python indian_etfs.py

# Regenerate website
python generate_website.py

# Push to GitHub
git add -A
git commit -m "Update $(date +%Y-%m-%d)"
git push
```

---

## 🚀 Advanced Features

### Add Custom Domain

1. Buy a domain (e.g., stockanalysis.com)
2. In GitHub Settings > Pages, add your custom domain
3. Configure DNS with your domain provider:
   - Add CNAME record pointing to: `dineshratn.github.io`

### Enable HTTPS

- GitHub Pages automatically provides HTTPS
- Check "Enforce HTTPS" in Settings > Pages

### Add Analytics

Add Google Analytics to `docs/index.html`:

```html
<!-- Before </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## 📱 Mobile Optimization

The website is already mobile-responsive! Test on:

- Different screen sizes
- Chrome DevTools (F12 > Toggle device toolbar)
- Real mobile devices

---

## 🎉 Your Website is Ready!

Once you complete Step 3 above, your professional stock analysis website will be live at:

### 🌐 **https://dineshratn.github.io/angel-one-stock-analysis/**

Share it with friends, investors, and on social media!

---

## 📞 Need Help?

- **GitHub Pages Docs:** https://docs.github.com/en/pages
- **Repository Issues:** https://github.com/dineshratn/angel-one-stock-analysis/issues
- **GitHub Community:** https://github.com/orgs/community/discussions

---

**Happy Publishing! 🚀📊**
