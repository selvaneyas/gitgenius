# gitgenius/cli.py

import argparse
import getpass
from .explainer import explain_error, add_error_to_db
from .error_db import GIT_ERRORS  
from .admin import run_admin_panel
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.box import DOUBLE, HEAVY

console = Console()

ROOT_PASSWORD = "admin123"  # Change for security
def main():
    parser = argparse.ArgumentParser(
        description="🔍 GitGenius: Understand common Git errors and how to fix them."
    )

    parser.add_argument("message", type=str, nargs="?", help="The Git error message to explain (in quotes).")
    parser.add_argument("--admin", action="store_true", help="Access the admin panel (password protected).")

    args = parser.parse_args()

    if args.admin:
        password = getpass.getpass("Enter admin password: ")
        if password != ROOT_PASSWORD:
            console.print("[bold red]❌ Access Denied: Incorrect Password[/bold red]")
            return
        run_admin_panel()
        return

    if not args.message:
        console.print("[bold red]Please provide a Git error message to explain.[/bold red]")
        return

    result = explain_error(args.message)

    # ────────────── FORMATTED OUTPUT ──────────────
    console.print(Panel(f"Git Error: [bold red]{result['error']}[/bold red]", title="⚠ Git Error", style="bold red", expand=False))

    explanation_panel = Panel(
            Text(result['explanation'], style="yellow"),
            title="📝 Explanation",
            style="yellow",
            expand=False,
            box=DOUBLE
        )
    console.print(explanation_panel)

    fix_panel = Panel(
        f"Suggested Fix:\n{result['solution']}",
        title="✅ Success",
        title_align="center",
        style="green",
        expand=False
    )
    console.print(fix_panel)

    console.print(f"\n[bold yellow]Explanation:[/bold yellow] {result['explanation']}")

    # Tip
    tip = Text("\nTip: Run with '--admin' to add or manage Git errors.", style="dim italic")
    console.print(tip)
    console.print("\n[dim] GitGenius : version : 0.0.1 ✅[/dim]")
