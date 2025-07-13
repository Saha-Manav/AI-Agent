def dispatch(source):
    return "realTime" if source in ["frontend", "api"] else "background"
