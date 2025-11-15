# MCP Server Not Loading - Diagnosis & Solutions

## Current Situation

**Problem:** `stock-analysis` MCP server is configured but Claude Desktop is not loading it.

**Evidence:**
- ✅ Config file is correct at: `C:\Users\dines\AppData\Roaming\Claude\claude_desktop_config.json`
- ✅ Docker image exists and works: `stock-analysis-yfinance`
- ✅ MCP_DOCKER loads successfully
- ❌ No `mcp-server-stock-analysis.log` file created
- ❌ Main.log shows ONLY MCP_DOCKER being loaded

## Possible Root Causes

### 1. Claude Desktop MCP Server Selection
Claude Desktop might be:
- Only loading servers it recognizes as "official"
- Having issues with the long Windows path in the volume mount
- Not supporting arbitrary Docker commands (only specific MCP formats)

### 2. Version/Compatibility Issue
Your Claude Desktop version: `1.0.332`
- This might have strict MCP server requirements
- Might need servers packaged in a specific way

### 3. Path Length Limitation
The volume mount path is very long:
```
C:\\Users\\dines\\Downloads\\claud_stock_files\\angel-one-stock-analysis\\angel-one-stock-analysis\\src\\database
```
Windows has a 260-character path limit that might be affecting this.

---

## Solutions to Try

###  Solution 1: Use UVX (Recommended by Anthropic)

Claude Desktop works best with `uvx`-based MCP servers. Let's install the dependencies locally:

**Step 1: Install UV (Python package manager)**
```bash
# In PowerShell (as Administrator):
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Step 2: Create uvx-compatible config**
Update `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "stock-analysis": {
      "command": "uvx",
      "args": [
        "--from",
        "C:\\Users\\dines\\Downloads\\claud_stock_files\\angel-one-stock-analysis\\angel-one-stock-analysis",
        "python",
        "-m",
        "src.stock_analysis.main"
      ]
    }
  }
}
```

---

### Solution 2: Simplify the Path

Move the project to a shorter path:

**Step 1: Move project**
```bash
# In Windows:
move C:\Users\dines\Downloads\claud_stock_files\angel-one-stock-analysis\angel-one-stock-analysis C:\stock-analysis
```

**Step 2: Update config**
```json
{
  "mcpServers": {
    "stock-analysis": {
      "command": "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "C:\\stock-analysis\\src\\database:/app/src/database",
        "stock-analysis-yfinance"
      ]
    }
  }
}
```

---

### Solution 3: Use Batch File Wrapper

**Step 1: Create simple batch file**
File: `C:\stock-mcp.bat`
```batch
@echo off
docker run -i --rm -v "C:\Users\dines\Downloads\claud_stock_files\angel-one-stock-analysis\angel-one-stock-analysis\src\database:/app/src/database" stock-analysis-yfinance
```

**Step 2: Update config**
```json
{
  "mcpServers": {
    "stock-analysis": {
      "command": "C:\\stock-mcp.bat"
    }
  }
}
```

---

### Solution 4: Install Python Packages Locally (No Docker)

This avoids Docker entirely and runs the MCP server natively:

**Step 1: Install dependencies**
```bash
cd /mnt/c/Users/dines/Downloads/claud_stock_files/angel-one-stock-analysis/angel-one-stock-analysis
pip install -r requirements.txt
```

**Step 2: Update config**
```json
{
  "mcpServers": {
    "stock-analysis": {
      "command": "python",
      "args": [
        "-m",
        "src.stock_analysis.main"
      ],
      "cwd": "C:\\Users\\dines\\Downloads\\claud_stock_files\\angel-one-stock-analysis\\angel-one-stock-analysis"
    }
  }
}
```

---

### Solution 5: Verify Claude Desktop MCP Support

Check if your Claude Desktop version supports custom MCP servers:

**Check version:**
- Open Claude Desktop
- Go to Settings → About
- Check if MCP is mentioned in features

**Update Claude Desktop:**
- Check for updates in Settings
- Or download latest from: https://claude.ai/download

---

## Debugging Steps

### Step 1: Check if Claude Desktop sees the config

After restart, check main.log:
```bash
tail -100 /mnt/c/Users/dines/AppData/Roaming/Claude/logs/main.log | grep -i "stock"
```

Expected: Should show "Launching MCP Server: stock-analysis"
Actual: Shows nothing about stock-analysis

### Step 2: Test Docker command manually

```bash
docker run -i --rm stock-analysis-yfinance python -c "from mcp.server.fastmcp import FastMCP; print('OK')"
```

This should print "OK" - if it doesn't, Docker setup has issues.

### Step 3: Check config file syntax

```bash
# Use a JSON validator
cat /mnt/c/Users/dines/AppData/Roaming/Claude/claude_desktop_config.json
```

Paste into: https://jsonlint.com/

### Step 4: Try minimal config

Remove all extra servers and test with ONLY stock-analysis:

```json
{
  "mcpServers": {
    "stock-analysis": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "stock-analysis-yfinance"]
    }
  }
}
```

---

## Recommended Action Plan

**Try these in order:**

1. **✅ Try Solution 4 first** (Python local install - no Docker complexity)
   - Fastest to test
   - Avoids Docker/path issues
   - Most compatible with Claude Desktop

2. **If that fails, try Solution 2** (Shorter path)
   - Simpler paths are more reliable
   - Easier to debug

3. **If that fails, try Solution 1** (UVX)
   - Official Anthropic recommendation
   - Best long-term solution

4. **Last resort: Contact Anthropic support**
   - Your Claude Desktop version might have MCP limitations
   - Check https://docs.anthropic.com/claude/docs/claude-desktop

---

## Quick Test Command

After trying any solution, test with:

1. **Fully restart Claude Desktop** (Quit from system tray)
2. **Wait 30 seconds**
3. **Open Claude Desktop**
4. **Check for log file:**
   ```
   ls /mnt/c/Users/dines/AppData/Roaming/Claude/logs/mcp-server-stock-analysis.log
   ```
5. **If file exists:** Success! Check what it says
6. **If file doesn't exist:** That solution didn't work, try next one

---

## Let's Try Solution 4 Now

This is the easiest and most likely to work. Here's exactly what to do:

**1. Install Python packages locally:**
```bash
cd /mnt/c/Users/dines/Downloads/claud_stock_files/angel-one-stock-analysis/angel-one-stock-analysis
python3 -m pip install --user -r requirements.txt
```

**2. Test it works:**
```bash
python3 -m src.stock_analysis.main
```
(Press Ctrl+C to stop)

**3. I'll update your config file to use local Python**

Would you like me to try Solution 4 (local Python install) now?
