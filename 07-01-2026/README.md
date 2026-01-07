# Sci-Fi World Building Agent: Structured Data Extraction

This project demonstrates the transition from unstructured LLM chat to **Structured AI Output**. By using Pydantic schemas, we ensure that the AI's creative output is formatted as a reliable data object that can be used in downstream applications (like games, databases, or websites).

---

## 🧠 Key Learning Concepts

Today's focus was on bridging the gap between creative writing and data engineering.

* **Pydantic Integration:** Using `BaseModel` to define a strict schema for the LLM. This prevents "hallucinated" formatting and ensures consistency.
* **System Prompting:** Defining a specific persona ("Science Fiction Writer") to guide the creative direction of the response.
* **Agentic Orchestration:** Utilizing `create_agent` to bundle the model, prompt, and response format into a single executable unit.
* **Structured Parsing:** Accessing the final result via the `["structured_response"]` key rather than parsing a raw string.

---

## 🛠️ Tech Stack

| Tool | Usage |
| :--- | :--- |
| **Python 3.12** | Core programming language. |
| **LangChain** | Agent orchestration and message management (`HumanMessage`). |
| **Pydantic** | Schema definition and data validation. |
| **Jupyter/IPyKernel** | Interactive development and rapid prototyping. |

---

## 💻 Code Implementation

### The Schema
We define exactly what information we want the agent to generate:
```python
class CapitalInfo(BaseModel):
    name: str
    location: str
    vibe: str
    economy: str
