import os
import streamlit as st
from PIL import Image
from components.navbar import show_navbar
from components.footer import show_footer

st.set_page_config(page_title="DevStackHQ", layout="wide")

# ---- Safe image loader ----
def load_image(filename):
    """Safely load an image from the assets folder."""
    path = os.path.join("assets", filename)
    if os.path.exists(path):
        return Image.open(path)
    else:
        st.warning(f"⚠️ Missing image: {path}")
        return None

# ---- Navbar ----
show_navbar()

# ---- Top section with Logo (left) and optional spacing ----
logo = load_image("logo.png")
col1, col2 = st.columns([1, 6])  # logo left, rest empty for spacing
with col1:
    if logo:
        st.image(logo, width=180)
    else:
        st.markdown("<h2>DevStackHQ</h2>", unsafe_allow_html=True)
with col2:
    pass  # empty column for spacing

st.markdown("---")

# ---- Banner Section (centered) ----
banner = load_image("banner.png")
if banner:
    st.image(banner, use_column_width=True)

# ---- Hero Text ----
st.markdown("""
<h1 style='text-align: center; color: #2C3E50;'>🚀 Welcome to DevStackHQ</h1>
<h3 style='text-align: center; color: #34495E;'>Your Launchpad for Developer Productivity & Deployment</h3>
""", unsafe_allow_html=True)

# ---- Description ----
st.markdown("""
<div style='text-align: center; font-size:18px; padding: 1rem 2rem;'>
We are building cutting-edge tools for CI/CD, DevOps, and deployment so that developers can 
<strong>focus on building</strong> rather than managing infrastructure.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---- Contact Section ----
st.markdown("""
### 📬 Contact Us
Reach us anytime at [contact@devstackhq.com](mailto:contact@devstackhq.com)
""")

# ---- Footer ----
show_footer()
