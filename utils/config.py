# utils/config.py
import os
from pathlib import Path

# --- Base directories ---
ROOT_DIR = Path(__file__).resolve().parent.parent  # project root (where app.py lives)
ASSETS_DIR = ROOT_DIR / "assets"
UTILS_DIR = ROOT_DIR / "utils"

# --- Streamlit global config ---
# Safe defaults for deployment
os.environ["STREAMLIT_SERVER_PORT"] = os.environ.get("PORT", "10000")
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

# Disable CORS + XSRF for custom domains (Render + Namecheap fix)
os.environ["STREAMLIT_SERVER_ENABLE_CORS"] = "false"
os.environ["STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION"] = "false"

# --- Helper function ---
def get_path(name: str):
    """Return absolute path of file/folder inside project."""
    p = ROOT_DIR / name
    if not p.exists():
        print(f"[config] Warning: {p} not found.")
    return p
