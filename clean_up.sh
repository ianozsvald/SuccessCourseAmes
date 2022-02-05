find . -name "__pycache__" -type d -name "__pycache__" -exec rm -rf {} +
find . -name ".pytest_cache" -type d -name ".pytest_cache" -exec rm -rf {} +
find . -name ".ipynb_checkpoints" -type d -name ".ipynb_checkpoints" -exec rm -rf {} +

