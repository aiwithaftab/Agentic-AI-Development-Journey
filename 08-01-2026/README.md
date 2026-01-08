# Learning Journey: AI Engineering & LangGraph
**Date:** January 8, 2026
**Topic:** State Persistence and Checkpointers in LangGraph

---

## 🎯 Learning Objective
Understand how to make AI agents "persistent" by implementing **Checkpointers** to manage conversation state, enable human-in-the-loop interactions, and ensure error recovery.

## 🧠 Key Concepts

### What is a Checkpointer?
In LangGraph, a **Checkpointer** is a thread-safe persistence layer. It snapshots the state of the graph at every "superstep," allowing the agent to:
* **Resume** after a crash or timeout.
* **Remember** user context across different sessions using a `thread_id`.
* **Time Travel**: Rewind the agent to a previous state to debug or branch the conversation.

### Persistence Types
1.  **In-Memory (`MemorySaver`):** Best for rapid prototyping; state is lost when the process ends.
2.  **Relational (`SqliteSaver`, `PostgresSaver`):** Ideal for development and production to ensure data survives restarts.

---
