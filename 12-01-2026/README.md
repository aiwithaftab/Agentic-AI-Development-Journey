# Daily Learning: Accessing Context in LangChain Tools

## 📅 Date: January 12, 2026
## 🏷️ Topic: Agentic Workflows & Context Injection

### 🎯 Objective
To understand how to pass environment-specific or user-specific data to AI agents via `ToolRuntime` without cluttering the prompt or requiring the agent to "guess" user preferences.

---

### 💻 Implementation Breakdown

The focus today was on the `@tool` decorator and the use of a runtime object to access a predefined context schema.

#### Key Components:
1. **`ToolRuntime`**: This acts as the bridge between the execution environment and the tool. It allows the tool to access data that isn't necessarily passed as an argument by the LLM.
2. **Context Schema**: By defining a `context_schema` (in this case, `ColourContext`), we provide a structured way for the agent to retrieve persistent user data.
3. **Implicit Retrieval**: Instead of the agent asking "What is your favorite color?", it calls `get_favourite_colour(runtime)`. The tool then pulls `runtime.context.favourite_colour` directly.

#### Code Snippet Analyzed:
```python
from langchain.tools import tool, ToolRuntime

@tool
def get_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the favourite colour of the user"""
    return runtime.context.favourite_colour

# Agent Configuration
agent = create_agent(
    model="gpt-5-nano",
    tools=[get_favourite_colour, get_least_favourite_colour],
    context_schema=ColourContext
)
