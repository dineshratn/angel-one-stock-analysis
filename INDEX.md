# Angel One Stock Analysis MCP Server - Navigation Guide

Welcome! This document helps you navigate the project and find what you need quickly.

## 🚀 Getting Started (Choose Your Path)

### I'm New Here
Start with these in order:
1. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Overview of what this project does
2. **[QUICK_START.md](QUICK_START.md)** - Get running in 10 minutes
3. **[SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)** - Track your progress

### I Want Details
- **[README.md](README.md)** - Comprehensive 8,300+ word guide

### I'm Migrating from TradingView Version
- **[CHANGES.md](CHANGES.md)** - What's different and how to migrate

### I Want to See Examples
- **[EXAMPLES.md](EXAMPLES.md)** - 20+ SQL queries and usage patterns

## 📚 Documentation Map

```
├─ 🎯 PROJECT_SUMMARY.md         → What you have and why it's awesome
├─ ⚡ QUICK_START.md             → Fastest path to success (5 steps)
├─ 📖 README.md                   → Complete reference guide
├─ ✅ SETUP_CHECKLIST.md         → Track setup progress
├─ 🔄 CHANGES.md                 → Migration from TradingView
├─ 💡 EXAMPLES.md                → Real-world usage examples
└─ 🗺️ INDEX.md                   → This navigation guide
```

## 🎯 Find What You Need

### Setup & Installation

