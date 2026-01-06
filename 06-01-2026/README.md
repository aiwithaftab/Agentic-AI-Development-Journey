# LangChain Development

## 📝 Overview
Today I reached the **17% completion** mark of the *Foundation: Introduction to LangChain - Python* course. My focus was on **Lesson 1: Foundational Models**, specifically mastering how to bridge the gap between creative AI generation and structured data requirements.

## 🛠️ Concepts & Skills
### 1. Structured Output with Pydantic
The core of today's learning was using **Pydantic** (`BaseModel`) to enforce a strict schema on LLM responses. This is a critical skill for building production-ready applications where the output needs to be parsed by a database or a frontend UI.

### 2. Agent Configuration
I practiced configuring an agent with:
* **System Prompts:** Setting the persona (e.g., "Science Fiction Writer").
* **Response Formats:** Binding a data class to the agent's output.
* **HumanMessage Objects:** Structuring inputs for the LangChain orchestration layer.

## 💻 Code Implementation
In the lab, I created a schema for fictional locations and invoked an agent to generate a structured response for the "Capital of the Moon."

```python
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

# Defining the schema
class CapitalInfo(BaseModel):
    name: str
    location: str
    vibe: str
    economy: str

# Initializing the agent with structured output
agent = create_agent(
    model='gpt-5-nano',
    system_prompt="You are a science fiction writer, create a capital city at the users request.",
    response_format=CapitalInfo
)

# Extracting a specific data point from the object
response = agent.invoke({"messages": [HumanMessage(content="What is the capital of The Moon?")]})
print(response["structured_response"].name)
# Output: 'Lunaris Prime'
