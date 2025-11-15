# 🎯 Angel One Stock Analysis MCP Server

**Welcome! You've downloaded a complete, production-ready MCP server for analyzing Indian stock markets with Claude AI.**

## ⚡ Quick Start (Choose One)

### 🏃 Super Fast (10 minutes)
1. Read: [QUICK_START.md](QUICK_START.md)
2. Follow the 5 steps
3. Start trading!

### 📖 Detailed Setup (20 minutes)
1. Read: [INDEX.md](INDEX.md) ← **Navigation guide**
2. Pick your path based on experience
3. Follow along with [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)

### 🎓 Learn First (30 minutes)
1. Read: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) ← **What you have**
2. Read: [README.md](README.md) ← **Complete guide**
3. Browse: [EXAMPLES.md](EXAMPLES.md) ← **See what's possible**

## 📦 What's Included

```
✅ Complete MCP Server (Python)
✅ Angel One API Integration
✅ Docker Configuration
✅ Test Scripts
✅ 2,650+ lines of documentation
✅ 20+ SQL query examples
✅ Setup checklists
✅ Troubleshooting guides
```

## 🎯 What You Can Do

- **Analyze stocks** with natural language via Claude
- **Run SQL queries** without writing SQL
- **Fetch historical data** for backtesting
- **Track markets** in real-time
- **Build workflows** for analysis
- **Extend easily** with your own features

## 📚 All Documentation Files

| File | What It Does | Read Time |
|------|-------------|-----------|
| **START_HERE.md** | You are here! | 2 min |
| **INDEX.md** | Navigate everything | 10 min |
| **QUICK_START.md** | Get running fast | 5 min |
| **README.md** | Complete guide | 25 min |
| **PROJECT_SUMMARY.md** | Overview & features | 10 min |
| **EXAMPLES.md** | Usage examples | 15 min |
| **CHANGES.md** | From TradingView | 10 min |
| **SETUP_CHECKLIST.md** | Track progress | 15 min |

## 🚀 First Steps

1. **Get Angel One Credentials**
   - Sign up: https://smartapi.angelbroking.com/
   - Enable TOTP: https://smartapi.angelbroking.com/enable-totp

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

3. **Test Connection**
   ```bash
   python test_connection.py
   ```

4. **Build Docker**
   ```bash
   docker build -t angel-one-stock-analysis .
   ```

5. **Configure Claude Desktop**
   - Edit: `claude_desktop_config.json`
   - Add server configuration
   - Restart Claude

## 🎉 That's It!

You're ready to analyze Indian stock markets with AI!

## 🗺️ Where to Go Next?

- **New here?** → [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
- **Ready to setup?** → [QUICK_START.md](QUICK_START.md)
- **Need navigation?** → [INDEX.md](INDEX.md)
- **Want examples?** → [EXAMPLES.md](EXAMPLES.md)
- **Need help?** → [README.md](README.md#-troubleshooting)

## 📞 Quick Help

**Error during setup?**
- Run: `python test_connection.py`
- Check: [README.md](README.md#-troubleshooting)
- Review: [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)

**Works but confused?**
- See: [EXAMPLES.md](EXAMPLES.md)
- Read: [README.md](README.md#-usage-examples)

**Want to extend?**
- Check: [README.md](README.md#-customization)
- Study: `src/stock_analysis/main.py`

## 🏆 Success Criteria

You'll know it works when:
- ✅ `test_connection.py` shows all green
- ✅ Docker builds successfully
- ✅ Claude shows "angel-one-stocks" in tools
- ✅ Claude can query and display data

## 💡 Pro Tips

1. **Always test first**: Run `test_connection.py` before Docker
2. **Use absolute paths**: In Docker volume mounts
3. **Check the logs**: `docker logs <container_id>`
4. **Start simple**: Try basic queries before complex ones
5. **Read examples**: [EXAMPLES.md](EXAMPLES.md) has 20+ patterns

## 🎓 Learning Path

```
Day 1: Setup (30 min)
   └─ QUICK_START.md → test_connection.py → Docker → Claude

Day 2: Learn (1 hour)
   └─ README.md → EXAMPLES.md → Try queries

Week 1: Master (ongoing)
   └─ Custom queries → Historical data → Workflows

Month 1: Extend (optional)
   └─ Add indicators → Build features → Contribute!
```

## 🔗 Essential Links

- **Angel One API**: https://smartapi.angelbroking.com/
- **Enable TOTP**: https://smartapi.angelbroking.com/enable-totp
- **API Docs**: https://smartapi.angelbroking.com/docs
- **Original Article**: [TradingView MCP Blog](https://medium.com/@varungangu1/building-a-stock-analysis-mcp-server-with-docker-and-claude-desktop-eae4963dc3a7)

## 🎊 Ready?

**Pick your next step:**
- 🏃 Fast: [QUICK_START.md](QUICK_START.md)
- 📖 Detailed: [README.md](README.md)
- 🗺️ Navigate: [INDEX.md](INDEX.md)

---

**Made with ❤️ for Indian traders**

**Powered by**: Angel One SmartAPI + FastMCP + Claude AI

**Happy Trading! 📈💚**
