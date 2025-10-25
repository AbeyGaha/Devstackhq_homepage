import os
import streamlit as st
from PIL import Image

# ---- Page Config ----
st.set_page_config(page_title="DevStackHQ", layout="wide", page_icon="💻")

# ---- Safe Image Loader ----
def load_image(filename, max_width=None):
    path = os.path.join("assets", filename)
    if not os.path.exists(path):
        st.warning(f"⚠️ Missing image: {path}")
        return None
    img = Image.open(path)
    if max_width and img.width > max_width:
        ratio = max_width / img.width
        img = img.resize((max_width, int(img.height * ratio)))
    return img

# ---- Logo Display ----
logo = load_image("logo.png", max_width=180)
if logo:
    st.image(logo, width=180)

# ---- Navigation without Signup ----
st.markdown(f"""
<div style='text-align:right; padding-top:10px;'>
    <a href='/' target='_self' style='margin-right:15px; text-decoration:none;'>🏠 Home</a>
    <a href='/About' target='_self' style='margin-right:15px; text-decoration:none;'>ℹ️ About</a>
    <a href='/Products' target='_self' style='margin-right:15px; text-decoration:none;'>🛍️ Products</a>
    <a href='/Contact_Us' target='_self' style='margin-right:15px; text-decoration:none;'>📞 Contact</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown("""
<h1 style='text-align:center; color:#2C3E50;'>🚀 Welcome to DevStackHQ</h1>
<h3 style='text-align:center; color:#34495E;'>Your Launchpad for Developer Productivity & Deployment</h3>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px; padding:1rem 2rem;'>
We build cutting-edge tools for CI/CD, DevOps, and deployment so developers can
<strong>focus on building</strong> instead of managing infrastructure.
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
    st.markdown("#### 🔧 DevOps Tools")
    st.markdown("- CI/CD Pipelines")
    st.markdown("- Deployment Automation")
    st.markdown("- Cloud Management")

with col2:
    st.markdown("#### 🚀 Developer Tools")
    st.markdown("- Code Quality Checkers")
    st.markdown("- API Management")
    st.markdown("- Database Tools")

with col3:
    st.markdown("#### ☁️ Cloud Services")
    st.markdown("- Serverless Solutions")
    st.markdown("- Container Services")
    st.markdown("- Monitoring Tools")

# ---- Signup CTA ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; background-color:#f0f2f6; padding:2rem; border-radius:10px;'>
<h3>Ready to Get Started?</h3>
<p>Create your account to access premium features and make purchases</p>
<a href='/Products' target='_self'>
<button style='background-color:#FF4B4B; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer;'>
Sign Up Now
</button>
</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---- Razorpay Required Pages Links ----
st.markdown("### 📋 Company Policies")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link("pages/Shipping_Policy.py", label="🚚 Shipping Policy", icon="🚚")
    
with col2:
    st.page_link("pages/Terms_Conditions.py", label="📄 Terms & Conditions", icon="📄")
    
with col3:
    st.page_link("pages/Cancellations_Refund.py", label="🔄 Cancellations & Refund", icon="🔄")
    
with col4:
    st.markdown("#### 🔒 Safe & Secure")
    st.markdown("""
    - ✅ SSL Encrypted
    - ✅ Razorpay Verified
    - ✅ 24/7 Support
    - ✅ Instant Delivery
    """)

# ---- Footer with All Required Links ----
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666;'>
<p>© 2024 DevStackHQ. All rights reserved.</p>
<p>
    <a href='/Shipping_Policy' style='margin:0 10px; text-decoration:none; color:#666;'>Shipping Policy</a> | 
    <a href='/Terms_Conditions' style='margin:0 10px; text-decoration:none; color:#666;'>Terms & Conditions</a> | 
    <a href='/Cancellations_Refund' style='margin:0 10px; text-decoration:none; color:#666;'>Cancellations & Refund</a> | 
    <a href='/Contact_Us' style='margin:0 10px; text-decoration:none; color:#666;'>Contact Us</a>
</p>
<p>Need help? <a href='mailto:support@devstackhq.com'>Contact our support team</a></p>
</div>
""", unsafe_allow_html=True)
