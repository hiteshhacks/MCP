🌦️ Weather MCP Server (Learning Project)

A simple Model Context Protocol (MCP) server built in Python that fetches real-time weather alerts from the U.S. National Weather Service (NWS) API and exposes them as tools inside Claude Desktop.

This project was built as part of learning MCP architecture, stdio-based tool servers, and Claude Desktop integration.

✨ Features

MCP server built using FastMCP

Exposes a tool to fetch active weather alerts for U.S. states

Integrates directly with Claude Desktop via mcp install

Uses async HTTP requests with httpx

Clean, minimal, and beginner-friendly MCP example

🧠 What I Learned

How MCP servers work over stdio (no HTTP ports)

Writing MCP tools using decorators

Integrating MCP servers with Claude Desktop

Using uv for clean Python execution and CLI tooling

Debugging Windows-specific permission and PATH issues

🛠️ Tech Stack

Python 3.10+

Model Context Protocol (MCP)

FastMCP

uv

httpx

Claude Desktop

📁 Project Structure
MCP/
│
├── server/
│   └── weather.py        # MCP server implementation
│
├── venv/                 # (optional) local virtual environment
│
└── req.txt               # Dependencies (for reference)

⚙️ Prerequisites

Windows

Python 3.10+

Claude Desktop (installed)

PowerShell

🚀 Step-by-Step Installation (Windows)
1️⃣ Install uv

Open PowerShell and run:

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


Restart PowerShell and verify:

uv --version

2️⃣ Install MCP CLI (with CLI extras)

Run PowerShell as Administrator, then:

uv pip install "mcp[cli]" --system


This installs the MCP CLI required for mcp install.

3️⃣ Navigate to Project Directory
cd C:\Users\Dell\Desktop\MCP

4️⃣ Install MCP Server into Claude Desktop
uv run mcp install server/weather.py


You should see:

Successfully installed weather in Claude app

5️⃣ Restart Claude Desktop

Close Claude Desktop completely

Reopen it

Navigate to Tools

You should now see:

weather


🎉 The MCP server is now connected.

🧪 Example Usage (Inside Claude Desktop)

Ask Claude:

“Get weather alerts for CA”

Claude will automatically call the MCP tool:

get_alerts(state="CA")


and return formatted weather alerts.