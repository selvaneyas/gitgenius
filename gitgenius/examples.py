# gitgenius/examples.py

EXAMPLE_ERRORS = [
    {
        "error": "fatal: not a git repository (or any of the parent directories): .git",
        "solution": "Run this command inside a valid Git repository or initialize one using 'git init'."
    },
    {
        "error": "error: failed to push some refs to 'origin'",
        "solution": "Pull the latest changes first with 'git pull --rebase origin <branch>' and try pushing again."
    },
    {
        "error": "merge conflict in <file>",
        "solution": "Open the file, resolve the conflicts, then run 'git add <file>' and 'git commit'."
    },
    {
        "error": "remote: Repository not found.",
        "solution": "Check if the remote URL is correct and you have access permissions."
    },
]
