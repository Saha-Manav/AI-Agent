def generate_explanation(lenses, results):
    return {
        "lenses_applied": lenses,
        "trace": f"Used lenses: {', '.join(lenses)} → summarized → reasoned → validated.",
        "output_summary": results['summary']
    }
