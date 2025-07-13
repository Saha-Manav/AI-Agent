def build_prompt(user_input, lenses):
    return f"""Act as a {', '.join(lenses)}.
User said: "{user_input['reflection']}"
Project Info: {user_input['project_data']}
Emotion: {user_input['emotion']}"""
