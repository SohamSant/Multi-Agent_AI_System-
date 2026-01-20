"""
Main entry point for the Muli-AI Agent application.
This script launches both the backend (FastAPI) and frontend (Streamlit) services.
"""
import subprocess
import sys
import os
import time
from pathlib import Path
from app.common.logger import get_logger

logger = get_logger("main")

def main():
    """Launch both backend and frontend services concurrently."""
    
    logger.info("Application launcher started")
    
    # Get the project root directory
    project_root = Path(__file__).parent.parent
    
    print("🚀 Starting Muli-AI Agent Application...")
    print("=" * 50)
    
    # Start backend server
    print("\n📡 Starting Backend Server (FastAPI)...")
    logger.info("Launching backend server process")
    backend_process = subprocess.Popen(
        [sys.executable, "-m", "app.backend.main"],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Give the backend a moment to start
    time.sleep(2)
    logger.info("Backend server process started")
    
    # Start frontend dashboard
    print("🎨 Starting Frontend Dashboard (Streamlit)...")
    logger.info("Launching frontend dashboard process")
    frontend_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "app/frontend/dashboard.py"],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    logger.info("Frontend dashboard process started")
    
    print("\n✅ Both services are starting!")
    print("=" * 50)
    print("📡 Backend API: http://localhost:8000")
    print("🎨 Frontend UI: http://localhost:8501")
    print("=" * 50)
    print("\n💡 Press Ctrl+C to stop both services\n")
    logger.info("Both services are running - Backend: http://localhost:8000, Frontend: http://localhost:8501")
    
    try:
        # Keep the script running and monitor both processes
        while True:
            # Check if backend is still running
            if backend_process.poll() is not None:
                print("\n❌ Backend server stopped unexpectedly!")
                logger.error("Backend server process terminated unexpectedly")
                frontend_process.terminate()
                logger.info("Terminating frontend dashboard process")
                break
            
            # Check if frontend is still running
            if frontend_process.poll() is not None:
                print("\n❌ Frontend dashboard stopped unexpectedly!")
                logger.error("Frontend dashboard process terminated unexpectedly")
                backend_process.terminate()
                logger.info("Terminating backend server process")
                break
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down services...")
        logger.info("Shutdown signal received, terminating all services")
        backend_process.terminate()
        frontend_process.terminate()
        
        # Wait for processes to terminate
        backend_process.wait()
        frontend_process.wait()
        
        print("✅ All services stopped successfully!")
        logger.info("All services stopped successfully")
        sys.exit(0)

if __name__ == "__main__":
    main()
