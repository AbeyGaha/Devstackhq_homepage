# app.py
import streamlit as st
from utils import config
from utils.auth import require_login, login_ui, logout
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="DevStackHQ", layout="centered", initial_sidebar_state="expanded")

# --- helpful paths ---
ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

# Inline CSS adapted from your HTML (kept minimal for Streamlit)
BASE_CSS = """
<style>
:root{
  --primary: #667eea;
  --secondary: #764ba2;
  --accent: #FF4B4B;
  --light: #f8f9fa;
  --dark: #343a40;
}
body {background-color: #f5f5f5; color: #333; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
.main-header {background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; padding: 1.25rem; border-radius: 10px;}
.hero {background: linear-gradient(135deg, #FF4B4B, #FF6B6B); padding: 3rem; border-radius: 12px; color: white;}
.feature-card {background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);}
.product-card {background: white; padding: 1.5rem; border-radius: 14px; box-shadow: 0 10px 30px rgba(0,0,0,0.08);}
.cta-button {background: linear-gradient(45deg,var(--primary),var(--secondary)); color: white; padding: .6rem 1rem; border-radius: 999px; text-decoration:none;}
</style>
"""

st.markdown(BASE_CSS, unsafe_allow_html=True)

# --- Sidebar: navigation + auth ---
st.sidebar.title("DevStackHQ")
nav = st.sidebar.radio("Navigate", ["Home", "Products", "Contact"], index=0)

# Authentication UI (simple)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_ui()
else:
    st.sidebar.markdown("**Logged in** ✅")
    if st.sidebar.button("Log out"):
        logout()

# --- page renderers ---
def render_header():
    col1, col2 = st.columns([1,4])
    with col1:
        logo_path = ASSETS / "logo.png"
        if logo_path.exists():
            st.image(str(logo_path), width=80)
        else:
            st.markdown("## 🚀")
    with col2:
        st.markdown('<div class="main-header"><h1 style="margin:0">DevStackHQ</h1><p style="margin:0">Developer Productivity & Deployment Solutions</p></div>', unsafe_allow_html=True)

def render_home():
    render_header()
    st.markdown('<div class="hero"><h1>Welcome to DevStackHQ</h1><h3>Your Launchpad for Developer Productivity & Deployment</h3><p>We build cutting-edge tools for CI/CD, DevOps, and deployment so developers can <strong>focus on building</strong>.</p></div>', unsafe_allow_html=True)
    st.write("")
    st.header("🎯 Why Choose DevStackHQ?")
    cols = st.columns(3)
    features = [
        ("🚀 Fast Deployment", "Deploy your applications in minutes with automated CI/CD pipelines"),
        ("🔧 Developer First", "Tools designed by developers for developers"),
        ("☁️ Cloud Native", "Built for modern cloud infrastructure")
    ]
    for c, f in zip(cols, features):
        with c:
            st.markdown(f'<div class="feature-card"><h4>{f[0]}</h4><p>{f[1]}</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.header("📋 Company Policies & Information")
    st.write("Shipping Policy · Terms & Conditions · Refunds · Privacy Policy")
    st.markdown("---")
    st.markdown('<div class="cta-button"> 🚀 <strong>Sign Up Now</strong> </div>', unsafe_allow_html=True)
    st.write("")
    st.write("© 2025 DevStackHQ. All rights reserved.")
    
def render_products():
    render_header()
    st.markdown("<h2 style='margin-top:1rem'>🚀 DevStackHQ Products</h2>", unsafe_allow_html=True)
    st.write("Discover powerful AI tools and developer solutions that boost productivity.")
    st.markdown("---")
    # Product cards
    def product_card(title, subtitle, features, url=None, tags=None, live_text="LIVE"):
        st.markdown(f'<div class="product-card"><h3>{title}</h3><p><strong>{subtitle}</strong></p>', unsafe_allow_html=True)
        if tags:
            tags_str = " ".join([f"<span style='padding:.2rem .6rem; border-radius:12px; background:#eee; margin-right:.3rem'>{t}</span>" for t in tags])
            st.markdown(tags_str, unsafe_allow_html=True)
        if url:
            st.markdown(f'<p style="margin-top:.5rem"><a href="{url}" target="_blank" class="cta-button">Open</a> <span style="margin-left:1rem"> <strong>{live_text}</strong></span></p>', unsafe_allow_html=True)
        st.write("")
        st.markdown("<ul>" + "".join([f"<li>{it}</li>" for it in features]) + "</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")

    product_card(
        "SearchPulse Chatbot",
        "AI-Powered Conversational Assistant with Creative Tools",
        ["4 messages conversation memory","File upload (PDF, images, text)","Creative tools integration"],
        url="https://advisiongenre.devstackhq.com/chat/",
        tags=["FastAPI","Groq LPU","Gradio","Python"],
        live_text="LIVE ON LINODE"
    )
    product_card(
        "AdVisionGenre",
        "AI Content Creation & Automated Publishing",
        ["Auto blog generation","WordPress auto-publish","SEO tools"],
        url="https://advisiongenre.devstackhq.com",
        tags=["WordPress API","FastAPI","Groq LLM"],
        live_text="LIVE ON LINODE"
    )
    product_card(
        "Reposcope",
        "Cloud Repository Intelligence Platform",
        ["Repository analysis","Cloud deployment automation","Streamlit dashboards"],
        url="https://reposcope.streamlit.app",
        tags=["Streamlit","Python","Data Viz"],
        live_text="LIVE ON STREAMLIT"
    )

    st.markdown("---")
    st.header("Quick Access Links")
    st.write("Open product demos directly:")
    st.write("- SearchPulse Chatbot — https://advisiongenre.devstackhq.com/chat/")
    st.write("- AdVisionGenre — https://advisiongenre.devstackhq.com")
    st.write("- Reposcope — https://reposcope.streamlit.app")

def render_contact():
    render_header()
    st.header("Contact Us")
    st.write("support@devstackhq.com")
    st.write("Need help? Send us an email with your repo and what you'd like deployed.")

# --- protect product page (optional) ---
if nav == "Products" and not st.session_state.logged_in:
    st.warning("Please log in to view Products.")
else:
    if nav == "Home":
        render_home()
    elif nav == "Products":
        render_products()
    elif nav == "Contact":
        render_contact()


