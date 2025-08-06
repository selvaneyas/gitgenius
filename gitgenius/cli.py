# gitgenius/cli.py

import argparse
import getpass
import json
from .explainer import explain_error, add_error_to_db
from .error_db import GIT_ERRORS  
from .admin import run_admin_panel
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.box import DOUBLE, HEAVY

console = Console()

VERSION = "0.1.1"
ROOT_PASSWORD = "admin123"  # Change for security


def show_examples():
    console.print(Panel("🧪 [bold cyan]Example Git Errors[/bold cyan]", expand=False))
    for err, details in GIT_ERRORS.items():
        console.print(f"\n❌ [bold red]{err}[/bold red]")
        console.print(f"[yellow]👉 Explanation:[/yellow] {details['explanation']}")
        console.print(f"[green]🔧 Solution:[/green] {details['solution']}")


def main():
    parser = argparse.ArgumentParser(
        description="🔍 GitGenius: Understand common Git errors and how to fix them.",
        epilog="📌 Example: gitgenius 'fatal: not a git repository'"
    )

    parser.add_argument("message", type=str, nargs="?", help="The Git error message to explain (in quotes).")
    parser.add_argument("--admin", action="store_true", help="Access the admin panel (password protected).")
    parser.add_argument("--version", action="store_true", help="Show the current version of GitGenius.")
    parser.add_argument("--examples", action="store_true", help="Show example Git errors and solutions.")
    parser.add_argument("--json", action="store_true", help="Output explanation in JSON format.")

    args = parser.parse_args()

    # ─── Version ─────────────────────────────────────
    if args.version:
        console.print(f"[bold green]GitGenius v{VERSION}[/bold green] ✅")
        return

    # ─── Examples ─────────────────────────────────────
    if args.examples:
        show_examples()
        return

    # ─── Admin Panel ─────────────────────────────────
    if args.admin:
        password = getpass.getpass("Enter admin password: ")
        if password != ROOT_PASSWORD:
            console.print("[bold red]❌ Access Denied: Incorrect Password[/bold red]")
            return
        run_admin_panel()
        return

    # ─── Main Message ────────────────────────────────
    if not args.message:
        console.print("[bold red]❗ Please provide a Git error message to explain.[/bold red]")
        console.print("📌 Example: gitgenius 'fatal: not a git repository'")
        return

    result = explain_error(args.message)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    # ─── FORMATTED OUTPUT ─────────────────────────────
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
        title="✅ Fix Suggestion",
        title_align="center",
        style="green",
        expand=False
    )
    console.print(fix_panel)

    # ─── Tip ─────────────────────────────────────────
    tip = Text("\n💡 Tip: Use '--examples' to learn more Git errors.\n🔐 Use '--admin' to add/manage errors.\n", style="italic dim")
    console.print(tip)
    console.print(f"[dim]GitGenius CLI - Version {VERSION}[/dim]")
