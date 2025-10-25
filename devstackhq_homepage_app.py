import os
import streamlit as st
from PIL import Image
import base64

# ---- Page Config ----
st.set_page_config(page_title="DevStackHQ", layout="wide", page_icon="💻")

# ---- Enhanced Image Loader with Multiple Paths ----
def load_image(filename, max_width=None):
    # Try multiple possible paths
    possible_paths = [
        os.path.join("assets", filename),
        os.path.join("./assets", filename),
        os.path.join("pages/assets", filename),
        os.path.join("../assets", filename),
        filename  # Direct path
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
                st.warning(f"Error loading image: {e}")
                return None
    
    st.warning(f"⚠️ Image not found: {filename}")
    st.info("Tried paths: " + ", ".join(possible_paths))
    return None

# ---- Convert Image to Base64 for Background ----
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# ---- Try to load logo with multiple approaches ----
logo = None
logo_paths = [
    "assets/logo.png",
    "./assets/logo.png", 
    "pages/assets/logo.png",
    "../assets/logo.png",
    "logo.png"
]

for path in logo_paths:
    if os.path.exists(path):
        logo = load_image(path.replace("assets/", "").replace("./", "").replace("pages/", "").replace("../", ""))
        if logo:
            break

# ---- Header Section with Logo ----
col1, col2 = st.columns([1, 4])

with col1:
    if logo:
        st.image(logo, width=180)
    else:
        # Fallback: Create a styled text logo
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 20px;
        '>
        🚀<br>DevStackHQ
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='text-align:right; padding-top:20px;'>
        <a href='/' target='_self' style='margin-right:15px; text-decoration:none; font-weight:bold;'>🏠 Home</a>
        <a href='/About' target='_self' style='margin-right:15px; text-decoration:none; font-weight:bold;'>ℹ️ About</a>
        <a href='/Products' target='_self' style='margin-right:15px; text-decoration:none; font-weight:bold;'>🛍️ Products</a>
        <a href='/Contact_Us' target='_self' style='text-decoration:none; font-weight:bold;'>📞 Contact</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---- Hero Section with Optional Background ----
# Try to load background image
background_image = None
bg_paths = [
    "assets/background.jpg",
    "assets/banner.png", 
    "assets/hero-bg.jpg",
    "./assets/background.jpg"
]

bg_base64 = None
for path in bg_paths:
    if os.path.exists(path):
        bg_base64 = get_image_base64(path)
        if bg_base64:
            break

if bg_base64:
    st.markdown(f"""
    <div style='
        background-image: url("data:image/jpeg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        padding: 60px 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    '>
        <h1 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>🚀 Welcome to DevStackHQ</h1>
        <h3 style='color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>Your Launchpad for Developer Productivity & Deployment</h3>
    </div>
    """, unsafe_allow_html=True)
else:
    # Fallback hero section without background image
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 60px 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    '>
        <h1 style='color: white;'>🚀 Welcome to DevStackHQ</h1>
        <h3 style='color: white;'>Your Launchpad for Developer Productivity & Deployment</h3>
    </div>
    """, unsafe_allow_html=True)

# ---- Main Content ----
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
<button style='background-color:#FF4B4B; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; font-size:16px;'>
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

# ---- Debug Section (Remove in production) ----
with st.expander("🔧 Debug Info"):
    st.write("Current working directory:", os.getcwd())
    st.write("Files in current directory:", os.listdir("."))
    if os.path.exists("assets"):
        st.write("Files in assets folder:", os.listdir("assets"))
    else:
        st.write("Assets folder not found!")
