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
    .feature-list {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ff6b35;
        margin: 1rem 0;
    }
    .product-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧩 Our Products")
st.markdown("Explore all developer tools and SaaS products from **DevStackHQ Labs**.")
st.markdown("---")

# ----------------------------
# Product 1: Reposcope
# ----------------------------
st.subheader("🧠 Reposcope – Cloud Repository Intelligence")

with st.container():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        **Reposcope** is a Streamlit-based AI platform for managing, analyzing, and automating repository workflows.
        It helps developers deploy, backtest, and visualize cloud-based models directly.
        """)
        
        st.markdown("**Status:** ✅ Live")
        st.markdown("**Stack:** Streamlit • Python • Cloud Deployment")
        st.markdown("**Hosted On:** Streamlit Cloud")
        st.markdown("**Use Case:** Data & AI model management")
    
    with col2:
        st.markdown("### 🚀 Launch")
        repo_url = "https://reposcope.streamlit.app"
        st.markdown(f"[Open Reposcope]({repo_url})")

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

# Main Chatbot Section
st.markdown("### 🤖 SearchPulse Chatbot Demo")

chatbot_url = "https://advisiongenre.devstackhq.com/chat/"
blog_url = "https://advisiongenre.devstackhq.com"

# Links in columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    **Live Chatbot URL:**  
    [{chatbot_url}]({chatbot_url})
    """)
    
    # Copy to clipboard functionality
    if st.button("📋 Copy Chatbot URL", key="copy_chatbot"):
        st.code(chatbot_url, language="text")
        st.success("URL copied to clipboard!")

with col2:
    st.markdown(f"""
    **Blog Platform URL:**  
    [{blog_url}]({blog_url})
    """)
    
    if st.button("📋 Copy Blog URL", key="copy_blog"):
        st.code(blog_url, language="text")
        st.success("URL copied to clipboard!")

# Features Card
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

# Product Details in Cards
col3, col4 = st.columns(2)

with col3:
    with st.container():
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 📰 AdVisionGenre")
        st.markdown("**Status:** 🧱 Live on Linode")
        st.markdown("**Stack:** FastAPI • Google Cloud API • Blogger Automation")
        st.markdown("**Use Case:** Automated content creation and publishing")
        st.markdown(f"**URL:** [{blog_url}]({blog_url})")
        st.markdown('</div>', unsafe_allow_html=True)

with col4:
    with st.container():
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 💬 SearchPulse Chatbot")
        st.markdown("**Status:** 💬 Live on Linode")
        st.markdown("**Stack:** FastAPI • LLM Integration • Gradio UI")
        st.markdown("**Use Case:** Conversational insights and search assistant")
        st.markdown(f"**URL:** [{chatbot_url}]({chatbot_url})")
        st.markdown('</div>', unsafe_allow_html=True)

# Direct Access Section
st.markdown("---")
st.markdown("### 🚀 Direct Access")

access_col1, access_col2, access_col3 = st.columns(3)

with access_col1:
    st.markdown("**🌐 Reposcope**")
    st.markdown(f"[reposcope.streamlit.app]({repo_url})")

with access_col2:
    st.markdown("**🤖 SearchPulse**")
    st.markdown(f"[advisiongenre.devstackhq.com/chat/]({chatbot_url})")

with access_col3:
    st.markdown("**📰 AdVisionGenre**")
    st.markdown(f"[advisiongenre.devstackhq.com]({blog_url})")

# Manual URL Input for Users
st.markdown("---")
st.markdown("### 🔗 Can't Click Links?")

st.info("""
**If links don't work from Streamlit Cloud, manually copy and paste these URLs in your browser:**

1. **SearchPulse Chatbot:** `https://advisiongenre.devstackhq.com/chat/`
2. **AdVisionGenre Blogs:** `https://advisiongenre.devstackhq.com`
3. **Reposcope:** `https://reposcope.streamlit.app`
""")

# Final CTA
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px;">
    <h3>🚀 Ready to Get Started?</h3>
    <p>Join hundreds of developers using our AI-powered tools to boost their productivity!</p>
    <p><strong>Manual URL: https://advisiongenre.devstackhq.com/chat/</strong></p>
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
