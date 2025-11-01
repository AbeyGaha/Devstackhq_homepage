import os
import streamlit as st
from components.navbar import show_navbar
from components.footer import show_footer

# ---- Page Setup ----
st.set_page_config(
    page_title="DevStackHQ Products", 
    layout="wide",
    page_icon="🧩"
)

# ---- Navbar ----
show_navbar()

# ---- Custom CSS for Better Styling ----
st.markdown("""
<style>
    .product-card {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-bottom: 1rem;
    }
    .feature-list {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ff6b35;
    }
    .streamlit-button {
        width: 100%;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

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
    # Use Streamlit's markdown link (works better in Streamlit Cloud)
    st.markdown(f"[🚀 Launch Reposcope]({reposcope_url})")

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

# Main Chatbot Button - Using Streamlit's native components
st.markdown("### 🤖 Try Our Free Demo Chatbot")
st.markdown(f"[🚀 Try Free Demo Chatbot](https://advisiongenre.devstackhq.com/chat/)")

# Features in a nice card
with st.container():
    st.markdown("""
    <div class="feature-list">
    <h4>🎁 Free Demo Features:</h4>
    <ul>
    <li>4 messages conversation memory</li>
    <li>File upload (PDF, images, text) - max 2048 KB</li>
    <li>Basic creative tools (Posters, Videos, Images)</li>
    <li>Download created files</li>
    <li>Full bot code access for developers</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Product details in columns
col3, col4 = st.columns([1, 1])

with col3:
    st.markdown("### 📰 AdVisionGenre")
    st.markdown("**Status:** 🧱 Live on Linode")
    st.markdown("**Stack:** FastAPI • Google Cloud API • Blogger Automation")
    st.markdown("**Use Case:** Automated content creation and publishing")
    
    # Blog button - Simple markdown link
    st.markdown("[📰 Read Our Blogs](https://advisiongenre.devstackhq.com)")

with col4:
    st.markdown("### 💬 SearchPulse Chatbot") 
    st.markdown("**Status:** 💬 Live on Linode")
    st.markdown("**Stack:** FastAPI • LLM Integration • Gradio UI")
    st.markdown("**Use Case:** Conversational insights and search assistant")
    
    # Chatbot button - Simple markdown link
    st.markdown("[🤖 Launch SearchPulse Chatbot](https://advisiongenre.devstackhq.com/chat/)")

# Alternative: Using Streamlit buttons with JavaScript (more reliable)
st.markdown("---")
st.markdown("### 🚀 Quick Access Links")

# Create columns for buttons
btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    if st.button("🧠 Launch Reposcope", use_container_width=True):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={reposcope_url}">', unsafe_allow_html=True)

with btn_col2:
    if st.button("🤖 Try Chatbot Demo", use_container_width=True):
        st.markdown('<meta http-equiv="refresh" content="0; url=https://advisiongenre.devstackhq.com/chat/">', unsafe_allow_html=True)

with btn_col3:
    if st.button("📰 Read Our Blogs", use_container_width=True):
        st.markdown('<meta http-equiv="refresh" content="0; url=https://advisiongenre.devstackhq.com">', unsafe_allow_html=True)

# Additional call-to-action
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px;">
    <h3>🚀 Ready to Get Started?</h3>
    <p>Join hundreds of developers using our AI-powered tools to boost their productivity!</p>
    <p><a href="https://advisiongenre.devstackhq.com/chat/" style="color: white; text-decoration: underline; font-weight: bold;">Start Free Trial Now</a></p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p><strong>🌐 All products are part of the DevStackHQ ecosystem — empowering developers with AI-driven tools.</strong></p>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
show_footer()
