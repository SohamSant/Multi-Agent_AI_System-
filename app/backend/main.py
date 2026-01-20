import sys
import os
# Ensure user site-packages are in path
sys.path.append(r"C:\Users\Admin\AppData\Roaming\Python\Python313\site-packages")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
from app.core.ai_agent import get_response_from_agents
from app.common.logger import get_logger

logger = get_logger("backend")

app = FastAPI(title="Muli-AI Agent API")

logger.info("Backend application started")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str
    llm_id: Optional[str] = "llama-3.3-70b-versatile"
    allow_search: Optional[bool] = False
    system_prompt: Optional[str] = "You are a helpful AI assistant."

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        logger.info(f"Received request: {request.query}")
        response = get_response_from_agents(
            llm_id=request.llm_id,
            query=request.query,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt
        )
        return ChatResponse(response=response)
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app.backend.main:app", host="0.0.0.0", port=8000, reload=True)
