# 🤖 Multi-Agent AI System

A production-ready intelligent AI agent application built with **LangChain**, **LangGraph**, and **FastAPI**. This full-stack platform enables conversational AI interactions with real-time web search capabilities through a clean, modern Streamlit interface.

## ✨ Features

- **🧠 Multi-Agent Architecture**: Built using LangGraph's ReAct (Reasoning + Acting) framework
- **🔍 Web Search Integration**: Real-time search capabilities via Tavily API
- **⚡ FastAPI Backend**: High-performance async API server
- **🎨 Streamlit Frontend**: Interactive, user-friendly dashboard
- **🔧 Configurable LLM**: Powered by Groq's LLM models
- **📝 Comprehensive Logging**: Built-in logging system for debugging and monitoring
- **🛡️ Error Handling**: Custom exception handling for robust operation
- **🚀 Concurrent Service Management**: Automated startup of both backend and frontend services

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server for FastAPI
- **Pydantic** - Data validation and settings management

### AI/ML
- **LangChain** - Framework for developing LLM applications
- **LangGraph** - Library for building stateful, multi-actor applications
- **langchain-groq** - Groq LLM integration
- **langchain-community** - Community-contributed tools and integrations

### Frontend
- **Streamlit** - Interactive web application framework

### External APIs
- **Groq API** - LLM inference
- **Tavily API** - Web search functionality

## 📋 Prerequisites

- Python 3.8+
- Groq API Key ([Get it here](https://console.groq.com/))
- Tavily API Key ([Get it here](https://tavily.com/))

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Muli-AI-Agent
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
TAV_API_KEY=your_tavily_api_key_here
```

## 💻 Usage

### Run the Complete Application
Launch both backend and frontend services simultaneously:
```bash
python -m app.main
```

This will start:
- **Backend API**: http://localhost:8000
- **Frontend UI**: http://localhost:8501

### Run Services Individually

**Backend Only:**
```bash
python -m app.backend.main
```

**Frontend Only:**
```bash
streamlit run app/frontend/dashboard.py
```

## 📁 Project Structure

```
Muli-AI-Agent/
├── app/
│   ├── backend/          # FastAPI backend server
│   │   └── main.py       # API endpoints
│   ├── common/           # Shared utilities
│   │   ├── logger.py     # Logging configuration
│   │   └── custom_exception.py
│   ├── config/           # Configuration management
│   │   └── settings.py   # Environment settings
│   ├── core/             # Core business logic
│   │   └── ai_agent.py   # AI agent implementation
│   ├── frontend/         # Streamlit dashboard
│   │   └── dashboard.py
│   └── main.py           # Application launcher
├── logs/                 # Application logs
├── .env                  # Environment variables (not in git)
├── .gitignore
├── requirements.txt      # Python dependencies
├── setup.py             # Package configuration
└── README.md
```

## 🎯 How It Works

1. **User Input**: Users interact through the Streamlit dashboard
2. **API Request**: Frontend sends requests to FastAPI backend
3. **Agent Processing**: LangGraph agent processes queries using ReAct framework
4. **LLM Inference**: Groq API provides intelligent responses
5. **Web Search** (Optional): Tavily API enables real-time information retrieval
6. **Response Delivery**: Results are displayed in the dashboard

## 🔧 Configuration

Customize agent behavior in `app/config/settings.py`:
- LLM model selection
- API configurations
- System prompts
- Search parameters

## 📊 Key Components

### AI Agent (`app/core/ai_agent.py`)
- Implements ReAct agent pattern
- Configurable LLM models
- Optional web search tool integration
- Handles message processing and response generation

### Backend API (`app/backend/main.py`)
- RESTful API endpoints
- Request/response handling
- Integration with AI agent

### Frontend Dashboard (`app/frontend/dashboard.py`)
- Interactive chat interface
- Model selection
- Search toggle
- Response visualization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a portfolio project demonstrating full-stack AI application development.

---

**Note**: Press `Ctrl+C` in the terminal to stop all services when running via `app.main`.
"# Multi-Agent_AI_System-" 
