# CRITICAL: How to Properly Restart Claude Desktop

## ✅ Configuration Updated!

Your config file has been updated with the **FULL Docker path** which should work better:

```json
{
  "mcpServers": {
    "MCP_DOCKER": { ... },
    "stock-analysis": {
      "command": "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe",
      "args": ["run", "-i", "--rm", "-v", "...", "stock-analysis-yfinance"]
    }
  }
}
```

---

## 🔴 STEP-BY-STEP: Restart Claude Desktop (CRITICAL)

### Method 1: Complete Shutdown (RECOMMENDED)

1. **Close ALL Claude Desktop windows**
   - Click X on every Claude window
   - Don't just minimize!

2. **Find Claude in System Tray**
   - Look bottom-right corner near clock
   - Look for Claude icon (blue/white icon)

3. **Right-Click → Quit**
   - Right-click the Claude icon
   - Click "Quit" or "Exit"
   - **Wait 10 seconds**

4. **Verify it's closed**
   - Open Task Manager (`Ctrl+Shift+Esc`)
   - Look for "Claude Desktop" or "Claude" processes
   - If found, right-click → "End Task"

5. **Start Claude Desktop fresh**
   - Search for "Claude" in Start menu
   - Click to open
   - **Wait for it to fully load** (30 seconds)

### Method 2: Task Manager Force Close

1. Press `Ctrl+Shift+Esc`
2. Find "Claude Desktop" or "Claude"
3. Right-click → "End Task"
4. Wait 10 seconds
5. Open Claude Desktop again

---

## 🔍 How to Check if It's Working

### After Restarting:

1. **Open Claude Desktop**
2. **Start a NEW conversation**
3. **Look for the hammer/tool icon** in the interface
4. **Click it** - you should see available tools

### Or ask Claude:

```
What MCP servers are connected?
```

or

```
List all available tools
```

You should see:
- ✅ `MCP_DOCKER` tools (if any)
- ✅ `stock-analysis` tools:
  - get_table_overview
  - query_database
  - refresh_market_data
  - get_historical_data
  - search_stocks

---

## 🧪 Test Commands

Once restarted, try these in Claude Desktop:

### Test 1: Check Tools
```
What tools do you have available?
```

### Test 2: Refresh Data
```
Refresh the stock market data
```

### Test 3: View Database
```
Show me the database overview
```

### Test 4: Search Stocks
```
Search for stocks containing "RELIANCE"
```

---

## 📋 Checklist Before Restarting

- [ ] Docker Desktop is running
- [ ] Config file is at: `C:\Users\dines\AppData\Roaming\Claude\claude_desktop_config.json`
- [ ] Config has both `MCP_DOCKER` and `stock-analysis`
- [ ] Docker image exists: Run `docker images | grep stock-analysis-yfinance`

---

## ❌ Still Not Working?

### Check Logs After Restart

After you restart Claude Desktop and try to use it, check the logs:

```bash
# In WSL/PowerShell:
ls /mnt/c/Users/dines/AppData/Roaming/Claude/logs/

# Look for:
# - mcp-server-stock-analysis.log (should appear after restart)
# - main.log (check for errors)
```

If `mcp-server-stock-analysis.log` **DOES NOT EXIST** after restart:
- Claude Desktop isn't loading the server
- There's a configuration issue

### View the logs:

```bash
# Main log
tail -50 /mnt/c/Users/dines/AppData/Roaming/Claude/logs/main.log

# Stock analysis log (if exists)
tail -50 /mnt/c/Users/dines/AppData/Roaming/Claude/logs/mcp-server-stock-analysis.log
```

---

## 🔧 Alternative: Manual Test

Test the Docker command manually to ensure it works:

```bash
"C:\Program Files\Docker\Docker\resources\bin\docker.exe" run -i --rm stock-analysis-yfinance python -c "print('MCP Server OK')"
```

This should print "MCP Server OK" with no errors.

---

## 📞 What to Report if Still Not Working

If it still doesn't work after restarting, check:

1. **Does the log file exist?**
   ```
   ls /mnt/c/Users/dines/AppData/Roaming/Claude/logs/mcp-server-stock-analysis.log
   ```

2. **What's in main.log?**
   ```
   tail -100 /mnt/c/Users/dines/AppData/Roaming/Claude/logs/main.log
   ```

3. **Can Docker run manually?**
   ```
   docker run --rm stock-analysis-yfinance python -c "print('OK')"
   ```

4. **Is the config file correct?**
   ```
   cat /mnt/c/Users/dines/AppData/Roaming/Claude/claude_desktop_config.json
   ```

---

## 💡 Key Points

1. **You MUST fully quit Claude Desktop** - not just close windows
2. **Wait at least 10 seconds** before restarting
3. **Check system tray** for hidden Claude icon
4. **Use Task Manager** if unsure it's fully closed
5. **After restart**, check logs for `mcp-server-stock-analysis.log`

---

## 🎯 Expected Behavior After Restart

✅ **Success looks like:**
- New log file appears: `mcp-server-stock-analysis.log`
- Tools show up in Claude Desktop
- You can ask Claude to refresh market data
- No errors in main.log

❌ **Problem looks like:**
- No `mcp-server-stock-analysis.log` file
- Only MCP_DOCKER shows up
- Claude says "I don't have access to those tools"

---

**Now: Completely quit Claude Desktop and restart it!**

Wait 10 seconds, then open it fresh and try asking:
```
"What MCP tools do you have?"
```
