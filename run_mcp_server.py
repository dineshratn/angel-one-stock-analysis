#!/usr/bin/env python3
"""
MCP Server launcher for Claude Desktop
This script launches the Docker container for the stock analysis MCP server
"""

import subprocess
import sys

# Docker command to run the MCP server
docker_cmd = [
    "docker",
    "run",
    "-i",
    "--rm",
    "-v",
    r"C:\Users\dines\Downloads\claud_stock_files\angel-one-stock-analysis\angel-one-stock-analysis\src\database:/app/src/database",
    "stock-analysis-yfinance"
]

# Run the Docker container
try:
    subprocess.run(docker_cmd, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running Docker container: {e}", file=sys.stderr)
    sys.exit(1)
except FileNotFoundError:
    print("Docker not found. Make sure Docker Desktop is installed and running.", file=sys.stderr)
    sys.exit(1)
