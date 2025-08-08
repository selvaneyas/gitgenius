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


---

## ✅ 1. 🧱 Project Structure Example

```
your-docs-project/
│
├── docs/
│   ├── index.md
│   └── ...other pages...
│
├── mkdocs.yml
└── .git
```

---

## ✅ 2. 📄 `mkdocs.yml` Configuration (Basic)

```yaml
site_name: GitGenius
site_description: Understand Git errors in plain English.
site_author: Selvaneyas

theme:
  name: material
  logo: assets/favicon.ico
  favicon: assets/favicon.ico
  palette:
    scheme: default

plugins:
  - search
  - mike  # Versioning (install separately)

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/selvaneyas/gitgenius
```

---

## ✅ 3. 🎨 Make Favicon Background White or Transparent

Use a transparent favicon or convert it to white background:



---

## 🌍 Free Deployment Using GitHub Pages

### 🔧 Step-by-step Setup:

#### 1. ✅ Install MkDocs

```bash
pip install mkdocs
pip install mkdocs-material
pip install mike
```

> ✅ Do NOT use `mkdocs-pwa` — it's not maintained or published on PyPI!

---

#### 2. ✅ Initialize Git & Push to GitHub

```bash
git init
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

#### 3. ✅ Configure Mike for Versioning (Optional)

```bash
mike deploy --update-aliases v1 latest
mike set-default v1
```

---

#### 4. ✅ Build & Deploy to `gh-pages`

```bash
mkdocs gh-deploy
mkdocs gh-deploy --ignore-version

```

> This creates the `gh-pages` branch and uploads static files.

---

## 🔁 Enable GitHub Pages

* Go to GitHub → Settings → Pages
* Select Branch: `gh-pages`
* Folder: `/ (root)`
* Your site will be live at:

  ```
  https://YOUR_USERNAME.github.io/YOUR_REPO
  ```

---

## 🌐 Add a Custom Domain (Optional)

1. Buy a domain from [Freenom](https://www.freenom.com/) or [Namecheap](https://www.namecheap.com/).
2. Create a file named `CNAME` inside `/docs` with your domain:

   ```
   www.gitgenius.tech
   ```
3. Update DNS settings of your domain to point to:

```
CNAME -> YOUR_USERNAME.github.io
```

# Install mike if not already
pip install mike

# Deploy v0.1.3 as the latest & default
mike deploy 0.1.3 latest
mike set-default latest

# Push to GitHub Pages
git push origin gh-pages

---

## 👨‍💻 Maintainer

**Author**: Selva Neyas U
**Email**: [selvaneyas@gmail.com](mailto:selvaneyas@gmail.com)
**License**: MIT
**PyPI**: [https://pypi.org/project/gitgenius/](https://pypi.org/project/gitgenius/)



---

