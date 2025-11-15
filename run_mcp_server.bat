@echo off
REM MCP Server Launcher for Claude Desktop

docker run -i --rm -v "C:\Users\dines\Downloads\claud_stock_files\angel-one-stock-analysis\angel-one-stock-analysis\src\database:/app/src/database" stock-analysis-yfinance
