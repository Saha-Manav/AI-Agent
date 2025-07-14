from agents.summarizer import summarize
from agents.reasoner import reason
from agents.qa import validate

def run_pipeline(user_input, lenses):
    reflection = user_input["reflection"]
    summary = summarize(reflection)
    reasoned = reason(summary)
    qa_status = validate(reasoned)
    
    return {
        "summary": summary,
        "reasoned_output": reasoned,
        "qa_status": qa_status
    }
