import os
import streamlit as st
from PIL import Image
from components.navbar import show_navbar
from components.footer import show_footer

# ---- Page Config ----
st.set_page_config(page_title="DevStackHQ", layout="wide", page_icon="💻")

# ---- Detect environment (Render or local or proxy) ----
REPO_BASE = os.getenv("REPOSCOPE_BASE", "https://reposcope.streamlit.app")
CUSTOM_DOMAIN = "https://reposcope.devstackhq.com"
current_base = CUSTOM_DOMAIN if "devstackhq.com" in st.request.url else REPO_BASE

# ---- Safe Image Loader ----
def load_image(filename, max_width=None):
    path = os.path.join("assets", filename)
    if not os.path.exists(path):
        st.warning(f"⚠️ Missing image: {path}")
        return None
    img = Image.open(path)
    if max_width and img.width > max_width:
        ratio = max_width / img.width
        img = img.resize((max_width, int(img.height * ratio)))
    return img

# ---- Navbar ----
show_navbar()

# ---- Logo and Icons ----
logo = load_image("logo.png", max_width=180)
col1, col2 = st.columns([1, 6])

with col1:
    if logo:
        st.image(logo, width=180)
    else:
        st.markdown("<h2>DevStackHQ</h2>", unsafe_allow_html=True)

with col2:
    # Icons with dynamic base URLs
    st.markdown(f"""
    <div style='text-align:right; padding-top:20px;'>
        <a href='{CUSTOM_DOMAIN}' target='_self'>
            <img src='https://img.icons8.com/material-rounded/24/000000/home.png' style='margin-right:10px;'/>
        </a>
        <a href='https://devstackhq.com' target='_blank'>
            <img src='https://img.icons8.com/material-rounded/24/000000/info.png' style='margin-right:10px;'/>
        </a>
        <a href='mailto:contact@devstackhq.com'>
            <img src='https://img.icons8.com/material-rounded/24/000000/email.png'/>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---- Banner ----
banner = load_image("banner.png", max_width=1200)
if banner:
    st.image(banner, use_container_width=True)

# ---- Hero Section ----
st.markdown("""
<h1 style='text-align:center; color:#2C3E50;'>🚀 Welcome to DevStackHQ</h1>
<h3 style='text-align:center; color:#34495E;'>Your Launchpad for Developer Productivity & Deployment</h3>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px; padding:1rem 2rem;'>
We build cutting-edge tools for CI/CD, DevOps, and deployment so developers can
<strong>focus on building</strong> instead of managing infrastructure.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---- Contact ----
st.markdown("""
### 📬 Contact Us
Reach us anytime at [contact@devstackhq.com](mailto:contact@devstackhq.com)
""")

# ---- Footer ----
show_footer()
