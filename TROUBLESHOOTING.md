# Troubleshooting Guide - MCP Server Not Showing in Claude Desktop

## ✅ Configuration Updated!

I've updated your Claude Desktop config file to include **both**:
1. **MCP_DOCKER** - Docker MCP Gateway (your existing setup)
2. **stock-analysis** - Our new Stock Analysis MCP Server

## Next Steps to Enable the MCP Server

### Step 1: Completely Restart Claude Desktop

**Important:** You MUST do a full restart, not just minimize!

**On Windows:**
1. Look for Claude Desktop in the system tray (bottom-right corner, near the clock)
2. Right-click the Claude icon
3. Click **"Quit"** or **"Exit"**
4. Wait 5 seconds
5. Open Claude Desktop again

**Alternative:**
- Press `Ctrl+Shift+Esc` to open Task Manager
- Find "Claude Desktop" or "Claude"
- Click "End Task"
- Relaunch Claude Desktop

### Step 2: Check if MCP Tools Appear

After restarting, you should see MCP tools available in Claude Desktop:

**How to check:**
1. Start a new conversation
2. Look for a **tool icon** or **hammer icon** in the interface
3. Click it to see available tools
4. You should see stock analysis tools listed

**Or simply ask Claude:**
```
"What MCP tools do you have access to?"
```

### Step 3: Test the Stock Analysis Server

Try these commands in Claude Desktop:

```
"Show me the table overview"
```

or

```
"Refresh the market data for stocks"
```

If it works, you'll see Claude using the `get_table_overview()` or `refresh_market_data()` tools!

---

## Common Issues & Solutions

### Issue 1: MCP Tools Still Don't Show Up

**Possible Causes:**
- Claude Desktop wasn't fully restarted
- Docker Desktop isn't running
- Configuration file has JSON syntax errors

**Solutions:**

✅ **Check Docker Desktop is Running:**
```bash
docker ps
```
You should see a table (even if empty). If you get an error, start Docker Desktop.

✅ **Verify Config File Syntax:**
Open: `C:\Users\dines\AppData\Roaming\Claude\claude_desktop_config.json`

