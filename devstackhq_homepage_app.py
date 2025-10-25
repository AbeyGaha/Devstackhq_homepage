import os
import streamlit as st
from PIL import Image
import base64

# ---- Page Config ----
st.set_page_config(page_title="DevStackHQ", layout="wide", page_icon="💻")

# ---- Enhanced Image Loader ----
def load_image(filename, max_width=None):
    possible_paths = [
        os.path.join("assets", filename),
        os.path.join("./assets", filename),
        filename
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            try:
                img = Image.open(path)
                if max_width and img.width > max_width:
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                return img
            except Exception as e:
                return None
    return None

# ---- Header with Beautiful Text Logo ----
st.markdown("""
<div style='
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 20px;
'>
    <h1 style='margin:0; font-size: 36px;'>🚀 DevStackHQ</h1>
    <p style='margin:0; font-size: 18px; opacity: 0.9;'>Developer Productivity & Deployment Solutions</p>
</div>
""", unsafe_allow_html=True)

# ---- Navigation Menu ----
st.markdown("""
<div style='
    text-align: center;
    padding: 15px;
    background-color: #f8f9fa;
    border-radius: 10px;
    margin-bottom: 20px;
'>
    <a href='/' target='_self' style='margin: 0 20px; text-decoration: none; font-weight: bold; color: #333; font-size: 16px;'>🏠 Home</a>
    <a href='/About' target='_self' style='margin: 0 20px; text-decoration: none; font-weight: bold; color: #333; font-size: 16px;'>ℹ️ About</a>
    <a href='/Products' target='_self' style='margin: 0 20px; text-decoration: none; font-weight: bold; color: #333; font-size: 16px;'>🛍️ Products</a>
    <a href='/Contact_Us' target='_self' style='margin: 0 20px; text-decoration: none; font-weight: bold; color: #333; font-size: 16px;'>📞 Contact</a>
</div>
""", unsafe_allow_html=True)

# ---- Hero Section (Clean - No Background Image Text) ----
st.markdown("""
<div style='
    background: linear-gradient(135deg, #FF4B4B 0%, #FF6B6B 100%);
    padding: 80px 20px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
'>
    <h1 style='color: white; margin-bottom: 20px; font-size: 48px;'>Welcome to DevStackHQ</h1>
    <h3 style='color: white; margin-bottom: 30px; font-size: 24px;'>Your Launchpad for Developer Productivity & Deployment</h3>
    <p style='color: white; font-size: 18px; max-width: 800px; margin: 0 auto;'>
    We build cutting-edge tools for CI/CD, DevOps, and deployment so developers can 
    <strong>focus on building</strong> instead of managing infrastructure.
    </p>
</div>
""", unsafe_allow_html=True)

# ---- Main Features Section ----
st.markdown("### 🎯 Why Choose DevStackHQ?")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='padding: 20px; background-color: #f8f9fa; border-radius: 10px; height: 200px;'>
        <h4>🚀 Fast Deployment</h4>
        <p>Deploy your applications in minutes with our automated CI/CD pipelines</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 20px; background-color: #f8f9fa; border-radius: 10px; height: 200px;'>
        <h4>🔧 Developer First</h4>
        <p>Tools designed by developers for developers. Intuitive and powerful.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='padding: 20px; background-color: #f8f9fa; border-radius: 10px; height: 200px;'>
        <h4>☁️ Cloud Native</h4>
        <p>Built for modern cloud infrastructure with scalability in mind.</p>
    </div>
    """, unsafe_allow_html=True)

# ---- Browse Products Section ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🛍️ Browse Our Products")
st.markdown("""
Explore our amazing products without any signup required! When you're ready to purchase, simply create an account.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='padding: 15px; border-left: 4px solid #667eea;'>
        <h4>🔧 DevOps Tools</h4>
        <ul style='padding-left: 20px;'>
            <li>CI/CD Pipelines</li>
            <li>Deployment Automation</li>
            <li>Cloud Management</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 15px; border-left: 4px solid #FF4B4B;'>
        <h4>🚀 Developer Tools</h4>
        <ul style='padding-left: 20px;'>
            <li>Code Quality Checkers</li>
            <li>API Management</li>
            <li>Database Tools</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='padding: 15px; border-left: 4px solid #28a745;'>
        <h4>☁️ Cloud Services</h4>
        <ul style='padding-left: 20px;'>
            <li>Serverless Solutions</li>
            <li>Container Services</li>
            <li>Monitoring Tools</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---- Signup CTA ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style='
    text-align:center; 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 3rem;
    border-radius: 15px;
    color: white;
    margin: 30px 0;
'>
    <h2 style='color: white;'>Ready to Get Started?</h2>
    <p style='font-size: 18px; margin-bottom: 25px;'>Create your account to access premium features and make purchases</p>
    <a href='/Products' target='_self'>
        <button style='
            background-color: #FF4B4B; 
            color: white; 
            border: none; 
            padding: 15px 30px; 
            border-radius: 25px; 
            cursor: pointer; 
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        '>
        🚀 Sign Up Now
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# ---- Razorpay Required Pages Links ----
st.markdown("### 📋 Company Policies & Information")
st.markdown("""
<div style='
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0;
'>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link("pages/Shipping_Policy.py", label="🚚 Shipping Policy", icon="🚚", use_container_width=True)
    
with col2:
    st.page_link("pages/Terms_Conditions.py", label="📄 Terms & Conditions", icon="📄", use_container_width=True)
    
with col3:
    st.page_link("pages/Cancellations_Refund.py", label="🔄 Cancellations & Refund", icon="🔄", use_container_width=True)
    
with col4:
    st.page_link("pages/Contact_Us.py", label="📞 Contact Us", icon="📞", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---- Trust Indicators ----
st.markdown("### 🔒 Trust & Security")
trust_col1, trust_col2, trust_col3, trust_col4 = st.columns(4)

with trust_col1:
    st.markdown("""
    <div style='text-align: center; padding: 15px;'>
        <div style='font-size: 30px;'>✅</div>
        <strong>SSL Encrypted</strong>
        <p style='font-size: 12px;'>Secure transactions</p>
    </div>
    """, unsafe_allow_html=True)

with trust_col2:
    st.markdown("""
    <div style='text-align: center; padding: 15px;'>
        <div style='font-size: 30px;'>🛡️</div>
        <strong>Razorpay Verified</strong>
        <p style='font-size: 12px;'>Trusted payments</p>
    </div>
    """, unsafe_allow_html=True)

with trust_col3:
    st.markdown("""
    <div style='text-align: center; padding: 15px;'>
        <div style='font-size: 30px;'>🌐</div>
        <strong>24/7 Support</strong>
        <p style='font-size: 12px;'>Always available</p>
    </div>
    """, unsafe_allow_html=True)

with trust_col4:
    st.markdown("""
    <div style='text-align: center; padding: 15px;'>
        <div style='font-size: 30px;'>⚡</div>
        <strong>Instant Delivery</strong>
        <p style='font-size: 12px;'>Digital products</p>
    </div>
    """, unsafe_allow_html=True)

# ---- Footer with All Required Links ----
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666; padding: 20px;'>
    <p style='font-size: 16px; font-weight: bold;'>© 2024 DevStackHQ. All rights reserved.</p>
    <div style='margin: 15px 0;'>
        <a href='/Shipping_Policy' style='margin: 0 15px; text-decoration:none; color:#666; font-size: 14px;'>Shipping Policy</a> | 
        <a href='/Terms_Conditions' style='margin: 0 15px; text-decoration:none; color:#666; font-size: 14px;'>Terms & Conditions</a> | 
        <a href='/Cancellations_Refund' style='margin: 0 15px; text-decoration:none; color:#666; font-size: 14px;'>Cancellations & Refund</a> | 
        <a href='/Contact_Us' style='margin: 0 15px; text-decoration:none; color:#666; font-size: 14px;'>Contact Us</a>
    </div>
    <p style='font-size: 14px;'>
        Need help? <a href='mailto:support@devstackhq.com' style='color: #FF4B4B;'>Contact our support team</a>
    </p>
</div>
""", unsafe_allow_html=True)
