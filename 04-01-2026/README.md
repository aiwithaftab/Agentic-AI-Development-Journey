# AI Learning Journey: Local LLM Setup

Today I focused on setting up a local environment for running Large Language Models (LLMs) and interacting with them via Python.

## 🚀 Key Achievements
* **Ollama Server Management:** Learned how to resolve port conflicts (`bind: Only one usage of each socket address`) by managing the background process.
* **Model Deployment:** Successfully pulled and ran the **Gemma 3 4B** model locally.
* **API Integration:** Explored using `curl` to send POST requests to `http://localhost:11434/api/generate`.
* **Python for AI:** Set up a Python environment using version 3.12 and installed the `requests` library for API communication.
* **Hardware Optimization:** Monitored NVIDIA GeForce GTX 1650 performance, learning about "low VRAM mode" and memory management.

## 🛠️ Commands Mastered
| Task | Command |
| :--- | :--- |
| Start Server | `ollama serve` |
| Pull Model | `ollama pull gemma3:4b` |
| List Models | `ollama list` |
| Kill Process | `taskkill /F /IM ollama.exe` |
| Install Library | `pip install requests` |

## 💡 Important Concepts
* **Intent:** Samjha ke programming mein user ke "Maqsad" (goal) ko pehchanna kyun zaroori hai.
* **Client-Server Architecture:** Ollama background mein server ki tarah chalta hai aur Terminal/Python client ki tarah usse baat karte hain.
* **Troubleshooting:** Learned to debug `[WinError 10061]` by ensuring the server is active before running scripts.

* Explore system prompts to change the AI's behavior.
