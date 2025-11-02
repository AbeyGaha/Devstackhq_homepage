import streamlit as st
from utils import config
from utils.auth import require_login, login_ui, logout
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="DevStackHQ", layout="centered", initial_sidebar_state="expanded")

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

BASE_CSS = """<style>
:root{--primary:#667eea;--secondary:#764ba2;--accent:#FF4B4B;--light:#f8f9fa;--dark:#343a40;}
body{background-color:#f5f5f5;color:#333;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;}
.main-header{background:linear-gradient(135deg,var(--primary),var(--secondary));color:white;padding:1.25rem;border-radius:10px;}
.hero{background:linear-gradient(135deg,#FF4B4B,#FF6B6B);padding:3rem;border-radius:12px;color:white;}
.feature-card{background:white;padding:1rem;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.08);}
.product-card{background:white;padding:1.5rem;border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,0.08);}
.cta-button{background:linear-gradient(45deg,var(--primary),var(--secondary));color:white;padding:.6rem 1rem;border-radius:999px;text-decoration:none;}
</style>"""
st.markdown(BASE_CSS, unsafe_allow_html=True)

st.sidebar.title("DevStackHQ")
nav = st.sidebar.radio("Navigate", ["Home", "Products", "Contact"], index=0)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_ui()
else:
    st.sidebar.markdown("**Logged in** ✅")
    if st.sidebar.button("Log out"):
        logout()

# --------------- page sections ---------------
def render_header():
    col1, col2 = st.columns([1,4])
    with col1:
        logo = ASSETS / "logo.png"
        if logo.exists():
            st.image(str(logo), width=80)
        else:
            st.markdown("## 🚀")
    with col2:
        st.markdown('<div class="main-header"><h1>DevStackHQ</h1><p>Developer Productivity & Deployment Solutions</p></div>', unsafe_allow_html=True)

def render_home():
    render_header()
    st.markdown('<div class="hero"><h1>Welcome to DevStackHQ</h1><h3>Your Launchpad for Developer Productivity & Deployment</h3><p>We build cutting-edge tools for CI/CD, DevOps, and deployment so developers can <strong>focus on building</strong>.</p></div>', unsafe_allow_html=True)
    st.header("🎯 Why Choose DevStackHQ?")
    cols = st.columns(3)
    features = [("🚀 Fast Deployment","Deploy your apps in minutes"),("🔧 Developer First","Tools built for devs"),("☁️ Cloud Native","Optimized for cloud infra")]
    for c,f in zip(cols,features):
        with c:
            st.markdown(f'<div class="feature-card"><h4>{f[0]}</h4><p>{f[1]}</p></div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="cta-button">🚀 <strong>Sign Up Now</strong></div>', unsafe_allow_html=True)
    st.write("© 2025 DevStackHQ. All rights reserved.")

def render_products():
    render_header()
    st.markdown("## 🚀 DevStackHQ Products")
    st.write("Discover powerful AI tools and developer solutions that boost productivity.")
    st.markdown("---")
    def product_card(title, subtitle, url=None):
        st.markdown(f"<div class='product-card'><h3>{title}</h3><p>{subtitle}</p>", unsafe_allow_html=True)
        if url:
            st.markdown(f"<a href='{url}' target='_blank' class='cta-button'>Open</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    product_card("SearchPulse Chatbot","AI conversational assistant","https://advisiongenre.devstackhq.com/chat/")
    product_card("AdVisionGenre","AI content creation","https://advisiongenre.devstackhq.com")
    product_card("Reposcope","Cloud repo intelligence","https://reposcope.streamlit.app")

def render_contact():
    render_header()
    st.header("Contact Us")
    st.write("support@devstackhq.com")

# --- page routing ---
if nav == "Products" and not st.session_state.logged_in:
    st.warning("Please log in to view Products.")
else:
    {"Home":render_home,"Products":render_products,"Contact":render_contact}[nav]()
