# Learning Model Context Protocol (MCP)

This repository contains my notes and implementation examples for the **Model Context Protocol (MCP)**. As I deepen my expertise in AI development, I am exploring how MCP standardizes the way AI models interact with external data and tools.

## 📌 What is MCP?
The Model Context Protocol (MCP) is an open standard that enables developers to build secure, two-way connections between AI models (Hosts) and data sources (Servers). Think of it as **USB-C for AI applications**.

---

## 🏗️ Architecture & Concepts

### 1. The Host
The application that initiates the connection. This is where the LLM "lives."
* **Examples:** Claude Desktop, Cursor, IDEs, or custom-built Python/Node.js apps.

### 2. The Client
The bridge located inside the Host. It handles the communication protocol, ensuring the model can talk to the server.

### 3. The Server
A lightweight program that exposes specific capabilities to the AI.
* **Resources:** Static data (like documentation or database schemas).
* **Tools:** Executable functions (like running code or searching an API).
* **Prompts:** Templates to help the AI structure its reasoning.

---

## 🛠️ Implementation: My First MCP Server

I built a basic server using **Python** and the `FastMCP` framework to understand the tool-calling lifecycle.

### Prerequisites
- Python 3.10+
- `uv` (Fast Python package manager)
uv venv
source .venv/bin/activate
uv add "mcp[cli]"
