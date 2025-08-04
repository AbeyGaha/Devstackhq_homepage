# Home.py

import streamlit as st
from components.navbar import show_navbar
from components.footer import show_footer
from PIL import Image

st.set_page_config(page_title="DevStackHQ", layout="wide")

# Navbar
show_navbar()

# Hero Section
banner = Image.open("assets/banner.jpg")
st.image(banner, use_column_width=True)

st.markdown("""
<h1 style='text-align: center; color: #2C3E50;'>🚀 Welcome to DevStackHQ</h1>
<h3 style='text-align: center; color: #34495E;'>Your Launchpad for Developer Productivity & Deployment</h3>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size:18px; padding: 1rem 2rem;'>
We are building cutting-edge tools for CI/CD, DevOps, and deployment so that developers can <strong>focus on building</strong> rather than managing infrastructure.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Contact Section
st.markdown("""
### 📬 Contact Us
Reach us anytime at [contact@devstackhq.com](mailto:contact@devstackhq.com)
""")

# Footer
show_footer()


