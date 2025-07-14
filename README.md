# 🧠 AI Agent System

An AI-driven reasoning and explanation system that provides both Python-native and n8n workflow implementations of the same intelligent agent pipeline. Built with FastAPI, OpenAI and Gemini GPT models, and MongoDB, this system enables real-time summarization, reasoning, and Q&A validation of user reflections. Supports both REST API and CLI modes.

---
## 🔄 Two Versions Included

This repository includes **two parallel implementations** of the same modular AI agent system:

1. **Python-Native Version**
   - Fully implemented in Python using **FastAPI**
   - Supports both **API** and **CLI** execution
   - More customizable and suitable for deep integration and extension

2. **n8n Workflow Version**
   - Implements the same logic as a visual, **low-code workflow** using [n8n](https://n8n.io/)
   - Ideal for **automation, orchestration**, and connecting external services
   - Easier to deploy and maintain for users familiar with **no-code/low-code tools**
     
---
## ✨ Key Features

### 🐍 Native Python Version

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

### 🧩 n8n Docker Version

- 🖼️ **Visual low-code workflow** using [n8n](https://n8n.io/)
- 🌐 **API calls handled via Webhooks and HTTP Request nodes**
- 📤 **Outputs saved to MongoDB and Context-aware memory**
- 🧠 **AI agents orchestrated with custom nodes and logic branches**
- 🧩 **Reusable modular nodes** for summarization, reasoning, and QA
- 📥 **Easily integrates with external services** (e.g. Google Sheets)
- 🧠 **AI agents powered by the Gemini GPT API**
- 🔐 **Environment variables managed via n8n credentials**
- 📦 **Packaged in a Docker container** for easy deployment and testing


---

## 📂 Project Structure

n8n-docker-version/
- backend/
  - My workflow.json
- frontend/
    - app.js 
    - index.html
    - styles.css 

python-native-version/
- backend/
  - main.py  # FastAPI entrypoint + CLI mode
  - api_logic.py  # Shared logic between API and CLI
  - core/
    - orchestrator.py # Agent pipeline coordinator
    - prompt_compiler.py
    - dispatcher.py
  - agents/
    - summarizer.py
    - reasoner.py
    - qa.py
  - data/
    - input_simulator.py
    - memory_store.py
    - lens_selector.py
  - output/
    - writer.py
    - explain.py
  - routes/
    - router.py
  - .env  # Contains OPENAI_API_KEY, MONGO_URI
  - requirements.txt
   
- frontend/
    - app.js 
    - index.html
    - styles.css
 
- README.md
- LICENSE
---

## ⚙️ Setup Instructions

### ▶️ For Python-Native Version

#### 1. Clone Repository

```bash
git clone https://github.com/Saha-Manav/AI-Agent.git
cd AI-Agent/python-native-version/backend
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
#### 3. Run FastAPI Server
```bash
uvicorn main:app --reload
```
Access the server at: 
```bash
http://127.0.0.1:8000
```

### ▶️ For n8n Workflow Version

#### 1. Install and Start n8n (Docker Recommended)

```bash
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```
#### 2. Import the Workflow
Open 
```bash
http://localhost:5678
```
Import My workflow.json from n8n-docker-version/backend/ and configure environment variables and credentials (OpenAI key, MongoDB)
