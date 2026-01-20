import streamlit as st
import requests
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.common.logger import get_logger

logger = get_logger("frontend")

# Set page title
st.set_page_config(page_title="Muli-AI Agent", page_icon="🤖")

if "logger_initialized" not in st.session_state:
    logger.info("Frontend application started")
    st.session_state.logger_initialized = True

st.title("🤖 Muli-AI Agent")

# Sidebar Configuration
st.sidebar.header("Configuration")

# API URL
api_url = os.getenv("BACKEND_API_URL", "http://127.0.0.1:8000")

# Model Selection
model_options = [
    "llama-3.3-70b-versatile",
    "llama-3.2-70b-versatile", # Kept for compatibility if user has access
    "openai/gpt-oss-120b"
]
selected_model = st.sidebar.selectbox("Select Model", model_options, index=0)

# System Prompt
system_prompt = st.sidebar.text_area(
    "System Prompt",
    value="You are a helpful and knowledgeable AI assistant. Answer the user's questions clearly and concisely."
)

# Web Search Toggle
allow_search = st.sidebar.checkbox("Enable Web Search", value=False)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("What is on your mind?"):
    logger.info(f"User input received: {prompt}")
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare payload
    payload = {
        "query": prompt,
        "llm_id": selected_model,
        "allow_search": allow_search,
        "system_prompt": system_prompt
    }

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        try:
            response = requests.post(f"{api_url}/chat", json=payload)
            response.raise_for_status()
            data = response.json()
            ai_response = data.get("response", "Error: No response from backend.")
            message_placeholder.markdown(ai_response)
            
            # Add assistant message to history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            logger.info("Response received and displayed")
            
        except requests.exceptions.ConnectionError:
            logger.error("Connection error: Could not connect to backend")
            message_placeholder.error("Error: Could not connect to the backend. Is it running?")
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}", exc_info=True)
            message_placeholder.error(f"Error: {str(e)}")
