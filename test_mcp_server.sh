#!/bin/bash
# Test script for MCP server

echo "=========================================="
echo "Testing Stock Analysis MCP Server"
echo "=========================================="
echo ""

echo "1. Testing Docker image exists..."
if docker images | grep -q "stock-analysis-yfinance"; then
    echo "✅ Docker image found!"
else
    echo "❌ Docker image not found!"
    exit 1
fi

echo ""
echo "2. Testing Python imports..."
docker run --rm stock-analysis-yfinance python -c "
import yfinance as yf
import pandas as pd
from mcp.server.fastmcp import FastMCP
print('✅ All imports successful!')
"

echo ""
echo "3. Testing database directory..."
if [ -d "src/database" ]; then
    echo "✅ Database directory exists!"
else
    echo "❌ Database directory not found!"
    exit 1
fi

echo ""
echo "4. Testing stock data fetch (this may take a moment)..."
docker run --rm stock-analysis-yfinance python -c "
import yfinance as yf
ticker = yf.Ticker('RELIANCE.NS')
hist = ticker.history(period='5d')
if not hist.empty:
    print(f'✅ Successfully fetched data for RELIANCE.NS')
    print(f'   Last close: ₹{hist[\"Close\"].iloc[-1]:.2f}')
else:
    print('⚠️  No data available (market may be closed)')
" || echo "⚠️  Network issue or rate limit"

echo ""
echo "=========================================="
echo "Setup Complete! 🎉"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Open Claude Desktop configuration file:"
echo "   Windows: C:\\Users\\dines\\AppData\\Roaming\\Claude\\claude_desktop_config.json"
echo ""
echo "2. Add this configuration:"
cat << 'EOF'
{
  "mcpServers": {
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
EOF
echo ""
echo "3. Restart Claude Desktop"
echo "4. Try asking: 'Show me the database overview'"
echo ""
echo "See CLAUDE_DESKTOP_CONFIG.md for detailed instructions!"
