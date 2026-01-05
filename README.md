# 🌦️ Weather MCP Server

A simple **Model Context Protocol (MCP)** server built in Python that provides real-time U.S. weather alerts and integrates directly with **Claude Desktop**.

This project was created as a **learning implementation** to understand MCP servers, stdio-based tool execution, and Claude Desktop integration.

---

## 🚀 Overview

The Weather MCP Server fetches active weather alerts from the **U.S. National Weather Service (NWS) API** and exposes them as callable tools using the Model Context Protocol.  
Once installed, the tool becomes available directly inside Claude Desktop without running a web server.

---

## ✨ Features

- MCP server built using **FastMCP**
- Fetches real-time weather alerts by U.S. state code
- Runs over **stdio** (no HTTP ports required)
- Direct integration with **Claude Desktop**
- Clean and beginner-friendly implementation

---

## 🛠️ Tech Stack

- Python 3.10+
- Model Context Protocol (MCP)
- FastMCP
- uv
- httpx
- Claude Desktop

---

## 📂 Project Structure

```text
MCP/
│
├── server/
│   └── weather.py        # MCP server implementation
│
├── venv/                 # (optional) local virtual environment
│
└── req.txt               # Dependencies (reference)


⚙️ Installation
1️⃣ Install uv

Open PowerShell and run:

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


Restart PowerShell and verify:

uv --version

2️⃣ Install MCP CLI dependencies

Open PowerShell as Administrator and run:

uv pip install "mcp[cli]" --system


This installs the MCP CLI along with required dependencies such as typer.

3️⃣ Navigate to the project directory
cd C:\Users\Dell\Desktop\MCP

4️⃣ Register the MCP server with Claude Desktop
uv run mcp install server/weather.py


If successful, you will see a confirmation message indicating the server was added to Claude.

5️⃣ Restart Claude Desktop

Close Claude Desktop completely and reopen it.
The Weather MCP Server will now be available under Tools.

🧪 Usage

Once installed, you can call the MCP tool directly from Claude Desktop.

Example prompt:

Get weather alerts for CA


Claude will invoke the MCP tool and return formatted weather alerts.

📝 Notes

This MCP server runs over stdio and does not expose network ports.

No manual Claude configuration is required when using mcp install.

MCP Inspector is optional and only needed for debugging.