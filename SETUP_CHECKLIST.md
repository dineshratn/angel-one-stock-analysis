# Setup Checklist - Angel One Stock Analysis MCP Server

Use this checklist to track your setup progress. Check off each item as you complete it!

## 📋 Pre-Setup Checklist

- [ ] I have an Angel One trading account
- [ ] I have Docker Desktop installed and running
- [ ] I have Claude Desktop installed (latest version)
- [ ] I have a text editor (VSCode, Sublime, etc.)
- [ ] I have basic command line knowledge

## 🔐 Step 1: Angel One API Credentials

### 1.1 Register for SmartAPI
- [ ] Visited https://smartapi.angelbroking.com/
- [ ] Signed up with Angel One credentials
- [ ] Email verification completed

### 1.2 Create API App
- [ ] Clicked "Create an App"
- [ ] Selected "Market Feed API" option
- [ ] Entered app name: `_________________`
- [ ] Saved API Key: `✓ Saved securely`
- [ ] Saved Secret Key: `✓ Saved securely`

### 1.3 Enable TOTP
- [ ] Visited https://smartapi.angelbroking.com/enable-totp
- [ ] Entered Angel One client ID
- [ ] Entered password/MPIN
- [ ] Verified OTP from email/SMS
- [ ] **Saved TOTP token string** (not QR code!): `✓ Saved securely`

**⚠️ IMPORTANT**: Save the TOTP token string, NOT the QR code!

## 📁 Step 2: Project Setup

### 2.1 Download Project
- [ ] Downloaded complete project folder
- [ ] Extracted to location: `_________________`
- [ ] Navigated to project folder in terminal

### 2.2 Configure Environment
- [ ] Copied `.env.example` to `.env`
- [ ] Opened `.env` in text editor
- [ ] Filled in `ANGEL_API_KEY=`
- [ ] Filled in `ANGEL_CLIENT_ID=`
- [ ] Filled in `ANGEL_PASSWORD=`
- [ ] Filled in `ANGEL_TOTP_TOKEN=`
- [ ] Saved `.env` file

## 🧪 Step 3: Test Connection

### 3.1 Install Test Dependencies
```bash
pip install smartapi-python pyotp python-dotenv
```
- [ ] Dependencies installed successfully

### 3.2 Run Test Script
```bash
python test_connection.py
```
- [ ] Test 1: Credentials found ✅
- [ ] Test 2: TOTP generated ✅
- [ ] Test 3: API connected ✅
- [ ] Test 4: Session created ✅
- [ ] Test 5: Profile fetched ✅
- [ ] Test 6: Market data fetched ✅

**If any test failed, STOP and fix it before proceeding!**

## 🐳 Step 4: Docker Build

### 4.1 Build Image
```bash
docker build -t angel-one-stock-analysis .
```
- [ ] Build started
- [ ] Builder stage completed
- [ ] Final stage completed
- [ ] Image created successfully

### 4.2 Verify Image
```bash
docker images | grep angel-one
```
- [ ] Image appears in list
- [ ] Size is reasonable (~500MB-1GB)

## 🖥️ Step 5: Claude Desktop Configuration

### 5.1 Locate Config File
- [ ] Found Claude Desktop config file at:
  - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
  - Linux: `~/.config/Claude/claude_desktop_config.json`

### 5.2 Update Configuration
- [ ] Opened config file in text editor
- [ ] Added `mcpServers` section (or updated existing)
- [ ] Added `angel-one-stocks` server configuration
- [ ] Updated volume mount path with ABSOLUTE path
- [ ] Updated env-file path with ABSOLUTE path
- [ ] Saved config file

**Example configuration:**
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
        "/FULL/PATH/TO/PROJECT/src/database:/app/src/database",
        "--env-file",
        "/FULL/PATH/TO/PROJECT/.env",
        "angel-one-stock-analysis"
      ]
    }
  }
}
```

### 5.3 Verify Paths
- [ ] Database volume path is ABSOLUTE (starts with `/` or `C:\`)
- [ ] Env-file path is ABSOLUTE
- [ ] Both paths point to correct project location

## 🎉 Step 6: Final Testing

### 6.1 Restart Claude Desktop
- [ ] Closed Claude Desktop completely
- [ ] Reopened Claude Desktop

### 6.2 Verify MCP Server
- [ ] Opened Claude Desktop
- [ ] Clicked on tools/integrations menu
- [ ] Saw "angel-one-stocks" in the list
- [ ] Tools are enabled/available

### 6.3 Test Functionality
Try these commands with Claude:

- [ ] **Test 1**: "Show me the stock database schema"
  - Expected: Table structure displayed

- [ ] **Test 2**: "Refresh market data"
  - Expected: "Market data refreshed successfully"

- [ ] **Test 3**: "How many stocks are in the database?"
  - Expected: Number displayed

- [ ] **Test 4**: "Show me top 5 stocks by volume"
  - Expected: List of stocks with volumes

## ✅ Success Criteria

You've successfully completed setup if:
- [x] All tests in `test_connection.py` passed
- [x] Docker image built without errors
- [x] Claude Desktop shows angel-one-stocks in tools
- [x] Claude can query and display stock data
- [x] You can refresh market data on command

## 🐛 Troubleshooting Checklist

If something doesn't work, check these:

### Authentication Issues
- [ ] Credentials in `.env` are correct (no extra spaces)
- [ ] TOTP token is the string, not QR code
- [ ] Angel One account is active
- [ ] SmartAPI access is enabled

### Docker Issues
- [ ] Docker Desktop is running
- [ ] Image built successfully
- [ ] Volume paths are absolute
- [ ] `.env` file is in project root

### Claude Desktop Issues
- [ ] Config file has valid JSON syntax
- [ ] Paths in config are absolute
- [ ] Claude Desktop was restarted after config change
- [ ] No typos in server name or command

### Database Issues
- [ ] Database directory exists: `src/database/`
- [ ] Volume mount path is correct
- [ ] First time: Need to run "refresh market data"

## 📝 Notes Section

Use this space for your own notes:

**Project Location:**
```
_______________________________________
```

**API Key (first 4 chars):**
```
_______________________________________
```

**Common Issues I Encountered:**
```
_______________________________________
_______________________________________
_______________________________________
```

**Custom Modifications:**
```
_______________________________________
_______________________________________
_______________________________________
```

## 🎯 Next Steps After Setup

- [ ] Read EXAMPLES.md for usage patterns
- [ ] Try basic SQL queries
- [ ] Experiment with historical data
- [ ] Create custom analysis workflows
- [ ] Consider adding technical indicators
- [ ] Share feedback/improvements

## 📚 Reference Quick Links

- API Signup: https://smartapi.angelbroking.com/
- Enable TOTP: https://smartapi.angelbroking.com/enable-totp
- API Docs: https://smartapi.angelbroking.com/docs
- Scrip Master: https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json

## 🆘 Getting Help

If you're stuck:

1. **Check the logs**:
   ```bash
   docker logs <container_id>
   ```

2. **Re-run test script**:
   ```bash
   python test_connection.py
   ```

3. **Verify Docker is working**:
   ```bash
   docker run hello-world
   ```

4. **Check Claude Desktop logs**:
   - Look in Application logs/Console

5. **Review documentation**:
   - README.md - Full guide
   - QUICK_START.md - Fast setup
   - EXAMPLES.md - Usage examples

---

**Completion Date**: _______________

**Setup Time**: _______ minutes

**Status**: [ ] Completed Successfully

**Happy Trading! 📈**
