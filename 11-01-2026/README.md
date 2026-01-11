# MCP Server Integration: Web Search Tooling

## 📌 Project Overview
As part of my AI development learning path, this project demonstrates the implementation of a **Model Context Protocol (MCP)** server. The goal is to extend the capabilities of AI models by providing them with a "Search" tool, allowing the LLM to access real-time information via the **Tavily API**.

This implementation uses the `FastMCP` framework to create a high-performance bridge between the AI and external data sources.



---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Search Engine:** [Tavily AI](https://tavily.com/) (Optimized for LLMs)
* **Environment Management:** `python-dotenv`

---

## 📂 Code Highlights

The script `2.1_mcp_server.py` performs three critical functions:
1.  **Environment Setup:** Securely loads API credentials.
2.  **Server Initialization:** Sets up the `FastMCP` instance named `mcp_server`.
3.  **Tool Definition:** Exposes the `search_web` function as a tool the AI can autonomously decide to use.

### The Search Tool
```python
@mcp.tool()
def search_web(query: str) -> Dict[str, Any]:
    """Search the web for information"""
    results = tavily_client.search(query)
    return results
