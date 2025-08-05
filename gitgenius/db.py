# gitgenius/error_db.py

ERROR_DATABASE = {
    "fatal: not a git repository": "This error means you're trying to run a Git command outside a Git repository. You need to initialize it using 'git init' or navigate into an existing Git repo.",
    "merge conflict": "Git is unable to merge branches automatically because of conflicting changes. Open the affected files, look for conflict markers (<<<<), resolve them, then commit the merge.",
    "error: failed to push some refs": "This happens when your local branch is behind the remote one. Do a 'git pull --rebase' and then push again.",
    # Add more errors as needed
}


def get_explanation(error_message: str) -> str:
    for key in ERROR_DATABASE:
        if key.lower() in error_message.lower():
            return ERROR_DATABASE[key]
    return "❌ Sorry, I couldn’t understand this Git error. Try searching online or checking the documentation."

