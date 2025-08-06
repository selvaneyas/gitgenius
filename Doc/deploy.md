# Deploy

> git tag v1.0.0

> git push origin v1.0.0

---
# 🚀 Deployment Manual – GitGenius CLI

This document explains how to **build**, **test**, and **deploy** the GitGenius CLI Python package to [PyPI](https://pypi.org/project/gitgenius/).

---

## 📦 1. Install Required Tools

Make sure the following tools are installed:

```bash
pip install --upgrade setuptools wheel twine
```


---

## 🔧 2. Project Structure

```
gitgenius/
│
├── gitgenius/         # Python package
│   ├── __init__.py
│   ├── cli.py
│   ├── explainer.py
│   ├── error_db.py
│   └── admin.py
│
├── setup.py
├── README.md
├── LICENSE
├── MANIFEST.in
├── requirements.txt
└── doc/
    └── deploy.md
```

---

## ✏️ 3. Update `setup.py` Version

Each time you deploy a new version, bump the version number in `setup.py`:

```python
version="0.1.2"
```

Also update the version in:

* `gitgenius/cli.py` → `VERSION = "0.1.2"`

---

## 📚 4. Check or Create `MANIFEST.in`

Ensure this file exists at the root:

```
include README.md
include LICENSE
```

---

## 🧪 5. Test the Package Locally

```bash
pip uninstall gitgenius -y
python setup.py install
```

Then run:

```bash
gitgenius "fatal: not a git repository"
```

---

## 📦 6. Build the Package

```bash
python setup.py sdist bdist_wheel
```

Output appears in the `dist/` folder:

```
dist/
├── gitgenius-0.1.2.tar.gz
└── gitgenius-0.1.2-py3-none-any.whl
```

---

## 🚀 7. Upload to PyPI

Make sure you're registered on [https://pypi.org](https://pypi.org). Then:

```bash
twine upload dist/*
```

Enter your PyPI credentials when prompted.

---

## ✅ 8. Verify Installation from PyPI

Test in a fresh environment or virtualenv:

```bash
pip install gitgenius
gitgenius --version
gitgenius --examples
```

---

## 🧹 9. Clean Up Build Files

(Optional, but recommended)

```bash
rm -rf build dist *.egg-info
```

---



## 👨‍💻 Maintainer

**Author**: Selva Neyas U
**Email**: [selvaneyas@gmail.com](mailto:selvaneyas@gmail.com)
**License**: MIT
**PyPI**: [https://pypi.org/project/gitgenius/](https://pypi.org/project/gitgenius/)



---

