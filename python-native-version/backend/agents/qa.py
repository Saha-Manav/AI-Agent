def validate(output):
    if len(output.strip()) < 50:
        return "❌ Too short."
    return "✔ Validated successfully."