| I Need To... | Go To... |
|-------------|---------|
| Understand what this project does | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |
| Set up quickly (10 min) | [QUICK_START.md](QUICK_START.md) |
| Get detailed setup instructions | [README.md](README.md#-setup-guide) |
| Track my setup progress | [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md) |
| Test my Angel One credentials | Run `test_connection.py` |

### Usage & Examples

| I Want To... | Go To... |
|-------------|---------|
| See SQL query examples | [EXAMPLES.md](EXAMPLES.md) |
| Learn available MCP tools | [README.md](README.md#-available-mcp-tools) |
| Understand how to ask Claude | [EXAMPLES.md](EXAMPLES.md#-smart-assistant-queries) |
| Build complex workflows | [EXAMPLES.md](EXAMPLES.md#-workflow-examples) |

### Configuration & Customization

| I Need To... | Go To... |
|-------------|---------|
| Configure Angel One credentials | `.env.example` → copy to `.env` |
| Change stock filters | `src/stock_analysis/constant_parameters.py` |
| Modify database schema | `src/stock_analysis/constant_parameters.py` |
| Add new MCP tools | `src/stock_analysis/main.py` |
| Configure Docker | `Dockerfile` or `docker-compose.yml` |

### Troubleshooting

| Problem | Solution |
|---------|----------|
| Authentication failed | [README.md](README.md#common-issues) |
| Docker won't start | [README.md](README.md#docker-volume-issues) |
| Database not found | [README.md](README.md#database-not-found) |
| Rate limit errors | [README.md](README.md#rate-limit-errors) |
| Any issue | [README.md](README.md#-troubleshooting) + `test_connection.py` |

### Technical Details

| I Want Info About... | Go To... |
|---------------------|---------|
| Project architecture | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md#-technical-stack) |
| Database schema | [README.md](README.md#-database-schema) |
| API endpoints used | `src/stock_analysis/main.py` |
| Environment variables | `.env.example` |
| Dependencies | `pyproject.toml` or `requirements.txt` |

## 🔍 Code Files Guide

### Source Code
- **`src/stock_analysis/main.py`**
  - Purpose: MCP server implementation
  - Contains: API integration, MCP tools, database operations
  - Edit if: Adding features, modifying tools

- **`src/stock_analysis/constant_parameters.py`**
  - Purpose: Configuration constants
  - Contains: URLs, schema, mappings
  - Edit if: Changing data structure, filters

- **`src/stock_analysis/__init__.py`**
  - Purpose: Package initialization
  - Contains: Version info
  - Rarely edited

### Configuration Files
- **`.env`** (create from `.env.example`)
  - Purpose: Store API credentials
  - NEVER commit this file!

- **`pyproject.toml`**
  - Purpose: Poetry dependency management
  - Edit if: Adding Python packages

- **`requirements.txt`**
  - Purpose: Pip dependency list
  - Alternative to Poetry

- **`Dockerfile`**
  - Purpose: Container configuration
  - Edit if: Changing base image, build process

- **`docker-compose.yml`**
  - Purpose: Docker Compose orchestration
  - Edit if: Adding services, volumes

### Utility Scripts
- **`test_connection.py`**
  - Purpose: Verify Angel One credentials
  - Run: `python test_connection.py`
  - Before Docker setup

- **`.gitignore`**
  - Purpose: Git ignore rules
  - Edit if: Adding ignored patterns

## 📊 Documentation By Use Case

### For Beginners
1. Start: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
2. Setup: [QUICK_START.md](QUICK_START.md)
3. Track: [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)
4. Use: [EXAMPLES.md](EXAMPLES.md#-basic-examples)

### For Intermediate Users
1. Guide: [README.md](README.md)
2. Examples: [EXAMPLES.md](EXAMPLES.md#-market-analysis-examples)
3. Customize: Edit `constant_parameters.py`
4. Extend: Add tools in `main.py`

### For Advanced Users
1. Architecture: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md#-technical-stack)
2. Migration: [CHANGES.md](CHANGES.md)
3. Extend: All source files in `src/`
4. Deploy: Production Docker setup

### For Traders
1. Quick Setup: [QUICK_START.md](QUICK_START.md)
2. Query Examples: [EXAMPLES.md](EXAMPLES.md#-market-analysis-examples)
3. Workflows: [EXAMPLES.md](EXAMPLES.md#-workflow-examples)
4. Reference: Keep [README.md](README.md) handy

### For Developers
1. Tech Details: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
2. Changes: [CHANGES.md](CHANGES.md)
3. Source: `src/stock_analysis/`
4. Extend: [README.md](README.md#-customization)

## 🎓 Learning Path

### Day 1: Setup
- [ ] Read PROJECT_SUMMARY.md (5 min)
- [ ] Follow QUICK_START.md (10 min)
- [ ] Complete SETUP_CHECKLIST.md (5 min)
- [ ] Test basic queries (10 min)

### Day 2: Learning
- [ ] Read full README.md (20 min)
- [ ] Try examples from EXAMPLES.md (30 min)
- [ ] Experiment with SQL queries (20 min)

### Day 3: Mastery
- [ ] Build custom queries (30 min)
- [ ] Explore historical data (20 min)
- [ ] Create analysis workflows (30 min)

### Week 2: Advanced
- [ ] Add technical indicators
- [ ] Customize database schema
- [ ] Build new MCP tools
- [ ] Share your improvements!

## 🔗 External Resources

### Angel One
- [SmartAPI Portal](https://smartapi.angelbroking.com/)
- [Enable TOTP](https://smartapi.angelbroking.com/enable-totp)
- [API Documentation](https://smartapi.angelbroking.com/docs)
- [Python SDK GitHub](https://github.com/angel-one/smartapi-python)

### MCP Protocol
- [MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp)

### Docker
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Docker Documentation](https://docs.docker.com/)

### Original Inspiration
- [TradingView MCP Article](https://medium.com/@varungangu1/building-a-stock-analysis-mcp-server-with-docker-and-claude-desktop-eae4963dc3a7)

## 📞 Quick Reference

### Important Commands
```bash
# Test connection
python test_connection.py

# Build Docker image
docker build -t angel-one-stock-analysis .

# Run manually (testing)
docker run -i --rm --env-file .env angel-one-stock-analysis

# View logs
docker logs <container_id>

# Stop all containers
docker stop $(docker ps -q)
```

### Important Paths
```
Config File:
- macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
- Windows: %APPDATA%\Claude\claude_desktop_config.json
- Linux: ~/.config/Claude/claude_desktop_config.json

Database: src/database/YYYY-MM-DD.db
Credentials: .env
```

### Important URLs
- Angel API: https://smartapi.angelbroking.com/
- TOTP Setup: https://smartapi.angelbroking.com/enable-totp
- Scrip Master: https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json

## 🎯 Next Steps

Based on where you are:

**Haven't started?**
→ Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) next

**Ready to setup?**
→ Follow [QUICK_START.md](QUICK_START.md) now

**Already setup?**
→ Explore [EXAMPLES.md](EXAMPLES.md) for ideas

**Want to customize?**
→ Check [README.md](README.md#-customization)

**Having issues?**
→ See [README.md](README.md#-troubleshooting)

## 📝 Document Status

| Document | Lines | Purpose | Read Time |
|----------|-------|---------|-----------|
| PROJECT_SUMMARY.md | ~450 | Overview & features | 10 min |
| QUICK_START.md | ~150 | Fast setup | 5 min |
| README.md | ~550 | Complete guide | 25 min |
| SETUP_CHECKLIST.md | ~350 | Track progress | 15 min |
| CHANGES.md | ~300 | Migration notes | 10 min |
| EXAMPLES.md | ~500 | Usage examples | 15 min |
| INDEX.md | ~350 | Navigation (you are here) | 10 min |

**Total documentation: ~2,650 lines** across 7 files!

## 🎉 You're All Set!

You now know where everything is. Pick your starting point and dive in!

**Questions?** Everything is documented. Use this index to find answers quickly.

**Stuck?** Check the troubleshooting sections in relevant docs.

**Ready?** Start with [QUICK_START.md](QUICK_START.md) and be running in 10 minutes!

---

**Happy Trading! 📈💚**
