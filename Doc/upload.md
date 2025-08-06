# Clean old builds
python setup.py clean --all
rm -rf dist/ build/ *.egg-info  # Or use del /s dist if on Windows CMD

# Build new distribution
python setup.py sdist bdist_wheel
