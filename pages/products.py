import streamlit as st
import webbrowser
from components.navbar import show_navbar
from components.footer import show_footer

# Page setup
st.set_page_config(page_title="DevStackHQ Products", layout="wide")

# Navbar
show_navbar()

# Title
st.title("🧩 Our Products")
st.markdown("Explore all developer tools and AI-powered SaaS platforms by **DevStackHQ Labs**.")
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
    st.markdown("**Hosted On:** Streamlit Cloud")
    st.markdown("**Use Case:** Data & AI model management")
with col2:
    if st.button("🚀 Launch Reposcope", key="launch_reposcope"):
        webbrowser.open("https://devstackhq.streamlit.app/reposcope")

st.markdown("---")

# ----------------------------
# Product 2: AdVisionGenre Suite (with SearchPulse Chatbot)
# ----------------------------
st.subheader("🎯 AdVisionGenre Suite – AI Blogging & Chat Automation")
st.write("""
**AdVisionGenre Suite** combines advanced AI-driven blogging automation, keyword discovery, and ad creative generation tools,  
with an integrated **SearchPulse Chatbot** for smart content interaction and search assistance.
""")

col3, col4 = st.columns([1, 1])
with col3:
    st.markdown("**Status:** 🟢 Live (Hosted on Linode Cloud)**")
    st.markdown("**Stack:** FastAPI • Streamlit • Google API • LLM Engine")
    st.markdown("**Use Case:** Blogging automation, Keyword Finder, Chat assistant, Creative ad design")
    st.markdown("**Hosted On:** Linode Cloud VM")
with col4:
    st.markdown("### 🌐 Access Tools")
    if st.button("📰 Read Our Blogs", key="read_blogs"):
        webbrowser.open("http://170.187.237.185/wp-json/wp/v2")
    if st.button("🤖 Launch SearchPulse Chatbot", key="launch_searchpulse"):
        webbrowser.open("http://170.187.237.185/chat")

st.markdown("---")

# Footer
show_footer()
