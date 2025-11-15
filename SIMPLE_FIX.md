# Simple Fix: Move Project to Shorter Path

## The Issue

Claude Desktop isn't loading the `stock-analysis` MCP server. The most likely reasons:
1. **Path is too long** (Windows has 260-char limit)
2. **Claude Desktop is picky** about MCP server configurations

## ✅ SIMPLE SOLUTION: Move to Shorter Path

### Step 1: Move the Project

**In Windows Explorer or PowerShell:**

```powershell
# Option A: PowerShell
Move-Item "C:\Users\dines\Downloads\claud_stock_files\angel-one-stock-analysis\angel-one-stock-analysis" "C:\stock-analysis"

# Option B: Windows Explorer
# Just drag the folder from:
#   C:\Users\dines\Downloads\claud_stock_files\angel-one-stock-analysis\angel-one-stock-analysis
# To:
#   C:\stock-analysis
```

### Step 2: Update Claude Desktop Config

I'll update your config file to use the new shorter path.

**New config will be:**
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
        "C:\\stock-analysis\\src\\database:/app/src/database",
        "stock-analysis-yfinance"
      ]
    }
  }
}
```

### Step 3: Restart Claude Desktop

1. Quit Claude Desktop completely (system tray → Quit)
2. Wait 10 seconds
3. Open Claude Desktop
4. Check for: `C:\Users\dines\AppData\Roaming\Claude\logs\mcp-server-stock-analysis.log`

---

## Alternative: Even Simpler - Remove Volume Mount

If moving doesn't work, we can run without persistent database:

```json
{
  "mcpServers": {
    "stock-analysis": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "stock-analysis-yfinance"
      ]
    }
  }
}
```

**Pros:** Simplest possible config, most likely to work
**Cons:** Database isn't saved between sessions (but can refresh data anytime)

---

## Do you want me to:

**Option A:** Help you move the project to `C:\stock-analysis`
**Option B:** Update config to run without volume mount (simplest)
**Option C:** Try a completely different approach (use Python directly on Windows)

**I recommend Option B** - it's the simplest and will tell us if Claude Desktop can load the server at all.

Let me know which you'd like to try!
