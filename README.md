# 🧠 AI Agent System

A modular, intelligent AI agent system built using **FastAPI** and **OpenAI's GPT models**, designed for real-time reasoning, summarization, and explanation of user reflections. This system supports both **web-based** and **CLI-based** execution modes.

---

## ✨ Key Features

- 🧩 **Modular AI pipeline** (`summarizer → reasoner → QA validator`)
- 🌐 **REST API** built with FastAPI
- 📤 **Outputs saved to MongoDB** (via `output.writer`)
- 🧪 **CLI simulator mode** with `input_simulator`
- 📚 **Context-aware memory** with `memory_store`
- 🧠 **Lens-based prompt transformation** (`lens_selector`)
- 🔍 **Explanation generation and logging**
- ✅ **OpenAI GPT-3.5 integration**
- 🔌 **CORS-enabled** for frontend connection
- ⚙️ **Clean folder structure** with `core`, `agents`, `output`, and `data` modules

---

## 📂 Project Structure

AI_AGENT/
- backend/
- - main.py # FastAPI entrypoint + CLI mode
│ ├── api_logic.py # Shared logic between API and CLI
│ ├── core/
│ │ ├── orchestrator.py # Agent pipeline coordinator
│ │ ├── prompt_compiler.py
│ │ ├── dispatcher.py
│ ├── agents/
│ │ ├── summarizer.py
│ │ ├── reasoner.py
│ │ ├── qa.py
│ ├── data/
│ │ ├── input_simulator.py
│ │ ├── memory_store.py
│ │ ├── lens_selector.py
│ ├── output/
│ │ ├── writer.py
│ │ ├── explain.py
│ ├── routes/
│ │ └── router.py
- frontend/
│ ├── app.js # Frontend
│ ├──index.html
│ ├──styles.css
├── .env # Contains OPENAI_API_KEY, MONGO_URI
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```
### 1. Clone the repository

```bash
git clone https://github.com/Saha-Manav/AI-Agent.git
cd AI-Agent
