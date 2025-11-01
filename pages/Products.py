import os
import streamlit as st
from components.navbar import show_navbar
from components.footer import show_footer
import requests

# ---- Page Setup ----
st.set_page_config(
    page_title="DevStackHQ Products", 
    layout="wide",
    page_icon="🧩"
)

# ---- Navbar ----
show_navbar()

# ---- Custom CSS ----
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .product-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border: 1px solid #e0e0e0;
        transition: transform 0.2s ease;
    }
    .product-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .feature-list {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ff6b35;
        margin: 1rem 0;
    }
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        margin: 0.25rem;
    }
    .status-live { background: #d4edda; color: #155724; }
    .status-beta { background: #fff3cd; color: #856404; }
    .url-box {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        font-family: 'Courier New', monospace;
        margin: 0.5rem 0;
        word-break: break-all;
    }
    .server-status {
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        text-align: center;
        font-weight: bold;
    }
    .status-online { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
    .status-offline { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
</style>
""", unsafe_allow_html=True)

# ---- URLs ----
CHATBOT_URL = "https://advisiongenre.devstackhq.com/chat/"
BLOG_URL = "https://advisiongenre.devstackhq.com"
REPOSCOPE_URL = "https://reposcope.streamlit.app"
SERVER_URL = "http://170.187.237.185:8000"

# ---- Header ----
st.markdown("""
<div class="main-header">
    <h1>🚀 DevStackHQ Products</h1>
    <p>Explore all developer tools and SaaS products from <strong>DevStackHQ Labs</strong></p>
</div>
""", unsafe_allow_html=True)

# ---- Server Status Check ----
st.markdown("### 🔍 Real-time Server Status")

try:
    response = requests.get(f"{SERVER_URL}/health", timeout=10)
    if response.status_code == 200:
        server_data = response.json()
        st.markdown(f"""
        <div class="server-status status-online">
            ✅ SERVER ONLINE | Model: {server_data.get('model', 'llama-3.3-70b-versatile')} | Users: {server_data.get('max_concurrent_users', 100)}
        </div>
        """, unsafe_allow_html=True)
        
        # Show server details in expander
        with st.expander("📊 Server Details"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Status", server_data.get('status', 'healthy').upper())
            with col2:
                st.metric("Model", server_data.get('model', 'llama-3.3-70b-versatile'))
            with col3:
                st.metric("Provider", server_data.get('provider', 'Groq'))
                
    else:
        st.markdown("""
        <div class="server-status status-offline">
            ❌ SERVER OFFLINE | Please check the server
        </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.markdown(f"""
    <div class="server-status status-offline">
        ❌ CANNOT REACH SERVER | Error: {str(e)}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ----------------------------
# Product 1: Reposcope
# ----------------------------
st.subheader("🧠 Reposcope – Cloud Repository Intelligence")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    **Reposcope** is a Streamlit-based AI platform for managing, analyzing, and automating repository workflows.
    It helps developers deploy, backtest, and visualize cloud-based models directly with cloud integration.
    """)
    
    st.markdown("**📊 Key Features:**")
    st.markdown("""
    - Repository analysis and insights
    - Cloud deployment automation  
    - Model backtesting framework
    - Real-time visualization dashboards
    - Multi-cloud support
    """)
    
    st.markdown("**🛠 Tech Stack:**")
    st.markdown("Streamlit • Python • Cloud Deployment • Data Visualization")

with col2:
    st.markdown("### 🚀 Quick Access")
    st.markdown('<div class="url-box">https://reposcope.streamlit.app</div>', unsafe_allow_html=True)
    
    st.markdown("**Status:** <span class='status-badge status-live'>✅ LIVE</span>", unsafe_allow_html=True)
    st.markdown("**Host:** Streamlit Cloud")
    st.markdown("**Use Case:** Data & AI model management")
    
    if st.button("🌐 Open Reposcope", key="repo_btn"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={REPOSCOPE_URL}">', unsafe_allow_html=True)
        st.success("Redirecting to Reposcope...")

st.markdown("---")

# ----------------------------
# Product 2: AdVisionGenre & SearchPulse
# ----------------------------
st.subheader("🎯 AdVisionGenre + SearchPulse – AI Content & Chatbot Suite")

st.write("""
**AdVisionGenre** automates content creation, ad design, and blog publishing using AI.  
**SearchPulse** is an AI-powered chatbot that helps you explore blogs, keywords, and insights interactively.  
Both products run securely on our Linode Cloud infrastructure with Groq LPU acceleration.
""")

# Main URLs Section
st.markdown("### 🌐 Live Access URLs")

url_col1, url_col2 = st.columns(2)

with url_col1:
    st.markdown("#### 🤖 SearchPulse Chatbot")
    st.markdown('<div class="url-box">https://advisiongenre.devstackhq.com/chat/</div>', unsafe_allow_html=True)
    
    st.markdown("**Status:** <span class='status-badge status-live'>✅ LIVE</span>", unsafe_allow_html=True)
    st.markdown("**Host:** Linode Cloud")
    st.markdown("**Tech:** FastAPI • Groq LLM • Gradio UI")
    
    if st.button("💬 Open Chatbot", key="chat_btn", type="primary"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={CHATBOT_URL}">', unsafe_allow_html=True)
        st.success("Opening SearchPulse Chatbot...")

with url_col2:
    st.markdown("#### 📰 AdVisionGenre Blogs")
    st.markdown('<div class="url-box">https://advisiongenre.devstackhq.com</div>', unsafe_allow_html=True)
    
    st.markdown("**Status:** <span class='status-badge status-live'>✅ LIVE</span>", unsafe_allow_html=True)
    st.markdown("**Host:** Linode Cloud") 
    st.markdown("**Tech:** FastAPI • WordPress API • Google Cloud")
    
    if st.button("📖 Open Blogs", key="blog_btn"):
        st.markdown(f'<meta http-equiv="refresh" content="0; url={BLOG_URL}">', unsafe_allow_html=True)
        st.success("Opening AdVisionGenre Blogs...")

# Features Section
st.markdown("### 🎁 Free Demo Features")

with st.container():
    st.markdown("""
    <div class="feature-list">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
        <div>
            <h4>🤖 AI Chatbot</h4>
            <ul>
            <li>4 messages conversation memory</li>
            <li>Powered by Groq LPU inference</li>
            <li>Real-time responses</li>
            <li>Context-aware conversations</li>
            </ul>
        </div>
        <div>
            <h4>🎨 Creative Tools</h4>
            <ul>
            <li>Poster design & generation</li>
            <li>Video advertisement creation</li>
            <li>AI image generation</li>
            <li>Music composition tools</li>
            </ul>
        </div>
        <div>
            <h4>📁 File Management</h4>
            <ul>
            <li>File upload (PDF, images, text)</li>
            <li>Max file size: 2048 KB</li>
            <li>Download created files</li>
            <li>10-minute auto cleanup</li>
            </ul>
        </div>
        <div>
            <h4>🔧 Developer Features</h4>
            <ul>
            <li>Full bot code access</li>
            <li>API documentation</li>
            <li>SEO keyword research</li>
            <li>Location-based trends</li>
            </ul>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# Product Details Cards
st.markdown("### 📋 Product Details")

detail_col1, detail_col2 = st.columns(2)

with detail_col1:
    with st.container():
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("#### 📰 AdVisionGenre")
        st.markdown("**Primary Function:** Automated content creation and publishing")
        
        st.markdown("**Core Features:**")
        st.markdown("""
        - AI-powered blog content generation
        - WordPress auto-publishing
        - SEO optimization tools
        - Social media content creation
        - Multi-platform publishing
        """)
        
        st.markdown("**Technology Stack:**")
        st.markdown("""
        - FastAPI backend
        - Google Cloud APIs
        - WordPress REST API
        - Groq LLM integration
        - Linode cloud hosting
        """)
        st.markdown('</div>', unsafe_allow_html=True)

with detail_col2:
    with st.container():
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("#### 💬 SearchPulse Chatbot")
        st.markdown("**Primary Function:** Conversational AI assistant with creative tools")
        
        st.markdown("**Core Features:**")
        st.markdown("""
        - Natural language conversations
        - Creative content generation
        - File processing & analysis
        - Real-time market research
        - Multi-format downloads
        """)
        
        st.markdown("**Technology Stack:**")
        st.markdown("""
        - Gradio web interface
        - Groq LPU inference
        - FastAPI backend
        - Creative tools integration
        - File management system
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# Manual Access & Troubleshooting
st.markdown("---")
st.markdown("### 🔗 Manual Access Instructions")

st.warning("""
**If the buttons don't work (Streamlit Cloud restrictions), manually copy and paste these URLs in your browser:**
""")

manual_col1, manual_col2, manual_col3 = st.columns(3)

with manual_col1:
    st.markdown("**🤖 SearchPulse Chatbot**")
    st.code(CHATBOT_URL, language="text")

with manual_col2:
    st.markdown("**📰 AdVisionGenre Blogs**")
    st.code(BLOG_URL, language="text")

with manual_col3:
    st.markdown("**🧠 Reposcope**")
    st.code(REPOSCOPE_URL, language="text")

# Quick Test Section
st.markdown("---")
st.markdown("### 🧪 Quick Connection Test")

test_col1, test_col2 = st.columns(2)

with test_col1:
    if st.button("Test Chatbot Connection", key="test_chat"):
        try:
            response = requests.get(CHATBOT_URL, timeout=10)
            if response.status_code == 200:
                st.success("✅ Chatbot is accessible!")
            else:
                st.warning(f"⚠️ Chatbot returned status: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Cannot reach chatbot: {str(e)}")

with test_col2:
    if st.button("Test Blog Connection", key="test_blog"):
        try:
            response = requests.get(BLOG_URL, timeout=10)
            if response.status_code == 200:
                st.success("✅ Blog platform is accessible!")
            else:
                st.warning(f"⚠️ Blog returned status: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Cannot reach blog: {str(e)}")

# Final CTA
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px;">
    <h2>🚀 Ready to Experience AI-Powered Tools?</h2>
    <p style="font-size: 1.2rem;">Join developers worldwide boosting their productivity with our AI suite</p>
    <p style="font-size: 1.1rem; background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
        <strong>Start with: {}</strong>
    </p>
    <p><em>No registration required • Free demo available • Full code access</em></p>
</div>
""".format(CHATBOT_URL), unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p><strong>🌐 All products are part of the DevStackHQ ecosystem</strong></p>
    <p><em>Empowering developers with AI-driven tools since 2024</em></p>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
show_footer()
