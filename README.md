<p align="center">
  <img src="https://raw.githubusercontent.com/selvaneyas/gitgenius/main/assert/2.png" alt="GitGenius CLI Logo" width="400"/>
</p>

<h1 align="center">GitGenius CLI</h1>

<p align="center">
  <em>Understand Git errors in plain English – directly from your terminal.</em>
</p>

<p align="center">
  <a href="https://pypi.org/project/gitgenius/">
    <img src="https://img.shields.io/pypi/v/gitgenius" alt="PyPI Version">
  </a>
  <a href="https://pypi.org/project/gitgenius/">
    <img src="https://img.shields.io/pypi/pyversions/gitgenius" alt="Python Versions">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://github.com/selvaneyas/gitgenius/stargazers">
    <img src="https://img.shields.io/github/stars/selvaneyas/gitgenius.svg?style=social" alt="GitHub Stars">
  </a>
  <a href="https://github.com/selvaneyas/gitgenius/issues">
    <img src="https://img.shields.io/github/issues/selvaneyas/gitgenius.svg" alt="GitHub Issues">
  </a>
  <a href="https://github.com/selvaneyas/gitgenius/commits/main">
    <img src="https://img.shields.io/github/last-commit/selvaneyas/gitgenius" alt="Last Commit">
  </a>
</p>

---

## 📦 Installation

Install GitGenius using:

```bash
pip install gitgenius
```
Or from the local source:

```bash
pip install .
```

---

## 🚀 Usage

Basic command:

```bash
gitgenius "fatal: not a git repository"
```

Or run the assistant mode:

```bash
gitgenius --admin
```

---

## ✅ Example Output

```
Explanation: This error means you're trying to run a Git command outside a Git repository.
Solution: Navigate to a folder that is a Git repo, or initialize one with `git init`.
```

---

## 🧪 Run Tests

```bash
python3 -m unittest discover tests
```

---

## 💡 Features

* Explains Git errors in simple terms.
* Suggests solutions and fixes.
* CLI and admin assistant modes available.
* Lightweight and beginner-friendly tool.

---

## ❓ Why GitGenius?

Git errors can be frustrating, especially for beginners. GitGenius makes it easier to:

* Understand what's wrong.
* Know how to fix it.
* Learn Git through the terminal.

---

## 🖥️ Compatibility

* ✅ Windows (CMD/PowerShell) *(emoji support optional, see below)*
* ✅ Linux
* ✅ macOS

### ⚠️ Windows CMD Emoji Issue

Windows CMD does not support emojis by default.

#### 💡 Fix Options:

* Use **Windows Terminal**, **PowerShell**, or **Git Bash**.
* Or remove emojis by adding a `--no-emoji` flag in your tool (recommended feature to add).

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🌟 Star & Contribute

If you find this project helpful, give it a ⭐ on [GitHub](https://github.com/selvaneyas/gitgenius)!
Feel free to fork and improve the tool — contributions are welcome.

---

## 📫 Contact

Built with ❤️ by [Selva Neyas U](https://github.com/selvaneyas)

---