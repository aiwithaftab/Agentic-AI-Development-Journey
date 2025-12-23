# Day 013 – Tavily Advanced Search

## 📌 Purpose
This script demonstrates how to use the Tavily Search API to retrieve
recent, high-quality search results using advanced search configuration.

The goal was to understand how search depth, topic filtering, and recency
controls affect result quality and cost.

## 🔍 Key Concepts Learned
- Using `search_depth="advanced"` for richer results
- Applying `topic="news"` for time-sensitive queries
- Filtering results using `time_range`
- Excluding low-quality domains
- Avoiding raw content for faster responses

## ⚙️ Configuration Explained
- **search_depth**: advanced (higher quality, higher cost)
- **time_range**: "w" (last week)
- **num_results**: 10
- **raw content**: disabled for performance

## ▶️ How to Run
```bash
pip install tavily-python
export TAVILY_API_KEY="your_api_key"
python tavily_search.py
