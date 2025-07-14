from data.memory_store import store_context_memory
from data.lens_selector import select_lenses
from core.prompt_compiler import build_prompt
from core.dispatcher import dispatch
from core.orchestrator import run_pipeline
from output.writer import write_output
from output.explain import generate_explanation

def process_user_reflection(user_input):
    # user_input should be a dict, not from get_user_input()
    store_context_memory(user_input)
    lenses = select_lenses(user_input['session_context'])
    compiled_prompt = build_prompt(user_input, lenses)
    mode = dispatch("frontend")
    results = run_pipeline(user_input, lenses)
    explanation = generate_explanation(lenses, results)
    write_output(user_input, results, explanation)
    return {
        "results": results,
        "explanation": explanation,
        "mode": mode,
        "compiled_prompt": compiled_prompt,
    }

# Optionally keep main() for standalone testing
def main():
    print("DeepThought Agent System Started")
    from data.input_simulator import get_user_input
    user_input = get_user_input()
    output = process_user_reflection(user_input)
    print("Execution Complete.")
    print(output)

if __name__ == "__main__":
    main()
