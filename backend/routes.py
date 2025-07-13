from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from data.memory_store import store_context_memory
from data.lens_selector import select_lenses
from core.prompt_compiler import build_prompt
from core.dispatcher import dispatch
from core.orchestrator import run_pipeline
from output.writer import write_output
from output.explain import generate_explanation

router = APIRouter()

class UserInput(BaseModel):
    reflection: str
    session_context: Dict[str, Any]
    project_data: Dict[str, Any] = {}
    emotional_metadata: Dict[str, Any] = {}

@router.post("/run-agent")
async def run_agent(user_input: UserInput):
    try:
        user_input_dict = user_input.dict()

        store_context_memory(user_input_dict)
        lenses = select_lenses(user_input_dict["session_context"])
        _ = build_prompt(user_input_dict, lenses)
        _ = dispatch("api")

        results = run_pipeline(user_input_dict, lenses)
        explanation = generate_explanation(lenses, results)

        write_output(user_input_dict, results, explanation)

        return {
            "status": "success",
            "results": results,
            "explanation": explanation,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
