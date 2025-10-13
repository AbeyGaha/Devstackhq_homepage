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
    st.markdown("**Hosted On:** Streamlit Cloud")
    st.markdown("**Use Case:** Data & AI model management")
with col2:
    if st.button("🚀 Launch Reposcope", key="launch_reposcope"):
        webbrowser.open("https://reposcope.streamlit.app")

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
    if st.button("📰 Read Our Blogs", key="visit_advision"):
        webbrowser.open("https://advisiongenre.devstackhq.com")

with col4:
    st.markdown("**SearchPulse Chatbot:** 💬 Live on Linode")
    st.markdown("**Stack:** FastAPI • LLM Integration • Gradio UI")
    st.markdown("**Use Case:** Conversational insights and search assistant")
    if st.button("🤖 Launch SearchPulse Chatbot", key="launch_searchpulse"):
        webbrowser.open("https://searchpulse.devstackhq.com")

st.markdown("---")

st.markdown("""
🌐 *All products are part of the DevStackHQ ecosystem — empowering developers with AI-driven tools.*  
""")

# Footer
show_footer()
