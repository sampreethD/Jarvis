"""JARVIS Web Application"""

import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="JARVIS AI Assistant")


# Read HTML from file
def get_html():
    with open("/workspace/project/jarvis/templates/index.html", "r") as f:
        return f.read()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    return get_html()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time chat with JARVIS"""
    await websocket.accept()
    
    # Check for API key
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        await websocket.send_text("ERROR: LLM_API_KEY not configured. Set it in environment variables.")
        await websocket.close()
        return
    
    try:
        from jarvis import JARVIS
        
        # Initialize JARVIS
        jarvis = JARVIS(api_key=api_key)
        
        # Send welcome message
        await websocket.send_text("JARVIS: Hello! I'm ready. How can I help you today?")
        
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            
            # Process the message
            response = await jarvis.process(data)
            
            # Send response back to client
            await websocket.send_text(f"JARVIS: {response}")
            
    except WebSocketDisconnect:
        pass
    except Exception as e:
        await websocket.send_text(f"ERROR: {str(e)}")
        await websocket.close()


def run_server(host: str = "0.0.0.0", port: int = 8000):
    """Run the web server"""
    import uvicorn
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
