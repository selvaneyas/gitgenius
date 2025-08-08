# # gitgenius/error_db1.py

# gitgenius/error_db.py
# gitgenius/error_db.py

import json
import os

ERRORS_FILE = os.path.join(os.path.dirname(__file__), "error_db.json")

def load_errors():
    """Load Git error messages from JSON file."""
    if os.path.exists(ERRORS_FILE):
        with open(ERRORS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_errors(errors):
    """Save Git error messages to JSON file."""
    with open(ERRORS_FILE, "w") as f:
        json.dump(errors, f, indent=4)

# Load errors once at import
GIT_ERRORS = load_errors()

# error_database = {
#     "fatal: not a git repository":
#         "This error means that the command you're trying to run isn't inside a Git repository folder.\n"
#         "💡 Solution: Navigate into a valid Git repository or initialize one with `git init`.",

#     "fatal: remote origin already exists":
#         "You've already added a remote named 'origin'.\n"
#         "💡 Solution: Either use a different name with `git remote add newname <url>`\n"
#         "or update the existing one with `git remote set-url origin <url>`.",

#     "error: failed to push some refs":
#         "This usually happens when your local branch is behind the remote branch.\n"
#         "💡 Solution: Run `git pull --rebase` before pushing, or use `git push --force` cautiously.",

#     "merge conflict":
#         "Git can’t automatically merge the changes between two branches.\n"
#         "💡 Solution: Open the conflicting files, resolve conflicts manually, then add and commit again.",

#     "fatal: refusing to merge unrelated histories":
#         "This happens when Git can't find a common base between two branches.\n"
#         "💡 Solution: Use `git pull origin main --allow-unrelated-histories` to force merge.",

#     "Updates were rejected because the tip of your current branch is behind":
#         "Your local branch is outdated compared to the remote.\n"
#         "💡 Solution: Run `git pull --rebase` to sync changes before pushing.",

#     "You have not concluded your merge":
#         "A merge was started but not completed.\n"
#         "💡 Solution: Run `git commit` to finish the merge or `git merge --abort` to cancel.",

#     "fatal: destination path already exists and is not an empty directory":
#         "You're trying to clone into a folder that already has files.\n"
#         "💡 Solution: Use an empty folder or delete the existing one before cloning.",

#     "Permission denied (publickey)":
#         "Git couldn't authenticate with the remote using your SSH key.\n"
#         "💡 Solution: Make sure your SSH key is added to your Git host and the SSH agent.",

#     "Could not resolve hostname":
#         "The remote repository address is incorrect or unreachable.\n"
#         "💡 Solution: Double-check the URL. Try pinging the server or using HTTPS instead.",

#     "Your branch is ahead of 'origin/main' by":
#         "Your local branch has commits that aren't pushed.\n"
#         "💡 Solution: Run `git push` to sync your changes to the remote repository.",

#     "Your branch is behind 'origin/main' by":
#         "Your local branch lacks commits from the remote.\n"
#         "💡 Solution: Run `git pull` or `git pull --rebase` to update.",

#     "fatal: bad revision":
#         "You tried to checkout or reference a non-existent commit/branch.\n"
#         "💡 Solution: Check your spelling and use `git branch` or `git log` to find the right name.",

#     "fatal: ambiguous argument":
#         "Git couldn’t interpret what you typed (branch/commit/tag/etc).\n"
#         "💡 Solution: Use full references or clarify your command. Example: `git checkout origin/main`.",

#     "error: pathspec did not match any file(s) known to git":
#         "The file or branch you're trying to checkout or reset doesn’t exist.\n"
#         "💡 Solution: Check for typos or run `git status` to see current paths and files."
# }
