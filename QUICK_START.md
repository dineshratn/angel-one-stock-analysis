# Quick Start Guide - Angel One Stock Analysis MCP Server

Get up and running in 5 simple steps!

## ⚡ Quick Setup (10 minutes)

### Step 1: Get Angel One API Access (5 minutes)

1. **Create SmartAPI Account**:
   - Go to: https://smartapi.angelbroking.com/
   - Sign up (you'll need your Angel One trading account)

2. **Create an App**:
   - Click "Create an App"
   - Choose "Market Feed API"
   - Save your **API Key**

3. **Enable TOTP**:
   - Go to: https://smartapi.angelbroking.com/enable-totp
   - Save the **TOTP Token** (long string, not the QR code)

### Step 2: Configure Credentials (1 minute)

```bash
# Copy example file
cp .env.example .env

# Edit .env and add your credentials
nano .env  # or use any text editor
```

Fill in:
```env
ANGEL_API_KEY=your_api_key_here
ANGEL_CLIENT_ID=your_angel_client_id
ANGEL_PASSWORD=your_angel_password
ANGEL_TOTP_TOKEN=your_totp_token_here
```

### Step 3: Test Connection (1 minute)

```bash
# Install dependencies first
pip install smartapi-python pyotp python-dotenv

# Test your connection
python test_connection.py
```

You should see: ✅ ALL TESTS PASSED!

### Step 4: Build Docker Image (2 minutes)

```bash
# Build the image
docker build -t angel-one-stock-analysis .

# Verify
docker images | grep angel-one
```

### Step 5: Configure Claude Desktop (1 minute)

**Find config file**:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

**Add this** (replace paths with your actual paths):
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
        "/Users/yourname/projects/angel-one-stock-analysis/src/database:/app/src/database",
        "--env-file",
        "/Users/yourname/projects/angel-one-stock-analysis/.env",
        "angel-one-stock-analysis"
      ]
    }
  }
}
```

**Restart Claude Desktop**

## 🎉 You're Done!

Try asking Claude:
- "Show me the stock database overview"
- "Refresh market data and show me top 10 stocks by volume"
- "Which NSE stocks are available?"

## 🐛 Troubleshooting

### Error: "Authentication Failed"
- Double-check your credentials in `.env`
- Verify TOTP token is correct (not the QR code!)
- Run `python test_connection.py` to diagnose

### Error: "Database not found"
- First time use? Ask Claude to "refresh market data"
- Check Docker volume mount path is correct

### Error: "Docker container not starting"
- Ensure `.env` file exists
- Check volume mount paths are absolute paths
- Try: `docker run -i --rm --env-file .env angel-one-stock-analysis`

## 📖 Full Documentation

For detailed information, see [README.md](README.md)

## 🔗 Helpful Links

- [Angel One SmartAPI](https://smartapi.angelbroking.com/)
- [Enable TOTP](https://smartapi.angelbroking.com/enable-totp)
- [API Documentation](https://smartapi.angelbroking.com/docs)

---

Need help? Check the [troubleshooting section](README.md#-troubleshooting) in the full README.
