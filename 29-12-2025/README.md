# 📝 Daily AI Learning Log: December 29, 2025

## 🎯 Today's Focus
**LLMs Don’t Have Memory — So How Do They Remember?**

## ✅ What I Accomplished Today
- **Environment Management:** Created and configured a Python virtual environment (`venv`) in VS Code to isolate project dependencies.
- **Library Integration:** Successfully installed and mapped `langchain-openai`, `langchain-google-genai`, and `python-dotenv` within a local kernel.
- **API Troubleshooting:** Resolved a `404 NOT_FOUND` error by identifying and updating deprecated model strings (transitioning from `gemini-1.5-flash` to the stable `gemini-2.0-flash`).
- **Secure Configuration:** Set up a `.env` system to securely manage API keys, following industry best practices for security.

## 🛠️ Tech Stack Used
- **Language:** Python
- **IDE:** VS Code
- **Framework:** LangChain
- **Models:** Google Gemini 2.0 Flash
- **Tools:** venv, pip, dotenv

## 💡 Key Learnings
- **Kernel Mismatch:** Learned that installing a package in the terminal doesn't automatically update the Jupyter notebook kernel; manual selection is required.
- **Model Versioning:** Discovered that Google API versions (v1 vs v1beta) require specific model string matches to avoid 404 errors.
- **Dependency Isolation:** Understood the importance of `requirements.txt` and `venv` for reproducible AI workflows.
