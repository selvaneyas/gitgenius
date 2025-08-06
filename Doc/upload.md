# Clean old builds
python setup.py clean --all
rm -rf dist/ build/ *.egg-info  # Or use del /s dist if on Windows CMD

> rmdir /s /q dist
> rmdir /s /q build
> del /s /q *.egg-info

# Build new distribution
python setup.py sdist bdist_wheel


# use Publish.yml

git tag v0.1.2
git push origin v0.1.2



---

## 🔍 1. ✅ List All Git Tags

```bash
git tag
```

This shows a list of all local tags, like:

```
v0.1.0
v0.1.1
v0.1.2
```

---

## 🗑️ 2. ✅ Delete a Tag

### 🔹 Delete a **local** tag:

```bash
git tag -d v0.1.1
```

### 🔹 Delete a **remote** tag (e.g., on GitHub):

```bash
git push origin --delete v0.1.1
```

> You **must do both** if the tag is already pushed.

---

## 🚀 3. 🔁 Create and Push a New Tag (if you updated version)

### Create a tag:

```bash
git tag v0.1.3
```

### Push the tag to GitHub:

```bash
git push origin v0.1.3
```

---

## ❌ Should You Delete Previous Tags?

**Depends:**

* ✅ If the previous version is broken or wrongly tagged → **Yes**, delete it.
* 🚫 If the version was already published to **PyPI**, you **cannot re-upload the same version**, even if you delete the tag. PyPI doesn’t allow replacing the same version.

> If you've already uploaded version `0.1.2` to PyPI, and it has issues, you must:
>
> * Increment to `0.1.3`
> * Update your `setup.py` or `pyproject.toml`
> * Create a new tag: `git tag v0.1.3`
> * Push and upload again

---

## ✅ Quick Recap

| Action            | Command                           |
| ----------------- | --------------------------------- |
| List all tags     | `git tag`                         |
| Delete local tag  | `git tag -d v0.1.1`               |
| Delete remote tag | `git push origin --delete v0.1.1` |
| Create new tag    | `git tag v0.1.3`                  |
| Push new tag      | `git push origin v0.1.3`          |


---

## ✅ 1. 🔍 SEO – Add `site_description` & `site_author`

Add this to your `mkdocs.yml`:

```yaml
site_name: GitGenius
site_description: "GitGenius - A smart CLI tool that explains Git errors in plain English."
site_author: "Selva Neyas"
```

---

## ✅ 2. 📱 PWA (Installable Web App)

Add the [PWA plugin](https://github.com/LukasMasuch/mkdocs-pwa-plugin):

### ➤ Step 1: Install it

```bash
pip install mkdocs-pwa-plugin
```

### ➤ Step 2: Add to `mkdocs.yml`

```yaml
plugins:
  - search
  - pwa

extra:
  manifest:
    name: GitGenius
    short_name: GitGenius
    start_url: /
    display: standalone
    background_color: "#ffffff"
    theme_color: "#1a73e8"
    icons:
      - src: assets/favicon-512.png
        sizes: 512x512
        type: image/png
```

> 🔄 Use your transparent PNG for `favicon-512.png`

---

## ✅ 3. 🧪 Versioning with Mike

Mike is a versioning tool for MkDocs.

### ➤ Step 1: Install Mike

```bash
pip install mike
```

### ➤ Step 2: Update `mkdocs.yml`

```yaml
plugins:
  - mike
  - search
  - pwa
```

### ➤ Step 3: Deploy version

```bash
mike deploy 1.0 --push
mike set-default 1.0 --push
```

---

## ✅ 4. 📷 Social Banner (`assets/social-banner.png`)

Create a **1200x630 PNG** image, save as:

```bash
assets/social-banner.png
```

Add to your `mkdocs.yml`:

```yaml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/selvaneyas/gitgenius
      name: GitHub
  social_banner: assets/social-banner.png
```

---

## ✅ 5. 🌍 Custom Domain with Free Hosting (GitHub Pages)

### ➤ Step 1: Use GitHub Pages (Free & Global)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.10
      - run: pip install mkdocs-material mike mkdocs-pwa-plugin
      - run: mike deploy latest --push
      - run: mike set-default latest --push
```

### ➤ Step 2: Setup GitHub Pages

* Go to your repo → Settings → Pages
* Source: `gh-pages` branch → `/ (root)`
* Save

### ➤ Step 3: Add `CNAME` for custom domain

In root folder, create `CNAME` file:

```text
yourdomain.com
```

Make sure DNS points to GitHub using:

```
Type: CNAME
Host: www
Value: yourusername.github.io
```

---

## ✅ 6. Final `mkdocs.yml` Footer & Navbar Example

```yaml
site_name: GitGenius
site_description: "Explain Git errors in plain English"
site_author: "Selva Neyas"

theme:
  name: material
  logo: assets/favicon.ico
  favicon: assets/favicon.ico
  icon:
    repo: fontawesome/brands/github
  features:
    - navigation.tabs
    - navigation.indexes
  palette:
    primary: blue
    accent: blue
  font:
    text: Roboto
    code: Roboto Mono

nav:
  - Home: index.md
  - Installation: install.md
  - Usage: usage.md
  - Features: features.md
  - FAQ: faq.md
  - Changelog: changelog.md

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/selvaneyas/gitgenius
      name: GitHub
  social_banner: assets/social-banner.png

plugins:
  - search
  - pwa
  - mike

extra_footer:
  copyright:
    text: 'Made with ❤️ using MkDocs Material by Selva Neyas'
```

---

