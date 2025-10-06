# pages/Products.py

import streamlit as st
import webbrowser
from components.navbar import show_navbar
from components.footer import show_footer

# Page Setup
st.set_page_config(page_title="DevStackHQ Products", layout="wide")

# Navbar
show_navbar()

st.title("🧩 Our Products")
st.markdown("Explore all developer tools and SaaS products from **DevStackHQ Labs**.")

st.markdown("---")

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
    st.markdown("**Hosted On:** advisiongenre cloud VM")
    st.markdown("**Use Case:** Data & AI model management")
with col2:
    if st.button("🚀 Launch Reposcope", key="launch_reposcope"):
        webbrowser.open("https://cloud.advisiongenre.com/reposcope")

st.markdown("---")

# ----------------------------
# Product 2: AdVisionGenre
# ----------------------------
st.subheader("🎯 AdVisionGenre – AI Content & Blogger Automation")
st.write("""
**AdVisionGenre** automates content creation, design, and blog publishing workflows.
It connects to **Google Cloud API** to generate and post blogs automatically using a secure `token.json` authentication flow.
""")

col3, col4 = st.columns([1, 1])
with col3:
    st.markdown("**Status:** 🧱 In Development (Linode VM)**")
    st.markdown("**Stack:** FastAPI • Streamlit • Google API Integration")
    st.markdown("**Use Case:** Automated blogging, ad design, and content publishing")
with col4:
    if st.button("🧩 Visit AdVisionGenre (Coming Soon)", key="visit_advision"):
        st.info("AdVisionGenre is currently being set up on Linode VM.")
        # Later this will point to your Linode app
        # webbrowser.open("https://advisiongenre.com")

st.markdown("---")

st.markdown("""
🌐 *All products are part of the DevStackHQ ecosystem — building secure, modular tools for developers worldwide.*
""")

# Footer
show_footer()
