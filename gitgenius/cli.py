import argparse
import getpass
import json
import subprocess
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.box import DOUBLE

from .explainer import explain_error
from .error_db import GIT_ERRORS
from .admin import run_admin_panel
from .config import load_config, save_config
from .examples import EXAMPLE_ERRORS  # ✅ load once here
from . import __version__

console = Console()
ROOT_PASSWORD = "admin123"  # Change this for production

# Load user config (emoji preference)
config = load_config()
EMOJI_ENABLED = config.get("emoji", True)


def format_text(emoji_text: str, plain_text: str) -> str:
    """Return emoji or plain text based on user preference."""
    return emoji_text if EMOJI_ENABLED else plain_text


def show_examples():
    """Print example Git errors from EXAMPLE_ERRORS."""
    console.print(
        Panel(
            format_text("🧪 [bold cyan]Example Git Errors[/bold cyan]", "Example Git Errors"),
            expand=False
        )
    )
    for err in EXAMPLE_ERRORS:
        console.print(f"[bold red]{err['error']}[/bold red] → {err['solution']}")


def show_git_basics():
    basics = [
        ("git init", "Create a new Git repository."),
        ("git clone <url>", "Download an existing repository."),
        ("git status", "Check changes in the working directory."),
        ("git add <file>", "Stage changes for the next commit."),
        ("git commit -m 'msg'", "Save staged changes."),
        ("git push", "Send commits to remote repository."),
        ("git pull", "Fetch and merge remote changes."),
        ("git branch", "List branches."),
        ("git checkout <branch>", "Switch branches."),
        ("git merge <branch>", "Merge another branch."),
        ("git log", "Show commit history."),
    ]
    console.print(format_text("📚 Basic Git Commands:", "Basic Git Commands:"))
    for cmd, desc in basics:
        console.print(f"[cyan]{cmd}[/cyan] - {desc}")


def show_git_version():
    try:
        output = subprocess.check_output(["git", "--version"], text=True)
        console.print(f"[bold green]{output.strip()}[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")


def show_current_branch():
    try:
        output = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True
        )
        console.print(f"[cyan]Current branch:[/cyan] {output.strip()}")
    except subprocess.CalledProcessError:
        console.print("[red]Not inside a Git repository.[/red]")


def show_repo_status():
    try:
        output = subprocess.check_output(["git", "status", "--short"], text=True)
        console.print(f"[yellow]{output.strip()}[/yellow]" if output else "[green]Clean working tree[/green]")
    except subprocess.CalledProcessError:
        console.print("[red]Not inside a Git repository.[/red]")


def show_recent_commits(n=5):
    try:
        output = subprocess.check_output(
            ["git", "log", f"-{n}", "--oneline"], text=True
        )
        console.print(f"[magenta]{output.strip()}[/magenta]")
    except subprocess.CalledProcessError:
        console.print("[red]Not inside a Git repository.[/red]")


def main():
    parser = argparse.ArgumentParser(
        description=format_text(
            "🔍 GitGenius: Understand common Git errors and how to fix them.",
            "GitGenius: Understand common Git errors and how to fix them."
        ),
        epilog=format_text(
            "📌 Example: gitgenius 'fatal: not a git repository'",
            "Example: gitgenius 'fatal: not a git repository'"
        )
    )

    # Emoji toggles
    parser.add_argument("--no-emoji", action="store_true", help="Disable emoji permanently.")
    parser.add_argument("--set-emoji", action="store_true", help="Enable emoji permanently.")

    # Git info commands
    parser.add_argument("--git-version", action="store_true", help="Show installed Git version.")
    parser.add_argument("--current-branch", action="store_true", help="Show current branch name.")
    parser.add_argument("--repo-status", action="store_true", help="Show repository status.")
    parser.add_argument("--recent-commits", type=int, nargs="?", const=5, help="Show recent commits (default 5).")
    parser.add_argument("--help-git", action="store_true", help="Show basic Git commands and explanations.")

    # Main CLI features
    parser.add_argument("message", type=str, nargs="?", help="The Git error message to explain (in quotes).")
    parser.add_argument("--admin", action="store_true", help="Access the admin panel (password protected).")
    parser.add_argument("--version", action="store_true", help="Show the current version of GitGenius.")
    parser.add_argument("--examples", action="store_true", help="Show example Git errors and solutions.")
    parser.add_argument("--json", action="store_true", help="Output explanation in JSON format.")

    args = parser.parse_args()

    # Emoji settings
    if args.no_emoji:
        config["emoji"] = False
        save_config(config)
        console.print("[yellow]Emojis disabled for all future runs.[/yellow]")
        return
    if args.set_emoji:
        config["emoji"] = True
        save_config(config)
        console.print("[green]Emojis enabled for all future runs.[/green]")
        return

    # Git info commands
    if args.git_version:
        show_git_version()
        return
    if args.current_branch:
        show_current_branch()
        return
    if args.repo_status:
        show_repo_status()
        return
    if args.recent_commits:
        show_recent_commits(args.recent_commits)
        return
    if args.help_git:
        show_git_basics()
        return

    # Version
    if args.version:
        console.print(f"[bold green]GitGenius v{__version__}[/bold green] {format_text('✅', '')}")
        return

    # Examples
    if args.examples:
        show_examples()
        return

    # Admin panel
    if args.admin:
        password = getpass.getpass("Enter admin password: ")
        if password != ROOT_PASSWORD:
            console.print(f"[bold red]{format_text('❌', 'X')} Access Denied: Incorrect Password[/bold red]")
            return
        run_admin_panel()
        return

    # Main error explanation
    if not args.message:
        console.print(f"[bold red]{format_text('❗', '!')} Please provide a Git error message to explain.[/bold red]")
        console.print(format_text(
            "📌 Example: gitgenius 'fatal: not a git repository'",
            "Example: gitgenius 'fatal: not a git repository'"
        ))
        return

    result = explain_error(args.message)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    # Output panels
    console.print(Panel(
        f"Git Error: [bold red]{result['error']}[/bold red]",
        title=format_text("⚠ Git Error", "Git Error"),
        style="bold red",
        expand=False
    ))

    explanation_panel = Panel(
        Text(result['explanation'], style="yellow"),
        title=format_text("📝 Explanation", "Explanation"),
        style="yellow",
        expand=False,
        box=DOUBLE
    )
    console.print(explanation_panel)

    fix_panel = Panel(
        f"Suggested Fix:\n{result['solution']}",
        title=format_text("✅ Fix Suggestion", "Fix Suggestion"),
        title_align="center",
        style="green",
        expand=False
    )
    console.print(fix_panel)

    # Tip
    tip = Text(
        f"\n{format_text('💡', 'Tip:')} Use '--examples' to learn more Git errors.\n"
        f"{format_text('🔐', 'Note:')} Use '--admin' to add/manage errors.\n",
        style="italic dim"
    )
    console.print(tip)
    console.print(f"[dim]GitGenius CLI - Version {__version__}[/dim]")


if __name__ == "__main__":
    main()