Should look exactly like this:
```json
{
  "mcpServers": {
    "MCP_DOCKER": {
      "command": "docker",
      "args": ["mcp", "gateway", "run"],
      "env": {
        "LOCALAPPDATA": "C:\\Users\\dines\\AppData\\Local",
        "ProgramData": "C:\\ProgramData",
        "ProgramFiles": "C:\\Program Files"
      }
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

**Common JSON mistakes:**
- ❌ Trailing comma after last item: `"stock-analysis-yfinance"]},`
- ❌ Missing quotes around strings
- ❌ Wrong slash direction: use `\\` for Windows paths

✅ **Check Claude Desktop Logs:**

Logs location: `C:\Users\dines\AppData\Roaming\Claude\logs\`

Look for recent `.log` files and search for:
- "stock-analysis" - to see if it's trying to load
- "error" or "ERROR" - to see what failed

---

### Issue 2: "Docker command not found" Error

**Cause:** Claude Desktop can't find Docker

**Solutions:**

✅ **Ensure Docker Desktop is running**
- Open Docker Desktop application
- Wait for it to fully start (whale icon in system tray should be steady, not animated)

✅ **Add Docker to System PATH**
1. Open System Properties → Environment Variables
2. Check if `C:\Program Files\Docker\Docker\resources\bin` is in PATH
3. If not, add it
4. Restart Claude Desktop

✅ **Alternative: Use full Docker path**

Update config to use full path:
```json
"stock-analysis": {
  "command": "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe",
  "args": [...]
}
```

---

### Issue 3: Docker Permission Errors

**Symptoms:**
- "permission denied" errors
- "cannot access /var/run/docker.sock"

**Solutions:**

✅ **Run Docker Desktop as Administrator**
- Right-click Docker Desktop
- Select "Run as administrator"

✅ **Check Docker Desktop Settings**
- Open Docker Desktop
- Go to Settings → Resources
- Ensure file sharing is enabled for the `C:\` drive

---

### Issue 4: Database Volume Mount Errors

**Symptoms:**
- "database not found" errors
- "permission denied" on database folder

**Solutions:**

✅ **Verify Database Folder Exists:**
```bash
ls "C:\Users\dines\Downloads\claud_stock_files\angel-one-stock-analysis\angel-one-stock-analysis\src\database"
```

✅ **Use WSL Path Instead (if on WSL):**

If using WSL, update config to use WSL path:
```json
"stock-analysis": {
  "command": "wsl",
  "args": [
    "docker", "run", "-i", "--rm",
    "-v", "/mnt/c/Users/dines/Downloads/claud_stock_files/angel-one-stock-analysis/angel-one-stock-analysis/src/database:/app/src/database",
    "stock-analysis-yfinance"
  ]
}
```

---

### Issue 5: Stock Data Fetch Fails

**Symptoms:**
- "No data available" errors
- Yahoo Finance connection errors

**Causes:**
- Internet connection issues
- Yahoo Finance rate limiting
- Market is closed (data will be from last session)

**Solutions:**

✅ **Check Internet Connection:**
```bash
ping finance.yahoo.com
```

✅ **Test Yahoo Finance Directly:**
```bash
docker run --rm stock-analysis-yfinance python -c "
import yfinance as yf
print(yf.Ticker('RELIANCE.NS').history(period='1d'))
"
```

✅ **Wait and Retry:**
Yahoo Finance sometimes has temporary slowdowns. Wait 1-2 minutes and try again.

---

## Debugging Commands

Run these from WSL/PowerShell to debug:

### Check Docker Image Exists:
```bash
docker images | grep stock-analysis-yfinance
```

### Test MCP Server Manually:
```bash
docker run -i --rm stock-analysis-yfinance python -m src.stock_analysis.main
```
Press `Ctrl+C` to stop.

### Test Stock Data Fetch:
```bash
./test_mcp_server.sh
```

### View Claude Desktop Logs:
```bash
ls /mnt/c/Users/dines/AppData/Roaming/Claude/logs/
cat /mnt/c/Users/dines/AppData/Roaming/Claude/logs/main.log
```

---

## How to Know It's Working

### Signs MCP Server is Connected:

1. ✅ **Tool Icons Visible:**
   - You'll see tool/hammer icons in Claude Desktop
   - Clicking shows "stock-analysis" tools

2. ✅ **Tools Work:**
   - Ask "show me the table overview"
   - Claude responds with database information

3. ✅ **No Error Messages:**
   - No "docker not found" errors
   - No "permission denied" errors

### What You Should See:

When you ask Claude to refresh market data, you'll see:
```
Using tool: refresh_market_data

[Tool output showing stock data being fetched]

Successfully refreshed market data for 50 Nifty stocks!
```

---

## Still Having Issues?

### Quick Checklist:

- [ ] Docker Desktop is running
- [ ] Config file has no JSON syntax errors
- [ ] Claude Desktop was FULLY restarted (not just minimized)
- [ ] Docker image exists: `docker images | grep stock-analysis`
- [ ] Database folder exists and is accessible
- [ ] No firewalls blocking Docker

### Get More Help:

1. **Check Docker logs:**
   ```bash
   docker logs <container-id>
   ```

2. **Run in interactive mode to see errors:**
   ```bash
   docker run -it --rm stock-analysis-yfinance /bin/bash
   python -m src.stock_analysis.main
   ```

3. **Verify config JSON is valid:**
   - Copy your config
   - Paste into https://jsonlint.com/
   - Fix any errors shown

---

## Success Checklist

Once it's working, you should be able to:

- [x] See MCP tools in Claude Desktop
- [x] Ask Claude to "refresh market data" and get results
- [x] Query the stock database
- [x] Get historical data for stocks
- [x] Search for stocks by name

**If all checks pass, congratulations! Your MCP server is working!** 🎉

---

## Need to Start Over?

If you want to rebuild everything:

```bash
cd /mnt/c/Users/dines/Downloads/claud_stock_files/angel-one-stock-analysis/angel-one-stock-analysis

# Remove old image
docker rmi stock-analysis-yfinance

# Rebuild
docker build -t stock-analysis-yfinance .

# Test
./test_mcp_server.sh

# Restart Claude Desktop
```

Then restart Claude Desktop and try again!
