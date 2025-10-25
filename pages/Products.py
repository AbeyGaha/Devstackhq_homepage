import os
import streamlit as st
from components.navbar import show_navbar
from components.footer import show_footer

# ---- Page Setup ----
st.set_page_config(page_title="DevStackHQ Products", layout="wide")

# ---- Navbar ----
show_navbar()

st.title("🧩 Our Products")
st.markdown("Explore all developer tools and SaaS products from **DevStackHQ Labs**.")
st.markdown("---")

# ---- Detect Environment ----
REPO_BASE = os.getenv("REPOSCOPE_BASE", "https://reposcope.streamlit.app")
CUSTOM_DOMAIN = "https://reposcope.devstackhq.com"
USE_CUSTOM = os.getenv("USE_CUSTOM_DOMAIN", "0") == "1"
reposcope_url = CUSTOM_DOMAIN if USE_CUSTOM else REPO_BASE

# ----------------------------
# Product 1: Reposcope
# ----------------------------
st.subheader("🧠 Reposcope – Cloud Repository Intelligence")
st.write("""
**Reposcope** is a Streamlit-based AI platform for managing, analyzing, and automating repository workflows.
It helps developers deploy, backtest, and visualize cloud-based models directly.
""")

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("**Status:** ✅ Live")
    st.markdown("**Stack:** Streamlit • Python • Cloud Deployment")
    st.markdown("**Hosted On:** Streamlit Cloud")
    st.markdown("**Use Case:** Data & AI model management")

with col2:
    st.markdown(f"""
    <a href="{reposcope_url}" target="_blank">
        <button style="padding:10px 20px; font-size:16px;">🚀 Launch Reposcope</button>
    </a>
    """, unsafe_allow_html=True)

st.markdown("---")

# ----------------------------
# Product 2: AdVisionGenre & SearchPulse
# ----------------------------
st.subheader("🎯 AdVisionGenre + SearchPulse – AI Content & Chatbot Suite")
st.write("""
**AdVisionGenre** automates content creation, ad design, and blog publishing using AI.  
**SearchPulse** is an AI-powered chatbot that helps you explore blogs, keywords, and insights interactively.  
Both products run securely on our Linode Cloud infrastructure.
""")

col3, col4 = st.columns([1, 1])
with col3:
    st.markdown("**AdVisionGenre:** 🧱 Live on Linode")
    st.markdown("**Stack:** FastAPI • Google Cloud API • Blogger Automation")
    st.markdown("**Use Case:** Automated content creation and publishing")
    st.markdown(f"""
    <a href="https://advisiongenre.devstackhq.com" target="_blank">
        <button style="padding:10px 20px; font-size:16px;">📰 Read Our Blogs</button>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("**SearchPulse Chatbot:** 💬 Live on Linode")
    st.markdown("**Stack:** FastAPI • LLM Integration • Gradio UI")
    st.markdown("**Use Case:** Conversational insights and search assistant")
    st.markdown(f"""
    <a href="https://advisiongenre.devstackhq.com/chat/" target="_blank">
        <button style="padding:10px 20px; font-size:16px;">🤖 Launch SearchPulse Chatbot</button>
    </a>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
🌐 *All products are part of the DevStackHQ ecosystem — empowering developers with AI-driven tools.*  
""")

# ---- Footer ----
show_footer()
