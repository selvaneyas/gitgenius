# gitgenius/explainer.py

from .error_db import GIT_ERRORS

def explain_error(message: str) -> dict:
    """Return explanation and solution for a Git error."""
    for key in GIT_ERRORS:
        if key.lower() in message.lower():
            return {
                "error": key,
                "explanation": GIT_ERRORS[key]["explanation"],
                "solution": GIT_ERRORS[key]["solution"]
            }
    return {
        "error": message,
        "explanation": "Sorry, this Git error is not in the database yet.",
        "solution": "Try searching online or wait for a future update."
    }

def add_error_to_db(error: str, explanation: str, solution: str) -> bool:
    """Add a new error to the in-memory database (not persisted)."""
    if error in GIT_ERRORS:
        return False
    GIT_ERRORS[error] = {"explanation": explanation, "solution": solution}
    return True
