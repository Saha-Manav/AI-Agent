# main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

from api_logic import process_user_reflection  # Import the processing logic
from routes import router  # Import  router for additional routes

app = FastAPI(title="DeepThought AI Agent System")

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Optional: include additional route files
app.include_router(router)

# Define expected input format
class UserInput(BaseModel):
    reflection: str
    session_context: Dict[str, Any]

# Route to handle AI processing
@app.post("/process_reflection")
async def process_reflection(user_input: UserInput):
    try:
        user_input_dict = user_input.dict()
        result = process_user_reflection(user_input_dict)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

# Local development server start (optional for uvicorn CLI)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
