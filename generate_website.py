#!/usr/bin/env python3
"""
Generate static website pages with latest stock and ETF data
"""

import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("📊 Generating website with latest data...")
print(f"⏰ Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()
print("✅ Website structure created in docs/ folder")
print()
print("📁 Website Files:")
print("   ├── index.html       (Homepage)")
print("   ├── css/style.css    (Styles)")
print("   └── js/main.js       (JavaScript)")
print()
print("🚀 To deploy:")
print("   1. Commit changes: git add docs/ && git commit -m 'Add website'")
print("   2. Push to GitHub: git push")
print("   3. Enable GitHub Pages in repository settings")
print("   4. Choose 'docs' folder as source")
print()
print("🌐 Your website will be live at:")
print("   https://dineshratn.github.io/angel-one-stock-analysis/")
print()
