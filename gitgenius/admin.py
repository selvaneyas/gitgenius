# gitgenius/admin.py

from .error_db import GIT_ERRORS, save_errors

def show_all_errors():
    if not GIT_ERRORS:
        print("\nℹ️ No errors stored yet.")
        return

    print("\n📘 All Stored Git Errors:\n")
    for idx, (error, details) in enumerate(GIT_ERRORS.items(), 1):
        print(f"{idx}. Error: {error}")
        print(f"   Explanation: {details.get('explanation', 'N/A')}")
        print(f"   Solution: {details.get('solution', 'N/A')}\n")

def add_new_error():
    error = input("📝 Enter new Git error message: ").strip()
    if not error:
        print("❗ Error message cannot be empty.")
        return
    if error in GIT_ERRORS:
        print("⚠️ This error already exists. Use update option.")
        return

    explanation = input("📖 Enter explanation: ").strip()
    solution = input("🛠️  Enter solution: ").strip()

    GIT_ERRORS[error] = {
        "explanation": explanation or "No explanation provided.",
        "solution": solution or "No solution provided."
    }
    save_errors(GIT_ERRORS)
    print("✅ Error added successfully!")

def update_error():
    error = input("✏️ Enter Git error to update: ").strip()
    if error not in GIT_ERRORS:
        print("❌ Error not found.")
        return

    explanation = input("📖 Enter updated explanation: ").strip()
    solution = input("🛠️ Enter updated solution: ").strip()

    GIT_ERRORS[error] = {
        "explanation": explanation or GIT_ERRORS[error]["explanation"],
        "solution": solution or GIT_ERRORS[error]["solution"]
    }
    save_errors(GIT_ERRORS)
    print("✅ Error updated successfully!")

def delete_error():
    error = input("🗑️ Enter Git error to delete: ").strip()
    if error in GIT_ERRORS:
        confirm = input(f"Are you sure you want to delete '{error}'? (yes/no): ").strip().lower()
        if confirm == "yes":
            del GIT_ERRORS[error]
            save_errors(GIT_ERRORS)
            print("✅ Error deleted.")
        else:
            print("🚫 Deletion canceled.")
    else:
        print("❌ Error not found.")

def run_admin_panel():
    print("\n👨‍💻 Welcome to GitGenius Admin Panel")

    while True:
        print("\n🔧 Options:\n1. Show All Errors\n2. Add Error\n3. Update Error\n4. Delete Error\n5. Exit")
        choice = input("🔍 Select an option [1-5]: ").strip()

        if choice == '1':
            show_all_errors()
        elif choice == '2':
            add_new_error()
        elif choice == '3':
            update_error()
        elif choice == '4':
            delete_error()
        elif choice == '5':
            print("👋 Exiting Admin Panel. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please enter a number between 1 and 5.")
