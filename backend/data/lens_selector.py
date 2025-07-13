def select_lenses(session_context):
    role = session_context["role"]
    config = {
        "PM": ["Project Management", "Meta-Reflection"],
        "Psychologist": ["Psychology", "Meta-Reflection"],
        "CXO": ["Business Strategy", "Meta-Reflection"]
    }
    return config.get(role, ["Meta-Reflection"])
