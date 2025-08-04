# pages/Product.py

import streamlit as st
from components.navbar import show_navbar
from components.footer import show_footer
import base64

show_navbar()

st.title("🛠️ DevStackHQ Products")
st.markdown("Explore our live tools. Plug-n-play and extend any of them easily.")

# REPOSCOPE Product Display
st.subheader("📦 Reposcope - Code Intelligence & Repository Scanner")
st.markdown("""
Reposcope is a developer tool that scans your GitHub repositories for:
- 🔍 License issues
- ⚠️ Vulnerabilities
- 📦 Package/Dependency conflicts
- 📊 Dev activity summaries

[👉 Visit Reposcope GitHub](https://github.com/AbeyGaha/Reposcope)
""")

if st.button("Open Reposcope"):
    st.success("Reposcope WebApp launching soon... (can be linked with Streamlit/GitHub deployment)")

show_footer()
