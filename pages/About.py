# pages/About.py
import streamlit as st
from pathlib import Path

ROOT = Path(__file__).parent.parent
ASSETS = ROOT / "assets"

st.set_page_config(page_title="About - DevStackHQ", layout="centered")

CSS = """
<style>
:root{--primary:#667eea;--secondary:#764ba2;--dark:#343a40;--light:#f8f9fa}
body{font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;background:var(--light); color:#222}
.header {background: linear-gradient(135deg,var(--primary),var(--secondary)); color:white; padding:2.2rem; border-radius:12px; text-align:center}
.card {background:white;padding:1rem;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-top:1rem}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="header"><h1>ℹ️ About DevStackHQ</h1><p>Developer Productivity & Deployment Solutions</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card"><h3>Our Mission</h3><p>We build cutting-edge tools for CI/CD, DevOps, and deployment so developers can focus on building instead of managing infrastructure.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card"><h3>Who we serve</h3><ul><li>Developers & DevOps engineers</li><li>Startups looking for fast deployment</li><li>Enterprises wanting reproducible pipelines</li></ul></div>', unsafe_allow_html=True)

st.markdown('<div class="card"><h3>Contact</h3><p>Email: support@devstackhq.com</p><p>For sales: sales@devstackhq.com</p></div>', unsafe_allow_html=True)

st.markdown("<footer style='text-align:center;margin-top:1.5rem;color:#555'>&copy; 2025 DevStackHQ Labs</footer>", unsafe_allow_html=True)
